import socket
import sctp

sk = sctp.sctpsocket_tcp(socket.AF_INET)
sk.connect((socket.gethostname(), 1234))

flag = True
while flag:
    
    msg_ = input("Enter a message to send")
    if msg_ == '0':
        break

    print("Sending Message")
    
    sk.sctp_send(msg=msg_)
    while True:
        data = sk.recv(999)
        if data:
            # output received data
            print ("Data: %s" % data)
            #connection.sendall(bytes("We recieved " + str(len(data)) + " bytes from you", 'utf-8'))
        else:
            # no more data -- quit the loop
            #print ("no more data.")
            break


sk.shutdown(0)
sk.close()
