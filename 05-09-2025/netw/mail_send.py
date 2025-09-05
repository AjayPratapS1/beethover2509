import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# from config import app_password, from_address, to_address
import os
from dotenv import load_dotenv

load_dotenv()  # This loads the variables from the .env file
f_a = os.getenv("from_address")
a_p = os.getenv("app_password")
to_a = os.getenv("to_address")
def send_gmail(to_a, subject, body):
    # Your Gmail address and App Password
    
    #from_address = "your_email@gmail.com"
    #app_password = "your_app_password"  # generate in Google Account -> Security -> App passwords
    

    try:
        # Create the email
        msg = MIMEMultipart()
        msg["From"] =f_a
        msg["To"] = to_a
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Connect to Gmail's SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(f_a, a_p)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        print("Error:", e)
        return False

#to_address = "receiver_username@gmail.com"
result = send_gmail(f_a, "Test Subject", "Hello from Python!")
print("Mail sent successfully?" , result)