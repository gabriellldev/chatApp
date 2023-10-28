import Pyro4
import threading

# Interface para notificações do servidor
@Pyro4.expose
class ChatClientNotifier:
    def receive_message(self, message):
        pass

# Classe do cliente
class ChatClient(ChatClientNotifier):
    def __init__(self, username, server):
        self.username = username
        self.server = server
        self.server.register_client(self)

    def send_message(self, message):
        self.server.send_message(message, self.username)

    def receive_message(self, message):
        print(message)

# Configuração do cliente
def main():
    Pyro4.config.SERVERTYPE = "thread"
    server = Pyro4.Proxy("PYRONAME:chat.server")
    username = input("Digite seu nome de usuário: ")
    
    # Inicialize o cliente
    client = ChatClient(username, server)

    while True:
        message = input()
        client.send_message(message)

if __name__ == "__main__":
    main()
