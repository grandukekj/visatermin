import smtplib

def send_gmailalert(sender_email, sender_password, receiver):

    subject = 'Alert: ein neuer Termin gefunden!'
    text = 'Bitte aendern Sie sofort deinen Termin.'
    content = 'Subject: %s\n\n%s' % (subject, text)

    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login(sender_email, sender_password)
    mail.sendmail(sender_email, receiver, content)
    mail.close()
    # raise error if the account-password do not match
