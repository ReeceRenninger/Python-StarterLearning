# IMAP internet message access protocol
# the built in imap module is very difficult to use so we will use third party module called imapclient and pyzmail
# docs can be found at: 
# https://imapclient.readthedocs.io/en/2.2.0/ 
# http://www.magiksys.net/pyzmail/
# https://automatetheboringstuff.com/chapter16/

#! pyzmail has some issues with specific versions of python so you may need to use pip install pyzmail36 if you are using python 3.6+

import imapclient
import pyzmail

conn = imapclient.IMAPClient('imap.gmail.com', ssl=True) # ssl is for encryption
conn.login('email', 'password') # login to email, this will return a bitesized string with b' notifying you of success

conn.select_folder('INBOX', readonly=True) # readonly=True means we can't delete emails

UIDS = conn.search(['SINCE 20-Aug-2022']) # search for emails since a certain date
print(UIDS) #unique ids of emails

#** you will need to pass the UID actual value to the fetch method
rawMessage = conn.fetch([UIDS[0]], ['BODY[]', 'FLAGS']) # fetch the first email in the list and get the body and flags which are parts of the email

#** you will need to pass the UID actual value to the pyzmail method
message = pyzmail.PyzMessage.factory(rawMessage[UIDS[0]][b'BODY[]']) # this will return a pyzmail object
message.get_subject() # get the subject of the email
message.get_addresses('from') # get the from address of who sent it
message.get_addresses('to') # get the to address of who it was sent to
message.get_addresses('bcc') # get the bcc address of who it was sent to

message.text_part # get the text part of the email
message.html_part # get the html part of the email

message.text_part.get_payload().decode('UTF-8') # get the text part of the email and decode it
message.html_part.get_payload().decode('UTF-8') # get the html part of the email and decode it

conn.list_folders() # list all the folders in the email in tuple form

conn.select_folder('INBOX', readonly=False) # readonly=False means we can delete emails
UIDS = conn.search(['ON 08-Sep-2023']) # search for emails on a certain date

conn.delete_messages([UIDS[0]]) # delete the first email in the list

conn.logout() # logout of email