from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Venda(BaseModel):
    item: str
    preco_unitario: float
    quantidade: int

vendas = {
    1: {"item": "lata", "preco_unitario": 4, "quantidade": 5},
    2: {"item": "garrafa 2L", "preco_unitario": 15, "quantidade": 5},
    3: {"item": "garrafa 750ml", "preco_unitario": 10, "quantidade": 5},
    4: {"item": "lata mini", "preco_unitario": 2, "quantidade": 5},
}

@app.get("/") ##decorator: atribui funcionalidade nova para quem está abaixo dele(async def: (função))
async def root():
    return {"Vendas": len(vendas)}

@app.get("/vendas/{id_venda}")
async def pegar_venda(id_venda: int):
    if id_venda in vendas: 
        return vendas[id_venda]
    else:
        return {"Erro": "ID Venda inexistente."}

@app.post("/vendas")
async def adicionar_venda(venda: Venda):
    id_novo = max(vendas.keys()) + 1 if vendas else 1
    vendas[id_novo] = venda.model_dump()
    return {"id": id_novo, "mensagem": "Venda adicionada com sucesso!"}

@app.put("/vendas/{id_venda}")
async def atualizar_venda(id_venda: int, venda: Venda):
    if id_venda in vendas:
        vendas[id_venda] = venda.model_dump()
        return {"mensagem": f"Venda {id_venda} atualizada com sucesso!"}
    else:
        return {"Erro": "ID Venda inexistente."}
    
@app.delete("/vendas/{id_venda}")
async def deletar_venda(id_venda: int):
    if id_venda in vendas:
        del vendas[id_venda]
        return {"mensagem": f"Venda {id_venda} removida com sucesso!"}
    else:
        return {"Erro": "ID Venda inexistente."}  
