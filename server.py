import grpc 
import time
from concurrent import futures 

import sleep_pb2 
import sleep_pb2_grpc 

import sleep 

# create class to define server functions derived from
# sleep_pb2_grpc.SleepTimeServicer
class SleepTimeServicer(sleep_pb2_grpc.SleepTimeServicer):

    def Sleep(self, request, context):
        response = sleep_pb2.Seconds()
        response.value = sleep.sleep(request.value)
        return response


# create gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use generated function add_SleepTimeServicer_to_server to add
# the defined class to the server
sleep_pb2_grpc.add_SleepTimeServicer_to_server(SleepTimeServicer(), server)

# listen on port 50051
print('start server and listen on port 50051')
server.add_insecure_port('[::]:50051')
server.start()
server.wait_for_termination()
