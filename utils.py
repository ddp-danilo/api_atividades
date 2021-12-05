from models import Pessoas, Atividades

# Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='dan',idade=21)
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

# Lista no terminal todas as atividades da base de dados #Use com cuidado.
def lista_atividades():
    atividades = Atividades.query.all()
    print([{'id':i.id, 'nome':i.nome, 'pessoa_id':i.pessoa_id,'status': i.status} for i in atividades])

# Lista no terminal todas as pessoas no banco de dados. #Use com cuidado.
def lista_pessoas():
    pessoas = Pessoas.query.all()
    print([{'id': i.id, 'nome': i.nome, 'idade': i.idade } for i in pessoas])

# remove todos os itens da tabela atividades #Use com cuidado
def limpa_atividades():
    conf_msg = 'Sim eu quero apagar todos os itens da tabela atividades'
    print('Isso vai remover todos os itens da tabela atividades.')
    print('se e isso  que você quer digite({})'.format(conf_msg))
    ipt = input(':')
    if ipt == conf_msg:
        tam = len(Atividades.query.all())
        for i in range(tam):
            print(lista_atividades())
            atividade = Atividades.query.filter_by(id=(i + 1)).first()
            print(atividade)
            atividade.delete()
        print(lista_atividades())
    else:
        tam = len(Atividades.query.all())
        print('Cancelado', tam)

            


if __name__=='__main__':
    #insere_pessoas()
    #exclui_pessoa()
    #consulta_pessoas()
    #altera_pessoa()
    #limpa_atividades()
    #lista_atividades()
    #lista_pessoas()
