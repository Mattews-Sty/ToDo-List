import os
import smtplib
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))

def send_email(user_email, task):
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(EMAIL_USER, EMAIL_PASS)
    message = f"Hola, la tarea '{task}' ha sido completada."
    server.sendmail(EMAIL_USER, user_email, message)
    server.quit()
    print(f"Correo enviado a {user_email}")

# Prueba del sistema
send_email("usuario@example.com", "Revisar feature branch")
