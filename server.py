import grpc
from concurrent import futures
import time

import calculator_pb2
import calculator_pb2_grpc

import calculator

class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):

    def SquareRoot(self, request, context):
        response = calculator_pb2.Number()
        response.value = calculator.square_root(request.value)
        return response

class Welcome_MessageServicer(calculator_pb2_grpc.Welcome_MessageServicer):
    
    def WelcomeMessage(self, request, context):
        response = calculator_pb2.Welcome()
        response.hello = calculator.welcome(request.hello)
        return response


class CalculatorNewServicer(calculator_pb2_grpc.CalculatorNewServicer):
    
    def SquareRoot(self, request, context):
        response = calculator_pb2.Number()
        response.value = calculator.square_root(request.value)
        return response

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
calculator_pb2_grpc.add_CalculatorNewServicer_to_server(CalculatorNewServicer(),server)
calculator_pb2_grpc.add_Welcome_MessageServicer_to_server(Welcome_MessageServicer(),server)

print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)