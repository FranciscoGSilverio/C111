dados_aluno = {
    'nome': '',
    'media': 0,
    'situacao': ''
}

dados_aluno['nome'] = input('Digite o nome do aluno: ')
dados_aluno['media'] = float(input('Digite a média do aluno: '))

if dados_aluno['media'] >= 50:
    dados_aluno['situacao'] = 'AP'
else:
    dados_aluno['situacao'] = 'RP'

print(dados_aluno.items())
