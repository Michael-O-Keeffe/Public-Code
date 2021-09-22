# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import line_pb2 as line__pb2


class GetLineServiceStub(object):
    """python3 -m grpc_tools.protoc --proto_path=. ./line.proto --python_out=../ --grpc_python_out=../

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetLine = channel.unary_unary(
                '/GetLineService/GetLine',
                request_serializer=line__pb2.Lines.SerializeToString,
                response_deserializer=line__pb2.CheckReponse.FromString,
                )


class GetLineServiceServicer(object):
    """python3 -m grpc_tools.protoc --proto_path=. ./line.proto --python_out=../ --grpc_python_out=../

    """

    def GetLine(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GetLineServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetLine': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLine,
                    request_deserializer=line__pb2.Lines.FromString,
                    response_serializer=line__pb2.CheckReponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'GetLineService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GetLineService(object):
    """python3 -m grpc_tools.protoc --proto_path=. ./line.proto --python_out=../ --grpc_python_out=../

    """

    @staticmethod
    def GetLine(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GetLineService/GetLine',
            line__pb2.Lines.SerializeToString,
            line__pb2.CheckReponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)