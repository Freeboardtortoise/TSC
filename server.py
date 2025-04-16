import _thread
sinit = []
connections = []


def init(ip):
    global sinit, connections
    IDs_used = [1]
    import socket
    print("Made with TSC")
    print("Darion Knighton-Fitt")
    server = ip
    port = 5555
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.bind((server, port))
        print("server started")
    except socket.error as e:
        print("ERROR, try again")
        print(e)

    s.listen()
    print("waiting for connection")
    sinit = [s, IDs_used]


def get_clients():
    global sinit, connections
    import TSC.client_function as client_function
    import _thread
    s = sinit[0]
    IDs_used = sinit[1]
    current_ID = 1
    import random
    while current_ID in IDs_used:
        current_ID = random.randint(10000000, 999999999)

    sinit[1] = sinit[1] + [current_ID]
    conn, addr = s.accept()
    print("\n new connection:" + str(addr))
    _thread.start_new_thread(
        client_function.client_threaded, (conn, addr, sinit[1]))
    connections = connections + [[conn, addr, current_ID]]


def recieve(conn):
    try:
        data = conn.recv(2048)
        data = data.decode("utf-8")

        if not data:
            return None
        else:
            return data
    except:
        return None


def send(conn, reply):
    try:
        conn.sendall(str.encode(reply))
        return True
    except:
        return False


def get_initc():
    global initc
    return initc


def get_connections():
    global connections
    return connections


def do_not_use():
    while True:
        get_clients()


def get_clients_threaded():
    _thread.start_new_thread(do_not_use, ())
