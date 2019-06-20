import sys

# clients = list(('Ramiro', 'Daniel', 'Jose'))
clients = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position': 'Software engineer',
    },
    {
        'name': 'Ricardo',
        'company': 'Facebook',
        'email': 'ricardo@facebook.com',
        'position': 'Data engineer',
    },
    {
        'name': 'Jose',
        'company': 'Apple',
        'email': 'jose@apple.com',
        'position': 'marketing chief',
    }]

def create_client(client):
    global clients
    if client_exists(client):
        _message_system(1)
    else:
        # clients += client_name
        # _add_coma()
        clients.append(client)
       

def delete_client(client):
    global clients
    if client_exists(client):
        # clients = clients.replace(client_name, '')
        clients.remove(client)
    else:
        _message_system(2)


def update_client(client_name, new_client_name):
    global clients
    if client_exists(client_name):
        # clients = clients.replace(client_name, new_client_name)
        while True:
            if client_exists(new_client_name):
                _message_system(1)
                new_client_name = _get_cliente_name(1)
            else:
                pos = clients.index(client_name) 
                # clients.pop(pos)
                # clients.insert(pos, new_client_name)
                clients[pos] = new_client_name
                break              
    else:
        _message_system(2)

"""
def search_client(client_name):
    clients_list = clients.split(', ')
    for client in clients:
        if client != client_name:
            continue
        else:
            return True
"""

def client_exists(client):
    global clients
    # if client_name+','in clients:
    if client in clients:
        return True

"""
def _add_coma():
    global clients
    clients += ', '
"""

def list_client():
    global clients
    # print(clients)
    for idx, client in enumerate(clients):
        print('{}: {}'.format(idx, client))


def _print_menu():
    print(('*' * 50) + '\nWELCOME TO PLATZI VENTAS\n' + ('*' * 50))
    print('What do you like to do today?')
    print('[C]reate client.')
    print('[U]pdate client.')
    print('[S]earch client')
    print('[D]elete client.')
    print('[L]ist clients')
    print('[E]xit')


def _message_system(num_message):
    if num_message == 0:
        return print('Thanks for everything.\nHave a nice day.')
    elif num_message == 1:
        return print('Client is in the client\'s list!.')
    elif  num_message == 2:
        return print('Client isn\'t in the client\'s list!.')
    elif  num_message == 3:
        return print('Invalid command.')


def _get_client_field(num_option, field_name):
    field = None

    if num_option == 0:
        while not field:
            field = input('What is the client {}:.\n'.format(field_name)).capitalize()
    
    elif num_option == 1:
        while not field:
            field_name = input('Please, Write the new client {}:\n'.format(field_name)).capitalize()

    return field


def _get_cliente_name(num_option):
    client_name = None

    if num_option == 0:
        while not client_name:
            client_name = input('What is the client name?.\n').capitalize()
        
    elif num_option == 1:
        while not client_name:
            client_name = input('Please, Write the new client name:\n').capitalize()

    return client_name

def crud_scheme():
    while True:
        command = input('\nOption:\t').upper()
        
        if command == 'C':
            client = {
                'name': _get_client_field(0,'name'),
                'company': _get_client_field(0,'company'),
                'email': _get_client_field(0,'email'),
                'position': _get_client_field(0,'position')
            }
            # client_name = _get_cliente_name(0)
            create_client(client)

        elif command == 'D':
            client_name = _get_cliente_name(0)
            delete_client(client_name)

        elif command == 'U':
            client_name = _get_cliente_name(0)
            if client_exists(client_name):
                update_client_name = _get_cliente_name(1)
                update_client(client_name, update_client_name)
            else:
                _message_system(2)

        elif command == 'L':
            list_client()

        elif command == 'S':
            client_name = _get_cliente_name(0)
            if client_exists(client_name):
                _message_system(1)
            else:
                _message_system(2)

        elif command == 'E':
            _message_system(0)
            break

        else:
            _message_system(3)


if __name__ == '__main__':
    _print_menu()
    
    crud_scheme()


        
    