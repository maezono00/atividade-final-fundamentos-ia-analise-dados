#Arquivo .py de testes para visualizar informações do dataset importado.
import pandas as pd

df = pd.read_csv("dataset_carros_usados_2.csv")

df.info()