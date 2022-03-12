#imports
import socket, pickle, random
from threading import Thread
from online import getLocalIp
from Assets.gameCode.gameObjects import Paddle, Ball

connecting = True

def waiting(conn, s):
    while connecting:
        if pickle.loads(conn.recv(2048)):
            conn.sendall(pickle.dumps(None))
            s.close()
            exit()
        conn.sendall(pickle.dumps(True))
    conn.sendall(pickle.dumps(False))


#defines the main funtion
def main(RES):
    global connecting
    #defines the res
    WIDTH = RES[0]
    HEIGHT = RES[1]

    #gets the ip and host name
    server = getLocalIp.main()
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
    connecting = True
    playerConn = []
    points = [0, 0]
    run = True
    
    for i in range(2):
        try:
            conn, addr = s.accept()# gets the client
        except OSError:
            exit()
        playerConn.append(conn)
        #sends the reply
        if i == 0:
            playerConn[0].sendall(pickle.dumps((60, WIDTH - 70)))
            Thread(target=waiting, args=(playerConn[0], s, )).start()
        else:
            playerConn[1].sendall(pickle.dumps((WIDTH - 70, 60)))
            connecting = False

    s.close()

    while run:
        runFrame = True
        objects[0].y = HEIGHT // 2 - 50
        objects[1].y = HEIGHT // 2 - 50
        objects[2].x = WIDTH // 2 - 10
        objects[2].y = HEIGHT // 2 - 10
        objects[2].yVel = 0

        if points[0] > points[1]:
            objects[2].xVel = 3
        elif points[0] < points[1]:
            objects[2].xVel = -3
        else:
            objects[2].xVel = random.choice([-3,3])# default vel

        while runFrame:
            try:
                p1 = pickle.loads(playerConn[0].recv(2048))
                if p1 != None:
                    objects[0].move(p1, HEIGHT)
            except EOFError:
                playerConn[1].recv(2048)
                playerConn[1].sendall(pickle.dumps("exit"))
                break
            try:
                p2 = pickle.loads(playerConn[1].recv(2048))
                if p2 != None:
                    objects[1].move(p2, HEIGHT)
            except EOFError:
                playerConn[0].recv(2048)
                playerConn[0].sendall(pickle.dumps("exit"))
                break

            replyp1 = {"otherP": (objects[1].y),"yourP": (objects[0].y), "points": points, "ball": (objects[2].x, objects[2].y)}
            replyp2 = {"otherP": (objects[0].y),"yourP": (objects[1].y), "points": points, "ball": (objects[2].x, objects[2].y)}

            if objects[2].x < 0: # if the ball is on the left increace the score by 1 and restart
                points[1] += 1
                runFrame = False
            elif objects[2].x + objects[2].size > WIDTH:# if the ball is on the right increace the score by 1 and restart
                points[0] += 1
                runFrame = False

            objects[2].move((objects[0], objects[1]))

            playerConn[0].sendall(pickle.dumps(replyp1))
            playerConn[1].sendall(pickle.dumps(replyp2))
        
        if points[0] >= 7:
            playerConn[0].recv(2048)
            playerConn[1].recv(2048)
            playerConn[0].sendall(pickle.dumps(1))
            playerConn[1].sendall(pickle.dumps(1))
            run = False
        elif points[1] >= 7:
            playerConn[0].recv(2048)
            playerConn[1].recv(2048)
            playerConn[0].sendall(pickle.dumps(2))
            playerConn[1].sendall(pickle.dumps(2))
            run = False
    
    playerConn[0].close()
    playerConn[1].close()