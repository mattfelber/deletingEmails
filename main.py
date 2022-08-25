import imaplib
import email
from email.header import decode_header

# insert gmail account login and password
username = ""
password = ""

# create an IMAP4 class with SSL
imap = imaplib.IMAP4_SSL("imap.gmail.com")
# authenticate
imap.login(username, password)

# select the mailbox to delete
imap.select("INBOX")

# emails before a specific date
status, messages = imap.search(None, 'BEFORE "01-OCT-2077"')

# convert messages to a list of email IDs
messages = messages[0].split(b' ')

for mail in messages:
    _, msg = imap.fetch(mail, "(RFC822)")
    # mark the mail as deleted
    imap.store(mail, "+FLAGS", "\\Deleted")


# Remove emails marked as deleted
imap.expunge()
# close mailbox
imap.close()
# logout from gmail
imap.logout()