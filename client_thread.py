# coding=utf-8
import socket
import pickle
import threading
import time
import keyboard
import sys

class myThread (threading.Thread):
   def __init__(self, threadID,name,data):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.data=data
      
   def run(self):
        #print ("Comecando " + self.name)
        print(self.data)
        encrypted_char=[(ord(char) ** e) % n for char in self.data]
        
        enc = pickle.dumps(encrypted_char)
        
        conexao_servidor.sendall(enc)
        #print("Saindo " + self.name)
      
if __name__=='__main__':

   host = "localhost"
   port = 12800
   conexao_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   conexao_servidor.connect((host, port))
   print("Conexao estabelecida com o servidor na porta {}".format(port))


   e = conexao_servidor.recv(1024)
   e = int(e.decode())

   n = conexao_servidor.recv(1024)
   n = int(n.decode())

   print(e,n)

   message = input("Insira uma mensagem para criptografar com sua chave pública: ")
   conexao_servidor.send((str(len(message))).encode())
   print("tamanho da mensagem:")
   print(len(message))

   threadList = ["Thread-{}".format(i) for i in range(1,len(message)+1)]
   chars=[message[i]+str(i) for i in range(len(message))]
   threads = []
   threadID = 0
   # Cria novas threads
   time.sleep(1)
   for tName in threadList:
       thread = myThread(threadID, tName,chars[threadID])
       thread.start()
       thread.join()
       threads.append(thread)
       threadID += 1

   # Espere que todos os tópicos sejam concluídos
   for t in threads:
      t.join()
   print ("Saindo da Thread principal")
   
   print("Fechando a conexão")
   
   print("Pressione ESC para sair ")
   while True:
    try:
        if keyboard.is_pressed('Esc'):
            print("\nVocê pressionou ESC, saindo...")
            sys.exit(0)
    except:
        break

   conexao_servidor.close()
