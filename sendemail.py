import os
import smtplib
from dotenv import load_dotenv

load_dotenv()
sendingAddress = os.getenv('sender')
email = os.getenv('email')
password = os.getenv('password')
body = """Subject: Your Email Subject\n
Hello friend,\n\nThe job has finished running. Please double check and let us know if anything is out of line.\n\nThank you,\nSender\n"""

def sendEmail():
    sender = sendingAddress
    recipients = ['yourListOfEmails@emails.com']
    message = body
    mailserver = smtplib.SMTP('smtp.office365.com', 587)

    mailserver.ehlo()
    mailserver.starttls()
    mailserver.login(email, password) # add your password 
    mailserver.sendmail(
        sender, 
        recipients, 
        message
        )
    mailserver.quit()

# call the method so the script can run
sendEmail() 
