import grpc

# import the generated classes
import calculator_pb2
import calculator_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = calculator_pb2_grpc.CalculatorStub(channel)

stub1 = calculator_pb2_grpc.CalculatorNewStub(channel)

stub2 = calculator_pb2_grpc.Welcome_MessageStub(channel)

number = calculator_pb2.Number(value=25)

new_number = calculator_pb2.Number(value=36)

message = calculator_pb2.Welcome(hello="Rajesh")

response = stub1.SquareRoot(new_number)

print (response.value)

response = stub.SquareRoot(number)

print(response.value)

response = stub2.WelcomeMessage(message)

print(response.hello)