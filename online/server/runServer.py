#imports
import socket, pickle
from _Thread import *
from Assets.gameCode.gameObjects import Paddle, Ball

#defines globals
timedOut = False
numPlayers = 0
players = []
ball = None
points = []

#defines the threaded client
def threaded_client(conn, player, mainServer):
    #defines the start up reply
    reply = {"yourP": (players[player].x, players[player].y),
        "otherP": (players[not(player)].x, players[not(player)].y),
        "ballPos": (ball.x, ball.y)}

    #sends the reply
    conn.sendall(pickle.dumps(reply))
    reply = ""
    while True:
        try:
            #receves the data
            data = pickle.loads(conn.recv(2048))
            #sets the player's y position to the data
            players[player].y = data

            # if there is no data then it is disconected
            if not data:
                print("Disconnected")
            else:
                if player == 1:#if it is player 1 reply the data for it
                    reply = {"otherP": (players[0].y), "points": points,
                    "printIp": False, "stop": False}
                else:#if it is player 2 reply the data from it
                    reply = {"otherP": (players[1].y), "points": points,
                    "printIp": False, "stop": False}

                # if there is only 1 player request the client to print the ip
                if numPlayers == 1:
                    reply["printIp"] = True

                    #if it is timed out, request the clint to leave
                    if timedOut:
                        reply["stop"] = True
                    
            #send the data
            conn.sendall(pickle.dumps(reply))
        except:# if there is an error, break
            break

    # if it is here it means it lost conection
    print("Lost connection")
    #close the main server and the connection
    mainServer.close()
    conn.close()

#defines the main funtion
def main(RES):
    #gets the globals
    global players, points, numPlayers, timedOut, ball

    #defines the res
    WIDTH = RES[0]
    HEIGHT = RES[1]

    #gets the ip and host name
    server = socket.gethostbyname(socket.gethostname())
    port = 5555

    #defines the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #tryes to bind the server to the port
    try:
        s.bind((server, port))
    except socket.error as e:
        str(e)

    s.listen(2)

    print("Waiting for a connection, Server Started")

    #inits the objects
    players = [Paddle((20, 100), (60, HEIGHT // 2 - 50)), Paddle((20, 100), (WIDTH - 70, HEIGHT // 2 - 50))]
    ball = Ball(20, (WIDTH//2 - 10, HEIGHT//2 - 10), (WIDTH, HEIGHT))
    #sets the vars
    points = [0, 0]
    timedOut = False
    numPlayers = 0
    
    s.settimeout(30)# sets the time out to 30 seconds
    try:
        while numPlayers <= 2:
            conn, addr = s.accept()# gets the client
            start_new_thread(threaded_client, (conn, numPlayers, s))# starts the thread
            numPlayers += 1
    except socket.timeout:# if it timed out say so and set the timeout var to true
        print("Server Timed out")
        timedOut = True
        
    print("Server Stoped Searching for ip's")