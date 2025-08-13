import smtplib
import base64
from email.mime.text import MIMEText
from config import config

def sendEmail():
    params = config('config.ini', 'env')

    from_email = params['email']
    to_email = params['test_receiver']

    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.ehlo()
    smtp.login(from_email, params['email_password'])

    msg = MIMEText("You the goat")
    msg['Subject'] = 'Weather Automation Test Email'

    smtp.sendmail(from_email, to_email, msg.as_string())

    smtp.quit()
    print(f"Email sent to {to_email} from {from_email}")

if __name__ == "__main__":
    sendEmail()