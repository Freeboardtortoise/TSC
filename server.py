import _thread
sinit = []
connections = []


def init(ip):
    global sinit, connections
    current_ID = 100000
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
    sinit = [s, current_ID]
    return [s, current_ID]


def get_clients():
    global sinit, connections
    import client_function
    import _thread
    s = sinit[0]
    sinit[1] += 1
    conn, addr = s.accept()
    print("\n new connection:" + str(addr))
    _thread.start_new_thread(
        client_function.client_threaded, (conn, addr, sinit[1]))
    connections = connections + [[conn, addr, sinit[1]]]


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
