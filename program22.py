#SENDING MAIL TO USER
import smtplib
#creating SMTP session
a=smtplib.SMTP('smtp.gmail.com',587)
#starting TLS for security
a.starttls()
#Authentication
a.login("syedulla7@gmail.com","syed123ulla")
#defining message
message="This is my test message for PWP."
#Sending mail to user
a.sendmail("syedulla7@gmail.com","rohan201120@gmail.com",message)
#Ending the session
a.quit()