import smtplib
import imapclient
import email
from email.message import EmailMessage
from email.policy import default

import mypass
id = mypass.id
passwd = mypass.passwd

imap_server = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imap_server.login(id, passwd)

imap_server.select_folder('INBOX')
mail_id_list = imap_server.gmail_search('등록 after:2024/4/23 before:2024/5/8')      # 특정 기간 동안 '등록'이라는 단어가 들어간 제목의 메일 번호

for id, raw_message in imap_server.fetch(mail_id_list, 'RFC822').items():
    # email message 읽기 완성
    email_message = email.message_from_bytes(raw_message[b'RFC822'], policy=default)
    date = email_message['Date']
    sender = email_message['From']
    subject = email_message['Subject']
    print(f'{id=} {date=} {sender=} {subject}')

imap_server.logout()
