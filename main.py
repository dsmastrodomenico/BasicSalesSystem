

clients = ''


def create_client(client_name):
    global clients
    clients += client_name
    _add_coma()


def _add_coma():
    global clients
    clients += ','


def list_client():
    global clients
    print(clients)


if __name__ == '__main__':
    create_client('darwin')
    create_client('daniel')
    list_client()
    