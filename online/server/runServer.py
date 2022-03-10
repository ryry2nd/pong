import socket, pickle
from _thread import *
from Assets.gameCode.gameObjects import Paddle

timedOut = False
numPlayers = 0
points = []

def threaded_client(conn, player):
    reply = {"yourP": [players[player].x, players[player].y],
        "otherP": [players[not(player)].x, players[not(player)].y]}

    conn.sendall(pickle.dumps(reply))
    reply = ""
    while True:
            data = pickle.loads(conn.recv(2048))
            players[player] = Paddle((20, 100), (60, data))

            if not data:
                print("Disconnected")
            else:
                if player == 1:
                    reply = {"otherP": (players[0].y), "points": points,
                    "printIp": False, "stop": False}
                else:
                    reply = {"otherP": (players[1].y), "points": points,
                    "printIp": False, "stop": False}

                if numPlayers == 1:
                    reply["printIp"] = True

                    if timedOut:
                        reply["stop"] = True
                    

            conn.sendall(pickle.dumps(reply))

    print("Lost connection")
    conn.close()

def main(RES):
    global players, points, numPlayers, timedOut

    WIDTH = RES[0]
    HEIGHT = RES[1]

    server = socket.gethostbyname(socket.gethostname())
    port = 5555

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind((server, port))

    s.listen(2)

    print("Waiting for a connection, Server Started")

    players = [Paddle((20, 100), (60, HEIGHT // 2 - 50)), Paddle((20, 100), (WIDTH - 70, HEIGHT // 2 - 50))]
    points = [0, 0]
    timedOut = False
    numPlayers = 0

    s.settimeout(30)
    try:
        while numPlayers <= 2:
            conn, addr = s.accept()
            start_new_thread(threaded_client, (conn, numPlayers))
            numPlayers += 1
    except socket.timeout:
        print("Server Timed out")

    timedOut = True
    print("Server Stoped Searching for ip's")