#simple mail transfer protocol
import smtplib
import smtplib, ssl
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart()
myid = email.utils.make_msgid()
msg["Subject"] = "sample gmail"
msg["From"] =sent_from
msg["To"] = send_to
msg.add_header("Message-ID", myid)
msgAlternative = MIMEMultipart('alternative')
msg.attach(msgAlternative)
msgText = MIMEText("sample email", 'html')
msgAlternative.attach(msgText)

server = smtplib.SMTP_SSL('smtp.gmail.com',465)
server.ehlo()
server.login("username","password" )
server.sendmail(sent_from, send_to, msg.as_string())
print(msg.add_header("In-Reply-To", myid))
print(msg.add_header("References", myid))
print(myid)
server.close()
#remstatus= 'email '+reminder+'   done.