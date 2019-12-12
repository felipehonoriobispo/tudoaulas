class Funcionario:
    def __init__(self, nome, email, numerorg, idade):
        self.nome = nome
        self.email = email
        self.numerorg = numerorg
        self.idade = idade

    def __str__(self):
        return f'Ola {self.nome}, portador do email : {self.email} você foi cadastrado com sucesso no nosso sistema'


dados_funcionarios = Funcionario(
    nome='Robsom',
    email='robsom.motoboy@gmail.com',
    numerorg='51359137811',
    idade='22'
)


print(dados_funcionarios)