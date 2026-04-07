Relatório de Testes e Refinamento

1. Teste de campo vazio (bug no cadastro):
Percebi que se o cara apertasse "Enter" direto na hora de cadastrar sem querer, o programa aceitava e gravava um nome em branco, o que zoava a lista toda depois. Pra resolver, eu botei um loop while no funcoes.py. Agora, se a pessoa não digitar nada (string vazia ""), o sistema não deixa passar e fica pedindo pra digitar um nome válido.

2. Teste de busca com letra maiúscula/minúscula:
Fui testar a busca e cadastrei um switch como "SW-CORE". Depois tentei buscar só por "core" e o programa não achou. Acontece que o Python diferencia maiúscula de minúscula. Arrumar isso foi fácil, só botei um .lower() no código pra forçar tudo pra minúsculo na hora do if comparar as strings. Agora acha de boa.

3. Teste de Persistência (Salvando e fechando):
Pra ver se a criação de arquivos tava ok, cadastrei 3 ativos e apertei a opção 4 pra Salvar e Sair. Fui na pasta e vi que ele criou o banco_dados.txt normal com os 3 lá dentro. Abri o programa de novo, apertei 2 pra listar, e ele carregou a lista do HD pra RAM certinho sem eu precisar cadastrar de novo.

Exemplos de Entrada/Saída do Arquivo:

Eu decidi usar o "pipe" (|) pra separar as coisas no arquivo de texto pra não dar conflito.

Exemplo do que eu digito no terminal:
Nome: Roteador Cisco
Tipo: Hardware
Local: Rack 2

Como fica salvo lá no arquivo banco_dados.txt:
Roteador Cisco|Hardware|Rack 2
Licenca Windows|Software|RH

Na hora que o main.py roda, ele chama o arquivos.carregar(), lê essa linha, dá um .split("|") e transforma num dicionário pro programa conseguir ler.