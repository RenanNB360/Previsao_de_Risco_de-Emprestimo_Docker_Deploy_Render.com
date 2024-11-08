from joblib import load
import numpy as np
import pickle

model = load('app/model.pkl')
scaler = load('app/scaler.pkl')


def previsao_risco(data):
    client = np.array([data.SalarioAnualAplicantePrincipal, data.SalarioAnualCoAplicante, data.Dependentes]).reshape(1, -1)

    client_scaled = scaler.transform(client)

    predict_client = model.predict(client_scaled)

    return predict_client[0]

