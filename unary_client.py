import grpc
import unary_pb2_grpc as pb2_grpc
import unary_pb2 as pb2

class UnaryClient():

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051
        self.channel = grpc.insecure_channel(
            "{}:{}".format(self.host, self.server_port)
        )
        self.stub = pb2_grpc.UnaryStub(self.channel)

    def get_url(self, message):
        message = pb2.Message(message=message)
        print(f"{message}")
        return self.stub.GetServerResponse(message)
    
if __name__ == "__main__":
    client = UnaryClient()
    while True:
        mat = str(input("Forneça uma matrícula: "))
        equip = str(input("Forneça um equipamento: "))
        defe = str(input("Forneça um defeito: "))
        set = str(input("Forneça um setor: "))
        msg = {
            "mat": mat, "equip": equip, "def": defe, "set": set
        }
        result = client.get_url(message=f"{msg}")
        print(f"{result}")
        opc = str(input("Deseja realizar outra solicitação? Y/N"))
        opc = opc.upper()
        if opc == 'N':
            break