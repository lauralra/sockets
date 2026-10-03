import socket

HOST = '127.0.0.1'  # Endereco IP do Servidor
PORT = 50000        # Porta que o Servidor está

# Criando a conexão
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
destino = (HOST, PORT)
tcp.connect(destino)

print('\nDigite suas mensagens')
print('Para sair use CTRL+X e ENTER\n')

# Enviando as mensagens para o Servidor TCP através da conexão
try:
    # Recebendo a mensagem do usuário final pelo teclado
    mensagem = input()
    while '\x18' not in mensagem:
        tcp.send(str(mensagem).encode())
        mensagem = input()
except (KeyboardInterrupt, EOFError):
    # CTRL+C ou CTRL+Z também encerram o cliente
    pass

# Fechando o Socket
tcp.close()
