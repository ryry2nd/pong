"""
starts the server
"""
#imports
import socket, pickle, random
from threading import Thread
from online import getLocalIp
from Assets.gameCode.game.gameObjects import Paddle, Ball

#is only true if it is connecting
connecting = True

# the waiting thread
def waiting(conn, s):
    while connecting:
        if pickle.loads(conn.recv(4)):# is True the reply is True
            conn.sendall(pickle.dumps(None))# sends the client nothing
            s.close()# closes the server
            exit()
        conn.sendall(pickle.dumps(True))# sends the client True because it is still connecting
    conn.sendall(pickle.dumps(False))# sends it False because it is done connecting


#defines the main function
def main(RES):
    global connecting# get global

    #defines the res
    WIDTH = RES[0]
    HEIGHT = RES[1]

    #gets the ip and host name
    server = getLocalIp.main()
    port = 5555

    #defines the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #starts the server
    s.bind((server, port))
    s.listen(2)

    #inits the objects
    objects = [Paddle((60, HEIGHT // 2 - 50)),#player 1
        Paddle((WIDTH - 70, HEIGHT // 2 - 50)),# player 2
        Ball((WIDTH//2 - 10, HEIGHT//2 - 10), (WIDTH, HEIGHT))]# ball
    
    #sets the vars
    connecting = True
    playerConn = []
    points = [0, 0]
    run = True
    
    #connects the variables
    for i in range(2):
        try:# if the s socket is closed, quit
            conn, addr = s.accept()# gets the client
        except OSError:
            exit()

        playerConn.append(conn)# appends the players connection
        
        #sends the reply
        if i == 0:# is true when player 1
            playerConn[0].sendall(pickle.dumps((60, WIDTH - 70)))# sends where it is and the other player
            Thread(target=waiting, args=(playerConn[0], s, )).start()# starts the connection thread
        else:
            playerConn[1].sendall(pickle.dumps((WIDTH - 70, 60)))# sends where it is and the other player
            connecting = False# stops the connection

    # stops searching
    s.close()

    #game loop
    while run:
        #resets the vars
        runFrame = True
        objects[0].y = HEIGHT // 2 - 50
        objects[1].y = HEIGHT // 2 - 50
        objects[2].x = WIDTH // 2 - 10
        objects[2].y = HEIGHT // 2 - 10
        objects[2].yVel = 0

        #says where the ball goes
        if points[0] > points[1]:
            objects[2].xVel = 3
        elif points[0] < points[1]:
            objects[2].xVel = -3
        else:
            objects[2].xVel = random.choice([-3,3])# default vel

        # loops every frame
        while runFrame:
            try:
                p1 = pickle.loads(playerConn[0].recv(4))
                if p1 != None:# if it is not getting nothing, move the paddle
                    objects[0].move(p1, HEIGHT)
            except EOFError:# if the person disconnected, send the disconnect code and quit
                playerConn[1].sendall(pickle.dumps(0))
                run = False
                break
            
            try:
                p2 = pickle.loads(playerConn[1].recv(4))
                if p2 != None:# if it is not getting nothing, move the paddle
                    objects[1].move(p2, HEIGHT)
            except EOFError:# if the person disconnected, send the disconnect code and quit
                playerConn[0].sendall(pickle.dumps(0))
                run = False
                break

            # defines the reply's
            replyP1 = {"otherP": (objects[1].y),"yourP": (objects[0].y), "points": points, "ball": (objects[2].x, objects[2].y)}
            replyP2 = {"otherP": (objects[0].y),"yourP": (objects[1].y), "points": points, "ball": (objects[2].x, objects[2].y)}

            if objects[2].x < 0: # if the ball is on the left increase the score by 1 and restart
                points[1] += 1
                runFrame = False
            elif objects[2].x + objects[2].size > WIDTH:# if the ball is on the right increase the score by 1 and restart
                points[0] += 1
                runFrame = False

            objects[2].move((objects[0], objects[1]))# move the ball

            #sends the reply's
            playerConn[0].sendall(pickle.dumps(replyP1))
            playerConn[1].sendall(pickle.dumps(replyP2))
        
        if points[0] >= 7:# if player1's points are >= 7 then player 1 wins
            playerConn[0].recv(4)
            playerConn[1].recv(4)
            #tells the clients who won
            playerConn[0].sendall(pickle.dumps(1))
            playerConn[1].sendall(pickle.dumps(1))
            run = False
        elif points[1] >= 7:# if player2's points are >= 7 then player 2 wins
            playerConn[0].recv(4)
            playerConn[1].recv(4)
            #tells the clients who won
            playerConn[0].sendall(pickle.dumps(2))
            playerConn[1].sendall(pickle.dumps(2))
            run = False
    
    # closes the connection
    playerConn[0].close()
    playerConn[1].close()