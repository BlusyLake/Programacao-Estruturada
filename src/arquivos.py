import os

nome_arquivo = "banco_dados.txt"

def carregar():
    inventario = []
    # Se o arquivo nao existir, devolve a lista vazia pra nao dar crash
    if not os.path.exists(nome_arquivo):
        return inventario

    arquivo = open(nome_arquivo, "r")
    linhas = arquivo.readlines()
    arquivo.close()

    for linha in linhas:
        linha = linha.strip()
        if linha != "":
            dados = linha.split("|")
            ativo = {
                "nome": dados[0],
                "tipo": dados[1],
                "local": dados[2]
            }
            inventario.append(ativo)
            
    return inventario

def salvar(inventario):
    arquivo = open(nome_arquivo, "w")
    for item in inventario:
        linha = item['nome'] + "|" + item['tipo'] + "|" + item['local'] + "\n"
        arquivo.write(linha)
    arquivo.close()