import socket, pickle
from Assets.gameCode.gameObjects import Paddle, Ball

class Network:
    def __init__(self, ip, RES):
        self.WIDTH = RES[0]
        self.HEIGHT = RES[1]
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = ip
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()
    
    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
        except socket.gaierror:
            return False

        reply = pickle.loads(self.client.recv(2048))
        return [Paddle((20, 100), (reply["yourP"][0], reply["yourP"][1])),
            Paddle((20, 100), (reply["otherP"][0], reply["otherP"][1])),
            Ball(20, (reply["ballPos"][0], reply["ballPos"][1]), (self.WIDTH, self.HEIGHT))]
        
    def send(self, data):
        self.client.send(pickle.dumps(data))
        return pickle.loads(self.client.recv(2048))