import socket, pickle
from _thread import *
import threading
from Assets.gameObjects import Paddle

currentPlayer = 0
players = []
points = []

def threaded_client(conn, player):
    reply = {"yourP": [players[player].x, players[player].y],
        "otherP": [players[not(player)].x, players[not(player)].y]}

    conn.sendall(pickle.dumps(reply))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = Paddle((20, 100), (60, data))

            if not data:
                print("Disconnected")
            else:
                if player == 1:
                    reply = {"otherP": (players[0].y), "points": points, "printIp": False}
                else:
                    reply = {"otherP": (players[1].y), "points": points, "printIp": False}

                if currentPlayer == 1:
                    reply["printIp"] = True
                    

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    conn.close()

def main(RES):
    global players, points, currentPlayer

    WIDTH = RES[0]
    HEIGHT = RES[1]

    server = socket.gethostbyname(socket.gethostname())
    port = 5555

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.bind((server, port))
    except socket.error as e:
        str(e)

    s.listen(2)

    print("Waiting for a connection, Server Started")

    players = [Paddle((20, 100), (60, HEIGHT // 2 - 50)), Paddle((20, 100), (WIDTH - 70, HEIGHT // 2 - 50))]
    points = [0, 0]

    while currentPlayer <= 2:
        conn, addr = s.accept()
        start_new_thread(threaded_client, (conn, currentPlayer))
        currentPlayer += 1