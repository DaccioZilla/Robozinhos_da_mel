import webbrowser
import pyautogui as pag
from time import sleep
from cliente import Cliente, Lista_de_clientes
import clientes_data as clientes

class WhatsappWeb:
    def __init__(self):
        self.__messenger_ativo = False
        self.__campo_busca = None


    @property
    def messenger_ativo(self):
        return self.__messenger_ativo
    
    @messenger_ativo.setter
    def messenger_ativo(self, value):
        self.__messenger_ativo = value
    
    @property
    def campo_busca(self):
        return self.__campo_busca
    
    @ campo_busca.setter
    def campo_busca(self, value):
        self.__campo_busca = value

    
    def abre_wpp_web(self):
        botoes = pag.locateOnScreen('wpp_buttons.png')
        
        if botoes is not None:
            self.messenger_ativo = True
            self.campo_busca = pag.locateCenterOnScreen('busca_wpp_web.png')

        elif not self.messenger_ativo:
            webbrowser.open('https://web.whatsapp.com/')

            max_tries = 0
            while True and max_tries <= 500:
                botoes = pag.locateOnScreen('wpp_buttons.png')
                sleep(1)
                max_tries += 1
                if botoes is not None:
                    self.messenger_ativo = True
                    self.campo_busca = pag.locateCenterOnScreen('busca_wpp_web.png')
                    break
            print('Campo de busca não detectado')

    def envia_pesquisa_satisfacao(self, lista_cliente):
        self.abre_wpp_web()

        for cliente in lista_cliente:
            pag.click(self.campo_busca)
            sleep(1)
            pag.write(cliente.telefone)
            sleep(1)
            pag.press('tab')
            sleep(1)
            pag.press('enter')
            sleep(1)
            pag.write(f'Oi, {cliente.nome}! Foi um prazer ter voce aqui!')
            pag.hotkey('shift', 'enter')
            pag.write('Queremos ouvir voce, entao nao deixe de responder a pesquisa em https://forms.gle/QZ7qWgp5q6tFcroAA')
            pag.hotkey('shift', 'enter')
            pag.write('Obrigada!!!')
            pag.click(self.campo_busca)
            sleep(1)

if __name__ == '__main__':
    app = WhatsappWeb()
    cliente1 = Cliente(clientes.cliente1['nome'], clientes.cliente1['telefone'])
    cliente2 = Cliente(clientes.cliente1['nome'], clientes.cliente1['telefone'])
    cliente3 = Cliente(clientes.cliente3['nome'], clientes.cliente3['telefone'])
    cliente4 = Cliente(clientes.cliente2['nome'], clientes.cliente2['telefone'])
    lista = Lista_de_clientes(cliente1, cliente2, cliente3, cliente4)
    app.envia_pesquisa_satisfacao(lista.clientes)