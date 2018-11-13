import socket

serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serversocket.bind((socket.gethostname(),800))
print ("running on {}".format(socket.gethostname()))

servCmd = ""
while servCmd != "exit":
    serversocket.listen(5)
    client, address = serversocket.accept()
    print ("{} débute une session".format(address[0]))
    client.sendall("HTTP/1.1 200 OK\n\nBonjour, vous etes connecte sur {} entrez stop pour deconnecte le serveur".format(socket.gethostname()).encode())
    response = ""
    while response != "stop":
        response =  client.recv(255).decode()
        if response != "":
            print (response)
            client.sendall(response.encode())
        if response == "stop":
            client.sendall("fin de la connection".encode())
            servCmd = "exit"
print ("Close")
client.close()
socket.close()