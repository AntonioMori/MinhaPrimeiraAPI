from fastapi import FastAPI

app = FastAPI()

produtos = [ 
    {
        codigo: 1,
        nome: "notebooks",
        quantidade: 10,
        preco: 2000
    
    }]

@app.get("/")
def raiz():
    return "ola mundo"

@app.get("/produtos")
def listagem_de_produtos():
    return produtos

@app.get("/produtos/{codigo}")
def listar_produto_por_codigo(codigo):
    return codigo

@app.get("/usuarios")
def listar_usuarios_por_cpf():
    return "List de usuarios por cpf"
