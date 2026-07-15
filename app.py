#Importando do framkework flask, a ferramenta Flask, request e jsonify.
from flask import Flask, request, jsonify
#Importando do flask_cors, a ferramenta CORS, muito usado para questões de segurança ao executar a API.
from flask_cors import CORS
#Importando a ferramenta LinearRegression do framework sklearn.
from sklearn.linear_model import LinearRegression
#Importando a biblioteca pandas e dando o alias de pd.
import pandas as pd

#Habilitando a executação da API
app = Flask(__name__)
CORS(app)

#Realizando a leitura do dataset, atribuindo o dataset na variável df, conhecida também como dataframe.
df = pd.read_csv("dataset_carros_usados_2.csv")

#Separando os dados usados para treinar o modelo.
#Atribuindo ao eixo X do gráfico de regressão linear as variáveis usadas para ajudar nas previsões desejadas.
X = df[["ano", "quilometragem", "motor", "num_revisoes"]]
#Atribuindo ao eixo Y a variável que queremos ter uma previsão, nesse caso, a variável preco.
y = df["preco"]

#Treinando o modelo.
modelo = LinearRegression()
modelo.fit(X, y)

#Criando os métodos e rotas.
#Foi criado um método GET para facilitar na hora de usar a API e assegurar de que a API está online.
@app.route("/", methods = ["GET"])
def inicio():
    return jsonify({"Resposta":"API online!!! 🤓"}), 200

#Criando o método POST para a previsão do preço dos carros.
@app.route("/prever", methods = ["POST"])
def prever():
    try:
        #Receber as informações do json e transformar esse json e um dataframe.
        dados = request.get_json()
        carro = pd.DataFrame({
            "ano" : [dados["ano"]],
            "quilometragem" : [dados["quilometragem"]],
            "motor" : [dados["motor"]],
            "num_revisoes" : [dados["num_revisoes"]]   
        })
        preco = modelo.predict(carro)[0]
        #Após toda a insierção das informações, é feito a exibição do preço, para formatar o preço exibido, é usado a função round(), dentro dela, para assegurar de que o preço será um número float, é inserido a variável preco dentro do float() e depois disso é indicado o número 2, ou seja, a função round vai arrendondar até duas casas decimais.
        return jsonify({"Preço" : round(float(preco),2)})
    except Exception as erro:
        return jsonify({"erro" : str(erro)}), 400
        
#Iniciar a API
#Fazendo uma condicional para garantir que o projeto esteja sendo rodado dentro da pasta main, ou seja, se o arquivo estiver dentro da pasta principal, o aplicativo vai inicializar sem problemas.
if __name__ == '__main__':
    app.run(port = 8000, host = "0.0.0.0", debug = True)