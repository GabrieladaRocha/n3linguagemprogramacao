from flask import Flask, request, json
from services.Livros import Livro

controller = Livro()

class Routes:
    def create(self, req):
        livro = req.get_json()
        if livro['nome'] == "":
            return json.dumps({"code": 400, "description": "o nome deve estar preenchido", }), 400
        elif len(livro['autor']) > 100:
            return json.dumps({"code": 400,
                               "description": "você deve registrar um autor para o livro", }), 400
        elif livro['ano'] == "":
            return json.dumps({"code": 400, "description": "O campo ano deve estra preenchido", }), 400
        response = controller.insert(livro)
        return response

    def remove(self, req):
        livro = req.get_json()
        codigo = livro['codigo']
        livroCadastrado = controller.findOne(codigo)
        if livroCadastrado == None:
            return json.dumps(
                {"code": 400, "description": "codigo do livro não encontrado", }), 400
        response = controller.delete(codigo)
        return response

    def findOne(self,req):
        livro = req.get_json()
        codigo = livro['codigo']
        response = controller.findOne(codigo)
        return response

    def findAll(self):
        response = controller.findAll()
        return response