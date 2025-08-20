from sapatos import Sapato

DESCONTO_PADRAO = 0.15

class Venda:
    def __init__(self, produto: Sapato, quantidade_str: str, desconto_padrao: float = DESCONTO_PADRAO):
        try: quantidade = int(quantidade_str)
        except ValueError: raise ValueError("Quantidade inválida. Use inteiro.")
        if quantidade <= 0: raise ValueError("Quantidade deve ser > 0.")
        if quantidade > produto.estoque: raise ValueError("Quantidade desejada maior que o estoque.")

        self.produto = produto
        self.quantidade = quantidade
        self.desconto_padrao = desconto_padrao
        self.total_bruto = 0.0
        self.valor_desconto = 0.0
        self.total_liquido = 0.0

    def processar(self):
        self.total_bruto = self.produto.preco * self.quantidade
        if self.total_bruto > 100.00:
            self.valor_desconto = self.total_bruto * self.desconto_padrao
        self.total_liquido = self.total_bruto - self.valor_desconto
        self.produto.estoque -= self.quantidade

    def resumo(self) -> str:
        return (
            "===== RESUMO DA VENDA =====\n"
            f"Produto: {self.produto.modelo} ({self.produto.marca}) Tam {self.produto.tamanho}\n"
            f"Preço unit.: R$ {self.produto.preco:.2f}\n"
            f"Quantidade: {self.quantidade}\n"
            f"Total bruto: R$ {self.total_bruto:.2f}\n"
            f"Desconto aplicado ({self.desconto_padrao*100:.2f}%): R$ {self.valor_desconto:.2f}\n"
            f"Total a pagar: R$ {self.total_liquido:.2f}\n"
            "==========================="
        )