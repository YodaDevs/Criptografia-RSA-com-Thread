Alunos: João da Silva Muniz Neto e Mateus Monteiro Santos<p>
Trabalho referente a disciplina de Redes de Computadores, do Instituto de Computação (IC) da Universidade Federal de Alagoas (UFAL) ministrada pelo professor Leandro Melo Sales. Trabalho com o objetivo de implementar os conhecimentos vistos em sala sobre Redes, valendo 40% da nota da AB2. A implementação consiste em aprensentar 1 códigos, que realiza a criptografia em RSA de uma mensagem enviada pelo cliente para o servidor, e por fim retornando-a criptografada.

# INSTRUÇÕES PARA UTILIZAÇÃO DA APLICAÇÃO

Primeiro, para o uso da aplicação, precisamos instalar alguns programas e pacotes:<p>
Instale Python3.9 (https://www.python.org/downloads/), ao acessar o link clique no botão amarelo “Download Python 3.9.5” (Na instalação lembre de marcar a opção “Add Python 3.9 to PATH” e siga em “Install Now”);<p>
Após a instalação do programa acima, será necessário o passo a passo da instalação do pip no PATH, para melhor esclarecimento, acesse o link: https://dicasdepython.com.br/resolvido-pip-nao-e-reconhecido-como-um-comando-interno/
Após instalado o pip, faremos o uso do promt de command (cmd) para instalação de alguns pacotes, abra o cmd e instale com os seguintes comandos:
<p>
 <a></a> • pip install python-socketio
</p>
<p>
 <a></a> • pip install pickle4
</p>
<p>
 <a></a> • pip install keyboard
</p>
<p>
 <a></a> • pip install random2
</p>
<p>
 <a></a> • pip install pycryptodome
</p>

Após a instalação dos pacotes reinicie o cmd e baixe os arquivos (“server_thread.py”,“client_thread.py”)  no seguinte link do github (https://github.com/YodaDevs/Criptografia-RSA-com-Thread.git)
Após baixado os dois arquivos, inicie o arquivo “server_thread.py” para abrir o servidor e inicie o arquivo “client_thread.py” para iniciar o cliente e ser possível a criptografia da mensagem(lembrando que o servidor está em localhost).<p>

Com a conexão estabelecida o servidor necessitará da resposta de quais numeros primos será utilizado para a criptografia do respectivo cliente, sendo assim colocando números primos, o cliente deverá informar qual mensagem será criptografada, sendo assim efetuado a funcionalidade do sistema. <p>

Aqui podemos ver que o servidor fará a criptografia perguntando quais números primos utilizaremos para gerar a criptografia, sendo assim podemos seguir passo a passo como solicitado no programa e ele retornará nossa mensagem. 

