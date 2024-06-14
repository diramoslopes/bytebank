from codigo.bytebank import Funcionario

diogo = Funcionario('Diogo Silveira','20/11/1996',10000)

print(diogo.idade())

def teste_idade():
    funcionario_teste = Funcionario('Fulano', '26/07/1973',5000)
    print(f'Teste = {funcionario_teste.idade()}')

teste_idade()