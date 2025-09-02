import random  # módulo de números aleatórios

# Função auxiliar para gerar estoque aleatório
def gerar_estoque_aleatorio(min_estoque=1, max_estoque=20):
    return random.randint(min_estoque, max_estoque)


class Sapataria:
    def __init__(self):
        self.produtos = []

    def cadastrar(self, modelo: str, marca: str, tamanho_str: str, preco_str: str, estoque_str: str):
        try:
            tamanho = int(tamanho_str)
        except ValueError:
            raise ValueError("Tamanho inválido. Use inteiro (ex.: 43).")

        try:
            preco = float(preco_str)
        except ValueError:
            raise ValueError("Preço inválido. Use decimal (ex.: 199.90).")

        try:
            estoque = int(estoque_str)
        except ValueError:
            raise ValueError("Estoque inválido. Use inteiro (ex.: 5).")

        prod = Sapato(modelo.strip(), marca.strip(), tamanho, preco, estoque)
        self.produtos.append(prod)
        return prod

    def listar(self, formatador=None) -> str:
        if not self.produtos:
            return "Nenhum produto cadastrado."

        if formatador is None:
            # Função padrão que retorna o __str__ do produto
            formatador = lambda sapato: str(sapato)

        def listar_recursivo(lista, idx=0):
            if idx == len(lista):
                return ""
            linha = f"[{idx}] {formatador(lista[idx])}"
            resto = listar_recursivo(lista, idx + 1)  # chamada recursiva
            return linha + ("\n" + resto if resto else "")

        return listar_recursivo(self.produtos)
