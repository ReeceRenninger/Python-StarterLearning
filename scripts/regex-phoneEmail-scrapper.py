#! /usr/bin/python3

import re, pyperclip

# TODO: create a regex for phone numbers
phoneRegex = re.compile(r''' 
# types of numbers to extract: 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
(
((\d{3})|(\(\d{3}\)))?     # area code (optional)
(\s|-)     # first separator 
\d{3}     # first 3 digits
-        # separator
\d{4}        # last 4 digits
((ext(\.)?\s|x)      # extension (optional)
\d{2,5})?    # extension number (optional)
)
''', re.VERBOSE)


# TODO: create a regex for email addresses
emailRegex = re.compile(r'''
# types of emails to extract: something@something.com

\b[a-zA-Z0-9_.+]+    # name part
@    # @ symbol
[a-zA-Z0-9_.+]+    # domain name   part                                 

                        
''', re.VERBOSE)

# TODO: get the text off the clipboard
text = pyperclip.paste()

# TODO: extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
  allPhoneNumbers.append(phoneNumber[0])
# print(allPhoneNumbers)


# TODO: copy the extracted email/phone to the clipboard
extractedEmail = emailRegex.findall(text)

# print(extractedEmail)

#! final results
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results) # copies results to clipboard