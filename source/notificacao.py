from service_email import EmailService 
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

arquivos_processados = [
    {"arquivo": "Empresas.csv", "status": "Sucesso", "tempo": "12 segundos"},
    {"arquivo": "Socios.csv", "status": "Sucesso", "tempo": "8 segundos"},
    {"arquivo": "Municipios.csv", "status": "Falha", "tempo": "-"},
]

# Dados do servidor (pode carregar do .env também)
smtp_server = os.getenv("SMTP_SERVER")
smtp_port = os.getenv("SMTP_PORT")
username = os.getenv("SMTP_USERNAME")
password = os.getenv("SMTP_PASSWORD")

# Instancia o serviço
email_service = EmailService(smtp_server, smtp_port, username, password)

def enviar_notificacao():    
    corpo_html = gerar_relatorio_html(arquivos_processados)
    corpo_texto = "Seu cliente de e-mail não suporta HTML. Relatório de processamento disponível."

   # Dispara um e-mail
    email_service.enviar_email(
        destinatarios=["cristiano.fer23@gmail.com"],
        assunto="Processamento finalizado",
        corpo_texto=corpo_texto,
        corpo_html=corpo_html
    )

# Gera o HTML do relatório
def gerar_relatorio_html(arquivos):
    linhas = ""
    for arq in arquivos:
        cor = "green" if arq["status"] == "Sucesso" else "red"
        linhas += f"""
            <tr>
                <td>{arq['arquivo']}</td>
                <td style='color:{cor}'>{arq['status']}</td>
                <td>{arq['tempo']}</td>
            </tr>
        """

    html = f"""
    <html>
    <body>
        <h2>Relatório de Processamento de Arquivos</h2>
        <h4>Dados atualizados e disponíveis da API</h4>
        <h5>Data hora da atualização: {datetime.now()}</h5>        
        <table border="1" cellpadding="5" cellspacing="0" style="border-collapse: collapse;">
            <thead>
                <tr>
                    <th>Arquivo</th>
                    <th>Status</th>
                    <th>Tempo de Processamento</th>
                </tr>
            </thead>
            <tbody>
                {linhas}
            </tbody>
        </table>
    </body>
    </html>
    """
    return html

 

