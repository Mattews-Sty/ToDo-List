import os
import smtplib
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener credenciales y configuración del servidor SMTP
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))

"""
Envía un correo electrónico notificando la finalización de una tarea.

:param user_email: Dirección de correo del destinatario.
:param task: Nombre de la tarea completada.
"""
def send_email(user_email, task):
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)

        # Asegurar que el mensaje use UTF-8
        subject = "Notificación De Tarea Completada"
        message = f"Hola,\n\nLa tarea '{task}' ha sido completada.\n\nSaludos!"
        email_body = f"Subject: {subject}\n\n{message}".encode("utf-8")

        # Enviar correo
        server.sendmail(EMAIL_USER, user_email, email_body)
        server.quit()

        print(f"✅ Correo enviado correctamente a {user_email}")

    except smtplib.SMTPAuthenticationError:
        print("❌ Error de autenticación: verifica tus credenciales.")
    except Exception as e:
        print(f"❌ Error al enviar el correo: {e}")


# Prueba del sistema
if __name__ == "__main__":
    send_email("mattews3007@gmail.com", "Revisar develop branch")
