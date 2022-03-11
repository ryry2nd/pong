#imports
import socket, pickle
from _thread import *
from Assets.gameCode.gameObjects import Paddle, Ball

#defines the main funtion
def main(RES):
    #defines the res
    WIDTH = RES[0]
    HEIGHT = RES[1]

    #gets the ip and host name
    server = socket.gethostbyname(socket.gethostname())
    port = 5555

    #defines the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #tryes to bind the server to the port
    s.bind((server, port))

    s.listen(2)

    #inits the objects
    objects = [Paddle((20, 100), (60, HEIGHT // 2 - 50)),
        Paddle((20, 100), (WIDTH - 70, HEIGHT // 2 - 50)),
        Ball(20, (WIDTH//2 - 10, HEIGHT//2 - 10), (WIDTH, HEIGHT))]
    
    #sets the vars
    playerConn = []
    points = [0, 0]
    run = True

    for i in range(2):
        conn, addr = s.accept()# gets the client
        playerConn.append(conn)

        reply = {"yourP": (objects[i].x, objects[i].y),
            "otherP": (objects[not(i)].x, objects[not(i)].y),
            "ballPos": (objects[2].x, objects[2].y)}

        #sends the reply
        playerConn[i].sendall(pickle.dumps(reply))

    s.close()

    while run:
        try:
            objects[0].y = pickle.loads(playerConn[0].recv(2048))
            objects[1].y = pickle.loads(playerConn[1].recv(2048))
        except EOFError:
            break
        
        replyp1 = {"otherP": (objects[1].y), "points": points}
        replyp2 = {"otherP": (objects[0].y), "points": points}

        playerConn[0].sendall(pickle.dumps(replyp1))
        playerConn[1].sendall(pickle.dumps(replyp2))
    
    playerConn[0].close()
    playerConn[1].close()