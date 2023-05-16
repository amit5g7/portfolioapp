import smtplib
import ssl

host = "smtp.gmail.com"
port = 465

username="amitguptawk@gmail.com"
password="zgtjepilpphaqvfw"

context= ssl.create_default_context()

receiver="amitguptawk@gmail.com"
message="""\
Subject: Hi
how are you

"""
with smtplib.SMTP_SSL(host,port,context=context) as server:
    server.login(username,password)
    server.sendmail(username,receiver,message)


