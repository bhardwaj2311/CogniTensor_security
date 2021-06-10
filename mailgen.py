import smtplib
def SendEmail(reciever,msg):

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('sender_mail_@gmail.com', 'sender_password')
    server.sendmail('sender_mail_@gmail.com', reciever, msg)
    server.close()