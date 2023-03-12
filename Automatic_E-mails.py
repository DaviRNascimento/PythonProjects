# Here I did a code with smtplib and email.message libraries to send a email from
# one email to another.
# coding: utf-8

import smtplib  # this support me to send email from one server to another
import email.message


def send_email():

    corpo_email = """
    <p>Hello Davi<p>
    <p>This is only a test<p>
    <p>God bless you<p>

    """

    msg = email.message.Message()
    msg['Subject'] = ""
    msg['From'] = ""
    msg['To'] = ""
    password = 'Your google password'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()  # Puts the connection to the SMTP server into TLS mode
    
    

    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print("Email enviado")

send_email()