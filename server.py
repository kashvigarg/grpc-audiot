from concurrent import futures
import time

import grpc
import audiotransfer_pb2
import audiotransfer_pb2_grpc

class TransferServicer(audiotransfer_pb2_grpc.TransferServicer):
    def AudioTransfer(self, request_iterator, context):
        for req in request_iterator:
            print('recieved')
            reply = audiotransfer_pb2.Response()
            yield reply

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    audiotransfer_pb2_grpc.add_TransferServicer_to_server(TransferServicer(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()