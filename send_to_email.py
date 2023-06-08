import smtplib
from email.message import EmailMessage

password = ""
sender = 'mirmukhammadmirkabilov@gmail.com'
server = "smtp.gmail.com"
port = 465
receiver = "absaitovdev@gmail.com"
msg = EmailMessage()
msg['Subject'] = "Imtihon / Mirmuhammad Mirkabilov"
msg['From'] = sender
msg['To'] = receiver
msg.set_content("githublink:https://github.com/Mirmukhammad/imtihon"
                "dockerhublink:mirmuhammad/my_exam_bot:latest")

with smtplib.SMTP_SSL(server, port) as mail:
    mail.login(sender, password)
    mail.send_message(msg)
    print("Success")