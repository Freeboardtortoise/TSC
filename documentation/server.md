# How to use TSC (Tortoise Server Client)

## Server

    import TSC.server
    currentServer = server.Server(port)

### scan for clients

    TSC.server.get_clients_threaded(client_function)

make sure to pass the client_function (this is the function that will be called when a new client joins)
### client_function
basic client function to pass into the get_clients_threaded() function
```
def client_threaded(conn, addr, ID):
    while True:
        data = server.recieve(conn)
        reply = data
        if data == None:
            continue
        print(f"recieved: {data}... replying with: {reply} to {addr}")

        server.send(conn, reply)
```
### send things to clients (use this in the client function in the TSC/client_function in order to have the conn

    TSC.server.send(conn, reply)

### listen for sends from the client (use the is in the client function in the client_function in order to do something with the connection to the client)

    TSC.server.recieve(conn)