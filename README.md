I want to build a python program that automates the online booking process for a visa appointment at the
Auslaendbehoerde (Berlin). Upon successful implementation, it would search for an open slot in the current
and the next month and alert the user through an e-mail.

## I. Gather user info

Ask for personal information of the user required for the booking process:

    0. Book a new appointment (1) or change the date of an existing appointment (2)?
        0.1 Visanummer (if applicable)
        0.2 Vorgangsnummer
    1. Vorname?
    2. Nachname?
    3. Geburtsdatum (Tag, Monat, Jahr)?
    4. Email address
        4.1 Sender gmail handle
        4.2 Sender password
        4.3 Receiver email

Information will be saved to a pikle file, so that it can be recalled later.


## II. Loop (book or change)

    1. Go through the automated process

    2.1 if there is an opening

        Send an email to the user
        close the Chrome window
        Log "Success"
        Terminate the program
        Delete the saved personal info

    2.2 else

        Close the Chrome window
        Log "Fail"
        Wait for 4 hours and return to 1


Currently, the program can check for an open slot once at a time. Also, some of the personal information 
are set to my needs (nationality, family member, visa type, and number of applicants).


## Yet to be implemented:
* Build a scheduler: checks for an opening every 4 hours (or at a specified time) - crontab
* Terminate the scheduler when an appointment is found - crontab
* Let users choose from a list for some of the personal information (nationality, family member, visa type,
  and number of applicants) - inquirer
* Add exception/error for inappropriate user input of personal information
* Update the codes for Python 3.7
