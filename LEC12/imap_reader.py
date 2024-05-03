import imapclient
import email
from email.policy import default

imap_server = imapclient.IMAPClient('imap.gmail.com', ssl=True)

import mypass
id = mypass.id
passwd = mypass.passwd

imap_server.login(id, passwd)
imap_server.select_folder('INBOX')
msg_id_list = imap_server.gmail_search('subject:(주소록) after:2024/5/2 before:2024/5/5')
# msg_id_list = imap_server.gmail_search('subject:(등록) after:2024/5/2 before:2024/5/5')
address_list = []


def print_message(msg):
    for part in msg.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get_content_maintype() == 'text':
            if part.get_content_maintype() == 'plain':
                body = str(part.get_payload(decode=True), part.get_content_charset())
                print(body)
        else:  # 첨부파일 존재
            fname = part.get_filename()
            if fname:
                print(f'{fname}을 저장합니다.....')
                with open(fname, 'wb') as fp:
                    fp.write(part.get_payload(decode=True))


for id, msg in imap_server.fetch(msg_id_list, 'RFC822').items():
    email_msg = email.message_from_bytes(msg[b'RFC822'], policy=default)
    print_message(email_msg)

# for id, raw_msg in imap_server.fetch(msg_id_list, 'RFC822').items():
#     email_msg = email.message_from_bytes(raw_msg[b'RFC822'], policy=default)
#     date = email_msg['Date']
#     sender_info = email_msg['From']
#     sender_address = f'{sender_info.addresses[0].username}@{sender_info.addresses[0].domain}'
#     name = email_msg['Subject'].split()[0]
#     print(f'{name=} {sender_address=}')
#     address_list.append([name, sender_address])
#
# import csv
# with open('address.csv', 'w', newline='') as wf:
#     writer = csv.writer(wf)
#     for address in address_list:
#         writer.writerow(address)
