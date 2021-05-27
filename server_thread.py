# coding=utf-8
import socket
import pickle
import random
import time
import queue
import threading
import keyboard
import sys
from Crypto.Util import number

def decrypt(pk, ciphertext):
    #Descompacte a chave em seus componentes
    key, n = pk[0],pk[1]
    #Gere o texto simples com base no texto cifrado e chave usando a^b mod m
    plain = [chr((int(elt) ** key) % n) for elt in ciphertext]
    #Retorna a matriz de bytes como uma string
    return ''.join(plain)
   
class myThread (threading.Thread):
   def __init__(self, threadID,clientsocket,n,d):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.clientsocket = clientsocket
      self.n=n
      self.d=d
      
   def run(self):
       print ("Comecando a thread-{}".format(self.threadID))
       enc=self.clientsocket.recv(1024)
       encrypted_msg = pickle.loads(enc)
       car = chr((encrypted_msg[0]**self.d)%n)
       pos=decrypt((self.d,self.n),encrypted_msg[1:])
       msg_dec=car+pos
       l.append(msg_dec)
       print ("Finalizando thread-{}".format(self.threadID))



'''
Algoritmo de Euclides para determinar o maior divisor comum
Use a iteração para torna-lo mais rápido para inteiros maiores
'''
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

'''
O algoritmo estendido de Euclides para encontrar o inverso multiplicativo de dois numeros
'''
def multiplicacao_inversa(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi//e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        
        x = x2- temp1* x1
        y = d - temp1 * y1
        
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    
    if temp_phi == 1:
        return d + phi

'''
Checando para ver se um numero eh primo.
'''
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Ambos os numeros devem ser primos.')
    elif p == q:
        raise ValueError('p e q não podem ser iguais')
    n = p * q

    #Phi é o totiente de n
    phi = (p-1) * (q-1)

    #Escolha um inteiro e tal que e, phi(n) sejam numeros primos entre si
    e = random.randrange(1, phi)

    #Use o algoritmo de Euclides para verificar se e e phi(n) são comprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    #Use o algoritmo de euclides estendido para gerar a chave privada
    d = multiplicacao_inversa(e, phi)
    
    #Retornar par de chaves pública e privada
    #A chave pública é (e,n) e a chave privada (d,n)
    return ((e, n), (d, n))
if __name__=='__main__':
   start = time.time()

   host = 'localhost'
   port = 12800
   conexao_principal = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   conexao_principal.bind((host, port))
   conexao_principal.listen(5)

   conexao_cliente, infos_connexion = conexao_principal.accept()

   p = int(input("Insira um numero primo (17, 19, 23, etc): "))
   q = int(input("Digite outro numero primo (nao aquele que voce digitou acima): "))

   print(q,p)
   print("Gerando seus pares de chaves publica/privada . . .")
   public, private = generate_keypair(p, q)
   print ("Sua chave publica eh ", public ," e sua chave privada eh ", private)

   e=public[0]
   n=public[1]


   conexao_cliente.send((str(e)).encode())
   conexao_cliente.send((str(n)).encode())
   comprimento = conexao_cliente.recv(1024)
   comprimento = int(comprimento.decode())

   global l
   l=[]
   threads = []
   for i in range(comprimento):
       print( "Esperando...")
       newthread = myThread(i,conexao_cliente,n,private[0])
       newthread.start()
       threads.append(newthread)

   # Espere que todos os tópicos sejam concluídos
   for t in threads:
      t.join()
   print ("Saindo da Thread principal")

   print("l=   ",l)

   dict={int(l[i][1:]):l[i][0] for i in range(len(l))}
   ch=""
   for cl in range(len(l)):
       ch=ch+str(dict[cl])


   print
   print("Sua Mensagem eh:")
   print(ch)
   
   end = time.time()
   print("O programa terminou em (tempo) ",end - start)
   print
   print("Fechando a conexão")
   
   print("Pressione Esc para sair: ")
   while True:
        try:
            if keyboard.is_pressed('Esc'):
                print("\nvocê pressionou Esc, saindo...")
                sys.exit(0)
        except:
            break

   conexao_cliente.close()
   conexao_principal.close()

