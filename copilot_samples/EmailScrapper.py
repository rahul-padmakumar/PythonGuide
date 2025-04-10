
# Function for parsing the eml email file

import email
from email.parser import BytesParser
from email import policy

def parse_email(file_path):
    """
    Parses an email file.

    Args:
        file_path (str): The path to the email file.
    """
    with open(file_path, 'rb') as file:
        msg = BytesParser(policy=policy.default).parse(file)

    print(f"Subject: {msg['Subject']}")
    print(f"Sender: {msg['From']}")
    
    # Get the body of the email
    if msg.is_multipart():
        body = ''
        for part in msg.walk():
            if part.get_content_type() == 'text/plain':
                body = part.get_payload(decode=True).decode()
                break
    else:
        body = msg.get_payload(decode=True).decode()

    print(f"Body: {body}")


# Example usage    
parse_email('web_scraping/email.eml')

