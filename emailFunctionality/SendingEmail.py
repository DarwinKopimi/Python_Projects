#!/usr/bin/env python3
#python -m smtpd -n -c DebuggingServer localhost:1025
#The ^ code is to start a local smtp server
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#first class made
class myEmailModule:

 def emailSendMod():
  emailMine = 'placeholder'
  with open('textfile','r') as fp:
   msg = MIMEText(fp.read())
   
  msg=MIMEMultipart()
  msg['Subject'] = "Test Email"
  msg['From']= emailMine
  msg['To']= emailMine
#server and port number it is on
  smtp = smtplib.SMTP('localhost',1025)
  smtp.send_message(msg)
  smtp.quit()
 emailSendMod()
