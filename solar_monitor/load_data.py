import json                                                 # Importa módulo json do Python para ler o arquivo JSON
from datetime import datetime                               # Importa datetime do Python para converter strings de data
from database import SessionLocal, init_db                  # Importa a sessão do banco e a função para inicializar as tabelas
from crud import create_metric                              # Importa a função para criar métricas no banco
from schemas import MetricCreate                            # Importa o modelo Pydantic para criação de métricas

init_db()                                                   # Inicializa as tabelas do banco de dados

with open('metrics.json', "r") as f:                        # Abre o arquivo metrics.json para leitura
    data = json.load(f)                                     # Carrega o JSON como uma lista de dicionários

db = SessionLocal()                                         # Cria uma sessão do banco de dados

for entry in data:                                                                              # Loop sobre cada registro no JSON    
    metric = MetricCreate(                                                                      # Cria um objeto MetricCreate validado, convertendo o campo datetime
        datetime=datetime.fromisoformat(entry["datetime"]["$date"].replace("Z", "+00:00")),     # Converte data no formato ISO
        inversor_id=entry["inversor_id"],
        potencia_ativa_watt=entry["potencia_ativa_watt"] or None,
        temperatura_celsius=entry["temperatura_celsius"] or None,
    )

    create_metric(db, metric)                                # Insere o registro no banco

db.close()                                                  # Fecha a sessão do banco   

print("Dados inseridos no banco!")                          # Imprime uma mensagem de sucesso
    