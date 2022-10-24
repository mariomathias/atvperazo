from threading import Thread
import threading
import time
import random

semaforo = threading.Semaphore(3)

clientes = []

class Nodo:
    """Esta classe representa um nodo de uma estrutura duplamente encadeada."""
    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)

class Fila:
    """Esta classe representa uma fila usando uma estrutura encadeada."""
    def __init__(self):
        self.primeiro = None
        self.ultimo   = None

    def __repr__(self):
        return "[" + str(self.primeiro) + "]"

    def insere(self, novo_dado):
        # Cria um novo nodo com o dado a ser armazenado.
        novo_nodo = Nodo(novo_dado)

        # Insere em uma fila vazia.
        if self.primeiro == None:
            self.primeiro = novo_nodo
            self.ultimo = novo_nodo
        else:
            # Faz com que o novo nodo seja o último da fila.
            self.ultimo.proximo = novo_nodo

            # Faz com que o último da fila referencie o novo nodo.
            self.ultimo = novo_nodo
    
    def remove(self):
        self.primeiro = self.primeiro.proximo

        if self.primeiro == None:
            self.ultimo = None

fila = Fila()

for i in range(1, 31):
    fila.insere(i)

def atendimento():
    semaforo.acquire()
    while fila.primeiro != None:
        fila.remove()
        time.sleep(random.randint(1,2))
        print("Situação da fila:", fila)
    semaforo.release()

t1 = threading.Thread(target=atendimento, args = [])
t2 = threading.Thread(target=atendimento, args = [])
t3 = threading.Thread(target=atendimento, args = [])

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()