import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Email configuration
sender_email = 'enviaemailpy@gmail.com'
sender_password = 'litfdpbgjiaufdsh'
receiver_email = 'joaovitormendesborges@gmail.com'
subject = 'Preço dos Produtos'

# Create a multipart message and set the headers
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject

# Add the file attachment to the message
attachment_path = 'preco_ordem.xlsx'

with open(attachment_path, 'rb') as file:
    # Add file as application/octet-stream
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(file.read())

# Encode the file in ASCII characters to send by email    
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    'Content-Disposition',
    f'attachment; filename=preco_ordem.xlsx'
)

# Attach the file to the message
message.attach(part)

# Convert the message to a string and send the email
try:
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    print('Email sent successfully!')
except smtplib.SMTPException as e:
    print('Error sending email:', str(e))
