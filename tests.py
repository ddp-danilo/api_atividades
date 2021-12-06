from requests import put, get, delete, post
import pytest
from models import Pessoas, Atividades

link = 'http://127.0.0.1:5000'


# compara os values de dois dictionaries
def compara_dicionarios(dic1, dic2):
    keys = ['nome', 'idade', 'id', 'status', 'pessoa']
    for key in keys:
        if key in dic2:
            if dic1[key] != dic2[key]:
                return False
    return True

# Adiciona uma pessoa a banco de dados para o teste.
def addpessoa(tspessoa):
    pessoa = Pessoas(nome=tspessoa['nome'], idade=tspessoa['idade'])
    pessoa.save()
    return pessoa.id

def removepessoa(pessoaid):
    pessoa = Pessoas.query.filter_by(id=pessoaid).first()
    pessoa.delete()
    return


test_data_pessoas = [{'nome': 'teste', 'idade': 1}]


@pytest.fixture(scope='function')
def setup_and_teardown(pessoa_teste):
    print(pessoa_teste)
    yield
    pessoa = Pessoas.query.filter_by(nome=pessoa_teste['nome']).first()
    if pessoa != None:
        print('A pessoa de teste foi encontrada na base de dados removendo, Removendo!')
        pessoa.delete()
    else:
        print('Tudo Certo')


@pytest.mark.parametrize('pessoa_teste', test_data_pessoas)
# testes da tabela pessoas.
class TestPessoas:
    # teste de post
    def test_pessoaspost(self, pessoa_teste, setup_and_teardown):
        retn = post(link+'/listapessoas', json=pessoa_teste).json()
        assert compara_dicionarios(retn, pessoa_teste)
        pessoa = Pessoas.query.filter_by(id=retn['id']).first()
        assert pessoa.nome == pessoa_teste['nome'] and pessoa.idade == pessoa_teste['idade']
        pessoa.delete()

    #teste de get
    def test_pessoasget(self, pessoa_teste, setup_and_teardown):
        psid = addpessoa(pessoa_teste)
        retn = get(link+'/pessoa/{}'.format(pessoa_teste['nome'])).json()
        assert compara_dicionarios(retn, pessoa_teste)
        removepessoa(psid)
    # teste do put
    def test_pessoasput(self, pessoa_teste, setup_and_teardown):
        psid = addpessoa(pessoa_teste)
        alt = {'nome': 'abc'+pessoa_teste['nome'],
               'idade': 15}
        retnput = put(link+'/pessoa/{}'.format(pessoa_teste['nome']), json=alt).json()
        assert compara_dicionarios(retnput, alt)
        pessoa = Pessoas.query.filter_by(id=psid).first()
        assert pessoa.nome == alt['nome'] and pessoa.idade == alt['idade']
        removepessoa(psid)

    # teste do delete
    def test_pessoasdelete(self, pessoa_teste, setup_and_teardown):
        psid = addpessoa(pessoa_teste)
        retndelete = delete(link+'/pessoa/{}'.format(pessoa_teste['nome'])).json()
        assert retndelete['status'] == 'Sucesso'
        assert Pessoas.query.filter_by(id=psid).first() == None



