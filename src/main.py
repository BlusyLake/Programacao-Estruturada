import os

# --- VARIAVEIS GLOBAIS ---
arquivo_banco = "banco_dados.txt"
inventario = []

# --- MODULO DE ARQUIVOS  ---
def carregar_dados():
    # Se nao existe arquivo, ignora e comeca vazio
    if not os.path.exists(arquivo_banco):
        return

    # Manipulacao de Arquivo: Abre o txt em modo leitura 
    arquivo = open(arquivo_banco, "r")
    linhas = arquivo.readlines()
    arquivo.close()

    # Transforma cada linha do txt em um dicionario
    for linha in linhas:
        linha = linha.strip()
        if linha != "":
            # Corta a string usando o |
            dados = linha.split("|")
            ativo = {
                "nome": dados[0],
                "tipo": dados[1],
                "local": dados[2]
            }
            inventario.append(ativo)

def salvar_dados():
    # Sobrescreve o txt com os dados da lista (w)
    arquivo = open(arquivo_banco, "w")
    for item in inventario:
        # Monta a linha no formato padrao: Nome|Tipo|Local
        linha = item['nome'] + "|" + item['tipo'] + "|" + item['local'] + "\n"
        arquivo.write(linha)
    
    arquivo.close()
    print("Dados gravados com sucesso no disco.")

# --- MODULO DE CADASTRO E CONSULTA (Modularizacao) ---
def cadastrar():
    print("\n--- NOVO CADASTRO ---")
    nome = input("Nome do Ativo: ")
    tipo = input("Tipo (Hardware/Software): ")
    local = input("Local/Licenca: ")

    # Estrutura de dados basica (Dicionario)
    novo_ativo = {
        "nome": nome,
        "tipo": tipo,
        "local": local
    }
    
    inventario.append(novo_ativo)
    print("Cadastrado com sucesso!")

def listar():
    print("\n--- LISTA DE ATIVOS ---")
    # Estrutura de Controle: Verifica se a lista esta vazia
    if len(inventario) == 0:
        print("Nenhum ativo cadastrado.")
    else:
        # Loop para mostrar todos os itens
        for item in inventario:
            print("Nome: " + item['nome'] + " | Tipo: " + item['tipo'] + " | Local: " + item['local'])

def buscar():
    print("\n--- BUSCA ---")
    termo = input("Digite o nome para buscar: ")
    encontrou = False

    #  Loop de repeticao para procurar o termo em cada item do inventario
    for item in inventario:
        if termo.lower() in item['nome'].lower():
            print("Encontrado: " + item['nome'] + " - " + item['local'])
            encontrou = True
    
    if encontrou == False:
        print("Nada encontrado.")

# --- FUNCAO PRINCIPAL ---
def main():
    carregar_dados()

    # Loop infinito do menu principal
    while True:
        print("\n=== GESTAO DE T.I. ===")
        print("1. Cadastrar Ativo")
        print("2. Listar Tudo")
        print("3. Buscar")
        print("4. Salvar e Sair")
        
        opcao = input("Opcao: ")

        # Menu
        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            buscar()
        elif opcao == "4":
            salvar_dados()
            break # Quebra o loop e sai do programa
        else:
            print("Opcao invalida.")

# Inicio do programa
if __name__ == "__main__":
    main()