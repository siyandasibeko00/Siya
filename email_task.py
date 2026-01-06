
class Email:
    has_been_read = False

    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    def mark_as_read(self):
        self.has_been_read == True

inbox = Email([])

def populate_inbox():
    first_email = Email("name1@classes.com", "Welcome to HyperionDev!", "We strive to enure that have a great experience with us.")
    second_email = Email("name2@classes.com", "Great work on the bootcamp!", "You making great progress so far, keep pushing!")
    third_email = Email("name3@classes.com", "Your excellent marks!", "Well done! You have scored a really high mark on your task.")

    inbox.append([first_email, second_email, third_email])

def list_emails():
    print("Inbox: ")

    for index, inbox in enumerate():