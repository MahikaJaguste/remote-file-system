import socket
from client_encryption import encrypt

def client_system(payload):
    HOST = "127.0.0.1"  # The server's hostname or IP address
    PORT = 65432  # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        s.sendall(payload)
        print('CLIENT sent request ...')

        data = s.recv(2048)
        print('CLIENT received response ...')

    response = data.decode()

    # decrypt received response
    crypt_num = int(response[0])
    response = response[1:]

    answer = ''

    if crypt_num > 0 and crypt_num < 4:
        response = encrypt(response, crypt_num, 1)

    else:
        # error message
        answer = 'Invalid crypt mode'
        
    return [answer, response]