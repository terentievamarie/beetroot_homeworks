import re


class EmailValidator:
    def __init__(self, email):
        if EmailValidator.validate(email):
            self.email = email
            print("Valid email. ")
        else:
            print(f"{email} is not valid. ")

    @classmethod
    def validate(cls, email):
        parts = email.split('@')

        if len(parts) == 2:
            prefix_part = parts[0]
            domain_part = parts[1].split('.')
            special_s = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

            if prefix_part[0] in special_s or domain_part[0][0] in special_s:
                return False

            if re.search(r'\.{2,}', prefix_part) or any(re.search(r'\.{2,}', part) for part in domain_part):
                return False

            if all(s.replace('-', "").replace('_', "").replace(".", "").isalnum() for s in prefix_part) and \
                    all(s.replace('.', '').isalnum() for s in domain_part):
                return True

        return False


user_1 = EmailValidator("a@gmail.com")
user_2 = EmailValidator("ter..@gmail.com")

user_3 = EmailValidator("!gmail.com")
