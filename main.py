from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#bearbed theme ruby
#criando modelo de dados usando pydantic basemodel
class ProdutoCriar(BaseModel):
    codigo: int
    nome: str
    quantidade: int
    preco: float

#get , post(criar) , put(atualizar) , delete
produtos = [ 
    {
        "codigo": 1,
        "nome": "notebooks",
        "quantidade": 10,
        "preco": 2000
    
    }]

@app.get("/")
def raiz():
    return "ola mundo"


@app.get("/produtos")
def listagem_de_produtos():
    return produtos


@app.get("/produtos/{codigo}")
def listar_produto_por_codigo(codigo: int):
    for i in produtos:
        if i["codigo"] == codigo:
            return i
        else:
            return "Produto não encontrado"

@app.post("/produtos")
def cadastrar_produto(dados: ProdutoCriar):
    produtos.append(
        {
            "codigo": dados.codigo,
            "nome": dados.nome,
            "quantidade": dados.quantidade,
            "preco": dados.preco
        }
    )
    return "Produto cadastrado com sucesso"

#atividadezinha
@app.get("/usuarios")
def listar_usuarios_por_cpf():
    return "List de usuarios por cpf"
