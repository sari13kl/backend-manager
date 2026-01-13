from fastapi import FastAPI
from app.routes.tasks import task_router
from app.routes.auth import auth_router

app = FastAPI(title="Task Management API", version="1.0.0")

# Incluir routers
app.include_router(auth_router)
app.include_router(task_router)



# criar tarefa(título, descrição, status, prioridade, data de criação,
# prazo e dono(usuário))
# listar tarefas
# atualizar tarefa
# deletar tarefa





#para rodar o servidor, use o comando:
# uvicorn app.main:app --reload

# Rest APIs
# Get -> leitura/pegar
# Post -> enviar/criar
# Put/Patch -> atualizar/editar
# Delete -> deletar/remover