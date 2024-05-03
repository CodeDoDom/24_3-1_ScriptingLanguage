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
msg['Subject'] = 'PDF 첨부 전송'
msg['From'] = '윤이하나<8000gameplayer@gmail.com>'
msg['To'] = '8000gameplayer@gmail.com'
msg.set_content('첨부')

import mimetypes

# fname = 'dog1.png'
# ctype, _ = mimetypes.guess_type(fname)
# if not ctype:
#     ctype = 'application/octect-stream'     # 잘 모를 때 디폴트로
#
# maintype, subtype = ctype.split('/')
#
# with open(fname, 'rb') as f:
#     msg.add_attachment(f.read(), maintype=maintype, subtype=subtype, filename='dog1')

fname = 'LEC12 - Email.pdf'
ctype, _ = mimetypes.guess_type(fname)
if not ctype:
    ctype = 'application/octect-stream'     # 잘 모를 때 디폴트로

maintype, subtype = ctype.split('/')

with open(fname, 'rb') as f:
    msg.add_attachment(f.read(), maintype=maintype, subtype=subtype, filename=fname)

mail_server.send_message(msg)
