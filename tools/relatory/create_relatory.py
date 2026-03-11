
from database import models
from database.connection import SessionLocal
from sqlalchemy import func

def create_relatory():

    db = SessionLocal()

    transactions = db.query(models.Transaction).all()
    tasks = db.query(models.Tasks).all()

    total_ganho = db.query(func.sum(models.Transaction.value)).filter(models.Transaction.type == "ganho").scalar()
    total_gasto = db.query(func.sum(models.Transaction.value)).filter(models.Transaction.type == "gasto").scalar()

    saldo = total_ganho - total_gasto

    porcentagem_gasto = (total_gasto / total_ganho * 100) if total_ganho > 0 else 0

    tarefas_pendentes = db.query(models.Tasks).filter(models.Tasks.status == "pendente").count()
    tarefas_concluidas = db.query(models.Tasks).filter(models.Tasks.status == "concluida").count()

    maior_gasto = db.query(func.max(models.Transaction.value)).filter(models.Transaction.type == "gasto").scalar()

    db.close()

    return {
        "ganho": total_ganho,
        "gasto": total_gasto,
        "saldo": saldo,
        "porcentagem_gasto": porcentagem_gasto,
        "tarefas_pendentes": tarefas_pendentes,
        "tarefas_concluidas": tarefas_concluidas,
        "maior_gasto": maior_gasto
    }

def create_ai_prompt(data):

    prompt = f"""
    Gere um pequeno relatório diário financeiro amigável.

    Dados do dia:
    - Dinheiro ganho: {data["ganho"]}
    - Dinheiro gasto: {data["gasto"]}
    - Saldo final: {data["saldo"]}
    - Porcentagem de gastos: {data["porcentagem_gasto"]:.2f}%
    - Tarefas concluídas: {data["tarefas_concluidas"]}
    - Tarefas pendentes: {data["tarefas_pendentes"]}
    - Maior gasto do dia: {data["maior_gasto"]}

    Gere uma mensagem curta motivacional como se fosse um assistente financeiro.
    """

    return prompt