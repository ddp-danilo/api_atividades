from models import Pessoas

# Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='das',idade=15)
    print(pessoa)
    pessoa.save()
# Realiza consulta na tabela pessoa
def consulta_pessoas():
    pessoa = Pessoas.query.all()
    print(pessoa)
    pessoa = Pessoas.query.filter_by(nome='das').first()
    print(pessoa.idade)

# Altera dados na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='das').first()
    pessoa.idade = 20
    pessoa.save()

# Exclui dados da tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Dan').first()
    pessoa.delete()

if __name__=='__main__':
    #insere_pessoas()
    exclui_pessoa()
    consulta_pessoas()
    #altera_pessoa()