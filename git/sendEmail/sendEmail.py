import yagmail, os


def sendEmail(subject = 'League of Legends', content = ['Game accepted']):
    '''takes subject and content of the email as parameters, sends an email'''
    app_passwd = os.environ.get('PYTHON_APP_PASSWD')
    email_address = 'testpython570@gmail.com'
    with yagmail.SMTP(email_address, app_passwd) as yag:
        yag.send(email_address, subject, content)

sendEmail()
