from exemplo_pb2 import ExampleReply
from exemplo_pb2_grpc import exampleStub

from nameko_grpc.entrypoint import Grpc

grpc = Grpc.implementing(exampleStub)


class ExampleService:
    name = "example"

    @grpc
    def unary_unary(self, request, context):
        message = request.value * (request.multiplier or 1)
        print(message)
        return ExampleReply(message=message)

    @grpc
    def unary_stream(self, request, context):
        message = request.value * (request.multiplier or 1)
        yield ExampleReply(message=message, seqno=1)
        yield ExampleReply(message=message, seqno=2)

    @grpc
    def stream_unary(self, request, context):
        messages = []
        for req in request:
            message = req.value * (req.multiplier or 1)
            messages.append(message)

        return ExampleReply(message=",".join(messages))

    @grpc
    def stream_stream(self, request, context):
        for index, req in enumerate(request):
            message = req.value * (req.multiplier or 1)
            yield ExampleReply(message=message, seqno=index + 1)
