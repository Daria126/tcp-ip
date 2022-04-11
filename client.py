from socket import *
import yaml

with open('config_client.yaml', 'r') as config:
    config = yaml.full_load(config)

server_name, port, buffer = config['server_name'], config['port'], config['buffer_size']


def start_client(server_name, port):
    client_socket = socket()
    try:
        print('Connecting to the server...')
        client_socket.connect((server_name, port))
        print('Connected')
    except Exception as e:
        print(f'Connection failed.\n'
              f'type={type(e)}: {str(e)}')
    serv_comm(client_socket)


def serv_comm(client_socket):
    while True:
        print('Print your input')
        client_socket.send(bytes(input(), encoding='UTF-8'))
        recv_data = client_socket.recv(buffer)
        if recv_data.decode('utf-8') == 'pong':
            break
    client_socket.close()
    print('server session ended')


if __name__ == '__main__':
    start_client(server_name, port)





# try:
#     recv_data = new_socket.recv(1024)
# except:
#     print('Data is not valid')
# else:
#     recv_data = recv_data.decode('utf-8')
#     print(f'Received message is \'{recv_data}\'')
# finally:
#     new_socket.close()




