# How to use TSC (Tortoise Server Client)

# base functionality

### Server

import TSC.server
TSC.server.init(server IP)

#### scan for clients
TSC.server.get_clients()

#make sure to put the client function in the TSC/client_function.py (this is the function that will be called when a new client joins)

#### send things to clients (use this in the client function in the TSC/client_function in order to have the conn
TSC.server.send(conn, reply)

#### listen for sends from the client (use the is in the client function in the TSC/client_function in order to have the conn
TSC.server.recieve(conn)

## Client

#### initialise

import TSC.client
TSC.client.init(server IP)

#### send messages to the server
TSC.client.send(message)


## Plugins
find the documentation for importing plugins in the folowing file /TSC/documentation/importing_plugins.md and /TSC/documentation/developin_/plugins.md
