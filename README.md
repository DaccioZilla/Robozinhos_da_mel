# Robozinhos_da_mel

Esse repositório é um exercício da solução de problemas reais via programação.

Minha esposa (a Mel), precisa se comunicar com frequência com as clientes, por vezes de maneira previsível e estruturada.

Com isso, e na ausência de recursos para contratar uma secretária ou um fornecedor especializado de API para Whatsapp, pensei em configurar scripts que simulam entradas de mouse e teclado.

Até o momento, consegui fazer com que o script:

1 - Abra o Whatsapp Web (é preciso estar logado previamente para que o processo dê certo, tentei o acesso via Selenium, mas o login com QR Code via celular me quebrou).

2 - Receba set de clientes, busque o número do telefone e mande uma mensagem para cada cliente do set. Como o set built-in do Python é uma coleção não ordenada de itens exclusivos eu não precisei implementar garantias de exclusividade, mas tive que sobrescrever as funções eq, ne e hash da Classe Clientes.

Próximos passos consistem em recuperar listas de clientes do aplicativo Booksy segundo alguma condição e possibilitar o envio de outros tipos de mensagens (lembrete de agendamento, convites para agendar, comunicação de ausência, mensagens de aniversário, etc).