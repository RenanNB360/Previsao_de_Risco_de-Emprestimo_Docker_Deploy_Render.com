from fastapi import FastAPI
from app.schemas import DadosEntrada, Message
from app.functions import previsao_risco


app = FastAPI()



@app.post('/previsao/', response_model=Message)
def risco(data: DadosEntrada):

    result = previsao_risco(data)


    return {'message': f'Score de Risco Previsto: {result:.3f}'}