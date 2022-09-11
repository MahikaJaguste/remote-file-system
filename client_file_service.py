from encryption import encrypt
from echo_client import client_system

def main():

    payload = ''

    cmd_num = int(input('''What action do you want to perform? (Enter number from 1-5)
    1. cwd
    2. ls 
    3. cd
    4. dwd
    5. upd
    '''))
    
    if cmd_num == 1:
        payload = 'cwd'

    elif cmd_num == 2:
        payload = 'ls'

    elif cmd_num == 3:
        payload = 'cd' + '&!$'
        cd_path = input('''Enter path to change directory to:''')
        payload += cd_path
    
    elif cmd_num == 4:
        payload = 'dwd' + '&!$'
        dwd_file = input('''Enter filename to download:''')
        payload += dwd_file

    elif cmd_num == 5:
        payload = 'upd' + '&!$'
        upload_file = input('''Enter filename to upload:''')
        try:
            f = open(upload_file, "r")
            try:
                file_content = f.read()
                payload += upload_file + '&!$' + file_content
            except:
                print("Exception occurred while reading file")
                f.close()
                quit()
        except:
            print("Exception occurred while opening file")
            quit()


    else:
        print("Invalid command")
        quit()

    crypt_num = int(input('''What mode of encryption do you want? (Enter number from 1-3)
    1. Plaintext
    2. Substitute
    3. Transpose
    '''))
    
    if crypt_num > 0 and crypt_num < 4:
        payload = encrypt(payload, crypt_num)
        payload = str(crypt_num) + payload

    else:
        print("Invalid command")
        quit()

    print('--')

    # send payload via echo client
    (answer, response) = client_system(bytes(payload, 'utf-8'))
    if(answer != 'Invalid crypt mode'):
        answer = process_response(cmd_num, answer, response)

    print(answer)




def process_response(cmd_num, answer, response):
    # process received response
    error_flag = int(response[0])
    response = response[1:]

    if error_flag:
        answer = response
    
    else:
        if cmd_num == 1:
            answer = response 

        elif cmd_num == 2:
            answer = eval(response)
            
        elif cmd_num == 3:
            answer = 'Directory changed successfully'

        elif cmd_num == 4:
            try:
                (file_name, file_content) = response.split('&!$')
                file_name = file_name.split('/')[-1]
                f = open(file_name, "w")
                f.write(file_content)
                f.close()
                answer = file_name + ' downloaded successfully.'
            except:
                answer = 'Exception occurred while downloading file. File content is:\n' + file_content


        elif cmd_num == 5:
            answer = response

        else:
            answer = 'Invalid command'

    return answer


main()