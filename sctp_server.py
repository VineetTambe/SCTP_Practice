import socket
import sctp

host = socket.gethostname()
port = 1234

sock = sctp.sctpsocket_tcp(socket.AF_INET)
sock.bind((host, port))
sock.listen(5)

flag = True

while flag:
    # wait for a connection
    print ('waiting for a connection')
    connection, client_address = sock.accept()

    try:
        # show who connected to us
        #print ('connection from', client_address)
        #print (connection)
        # receive the data in small chunks and print it
        while True:
            data = connection.recv(999)
            if data:
                # output received data
                print ("Data: %s" % data)
                #connection.sendall(bytes("We recieved " + str(len(data)) + " bytes from you", 'utf-8'))
            else:
                # no more data -- quit the loop
                #print ("no more data.")
                break
        msg_ = input("Enter message to reply")
        if msg_ == '0':
            flag = False
        else:
            sock.sctp_send(msg=msg_)
            
    finally:
        # do nothing
        connection.close()
