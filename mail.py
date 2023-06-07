import smtplib
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
fromaddr = "davisdavis448@gmail.com"
toaddr = "hung.nguyen0304@hcmut.edu.vn"
msg = MIMEMultipart()    
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "TIÊU ĐỀ CỦA MAIL (SUBJECT)"
body = "NỘI DUNG MAIL"
try:
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "aqkjshphizdcdkcq")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
except Exception as e:
    print(str(e))