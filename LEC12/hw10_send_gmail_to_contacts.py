import csv
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


def send_mail(receiver_name, receiver_gmail):
    msg = EmailMessage()
    msg['Subject'] = '안녕하세요. 반갑습니다.'
    msg['From'] = '윤이하나<8000gameplayer@gmail.com>'
    msg['To'] = receiver_gmail
    msg.set_content(f"""
    안녕하세요. {receiver_name}님. 반갑습니다.
    저는 윤이하나라고 합니다.
    잘 부탁드립니다.
    """)

    import mimetypes

    fname = 'maplestory.jpg'
    ctype, _ = mimetypes.guess_type(fname)
    if not ctype:
        ctype = 'application/octect-stream'

    maintype, subtype = ctype.split('/')

    with open(fname, 'rb') as f:
        msg.add_attachment(f.read(), maintype=maintype, subtype=subtype, filename=fname)

    mail_server.send_message(msg)


with open('address.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for address in reader:
        name, gmail = address
        send_mail(name, gmail)
        print(f"Send gmail to {name}, {gmail}")
