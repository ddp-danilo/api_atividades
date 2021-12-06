from requests import put, get, delete, post
import pytest

link = 'http://127.0.0.1:5000'

# compara os values de dois dictionaries
def compara_dicionarios(dic1, dic2):
    keys = ['nome', 'idade', 'id', 'status', 'pessoa']
    for key in keys:
        if key in dic2:
            if dic1[key] != dic2[key]:
                return False
    return True


@pytest.mark.parametrize('pessoa_teste',[
    ({'nome': 'teste', 'idade': 1}),
])
# Testes da tabela pessoas.
def testpessoas(pessoa_teste):
    retnpost = post(link+'/listapessoas', json=pessoa_teste).json()
    assert compara_dicionarios(retnpost, pessoa_teste)
    retnget = get(link+'/pessoa/{}'.format(pessoa_teste['nome'])).json()
    assert compara_dicionarios(retnget, pessoa_teste)
    alt = {'id': retnpost['id'],
           'nome': 'abc'+pessoa_teste['nome'],
           'idade': 15}
    retnput = put(link+'/pessoa/{}'.format(pessoa_teste['nome']), json=alt).json()
    assert compara_dicionarios(retnput, alt)
    retndelete = delete(link+'/pessoa/{}'.format(alt['nome'])).json()
    assert retndelete['status'] == 'Sucesso'




