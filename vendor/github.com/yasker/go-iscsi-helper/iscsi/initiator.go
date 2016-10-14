package iscsi

import (
	"bufio"
	"fmt"
	"strconv"
	"strings"
	"time"

	"github.com/yasker/go-iscsi-helper/util"
)

var (
	DeviceWaitRetryCounts   = 5
	DeviceWaitRetryInterval = 1 * time.Second
)

const (
	iscsiBinary = "iscsiadm"
)

func CheckForInitiatorExistence(ne *util.NamespaceExecutor) error {
	opts := []string{
		"--version",
	}
	_, err := ne.Execute(iscsiBinary, opts)
	if err != nil {
		return err
	}
	return nil
}

func DiscoverTarget(ip, target string, ne *util.NamespaceExecutor) error {
	opts := []string{
		"-m", "discovery",
		"-t", "sendtargets",
		"-p", ip,
	}
	output, err := ne.Execute(iscsiBinary, opts)
	if err != nil {
		return err
	}
	if !strings.Contains(output, target) {
		return fmt.Errorf("Cannot find target %s in discovered targets %s", target, output)
	}
	return nil
}

func DeleteDiscoveredTarget(ip, target string, ne *util.NamespaceExecutor) error {
	opts := []string{
		"-m", "node",
		"-o", "delete",
		"-p", ip,
		"-T", target,
	}
	_, err := ne.Execute(iscsiBinary, opts)
	if err != nil {
		return err
	}
	return nil
}

func LoginTarget(ip, target string, ne *util.NamespaceExecutor) error {
	opts := []string{
		"-m", "node",
		"-T", target,
		"-p", ip,
		"--login",
	}
	_, err := ne.Execute(iscsiBinary, opts)
	if err != nil {
		return err
	}
	return nil
}

func LogoutTarget(ip, target string, ne *util.NamespaceExecutor) error {
	opts := []string{
		"-m", "node",
		"-T", target,
		"-p", ip,
		"--logout",
	}
	_, err := ne.Execute(iscsiBinary, opts)
	if err != nil {
		return err
	}
	return nil
}

func GetDevice(ip, target string, lun int, ne *util.NamespaceExecutor) (string, error) {
	var err error

	dev := ""
	for i := 0; i < DeviceWaitRetryCounts; i++ {
		dev, err = findScsiDevice(ip, target, lun, ne)
		if err == nil {
			break
		}
		time.Sleep(DeviceWaitRetryInterval)
	}
	if err != nil {
		return "", err
	}
	return strings.TrimSpace(dev), nil
}

func findScsiDevice(ip, target string, lun int, ne *util.NamespaceExecutor) (string, error) {
	dev := ""

	opts := []string{
		"-m", "session",
		"-P", "3",
	}
	output, err := ne.Execute(iscsiBinary, opts)
	if err != nil {
		return "", err
	}
	/*
		Now we got something like this in output, and need to parse it
		Target: iqn.2016-09.com.rancher:for.all (non-flash)
			Current Portal: 172.17.0.2:3260,1
			Persistent Portal: 172.17.0.2:3260,1
			...
			Attached SCSI devices:
			...
			scsi12 Channel 00 Id 0 Lun: 0
			scsi12 Channel 00 Id 0 Lun: 1
				Attached scsi disk sdb		State: running
		...
		Target: ...
	*/
	scanner := bufio.NewScanner(strings.NewReader(output))
	targetLine := "Target: " + target
	lunLine := "Lun: " + strconv.Itoa(lun)
	diskPrefix := "Attached scsi disk"
	stateLine := "State:"
	inTarget := false
	inLun := false
	for scanner.Scan() {
		if !inTarget && strings.Contains(scanner.Text(), targetLine) {
			inTarget = true
			continue
		}
		if inTarget && strings.Contains(scanner.Text(), lunLine) {
			inLun = true
			continue
		}
		// The line we need
		if inLun {
			line := scanner.Text()
			if !strings.Contains(line, diskPrefix) {
				return "", fmt.Errorf("Invalid output format, cannot find disk in: %s", line)
			}
			line = strings.TrimSpace(strings.Split(line, stateLine)[0])
			line = strings.TrimPrefix(line, diskPrefix)
			dev = strings.TrimSpace(line)
			break
		}
	}
	if dev == "" {
		return "", fmt.Errorf("Cannot find iscsi device")
	}
	dev = "/dev/" + dev
	return dev, nil
}