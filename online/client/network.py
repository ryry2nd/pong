#imports
import socket, pickle

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
        return reply

    #defines the send funtion
    def send(self, data=False):
        #sends the data
        self.client.send(pickle.dumps(data))

        #recieves other data
        return pickle.loads(self.client.recv(2048))