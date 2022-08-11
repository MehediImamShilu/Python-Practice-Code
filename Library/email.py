# Caution
# NOTE: This code not work properly
# Values must be appropriate

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

template = Template(Path("template.html").read_text())

message = MIMEMultipart()

# E-mail sending procedure
message["from"] = "Mehedi Imam Shilu"
message["to"] = "hh1708741@gmail.com"
message["subject"] = "This is a test"

# attaching Text body from html template file
# Without using dictionary: name="Hasan"
body = template.substitute({"name": "Hasan"})
message.attach(MIMEText(body, "html"))

# attaching image to mail body in binary format
message.attach(MIMEImage(Path("Tuwel.jpg").read_bytes()))

# This line is not clear to me
with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:     # imaginary
    smtp.ehlo()
    smtp.starttls()
    smtp.login("mehediimamshilu007@gmail.com", "evergiven")     # imaginary
    smtp.send_message(message)
    print("Sent...")
