import os
import math
import random
#  masukan library gmail
import smtplib

digits="0123456789"
otp=""
for i in range(6):
    otp+=digits[math.floor(random.random()*10)]
otp = otp + "is your OTP"
msg= otp
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("Your Gmail account", "you app passport")
emailid = input("enter your email : ")
s.sendmail('&&&&&&&&&&',emailid,msg)
if a == otp:
    print("Verified")
else:
    print("Please Check your otp again")