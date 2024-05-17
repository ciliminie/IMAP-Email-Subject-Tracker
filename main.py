import imaplib
import email
import getpass
from tqdm import tqdm

# Prompt the user for email server information
server_info = input("Enter the IMAP server : host|port|ssl|username|password: ")
# Prompt the user for the number of emails to search
num_emails = int(input("Enter the number of emails to search: "))
hostname, port, ssl, username, password = server_info.split('|')

# Convert the SSL input to a boolean
ssl = ssl.lower() == 'true'

# Connect to the IMAP server
if ssl:
    imap_server = imaplib.IMAP4_SSL(hostname, port)
else:
    imap_server = imaplib.IMAP4(hostname, port)
imap_server.login(username, password)

# Select the INBOX folder
imap_server.select('INBOX')





# Open the output file for writing
with open('out.txt', 'w') as f:
    # Loop over the selected email IDs with a progress bar
    for email_id in tqdm(reversed(email_ids.split()), total=num_emails, ncols=75):
        # Fetch the email message
        status, msg_data = imap_server.fetch(email_id, '(RFC822)')
        msg = email.message_from_bytes(msg_data[0][1])

        # Get and print the email subject
        subject = msg['Subject']
        print(subject)

        # Write the email subject to the output file
        f.write(subject + '\n')

# Close the IMAP connection
imap_server.close()
imap_server.logout()