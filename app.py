from flask import Flask, render_template, request, redirect, flash
import requests
import json
from datetime import datetime

app = Flask(__name__)
app.secret_key = "blue_clinica_secret_key_secure"

# --- CONFIGURAÇÃO ---
# Coloque aqui o link do seu Google Apps Script (o mesmo do passo anterior)
GOOGLE_SHEET_URL = "COLE_AQUI_SUA_URL_DO_APPS_SCRIPT"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    try:
        # Coleta os dados do formulário HTML
        dados = {
            "nome": request.form.get('nome'),
            "cpf": request.form.get('cpf'),
            "rg": request.form.get('rg'),
            "nascimento": request.form.get('nascimento'),
            "profissao": request.form.get('profissao'),
            "estado_civil": request.form.get('estado_civil'),
            "telefone": request.form.get('telefone'),
            "email": request.form.get('email'),
            "instagram": request.form.get('instagram'),
            "endereco": request.form.get('endereco'),
            "cep": request.form.get('cep'),
            "objetivo": request.form.get('objetivo'),
            "como_encontrou": request.form.get('como_encontrou'),
            "quem_indicou": request.form.get('quem_indicou'),
            "plano": request.form.get('plano')
        }

        # Envia para o Google Sheets
        requests.post(GOOGLE_SHEET_URL, json=dados)

        # Retorna para a página de sucesso
        return render_template('index.html', sucesso=True, nome_paciente=dados['nome'].split()[0])

    except Exception as e:
        return render_template('index.html', erro=True)

if __name__ == '__main__':
    app.run(debug=True)
