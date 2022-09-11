import socket
from encryption import encrypt
from server_file_service import process_request

def server_system():
    HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
    PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(2048)
                if not data:
                    break

                payload = data.decode()
                print('SERVER recieved request ...')

                crypt_num = int(payload[0])
                payload = payload[1:]

                # starts with 0 for OK and 1 for error repsonse
                response = ''

                if crypt_num > 0 and crypt_num < 4:
                    payload = encrypt(payload, crypt_num, 1)
                    response = process_request(payload)

                else:
                    # error message
                    response = '1Invalid crypt mode'
            
                response = encrypt(response, crypt_num)
                response = str(crypt_num) + response
                
                print('SERVER sent response ...')

                conn.sendall(bytes(response, 'utf-8'))

server_system()