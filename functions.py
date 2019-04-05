import smtplib
import pickle


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



def create_userinfo():
    userinfo = {}

    userinfo['task'] = int(raw_input('Do you want to book a new appointment (1) or '
                                     'change the date of your appointment (2)? Select 1 or 2: '))
    if userinfo['task'] == 1:
        userinfo['visanummer'] = raw_input('If you already have a visa, enter the visa number. Otherwise hit enter: ')
    elif userinfo['task'] == 2:
        userinfo['vorgangsnummer'] = raw_input('Enter Vorgangsnummer of your appointment: ')
    else:
        raise ValueError('Wrong input. Please either choose 1 for a new booking or 2 for a change')

    userinfo['vorname'] = raw_input('Enter your Vorname: ')
    # capitalize first letter and small the rest
    userinfo['nachname'] = raw_input('Enter your Nachname: ')
    # capitalize first letter and small the rest
    userinfo['GebDatum'] = raw_input('Enter your date of birth (yyyy-mm-dd): ')
    # check if the date exists in the calendar
    # check if the person is older than at least 16 and younger than 100
    userinfo['sender_email'] = raw_input('Enter the Gmail address of a sender: ')
    userinfo['sender_password'] = raw_input('Enter its password: ')
    userinfo['email_address'] = raw_input('Enter your Gmail address as a receiver: ')

    with open('userinfo.pickle', 'wb') as handle:
        pickle.dump(userinfo, handle, protocol=pickle.HIGHEST_PROTOCOL)


def load_userinfo():
    with open('userinfo.pickle', 'rb') as handle:
        user_info = pickle.load(handle)
    return user_info
