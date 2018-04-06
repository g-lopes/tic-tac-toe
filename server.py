# Save as server.py 
# Message Receiver
import os
from Game import Game
import Board
from socket import *
host = "localhost"
port = 13000
buf = 1024
addr = (host, port)

my_game = Game()

UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
print "Waiting to receive messages..."
while True:
    (data, addr) = UDPSock.recvfrom(buf)
    print("data received = " + data)
    while len(data) != 9:
        print("invalid game board. please send me another one :D")
        (data, addr) = UDPSock.recvfrom(buf)

    my_game.board = data
    print(my_game.board)
    my_game.getBoard()
    UDPSock.sendto(".!.", addr)


    if data == "exit":
        break
UDPSock.close()
os._exit(0)

