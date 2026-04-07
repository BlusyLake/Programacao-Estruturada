import arquivos
import funcoes

def main():
    # Puxa os dados salvos pra iniciar o programa
    inventario = arquivos.carregar()

    while True:
        print("\n=== MENU TI ===")
        print("1. Cadastrar")
        print("2. Listar")
        print("3. Buscar")
        print("4. Salvar e Sair")
        
        opcao = input("Opcao: ")

        if opcao == "1":
            inventario = funcoes.cadastrar(inventario)
        elif opcao == "2":
            funcoes.listar(inventario)
        elif opcao == "3":
            funcoes.buscar(inventario)
        elif opcao == "4":
            arquivos.salvar(inventario)
            print("Salvou. Ate mais!")
            break 
        else:
            print("Opcao invalida.")

if __name__ == "__main__":
    main()