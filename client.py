# https://grpc.io/docs/languages/python/basics/
# To run start server.py in one terminal and run client.py in another terminal.
import grpc
from concurrent import futures

# import the generated classes
import sleep_pb2_grpc
import sleep_pb2

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')


def print_res(future):
    print(f'receiving {future.result().value} ')


with futures.ThreadPoolExecutor() as executor:
    for i in range(5, 0, -1):
        # create a stub (client)
        stub = sleep_pb2_grpc.SleepTimeStub(channel)
        print(f'sending {i} seconds...')
        number = sleep_pb2.Seconds(value=i)
        # call service method Sleep
        future = executor.submit(stub.Sleep, number)
        future.add_done_callback(print_res)
