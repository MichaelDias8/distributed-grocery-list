# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import list_pb2 as list__pb2


class ListServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddItem = channel.unary_unary(
                '/main.ListService/AddItem',
                request_serializer=list__pb2.ItemRequest.SerializeToString,
                response_deserializer=list__pb2.ItemResponse.FromString,
                )
        self.CheckItem = channel.unary_unary(
                '/main.ListService/CheckItem',
                request_serializer=list__pb2.ItemRequest.SerializeToString,
                response_deserializer=list__pb2.ItemResponse.FromString,
                )
        self.GetItems = channel.unary_unary(
                '/main.ListService/GetItems',
                request_serializer=list__pb2.ItemsRequest.SerializeToString,
                response_deserializer=list__pb2.ItemsResponse.FromString,
                )
        self.DeleteItem = channel.unary_unary(
                '/main.ListService/DeleteItem',
                request_serializer=list__pb2.ItemRequest.SerializeToString,
                response_deserializer=list__pb2.ItemResponse.FromString,
                )
        self.JoinGroup = channel.unary_unary(
                '/main.ListService/JoinGroup',
                request_serializer=list__pb2.GroupRequest.SerializeToString,
                response_deserializer=list__pb2.GroupResponse.FromString,
                )
        self.CreateGroup = channel.unary_unary(
                '/main.ListService/CreateGroup',
                request_serializer=list__pb2.GroupRequest.SerializeToString,
                response_deserializer=list__pb2.GroupResponse.FromString,
                )
        self.SubscribeToUpdates = channel.unary_stream(
                '/main.ListService/SubscribeToUpdates',
                request_serializer=list__pb2.SubscribeRequest.SerializeToString,
                response_deserializer=list__pb2.Update.FromString,
                )


class ListServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetItems(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def JoinGroup(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateGroup(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeToUpdates(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ListServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddItem': grpc.unary_unary_rpc_method_handler(
                    servicer.AddItem,
                    request_deserializer=list__pb2.ItemRequest.FromString,
                    response_serializer=list__pb2.ItemResponse.SerializeToString,
            ),
            'CheckItem': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckItem,
                    request_deserializer=list__pb2.ItemRequest.FromString,
                    response_serializer=list__pb2.ItemResponse.SerializeToString,
            ),
            'GetItems': grpc.unary_unary_rpc_method_handler(
                    servicer.GetItems,
                    request_deserializer=list__pb2.ItemsRequest.FromString,
                    response_serializer=list__pb2.ItemsResponse.SerializeToString,
            ),
            'DeleteItem': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteItem,
                    request_deserializer=list__pb2.ItemRequest.FromString,
                    response_serializer=list__pb2.ItemResponse.SerializeToString,
            ),
            'JoinGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.JoinGroup,
                    request_deserializer=list__pb2.GroupRequest.FromString,
                    response_serializer=list__pb2.GroupResponse.SerializeToString,
            ),
            'CreateGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateGroup,
                    request_deserializer=list__pb2.GroupRequest.FromString,
                    response_serializer=list__pb2.GroupResponse.SerializeToString,
            ),
            'SubscribeToUpdates': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeToUpdates,
                    request_deserializer=list__pb2.SubscribeRequest.FromString,
                    response_serializer=list__pb2.Update.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'main.ListService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ListService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/main.ListService/AddItem',
            list__pb2.ItemRequest.SerializeToString,
            list__pb2.ItemResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/main.ListService/CheckItem',
            list__pb2.ItemRequest.SerializeToString,
            list__pb2.ItemResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetItems(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/main.ListService/GetItems',
            list__pb2.ItemsRequest.SerializeToString,
            list__pb2.ItemsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/main.ListService/DeleteItem',
            list__pb2.ItemRequest.SerializeToString,
            list__pb2.ItemResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def JoinGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/main.ListService/JoinGroup',
            list__pb2.GroupRequest.SerializeToString,
            list__pb2.GroupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/main.ListService/CreateGroup',
            list__pb2.GroupRequest.SerializeToString,
            list__pb2.GroupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeToUpdates(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/main.ListService/SubscribeToUpdates',
            list__pb2.SubscribeRequest.SerializeToString,
            list__pb2.Update.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)