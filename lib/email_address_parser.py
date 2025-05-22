# your code goes here!

import re

class EmailAddressParser:
    def __init__(self, email_string):
        self.email_string = email_string

    def parse(self):
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

      
        email_list = re.findall(email_pattern, self.email_string)

        unique_emails = list(set(email_list))

        unique_emails.sort()

        return unique_emails