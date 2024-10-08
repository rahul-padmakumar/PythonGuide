import imaplib
import email

"""


<tr>
    <td>'BEFORE date'</td>
    <td>
    Returns all messages before the date. Date must be formatted as 01-Nov-2000.
    </td>
</tr>

 <tr>
    <td>'ON date'</td>
    <td>
    Returns all messages on the date. Date must be formatted as 01-Nov-2000.
    </td>
</tr>

 <tr>
    <td>'SINCE date'</td>
    <td>
    Returns all messages after the date. Date must be formatted as 01-Nov-2000.
    </td>
</tr>

<tr> <td>'FROM some_string '</td> <td> Returns all from the sender in the string. String can be an email, for example 
'FROM user@example.com' or just a string that may appear in the email, "FROM example" </td> </tr>

<tr> <td>'TO some_string'</td> <td> Returns all outgoing email to the email in the string. String can be an email, 
for example 'FROM user@example.com' or just a string that may appear in the email, "FROM example" </td> </tr>

<tr>
    <td>'CC some_string' and/or 'BCC some_string'</td>
    <td>
    Returns all messages in your email folder. Often there are size limits from imaplib.
    To change these use imaplib._MAXLINE = 100 , where 100 is whatever you want the limit to be.
    </td>
</tr>

<tr> <td>'SUBJECT string','BODY string','TEXT "string with spaces"'</td> <td> Returns all messages with the subject 
string or the string in the body of the email. If the string you are searching for has spaces in it, wrap it in 
double quotes. </td> </tr>

<tr>
    <td>'SEEN', 'UNSEEN'</td>
    <td>
    Returns all messages that have been seen or unseen. (Also known as read or unread)
    </td>
</tr>


    <tr>
    <td>'ANSWERED', 'UNANSWERED'</td>
    <td>
    Returns all messages that have been replied to or unreplied to. 
    </td>
</tr>


    <tr>
    <td>'DELETED', 'UNDELETED'</td>
    <td>
    Returns all messages that have been deleted or that have not been deleted.
    </td>
</tr>

Keyword 	Definition 'ALL' 	Returns all messages in your email folder. Often there are size limits from imaplib. 
To change these use imaplib._MAXLINE = 100 , where 100 is whatever you want the limit to be."""

imap = imaplib.IMAP4_SSL('imap.gmail.com')

email_1 = input("Enter the email: ")
password = input("Enter the password: ")
imap.login(email_1, password)

# print(imap.list())
imap.select("INBOX")
typ, data = imap.search(None, 'SUBJECT "Test Mail"')
print(typ)
print(data)
for byt in data[0].split():
    result, email_data = imap.fetch(byt, '(RFC822)')
    raw_email = email_data[0][1].decode('utf-8')
    for part in email.message_from_string(raw_email).walk():
        if part.get_content_type() == 'text/plain':
            print(part.get_payload(decode=True))
