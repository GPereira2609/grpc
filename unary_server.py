import grpc
import time
import unary_pb2_grpc as pb2_grpc
import unary_pb2 as pb2

from concurrent import futures
from bd import tecnicos, servicos
from random import randrange
from datetime import date, timedelta

def get_hora():
    hora = f"{randrange(8, 17)}:{randrange(0, 59)}"
    return hora

def get_data():
    data_atual = date.today()
    data_servico = data_atual + timedelta(days=randrange(1, 3))
    return data_servico

class UnaryService(pb2_grpc.UnaryServicer):
    def __init__(self, *args, **kwargs):
        pass

    def GetServerResponse(self, request, context):
        servico = request.message
        if len(tecnicos) > 0:
            servicos.append(servico)
            msg = f"O técnico {tecnicos.pop(0)} irá realizar o conserto às {get_hora()} do dia {get_data()}"
        else:
            msg = "Nenhum técnico disponível"
        result = {'message': msg, 'received': True}

        return pb2.MessageResponse(**result)
    
def service():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_UnaryServicer_to_server(UnaryService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    service()