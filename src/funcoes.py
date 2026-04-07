def cadastrar(inventario):
    print("\n--- NOVO CADASTRO ---")
    
    nome = input("Nome do Ativo: ").strip()
    while nome == "":
        print("Erro: Digite um nome valido.")
        nome = input("Nome do Ativo: ").strip()

    tipo = input("Tipo (Hardware/Software): ").strip()
    while tipo == "":
        print("Erro: Digite o tipo.")
        tipo = input("Tipo (Hardware/Software): ").strip()

    local = input("Local/Licenca: ").strip()
    while local == "":
        print("Erro: Digite o local.")
        local = input("Local/Licenca: ").strip()

    novo_ativo = {
        "nome": nome,
        "tipo": tipo,
        "local": local
    }
    
    inventario.append(novo_ativo)
    print("Cadastrado com sucesso!")
    return inventario

def listar(inventario):
    print("\n--- LISTA DE ATIVOS ---")
    if len(inventario) == 0:
        print("Lista vazia.")
    else:
        for item in inventario:
            print("Nome: " + item['nome'] + " | Tipo: " + item['tipo'] + " | Local: " + item['local'])

def buscar(inventario):
    print("\n--- BUSCA ---")
    termo = input("Buscar por: ")
    achou = False

    for item in inventario:
        if termo.lower() in item['nome'].lower():
            print("Encontrado: " + item['nome'] + " - " + item['local'])
            achou = True
    
    if achou == False:
        print("Nao achei nada.")