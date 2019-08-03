# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import controller_pb2 as controller__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class ControllerServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.VolumeGet = channel.unary_unary(
        '/pb.ControllerService/VolumeGet',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=controller__pb2.Volume.FromString,
        )
    self.VolumeStart = channel.unary_unary(
        '/pb.ControllerService/VolumeStart',
        request_serializer=controller__pb2.VolumeStartRequest.SerializeToString,
        response_deserializer=controller__pb2.Volume.FromString,
        )
    self.VolumeShutdown = channel.unary_unary(
        '/pb.ControllerService/VolumeShutdown',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=controller__pb2.Volume.FromString,
        )
    self.VolumeSnapshot = channel.unary_unary(
        '/pb.ControllerService/VolumeSnapshot',
        request_serializer=controller__pb2.VolumeSnapshotRequest.SerializeToString,
        response_deserializer=controller__pb2.VolumeSnapshotReply.FromString,
        )
    self.VolumeRevert = channel.unary_unary(
        '/pb.ControllerService/VolumeRevert',
        request_serializer=controller__pb2.VolumeRevertRequest.SerializeToString,
        response_deserializer=controller__pb2.Volume.FromString,
        )
    self.VolumeFrontendStart = channel.unary_unary(
        '/pb.ControllerService/VolumeFrontendStart',
        request_serializer=controller__pb2.VolumeFrontendStartRequest.SerializeToString,
        response_deserializer=controller__pb2.Volume.FromString,
        )
    self.VolumeFrontendShutdown = channel.unary_unary(
        '/pb.ControllerService/VolumeFrontendShutdown',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=controller__pb2.Volume.FromString,
        )
    self.ReplicaList = channel.unary_unary(
        '/pb.ControllerService/ReplicaList',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=controller__pb2.ReplicaListReply.FromString,
        )
    self.ReplicaGet = channel.unary_unary(
        '/pb.ControllerService/ReplicaGet',
        request_serializer=controller__pb2.ReplicaAddress.SerializeToString,
        response_deserializer=controller__pb2.ControllerReplica.FromString,
        )
    self.ReplicaCreate = channel.unary_unary(
        '/pb.ControllerService/ReplicaCreate',
        request_serializer=controller__pb2.ReplicaAddress.SerializeToString,
        response_deserializer=controller__pb2.ControllerReplica.FromString,
        )
    self.ReplicaDelete = channel.unary_unary(
        '/pb.ControllerService/ReplicaDelete',
        request_serializer=controller__pb2.ReplicaAddress.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.ReplicaUpdate = channel.unary_unary(
        '/pb.ControllerService/ReplicaUpdate',
        request_serializer=controller__pb2.ControllerReplica.SerializeToString,
        response_deserializer=controller__pb2.ControllerReplica.FromString,
        )
    self.ReplicaPrepareRebuild = channel.unary_unary(
        '/pb.ControllerService/ReplicaPrepareRebuild',
        request_serializer=controller__pb2.ReplicaAddress.SerializeToString,
        response_deserializer=controller__pb2.ReplicaPrepareRebuildReply.FromString,
        )
    self.ReplicaVerifyRebuild = channel.unary_unary(
        '/pb.ControllerService/ReplicaVerifyRebuild',
        request_serializer=controller__pb2.ReplicaAddress.SerializeToString,
        response_deserializer=controller__pb2.ControllerReplica.FromString,
        )
    self.BackupReplicaMappingCreate = channel.unary_unary(
        '/pb.ControllerService/BackupReplicaMappingCreate',
        request_serializer=controller__pb2.BackupReplicaMapping.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.BackupReplicaMappingGet = channel.unary_unary(
        '/pb.ControllerService/BackupReplicaMappingGet',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=controller__pb2.BackupReplicaMap.FromString,
        )
    self.BackupReplicaMappingDelete = channel.unary_unary(
        '/pb.ControllerService/BackupReplicaMappingDelete',
        request_serializer=controller__pb2.BackupReplicaMappingDeleteRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.JournalList = channel.unary_unary(
        '/pb.ControllerService/JournalList',
        request_serializer=controller__pb2.JournalListRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.PortUpdate = channel.unary_unary(
        '/pb.ControllerService/PortUpdate',
        request_serializer=controller__pb2.PortUpdateRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.VersionDetailGet = channel.unary_unary(
        '/pb.ControllerService/VersionDetailGet',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=controller__pb2.VersionDetailGetReply.FromString,
        )
    self.MetricGet = channel.unary_stream(
        '/pb.ControllerService/MetricGet',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=controller__pb2.MetricGetReply.FromString,
        )


class ControllerServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def VolumeGet(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def VolumeStart(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def VolumeShutdown(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def VolumeSnapshot(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def VolumeRevert(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def VolumeFrontendStart(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def VolumeFrontendShutdown(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReplicaList(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReplicaGet(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReplicaCreate(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReplicaDelete(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReplicaUpdate(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReplicaPrepareRebuild(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReplicaVerifyRebuild(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BackupReplicaMappingCreate(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BackupReplicaMappingGet(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BackupReplicaMappingDelete(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def JournalList(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PortUpdate(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def VersionDetailGet(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MetricGet(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ControllerServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'VolumeGet': grpc.unary_unary_rpc_method_handler(
          servicer.VolumeGet,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=controller__pb2.Volume.SerializeToString,
      ),
      'VolumeStart': grpc.unary_unary_rpc_method_handler(
          servicer.VolumeStart,
          request_deserializer=controller__pb2.VolumeStartRequest.FromString,
          response_serializer=controller__pb2.Volume.SerializeToString,
      ),
      'VolumeShutdown': grpc.unary_unary_rpc_method_handler(
          servicer.VolumeShutdown,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=controller__pb2.Volume.SerializeToString,
      ),
      'VolumeSnapshot': grpc.unary_unary_rpc_method_handler(
          servicer.VolumeSnapshot,
          request_deserializer=controller__pb2.VolumeSnapshotRequest.FromString,
          response_serializer=controller__pb2.VolumeSnapshotReply.SerializeToString,
      ),
      'VolumeRevert': grpc.unary_unary_rpc_method_handler(
          servicer.VolumeRevert,
          request_deserializer=controller__pb2.VolumeRevertRequest.FromString,
          response_serializer=controller__pb2.Volume.SerializeToString,
      ),
      'VolumeFrontendStart': grpc.unary_unary_rpc_method_handler(
          servicer.VolumeFrontendStart,
          request_deserializer=controller__pb2.VolumeFrontendStartRequest.FromString,
          response_serializer=controller__pb2.Volume.SerializeToString,
      ),
      'VolumeFrontendShutdown': grpc.unary_unary_rpc_method_handler(
          servicer.VolumeFrontendShutdown,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=controller__pb2.Volume.SerializeToString,
      ),
      'ReplicaList': grpc.unary_unary_rpc_method_handler(
          servicer.ReplicaList,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=controller__pb2.ReplicaListReply.SerializeToString,
      ),
      'ReplicaGet': grpc.unary_unary_rpc_method_handler(
          servicer.ReplicaGet,
          request_deserializer=controller__pb2.ReplicaAddress.FromString,
          response_serializer=controller__pb2.ControllerReplica.SerializeToString,
      ),
      'ReplicaCreate': grpc.unary_unary_rpc_method_handler(
          servicer.ReplicaCreate,
          request_deserializer=controller__pb2.ReplicaAddress.FromString,
          response_serializer=controller__pb2.ControllerReplica.SerializeToString,
      ),
      'ReplicaDelete': grpc.unary_unary_rpc_method_handler(
          servicer.ReplicaDelete,
          request_deserializer=controller__pb2.ReplicaAddress.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'ReplicaUpdate': grpc.unary_unary_rpc_method_handler(
          servicer.ReplicaUpdate,
          request_deserializer=controller__pb2.ControllerReplica.FromString,
          response_serializer=controller__pb2.ControllerReplica.SerializeToString,
      ),
      'ReplicaPrepareRebuild': grpc.unary_unary_rpc_method_handler(
          servicer.ReplicaPrepareRebuild,
          request_deserializer=controller__pb2.ReplicaAddress.FromString,
          response_serializer=controller__pb2.ReplicaPrepareRebuildReply.SerializeToString,
      ),
      'ReplicaVerifyRebuild': grpc.unary_unary_rpc_method_handler(
          servicer.ReplicaVerifyRebuild,
          request_deserializer=controller__pb2.ReplicaAddress.FromString,
          response_serializer=controller__pb2.ControllerReplica.SerializeToString,
      ),
      'BackupReplicaMappingCreate': grpc.unary_unary_rpc_method_handler(
          servicer.BackupReplicaMappingCreate,
          request_deserializer=controller__pb2.BackupReplicaMapping.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'BackupReplicaMappingGet': grpc.unary_unary_rpc_method_handler(
          servicer.BackupReplicaMappingGet,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=controller__pb2.BackupReplicaMap.SerializeToString,
      ),
      'BackupReplicaMappingDelete': grpc.unary_unary_rpc_method_handler(
          servicer.BackupReplicaMappingDelete,
          request_deserializer=controller__pb2.BackupReplicaMappingDeleteRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'JournalList': grpc.unary_unary_rpc_method_handler(
          servicer.JournalList,
          request_deserializer=controller__pb2.JournalListRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'PortUpdate': grpc.unary_unary_rpc_method_handler(
          servicer.PortUpdate,
          request_deserializer=controller__pb2.PortUpdateRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'VersionDetailGet': grpc.unary_unary_rpc_method_handler(
          servicer.VersionDetailGet,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=controller__pb2.VersionDetailGetReply.SerializeToString,
      ),
      'MetricGet': grpc.unary_stream_rpc_method_handler(
          servicer.MetricGet,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=controller__pb2.MetricGetReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'pb.ControllerService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
