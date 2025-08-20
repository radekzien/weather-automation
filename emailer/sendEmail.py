import smtplib
import base64
import datetime
from .emailFormatter import format_email
from email.mime.text import MIMEText
from config import config

def sendEmail(theData=None, to_email=None, receiver_name=None):
    params = config('config.ini', 'env')

    from_email = params['email']

    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.ehlo()
    smtp.login(from_email, params['email_password'])

    msg = MIMEText('')

    if receiver_name is None:
        receiver_name = "User"

    if theData is None:
        theData = "No data provided."
        msg.set_content(theData)
        msg['Subject'] = 'Issue with your weather update'
        msg['From'] = from_email
    else:
        msg = format_email(receiver_name, theData)
        msg['Subject'] = 'Weather update for ' + datetime.datetime.now().strftime('%A %#d %B')
        msg['From'] = from_email

    if to_email:
        smtp.sendmail(from_email, to_email, msg.as_string())

    smtp.quit()
    print(f"Email sent to {receiver_name}")

if __name__ == "__main__":
    sendEmail()