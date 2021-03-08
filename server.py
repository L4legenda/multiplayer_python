import socket
import threading
import pickle

soc = socket.socket()

soc.bind(("", 5000))

soc.listen(100)

listConnect = []

posPlayer = {}

def connectClient(conn, addr, index):
    while True:
        try:
            data = conn.recv(1024)
            posPlayer[index] = pickle.loads(data)
            conn.send(pickle.dumps(posPlayer))
            if not data:
                break
        except BaseException:
            break

    listConnect.pop(index)
    posPlayer.pop(index)
    conn.close()

while True:
    conn, addr = soc.accept()
    listConnect.append(conn)
    threading.Thread(target=connectClient, args=(conn, addr, len(listConnect) - 1)).start()

