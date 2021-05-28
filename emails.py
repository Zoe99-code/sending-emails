import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
s = smtplib.SMTP('smtp.gmail.com', 587)
sender_email_id = 'lizzystrachan99@gmail.com'
receiver_email_id = ['thapelo@lifechoices.co.za, jamestjay85@gmail.com, mikaylabeelders@gmail.com, mujaid.kariem22@gmail.com', 'nathangiose@gmail.com']
password = input("Enter Senders Email Password: ")

subject = "Greetings"
msg = MIMEMultipart()
msg['from'] = sender_email_id
msg['To'] = ', '.join(receiver_email_id)
msg['Subject'] = subject
body = "hi guys how are you. i am doing fine\n"
body = body + "How was your task yesterday"

msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()
s.starttls()
s.login(sender_email_id, password)

s.sendmail(sender_email_id, receiver_email_id, text)
s.quit()