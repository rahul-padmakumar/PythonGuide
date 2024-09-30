import smtplib

smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
conn_resp = smtp_obj.ehlo()
tls = smtp_obj.starttls()
print(tls)

email = input("Input email: ")
password = input("Input pass: ")
smtp_obj.login(email, password)

from_address = email
to_address = email
subject = input("Input subject: ")
message = input("Enter the message: ")
msg = "Subject: " + subject + "\n" + message
smtp_obj.sendmail(from_address, to_address, msg)
smtp_obj.close()
