from fastapi import APIRouter

task_router = APIRouter(prefix="/tasks", tags=["Tasks"])

@task_router.get("/")
def get_tasks():
    """Listar todas as tarefas"""
    return {"message": "Lista de tarefas"}

@task_router.post("/")
def create_task():
    """Criar uma nova tarefa"""
    return {"message": "Tarefa criada"}

@task_router.get("/{task_id}")
def get_task(task_id: int):
    """Buscar uma tarefa específica"""
    return {"message": f"Tarefa {task_id}"}

@task_router.put("/{task_id}")
def update_task(task_id: int):
    """Atualizar uma tarefa"""
    return {"message": f"Tarefa {task_id} atualizada"}

@task_router.delete("/{task_id}")
def delete_task(task_id: int):
    """Deletar uma tarefa"""
    return {"message": f"Tarefa {task_id} deletada"}
