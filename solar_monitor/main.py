from fastapi import FastAPI                                                      # Importa a classe principal do FastAPI que será usada para criar a aplicação web
from database import init_db                                                     # Importa a função para inicializar o banco de dados
from routes import metrics, usinas, inversores, estatisticas                     # Importa as rotas

init_db()                                                                            # Inicializa o banco de dados

app = FastAPI()                                                                      # Cria uma instância da classe FastAPI

# Registrando as rotas
app.include_router(metrics.router, prefix="/metrics", tags=["Métricas"])
app.include_router(usinas.router, prefix="/usinas", tags=["Usinas"])
app.include_router(inversores.router, prefix="/inversores", tags=["Inversores"])
app.include_router(estatisticas.router, prefix="/estatisticas", tags=["Estatísticas"])
