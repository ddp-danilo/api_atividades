from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoas, Atividades

app = Flask(__name__)
api = Api(app)

class Pessoa(Resource):
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {'nome': pessoa.nome, 'idade': pessoa.idade, 'id': pessoa.id}
        except AttributeError:
            response = {'status': 'Erro',
                        'mensagem': 'Pessoa não encontrada.'
                        }
        return response
    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        pessoa.save()
        response = {'id': pessoa.id, 'nome': pessoa.nome, 'idade': pessoa.idade}
        return response
    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        pessoa.delete()
        mensagem = 'Pessoa {} excluída com sucesso.'.format(nome)
        return {'status':'Sucesso', 'mensagem': mensagem}

class ListaPessoas(Resource):
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{'id': i.id, 'nome': i.nome, 'idade': i.idade} for i in pessoas]
        return response
    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        response = {'id': pessoa.id, 'nome': pessoa.nome, 'idade': pessoa.idade}
        return response

class ListaAtividades(Resource):
    def get(self):
        atividades = Atividades.query.all()
        response = [{'id': i.id, 'pessoa': i.pessoa.nome, 'nome': i.nome} for i in atividades]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividades(nome=dados["nome"], pessoa=pessoa)
        atividade.save()
        response = {'nome': atividade.nome, 'pessoa':atividade.pessoa.nome, 'id':atividade.id}
        return response


api.add_resource(ListaAtividades, '/atividades')
api.add_resource(ListaPessoas, '/listapessoas')
api.add_resource(Pessoa, '/pessoa/<string:nome>')

if __name__ == '__main__':
    app.run(debug=True)
