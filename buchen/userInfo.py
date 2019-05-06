import pickle

class userInfo:

    def __init__(self, vorname, nachname, gebdatum, task, emailAlert):#visanummer, vorgangsnummer, senderEmail, senderPassword, emailAddress,):
        self.vorname = vorname
        self.nachname = nachname
        self.gebDatum = gebdatum
        self.task = task
        # self.nummer = nummer
        self.emailAlert = emailAlert

    @classmethod
    def from_input(cls):
        return (cls(
            raw_input('Enter your Vorname: '),
            raw_input('Enter your Nachname: '),
            raw_input('Enter your date of birth (yyyy-mm-dd): '),
            int(raw_input('Do you want to book a new appointment (1) or '
                          'change the date of your appointment (2)? Select 1 or 2: ')),
            int(raw_input('Do you want to set up an email alert? Select 1 (Yes) or 2 (No): '))

        ))

def create_userinfo():
    user = userInfo.from_input()
    # visa / vorgangs nummer
    if user.task == 1:
        visa_status = int(raw_input('Do you already have a visa? 1 (Yes) or 2 (No) :'))
        if visa_status == 1:
            user.visanummer = raw_input('Enter the visa number :')
    elif user.task == 2:
        user.vorgangsnummer = raw_input('Enter Vorgangsnummer of your appointment: ')

    # email alert setup
    if user.emailAlert == 1:
        user.senderEmail = raw_input("Let's set up an automated e-mail Alert. Enter a Gmail address, "
                                     "from which alert emails will be sent. Normally, this is your email address: ")
        user.senderPassword = raw_input('Enter your password for the above account: ')
        user.emailAddress = raw_input('Enter an email address, to which alert emails will be sent.'
                                      'Again, normally, this is your email address: ')

    with open('userInfo.pkl', 'wb') as output:
        pickle.dump(user, output, pickle.HIGHEST_PROTOCOL)

def load_userinfo():
    # with open('/Users/kwangjun/PycharmProjects/TerminBuchen/buchen/userInfo.pkl', 'rb') as handle:
    with open('userInfo.pkl', 'rb') as handle:
        user_info = pickle.load(handle)
    return user_info

