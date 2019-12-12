class Carro:# É o cachorro
    def __init__(self, proprietario, modelo, cor, placa, preco, marca): # como se fosse as caracteristicas do cachorro
        self.proprietario = proprietario
        self.modelo = modelo
        self.cor  = cor
        self.placa = placa
        self.preco = preco
        self.marca = marca

    def __str__(self):
        return f'Ola sr {self.proprietario}, o modelo do seu carro é {self.modelo} - {self.cor} - {self.marca}'

meu_carro = Carro(
    proprietario='Felipe',
    modelo='HB20',
    cor='verde',
    placa='TMJ - 17272',
    preco='900000',
    marca='Hyundai'
)

print(meu_carro)