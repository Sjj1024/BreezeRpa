import grpc
from GrpcDemo.proto_file import helloworld_pb2, helloworld_pb2_grpc


def run():
  # 连接 rpc 服务器
  channel = grpc.insecure_channel('localhost:50051')
  # 调用 rpc 服务
  stub = helloworld_pb2_grpc.GreeterStub(channel)
  response = stub.SayHello(helloworld_pb2.HelloRequest(name='czl'))
  print("Greeter client received: " + response.message)
  response = stub.SayHelloAgain(helloworld_pb2.HelloRequest(name='daydaygo'))
  print("Greeter client received: " + response.message)


if __name__ == '__main__':
  run()
