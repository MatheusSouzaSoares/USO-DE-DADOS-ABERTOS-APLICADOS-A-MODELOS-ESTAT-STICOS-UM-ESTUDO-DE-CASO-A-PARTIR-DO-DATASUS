import requests
import pandas as pd
import json
import time

def get_variables():
    api_key = 'insira sua chave aqui'

    dataframes = []

    for ano in range(2014, 2023):
        url = f'https://api.portaldatransparencia.gov.br/api-de-dados/despesas/por-orgao?ano={ano}&orgao=36000&pagina=1'
        print(url)
        headers = {"chave-api-dados": api_key}

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            # A requisição foi bem-sucedida
            print(response.text)
            data = json.loads(response.text)
            df = pd.DataFrame(data)
            dataframes.append(df)
            time.sleep(120)
            # Faça o que quiser com os dados da API
        else:
            # A requisição falhou
            print(f"A requisição falhou com código de status {response.status_code}.")


    df = pd.concat(dataframes, ignore_index=True)

    x = df['pago'].str.replace('.', '').str.replace(',', '.').astype(float).values

    leitos = pd.read_excel("Leitos.xlsx")
    y = leitos['Quantidade_SUS'].values

    return x, y



