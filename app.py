from sapataria import Sapataria
from venda import Venda, DESCONTO_PADRAO

def menu():
    print("\n=== SAPATARIA ===")
    print("1) Cadastrar produto")
    print("2) Listar produtos")
    print("3) Realizar venda")
    print("4) Sair")

def main():
    loja = Sapataria()
    desconto = DESCONTO_PADRAO

    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            print("\n-- Cadastro de Produto --")
            modelo = input("Modelo: ").strip()
            marca = input("Marca: ").strip()
            tamanho = input("Tamanho (inteiro): ").strip()
            preco = input("Preço (use ponto): ").strip()
            estoque = input("Estoque (inteiro): ").strip()
            try:
                prod = loja.cadastrar(modelo, marca, tamanho, preco, estoque)
                print(f"Produto cadastrado com sucesso!\n{prod}")
            except (TypeError, ValueError) as e:
                print(f"Erro: {e}")

        elif opcao == "2":
            print("\n-- Lista de Produtos --")
            print(loja.listar())

        elif opcao == "3":
            print("\n-- Venda --")
            if not loja.produtos:
                print("Não há produtos cadastrados para vender.")
                continue
            print(loja.listar())
            idx = input("Informe o índice do produto: ").strip()
            qtd = input("Quantidade: ").strip()
            try:
                produto = loja.obter_por_indice(idx)
                venda = Venda(produto, qtd, desconto)
                venda.processar()
                print(venda.resumo())
                print(loja.listar())  # estoque atualizado
            except (ValueError, IndexError, TypeError) as e:
                print(f"Erro: {e}")

        elif opcao == "4":
            print("Saindo... Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()