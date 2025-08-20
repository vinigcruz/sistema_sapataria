from sapatos import Sapato

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

        prod = Sapato(modelo.strip(), marca.strip(), tamanho, float(preco), int(estoque))
        self.produtos.append(prod)
        return prod

    def listar(self) -> str:
        if not self.produtos:
            return "Nenhum produto cadastrado."
        return "\n".join(f"[{i}] {p}" for i, p in enumerate(self.produtos))

    def obter_por_indice(self, indice_str: str) -> Sapato:
        try:
            idx = int(indice_str)
        except ValueError:
            raise ValueError("Índice inválido. Use número inteiro.")

        if idx < 0 or idx >= len(self.produtos):
            raise IndexError("Índice fora do intervalo.")

        return self.produtos[idx]
