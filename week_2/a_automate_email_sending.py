''' You work at a company that sends daily reports to clients via email.
The goal of this project is to automate the process of sending these reports
via email.

Here are the steps you can take to automate this process:

    - Use the smtplib library to connect to the email server and send
    the emails.

    - Use the email library to compose the email, including the recipient's
    email address, the subject, and the body of the email.

    - Use the os library to access the report files that need to be sent.

    - Use a for loop to iterate through the list of recipients and send the
    email and attachment.

    - Use the schedule library to schedule the script to run daily
    at a specific time.

    - You can also set up a log file to keep track of the emails that
    have been sent and any errors that may have occurred during the email
    sending process. '''

import smtplib
#from email.mime.text import MIMEText
#from email.mime.multipart import MIMEMultipart 

def sendEmailTo(rec_email, sub, body):

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'mentoriafamiliar@gmail.com'
    smtp_password = 'j1l2a3j4'

    message = f'Subject: {sub}\n\n{body}'

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as smtp:
            smtp.starttls()
            smtp.login(smtp_username, smtp_password)
            smtp.sendmail(smtp_username, rec_email, message)
    
    except TimeoutError as e:
        print('Oh no!! something wrong occured')
        print(type(e), e)
    
    else:
        print('Message sended succesfully!')


if (__name__ == "__main__"):
    email = "rangeljc@gmail.com"
    sub = "Python email automation test"
    body = "Hi my name is Julio. This is an automated email sent using Python."

    sendEmailTo(email, sub, body)