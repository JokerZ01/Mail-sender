import smtplib

user = "pythonsmtpmailerr@gmail.com"
user_password = "***Password***"

recipient = "****Mail you want to make the post.****"
subjects = "Hello I'm Mailer!"
msg = "Hello i am mailer this is also my test message"


email_text = """
From: {}
To: {}
Subject: {}
{}
""".format(user, recipient, subjects, msg)

try:
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(user,user_password)
    server.sendmail(user, recipient, email_text)
    server.close()

    print('Mail Sended')

except:
    print("OOOPPPSSS!!!!!")
