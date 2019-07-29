import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

msg = MIMEMultipart()
msg.attach("mapa.html")

msg['Subject'] = 'The contents of ' #+ airports.csv
msg['From'] = 'haaritsubaki@gmail.com'
msg['To'] = 'romanglegola@gmail.com'

s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
s.login('haaritsubaki@gmail.com', 'mko0nji9bhu8')
s.starttls()

s.sendmail(msg['From'], [msg['To']], msg.as_string())

s.quit()
