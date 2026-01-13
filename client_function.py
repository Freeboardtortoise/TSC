import TSC.server as server

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives import serialization

import json

CONFIG_FILE = "config.json"
def getIDENTITY():
    try:
        with open(CONFIG_FILE) as f:
            data = json.load(f)
    except:
        data = {}

    data.setdefault("myIdentity", {})
    
    if not data["myIdentity"]:
        with open("password.txt", "r") as file:
            password = file.read()
        print("generating new key")

        priv = Ed25519PrivateKey.generate()
        pub = priv.public_key()

        priv_pem = priv.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.BestAvailableEncryption(password.encode())

        ).decode()

        pub_pem = pub.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).decode()

        data["myIdentity"] = {
            "private_key_pem": priv_pem,
            "public_key_pem": pub_pem
        }

        with open(CONFIG_FILE, "w") as f:
            json.dump(data, f, indent=2)

    else:
        # Load existing keys
        priv = serialization.load_pem_private_key(
            data["myIdentity"]["private_key_pem"].encode(),
            password=b"local-password"
        )

        pub = serialization.load_pem_public_key(
            data["myIdentity"]["public_key_pem"].encode()
        )
    return data["myIdentity"]["private_key_pem"], data["myIdentity"]["public_key_pem"]

def unSerialise(pub,priv):
    with open("password.txt", "r") as file:
        password = file.read()
    priv = serialization.load_pem_private_key(
        data["myIdentity"]["private_key_pem"].encode(),
        password=password.encode()
    )

    pub = serialization.load_pem_public_key(
        data["myIdentity"]["public_key_pem"].encode()
    )
    return priv,pub
def serialise(pub, priv):
    with open("password.txt", "r") as file:
        password = file.read()

    priv_pem = priv.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption(password.encode())

    ).decode()

    pub_pem = pub.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ).decode()
    return pub_pem, priv_pem

def client_threaded(conn, addr, ID):
    HANDSHAKE_PORT = 5528
    HANDSHAKE_PHRASE = "HYDRANET_HANDSHAKE"
    HANDSHAKE_REPLY = "HANDSHAKE_ACCEPTED"
    identity = getIDENTITY()
    while True:
        data = server.recieve(conn)
        reply = data
        if data == None:
            continue

        if data == HANDSHAKE_PHRASE:
            reply = HANDSHAKE_REPLY
        elif data.split(":::::")[0] == "IDENTITY":
            identity = data.split(":::::")[1]
            print(f"recieving IDENTITY {identity[1]}")
            reply = f"IDENTITY_RECIEVED:::::{getIDENTITY}"
        print(f"recieved: {data}... replying with: {reply} to {addr}")

        server.send(conn, reply)