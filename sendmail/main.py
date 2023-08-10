import smtplib

my_email = "chaunm.hmc@gmail.com"
password = "fakepassword" # in app passwords

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="chauchaubau@gmail.com", msg="hello happy birthday be gau")
    connection.close()