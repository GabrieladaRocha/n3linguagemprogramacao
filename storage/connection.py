from pymongo import MongoClient


class MongoConnect():

    def connectionLivros(self):
        client = MongoClient('localhost', 27017)
        banco = client['n3linguagemprogramacao']
        livros = banco['livros']
        return livros

    def insert(self, obj):
        try:
            MongoConnect().connectionLivros().insert_one(obj).inserted_id

        except Exception as e:
            print(obj)
            print(e)

    def delete(self, codigo):
        try:
            return MongoConnect().connectionLivros().delete_one({"codigo": codigo})
        except Exception as e:
            print("--------//------")
            print(e)

    def findOne(self,codigo):
        try:
            return MongoConnect().connectionLivros().find_one({"codigo": codigo})
        except Exception as e:
            print("--------//------")
            print(e)

    def findAll(self):
        try:
            return MongoConnect().connectionLivros().find()
        except Exception as e:
            print("--------//------")
            print(e)