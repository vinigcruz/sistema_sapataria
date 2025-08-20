class Sapato:
    def __init__(self, modelo: str, marca: str, tamanho: int, preco: float, estoque: int):
        if not isinstance(modelo, str):  
            raise TypeError("Modelo deve ser string.")
        if not isinstance(marca, str):   
            raise TypeError("Marca deve ser string.")
        if not isinstance(tamanho, int): 
            raise TypeError("Tamanho deve ser int.")
        if not isinstance(preco, float): 
            raise TypeError("Preço deve ser float.")
        if not isinstance(estoque, int): 
            raise TypeError("Estoque deve ser int.")
        if tamanho <= 0:  
            raise ValueError("Tamanho deve ser > 0.")
        if preco < 0:     
            raise ValueError("Preço não pode ser negativo.")
        if estoque < 0:   
            raise ValueError("Estoque não pode ser negativo.")

        self.modelo = modelo
        self.marca = marca
        self.tamanho = tamanho
        self.preco = preco
        self.estoque = estoque

    def __str__(self):
        return (f"Modelo: {self.modelo} | Marca: {self.marca} | Tam: {self.tamanho} | "
                f"Preço: R$ {self.preco:.2f} | Estoque: {self.estoque}")