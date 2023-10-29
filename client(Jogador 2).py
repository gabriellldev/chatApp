import socket

def main():
    host = '127.0.0.1'
    port = 12345

    player_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    player_socket.connect((host, port))
    message = player_socket.recv(1024).decode('utf-8')
    print(message)

    player_name = player_socket.recv(1024).decode('utf-8')
    print(player_name)

    if "Jogador 2" in player_name:
        choice = input("Faça sua escolha (rock, paper, scissors): ")
        player_socket.send(choice.encode('utf-8'))
    else:
        print("Aguarde a escolha do Jogador 1.")

    result = player_socket.recv(1024).decode('utf-8')
    print(result)

    player_socket.close()

if __name__ == "__main__":
    main()
