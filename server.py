import socket

def play_rps(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return "Empate"
    if (
        (player1_choice == 'rock' and player2_choice == 'scissors') or
        (player1_choice == 'scissors' and player2_choice == 'paper') or
        (player1_choice == 'paper' and player2_choice == 'rock')
    ):
        return "Jogador 1 vence"
    return "Jogador 2 vence"

def main():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(2)
    print("Aguardando jogadores...")

    player1, addr1 = server_socket.accept()
    print(f"Jogador 1 ({addr1}) conectado.")
    player1.send("Você é o Jogador 1. Faça sua escolha (rock, paper, scissors).\n".encode('utf-8'))

    player2, addr2 = server_socket.accept()
    print(f"Jogador 2 ({addr2}) conectado.")
    player2.send("Você é o Jogador 2. Faça sua escolha (rock, paper, scissors).\n".encode('utf-8'))

    player1_choice = player1.recv(1024).decode('utf-8').strip()
    player2_choice = player2.recv(1024).decode('utf-8').strip()

    result = play_rps(player1_choice, player2_choice)

    player1.send(result.encode('utf-8'))
    player2.send(result.encode('utf-8'))

    player1.close()
    player2.close()

    server_socket.close()

if __name__ == "__main__":
    main()
