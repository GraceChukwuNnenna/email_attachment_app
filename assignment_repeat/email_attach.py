#Build an application that will send an attachment document to your email every 24hour. 
#The application should run as an executable file.

import smtplib
from email.message import EmailMessage
import ssl
import datetime
import time
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
import os
import sys

sender = input("senders email: ")
recipient = input("recipients email: ")

timenow = datetime.datetime.now()

# time.sleep(20)

# Create send_mail function
def send_attach():
    # Set the email parameters.
    sender = "emchadexglobal@gmail.com"
    recipient = ""
    mypassword = "ewhkaqtxojttbbub"
    subject = "Timed email attachment testing in python"

    # Create the email message; by Creating an Obj of MIMEmultipart()
    email_me = MIMEMultipart()
    email_me["Subject"] = subject
    email_me["From"] = sender
    email_me["To"] = recipient

  # Open the document to be attached.
    with open(os.path.join(sys.path[0], "Test_Data.pdf"), "rb") as fpd:
        file_content = fpd.read()

  # Create a MIME attachment object.
    attachment = MIMEBase("application", "octet-stream")
    attachment.set_payload(file_content)

  # Encode the attachment in base64.
    encoders.encode_base64(attachment)
    fpd.close()
  # Add the attachment to the email message.
    email_me.attach(attachment)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as mailme:
        mailme.login(sender, mypassword)
        mailme.sendmail(sender, recipient, email_me.as_string())
        # mailme.send_message(email_me)

    print(time.strftime("%c"))
    print("Attachment sent!")
    
    if timenow.second == 10:
        return mailme
# while loop for infinite excecution of send_mail at every time.sleep()
while True:
  send_attach()
  time.sleep(10)

send_attach()