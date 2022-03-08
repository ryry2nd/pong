import socket, pickle
from _thread import *
from Assets.gameObjects import Paddle

players = []
points = []

def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = Paddle((20, 100), (60, data))

            if not data:
                print("Disconnected")
            else:
                if player == 1:
                    reply = {"otherP": players[0].y, "points": points}
                else:
                    reply = {"otherP": players[1].y, "points": points}

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    conn.close()

def main(RES):
    global players, points

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

    currentPlayer = 0
    while True:
        conn, addr = s.accept()

        start_new_thread(threaded_client, (conn, currentPlayer))
        currentPlayer += 1