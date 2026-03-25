import smtplib
import ssl
from email.message import EmailMessage

class EmailService:
    def __init__(self, smtp_server, smtp_port, username, password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def enviar_email(self, destinatarios, assunto, corpo_texto, corpo_html=None, anexos=None):
        try:            
            mensagem = EmailMessage()
            mensagem["From"] = self.username
            mensagem["To"] = ', '.join(destinatarios) if isinstance(destinatarios, list) else destinatarios
            mensagem["Subject"] = assunto
            mensagem.set_content(corpo_texto)

            if corpo_html:
                mensagem.add_alternative(corpo_html, subtype="html")  # Versão HTML          

            # Adiciona anexos, se existirem
            if anexos:
                for caminho_arquivo in anexos:
                    with open(caminho_arquivo, "rb") as file:
                        file_data = file.read()
                        file_name = file.name.split("/")[-1]
                        mensagem.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)

            # Conecta no servidor SMTP com segurança
            contexto = ssl.create_default_context()
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as servidor:
                servidor.starttls()
                servidor.login(self.username, self.password)               
                servidor.send_message(mensagem)

            print("E-mail enviado com sucesso!")

        except Exception as e:
            print(f"Erro ao enviar e-mail: {e}")
        finally:
            servidor.quit()
