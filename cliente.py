import pyautogui as pag
from time import sleep

class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
    
    def __eq__(self, other):
        if isinstance(other, Cliente):
            return self.nome == other.nome and self.telefone == other.telefone
        return NotImplemented

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__ (self):
        return hash((self.nome, self.telefone))

class Lista_de_clientes:
    def __init__(self, *clientes):
        self.__clientes = {*clientes}

    def __str__ (self):
        clientes = []
        for cliente in self.__clientes:
            clientes.append(f'Nome: {cliente.nome}, Telefone: {cliente.telefone}')
        return "\n".join(clientes)

    def adiciona_cliente(self, cliente: Cliente):
        if cliente.telefone not in [cliente.telefone for cliente in self.__clientes]:
            self.__clientes.add(cliente)
        else:
            print('Cliente já consta na lista!')
    
    @property
    def clientes(self):
        return self.__clientes
