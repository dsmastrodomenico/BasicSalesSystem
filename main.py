import sys

clients = [
    {
        'name': 'pablo',
        'company': 'google',
        'email': 'pablo@google.com',
        'position': 'software engineer',
    },
    {
        'name': 'ricardo',
        'company': 'facebook',
        'email': 'ricardo@facebook.com',
        'position': 'data engineer',
    },
    {
        'name': 'jose',
        'company': 'apple',
        'email': 'jose@apple.com',
        'position': 'marketing chief',
    }]


# Creación de Clientes
def create_client(client):
    global clients
    if client_exists(client['name']):
        _message_system(2.0)   
    else:
        clients.append(client)
       

# Borrar Clientes
def delete_client(client_id):
    global clients
    
    for idx, client in enumerate(clients):
        if idx == client_id - 1:
            del clients[idx] 
            break


# Actualizar Informacion de Clientes
def update_client(client_id, update_info_client):
    global clients

    if len(clients) - 1 >= client_id:
        clients[client_id - 1] = update_info_client        
    
    else:
        _message_system(2.1)


# Verificar si existe nombre de cliente en lista
def client_exists(client_name):
    global clients
    
    for client in clients:
        if client['name'] == client_name:
            return True


def client_search(search_option, search_value):
    global clients
    
    for client in clients:
        if client[search_option] == search_value:
            _message_system(2.0)
            return True
        else:
            _message_system(2.1)
            return False 


# Listar todos los clientes registrados
def list_client():
    global clients

    for idx, client in enumerate(clients):
        print('{uid}: {name} - {company} - {email} - {position}.'.format(
            uid = idx + 1,
            name = client['name'], 
            company = client['company'], 
            email = client['email'], 
            position = client['position'],))


def _get_client_field(num_option, field_name):
    field = None

    if num_option == 0:
        while not field:
            field = input('What is the client {}:.\n'.format(field_name)).lower()
    
    elif num_option == 1:
        while not field:
            field = input('Please, Write the new client {}:\n'.format(field_name)).lower()

    return field


def _get_client_from_user(num_option):
    client = {
        'name': _get_client_field(num_option,'name'),
        'company': _get_client_field(num_option,'company'),
        'email': _get_client_field(num_option,'email'),
        'position': _get_client_field(num_option,'position'),
    }

    return client


def _message_system(num_message):
    
    if num_message == 0.0:
        return print(('-' * 40) + '\n|' + (' ' * 13) + 
            'sales system'.upper() + (' ' * 13) + '|\n' + ('-' * 40))
    
    elif num_message == 0.1:
        return print('Thanks for everything.\nHave a nice day.')

    elif  num_message == 0.3:
        return print('Invalid command.')

    # menus
    elif  num_message == 1.0:
        print(
            'What do you like to do?\n' +
            '   [C]reate client.\n' +
            '   [U]pdate client.\n' + 
            '   [S]earch client.\n' +
            '   [D]elete client.\n' +
            '   [L]ist clients.\n' +
            '   [E]xit.')

    elif  num_message == 1.1:
        print(
            'Option for search:\n' +
            '   [I]d client.\n' +
            '   [N]ame client.\n' + 
            '   [E]mail client.\n' +
            '   [C]ancel.')

    # mensajes de informacion
    elif  num_message == 2.0:
        return print('Client is in the client\'s list!.')
    
    elif  num_message == 2.1:
        return print('Client isn\'t in the client\'s list!.')

    
def crud_scheme():
    while True:
        command = None
        command = input('\nOption:\t').upper()
        
        if command == 'C':
            client = _get_client_from_user(0)
            create_client(client)

        elif command == 'D':
            client_id = int(_get_client_field(0,'id'))
            delete_client(client_id)

        elif command == 'U':
            client_id = int(_get_client_field(0,'id'))
            update_info_client = _get_client_from_user(1)
            update_client(client_id, update_info_client)

        elif command == 'L':
            list_client()

        elif command == 'S':
            while True:
                _message_system(1.1)
                command = input('\nOption:\t').upper()
                
                if command == 'N':
                    search_ref = 'name'
                    client_search(search_ref,_get_client_field(0,search_ref))
                    
                elif command == 'E':
                    search_ref = 'email'
                    client_search(search_ref,_get_client_field(0,search_ref))
                    
                elif command == 'C':
                    command = None
                    break

            _message_system(1.0)

        elif command == 'E':
            _message_system(0.1)
            break

        else:
            _message_system(0.3)


if __name__ == '__main__':
    _message_system(0.0)
    _message_system(1.0)
    
    crud_scheme()


        
    