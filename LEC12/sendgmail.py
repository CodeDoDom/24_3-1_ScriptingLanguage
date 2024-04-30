import smtplib
import email
from email.message import EmailMessage

import mypass
id = mypass.id
passwd = mypass.passwd

mail_server = smtplib.SMTP('smtp.gmail.com', 587)
mail_server.ehlo()
mail_server.starttls()
mail_server.login(id, passwd)

msg = EmailMessage()
msg['Subject'] = '[이름] 등록 요청'
msg['From'] = '8000gameplayer@gmail.com'
msg['To'] = '8000gameplayer@gmail.com'
msg.set_content('등록 요청')
mail_server.send_message(msg)
mail_server.quit()
