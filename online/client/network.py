#imports
import socket, pickle
from Assets.gameCode.gameObjects import Paddle, Ball

#defines Network class
class Network:
    #init
    def __init__(self, ip, RES):
        #defines the res
        self.WIDTH = RES[0]
        self.HEIGHT = RES[1]
        #sets up socket
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #defines the server ip
        self.server = ip
        #defines the port
        self.port = 5555
        #defines the address
        self.addr = (self.server, self.port)
        #defines the player
        self.p = self.connect()

    #gets the player
    def getP(self):
        return self.p

    #connects to the server
    def connect(self):
        # if it can connect conect, otherwise return false
        try:
            self.client.connect(self.addr)
        except socket.gaierror:
            return False

        #defines the reply from the server
        reply = pickle.loads(self.client.recv(2048))

        #returns all of the initualised objects
        return [Paddle((20, 100), (reply["yourP"][0], reply["yourP"][1])),
            Paddle((20, 100), (reply["otherP"][0], reply["otherP"][1])),
            Ball(20, (reply["ballPos"][0], reply["ballPos"][1]), (self.WIDTH, self.HEIGHT))]

    #defines the send funtion
    def send(self, data):
        #sends the data
        self.client.send(pickle.dumps(data))
        #recieves other data
        return pickle.loads(self.client.recv(2048))