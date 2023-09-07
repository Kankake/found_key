import imaplib
import email
from email.header import decode_header
import re

def found_key():
    mail_pass = "----" #Код mail
    username = "-----" #Название email
    imap_server = "imap.mail.ru"
    imap = imaplib.IMAP4_SSL(imap_server)
    imap.login(username, mail_pass)
    imap.select("INBOX")
    data = []
    while not data:
        result, data = imap.search(None, "UNSEEN")
        ids = data[0] # Получаем строку номеров писем
        id_list = ids.split() # Разделяем ID писем
        latest_email_id = id_list[-1] # Берем последний ID
    res, message = imap.fetch(latest_email_id, '(RFC822)')  #Для метода search по порядковому номеру письма
    msg = email.message_from_bytes(message[0][1])
    for part in msg.walk():
        if part.get_content_type() == 'text/html':
            html = part.get_payload(decode=True)
            charset = part.get_content_charset()
        if charset:
            html = html.decode(charset)
    regex= (r'\d{6}')
    return (re.findall(regex,html)[0])
