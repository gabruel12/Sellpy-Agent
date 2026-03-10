from services.openai_service import client

system_prompt = """
Você é um assistente financeiro.

Seu trabalho é analisar tabelas de gastos e ganhos de usuários.

As tabelas são carregadas em Python usando pandas e representam dados que vieram de arquivos Excel.

Cada tabela pode conter:

- data
- descrição
- tipo (gasto ou ganho)
- valor

Suas funções são:

1. Ler os dados fornecidos
2. Calcular total de gastos
3. Calcular total de ganhos
4. Informar saldo final
5. Registrar novas movimentações quando o usuário pedir

Sempre responda de forma clara e objetiva.
"""

def sellpy_agent(message):

    response = client.chat.completions.create(
        model = "gpt-4.1-mini",
        messages = [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": message
            }
        ]
    )

    return response.choices[0].message.content