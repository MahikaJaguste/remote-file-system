import os
from encryption import encrypt

def process_request(crypt_num, payload):

    cmd_num = int(payload[0])
    payload = payload[1:]
    response = ''

    if cmd_num == 1:
        try:
            response = '0' + os.getcwd()
        except:
            response = '1Exception when getting current working directory'


    elif cmd_num == 2:
        try:
            response = '0' + str(os.listdir())
        except:
            response = '1Exception when listing directory contents'
        

    elif cmd_num == 3:
        cd_path = payload
        try:
            os.chdir(cd_path)
            response = '0Directory changed successfully'
        except:
            response = '1Exception when changing directory'
    

    elif cmd_num == 4:
        dwd_file = payload
        try:
            f = open(dwd_file, "r")
            try:
                file_content = f.read()
                response = '0' + dwd_file + '&!$' + file_content
            except:
                response = '1Exception occurred while reading file'
            f.close()
        except:
            response = '1Exception occurred while opening file'

    elif cmd_num == 5:
        try:
            (file_name, file_content) = payload.split('&!$')
            file_name = file_name.split('/')[-1]
            f = open(file_name, "w")
            f.write(file_content)
            f.close()
            response = '0' + file_name + ' uploaded successfully'
        except:
            response = '1Exception occurred while writing file'

    else:
        response = '1Invalid command'

    return response

# payloads = ['1', '2', '4./client_file_system/client_sample_file.txt', '4server_sample.txt',  '3../', '3../hell']
# for payload in payloads:
#     process_request(1, payload)