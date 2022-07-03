import smtplib
import ssl
from email.message import EmailMessage

subject = "Email From Dhruv"
body = "Seth Printers 23-RMV Road, Udaipur"
sender_email = "aviseth.3214@gmail.com"
receiver_email = "sethdhruv46@gmail.com"
password = input("Enter your password: ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(body)

context = ssl.create_default_context()

print("Sending Email!")

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Success")    
