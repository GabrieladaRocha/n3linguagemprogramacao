from flask import json
import json
from bson import ObjectId
from storage.connection import MongoConnect

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

class Livro():

    def insert(self, livro):
        con = MongoConnect()
        model = {
            "codigo": livro['codigo'],
            "nome": livro['nome'],
            "autor": livro['autor'],
            "ano": livro['ano']
        }
        try:
            con.insert(model)
            return JSONEncoder().encode(model), 200
        except:
            return JSONEncoder().encode(model), 404

    def delete(self, codigo):
        con = MongoConnect()
        try:
            con.delete(codigo)
            return JSONEncoder().encode("Livro deletado pelo codigo"), 200
        except:
            return JSONEncoder().encode("Não encontramos esse livro"), 404

    def findOne(self, codigo):
        con = MongoConnect()
        try:
            result = con.findOne(codigo)
            print(result)
            if result == None:
                return JSONEncoder().encode("Não encontramos esse livro"), 404
            return JSONEncoder().encode(result), 200
        except:
            return JSONEncoder().encode("No have registers"), 404

    def findAll(self):
        con = MongoConnect()
        try:
            listLivros = []
            for livro in con.findAll():
                listLivros.append(livro)
            print(listLivros)
            return JSONEncoder().encode(listLivros), 200
        except Exception as e:
            print(e)
            return "error", 404