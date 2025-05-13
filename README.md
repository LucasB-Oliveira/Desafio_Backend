Desafio Backend - TECSCI

📌 Descrição

API para monitoramento de usinas fotovoltaicas, desenvolvida em Python com FastAPI.

O sistema permite:
- Ingestão e armazenamento de dados de métricas de inversores.
- Consulta de potência máxima, média de temperatura e geração acumulada.
- CRUD completo de usinas e inversores.
- Documentação automática gerada no Swagger.


💻 Tecnologias utilizadas

- Python 3.11+
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn
- Pydantic


⚙️ Como instalar e rodar o projeto

1️⃣ Clone o repositório:

git clone <https://github.com/LucasB-Oliveira/Desafio_Backend.git>
cd <Desafio_Backend>
cd.. (Se precisar voltar um diretório depois:)

2️⃣ Crie e ative um ambiente virtual na Pasta Principal:

python -m venv venv
venv\Scripts\activate

3️⃣ Instale as dependências na Pasta Principal:

pip install -r requirements.txt

4️⃣ Popule o banco de dados com o arquivo metrics.json:

cd solar_monitor

python load_data.py

5️⃣ Inicie a API:

cd solar_monitor

uvicorn main:app --reload

🌐 Como acessar a documentação
http://127.0.0.1:8000/docs

