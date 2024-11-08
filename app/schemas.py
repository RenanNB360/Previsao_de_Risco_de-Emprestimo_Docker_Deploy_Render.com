from pydantic import BaseModel
from typing import Optional


class DadosEntrada(BaseModel):
    SalarioAnualAplicantePrincipal: Optional[float] = 0.0
    SalarioAnualCoAplicante: Optional[float] = 0.0
    Dependentes: Optional[bool] = False


class Message(BaseModel):
    message: str