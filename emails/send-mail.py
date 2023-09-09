# SMTP is simple mail transfer protocol
# gmail requires tls encryption and you can create app password for it at https://myaccount.google.com/apppasswords

import smtplib
conn = smtplib.SMTP('smtp.gmail.com', 587) # 587 is port number usually
conn.ehlo() # to start connection

conn.starttls() # to start tls encryption

conn.login('email', 'password') # login to email 

conn.sendmail('from', 'to', 'Subject: subject \n\n body') # send mail

conn.quit() # quit connection