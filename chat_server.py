import Pyro4
import threading

# Classe do servidor
@Pyro4.expose
class ChatServer:
    def __init__(self):
        self.messages = []
        self.clients = []
        self.lock = threading.Lock()

    def send_message(self, message, username):
        with self.lock:
            self.messages.append(f"{username}: {message}")
        self.notify_clients(message)

    def get_messages(self):
        with self.lock:
            return self.messages

    def register_client(self, client):
        with self.lock:
            self.clients.append(client)

    def unregister_client(self, client):
        with self.lock:
            self.clients.remove(client)

    def notify_clients(self, message):
        with self.lock:
            for client in self.clients:
                client.receive_message(message)

# Inicialize o servidor Pyro4
if __name__ == "__main__":
    Pyro4.Daemon.serveSimple(
        {
            ChatServer: "chat.server"
        },
        host="localhost",
        port=9090
    )
