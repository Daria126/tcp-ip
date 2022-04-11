from socket import socket
from threading import Thread
from yaml import full_load

# Creating yaml file
# data = {'host_name': '', 'port': 9100}
# with open('config_server.yaml', 'w') as config_file:
#     yaml.dump(data, config_file)

with open('config_server.yaml', 'r') as config:
    config = full_load(config)

host_name, port, buffer = config['host_name'], config['port'], config['buffer_size']


def start_server(host='', port=9100):
    serv_socket = create_socket(host, port)
    while True:
        cli_socket, host_address = serv_socket.accept()
        print(f'Connected to: {host_address}')
        th = Thread(target=serve_client, args=(cli_socket, ))
        th.start()


def create_socket(host, serv_port):
    new_socket = socket()
    new_socket.bind((host, serv_port))
    new_socket.listen(5)
    return new_socket


def serve_client(cli_socket):
    request_data = get_request(cli_socket)
    if request_data is None:
        print('Client disconnected')
        # cli_socket.close()            #should the connection be closed or not
    else:
        send_response(cli_socket, request_data)


def get_request(cli_socket):
    try:
        while True:
            request = cli_socket.recv(buffer)
            # if not request:
            #     return None
            if request.decode('utf-8') != 'ping':
                cli_socket.send(bytes('Invalid', 'UTF-8'))
            else:
                break
        return request

    except Exception as e:
        print(f'Data is not valid. type={type(e)}: {str(e)}')
        return None


def send_response(cli_socket, request):
    cli_socket.send(bytes('pong', 'UTF-8'))
    cli_socket.close()


if __name__ == '__main__':
    start_server(host_name, port)






# try:
#     data = conn_socket.recv(1024)
# except Exception as e:
#     print(f'Data is not valid. type={type(e)} {str(e)}')
# else:
#     print('Message received\n...')
#     conn_socket.send(data.upper())
#     print('Message sent')
# finally:
#     conn_socket.close()


# try:
#     while True:
#         data = conn_socket.recv(1024)
#         if not data:
#             break
# except Exception as e:
#     print(f'Data is not valid. type={type(e)} {str(e)}')
# else:
#     print('Message received\n...')
#     conn_socket.send(data.upper())
#     print('Message sent')
# finally:
#     conn_socket.close()

