from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import pandas as pd
df=pd.read_csv("")#read email from a csv



# Define these once; use them twice!
for i in df["email"]:
    print(i)
    count=0
    try:
        strFrom = ' '
        strTo = str(i)

        # Create the root message and fill in the from, to, and subject headers
        msgRoot = MIMEMultipart('related')
        msgRoot['Subject'] = 'Whatever you wanna give it as subject'
        msgRoot['From'] = strFrom
        msgRoot['To'] = strTo
        msgRoot.preamble = 'This is a multi-part message in MIME format.'

        # Encapsulate the plain and HTML versions of the message body in an
        # 'alternative' part, so message agents can decide which they want to display.
        msgAlternative = MIMEMultipart('alternative')
        msgRoot.attach(msgAlternative)

        msgText = MIMEText('This is the alternative plain text message.')
        msgAlternative.attach(msgText)

        # We reference the image in the IMG SRC attribute by the ID we give it below
        msgText = MIMEText('<a href="https://goo.gl/KPwbM6"><img src="cid:image1" height=500px width=500px></a><br><br><b>Click Here:https://goo.gl/KPwbM6</b>', 'html')
        msgAlternative.attach(msgText)

        # This example assumes the image is in the current directory
        fp = open('b2.jpeg', 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()

        # Define the image's ID as referenced above
        msgImage.add_header('Content-ID', '<image1>')
        msgRoot.attach(msgImage)

        # Send the email (this example assumes SMTP authentication is required)
        import smtplib
        smtp = smtplib.SMTP('smtp.gmail.com:587')
        smtp.starttls()
        smtp.login('username@gmail.com', 'password')

        smtp.sendmail(strFrom, strTo, msgRoot.as_string())
        print("message sent")
        count=count=count+1
        print(count)
    except:
        pass
smtp.quit()





