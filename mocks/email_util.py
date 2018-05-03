import smtplib
from email.message import EmailMessage


def send_email(subject, body, from_email, destination_email):
    try:
        _send_email(subject, body, from_email, destination_email)
    except Exception as ex:
        raise ex
    return True


def _send_email(subject, body, from_email, destination_email):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['from'] = from_email
    msg['To'] = destination_email
    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()
