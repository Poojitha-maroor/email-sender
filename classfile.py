import smtplib as s

ob=s.SMTP("smtp.gmail.com",587)
ob.starttls()

ob.login("bityesplus16@gmail.com","Yesplus16")

print("Enter the Subject ")
subject=input()

print("Enter the body of your email ")
body=input()

message="Subject:{}\n\n{}".format(subject,body)

print("Give the mail id to be sent")
listofaddress=[input()]

ob.sendmail("bityesplus16@gmail.com",listofaddress,message)