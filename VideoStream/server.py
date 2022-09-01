import socket, cv2, pickle, struct
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
port = 7788
socket_address = (host_ip,port)
server_socket.bind(socket_address)
server_socket.listen(5)
while True:
    client_socket, addr = server_socket.accept()
    if client_socket :
        vid = cv2.VideoCapture(0)
        while(vid.isOpened()):
            img, frame = vid.read()
            a = pickle.dumps(frame)
            message = struct.pack("Q",len(a)) + a
            client_socket.sendall(message)
            cv2.imshow("Transmitting Video: ",frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                client_socket.close()
