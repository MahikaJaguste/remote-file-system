import os

def process_request(payload):
    print(payload)
    cmd_num = payload.split('&!$')[0]
    print(cmd_num)
    payload = payload[len(cmd_num)+3:]
    response = ''

    if cmd_num == 'cwd':
        try:
            response = '0' + os.getcwd()
        except:
            response = '1Exception when getting current working directory'


    elif cmd_num == 'ls':
        try:
            response = '0' + str(os.listdir())
        except:
            response = '1Exception when listing directory contents'
        

    elif cmd_num == 'cd':
        cd_path = payload
        try:
            os.chdir(cd_path)
            response = '0Directory changed successfully'
        except:
            response = '1Exception when changing directory'
    

    elif cmd_num == 'dwd':
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

    elif cmd_num == 'upd':
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