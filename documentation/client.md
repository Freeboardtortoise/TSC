# How to use TSC (Tortoise Server Client)

## How to Use TSC.client

### initialiseing the client

    import TSC.client
    TSC.client.init(server IP)

### send messages to the server

    TSC.client.send(message)

### Recieving messages from the server

To initialise allwaysC do the following

    TSC.client.allwaysC = True
    TSC.client.recieve_messages()

To get all of the messages in the storage run the following

    TSC.client.get_messages_all()

To get only the latest message run the following

    TSC.client.get_messages_latest()

To clear all of the messages run the following

    TSC.client.clear_messages()
