import smtplib

def send_email(subject,msg):
    try:
        server=smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(EMAIL_ADDRESS,PASSWORD)
        message= 'Subject:{}\n\n{}'.format(subject,msg)
        server.sendmail(EMAIL_ADDRESS,listofaddress,message)
        server.quit()
        print("Success:Email Sent!")
    except:
        print("Email failed to send")

EMAIL_ADDRESS="snp.project234@gmail.com"
PASSWORD="snpproject@123"


print("Enter the subject")
subject=input()

print("Enter the message to be sent")
msg=input()

print("Enter the recipient adressess")
listofaddress=list(map(str,input().split()))


send_email(subject,msg)