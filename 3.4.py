#task 3.4 from chapter 3

import re
import string

class UsernameContainsIllegalCharacter(Exception):
    """
    a class that represents an illegal character in username exception
    """
    def __init__(self, arg, index):
        self._arg = arg
        self._index = index

    def get_wrong(self):
        return self._arg[self._index]
    def get_index(self):
        return self._index

    def __str__(self):
        return f'The username contains an illegal character: "{self.get_wrong()}" at index {self.get_index()} '

class UsernameTooShort(Exception):
    """
    a class that represents an illegal short legth of a username exception
    """
    def __init__(self, arg):
        self._arg = arg
    def __str__(self):
        return "The username is too short"

class  UsernameTooLong(Exception):
    """
    a class that represents an illegal long legth of a username exception
    """
    def __init__(self, arg):
        self._arg = arg
    def __str__(self):
        return "The username is too long"

class PasswordTooShort(Exception):
    """
    a class that represents an illegal short legth of a password exception
    """
    def __init__(self, arg):
        self._arg = arg
    def __str__(self):
        return "The password is too short"

class PasswordTooLong(Exception):
    """
    a class that represents an illegal long legth of a password exception
    """
    def __init__(self, arg):
        self._arg = arg
    def __str__(self):
        return "The password is too long"

class PasswordMissingCharacter(Exception):
    """
    a class that represents an illegal password(doesn't contain the necessary characters) exception
    """
    def __init__(self, arg):
        self._arg = arg
    def __str__(self, missing):
        return f"The password is missing a character ({missing})"

#sub class for PasswordMissingCharacter in case an uppercase letter is missing
class missing_uppercase(PasswordMissingCharacter):
    def __init__(self, arg):
        super().__init__(arg)
    def __str__(self):
        return super().__str__("UpperCase")

#sub class for PasswordMissingCharacter in case a lowercase letter is missing
class missing_lowercase(PasswordMissingCharacter):
    def __init__(self, arg):
        super().__init__(arg)
    def __str__(self):
        return super().__str__("LowerCase")

#sub class for PasswordMissingCharacter in case a digit letter is missing
class missing_digit(PasswordMissingCharacter):
    def __init__(self, arg):
        super().__init__(arg)
    def __str__(self):
        return super().__str__("Digit")

#sub class for PasswordMissingCharacter in case a special letter is missing
class missing_special(PasswordMissingCharacter):
    def __init__(self, arg):
        super().__init__(arg)
    def __str__(self):
        return super().__str__("Special")

def check_input(username, password):
    """
    a function to check if a user's username and password are valid
    :param username: the user's username
    :type: string
    :param password: the user's password
    :type: string
    :return:
    """
    #username checks:
    #user name has wrong charcters
    from string import ascii_letters, digits, punctuation
    index = 0
    for letter in username:
        if letter not in ascii_letters + digits + '_':
            raise UsernameContainsIllegalCharacter(username, index )
        index += 1
    #user name too short
    if len(username) < 3:
        raise UsernameTooShort(username)
    #user name too long
    elif len(username) > 16:
        raise UsernameTooLong(username)

    #password checks:
    #password is too short
    if len(password) < 8:
        raise PasswordTooShort(password)
    #password is to long
    elif len(password) > 40:
        raise PasswordTooLong(password)
    # password doesn't contains necessary characters
    # Password checks:
    if not any(c.isupper() for c in password):
        raise missing_uppercase(password)
    if not any(c.islower() for c in password):
        raise missing_lowercase(password)
    if not any(c.isdigit() for c in password):
        raise missing_digit(password)
    if not any(c in punctuation for c in password):
        raise missing_special(password)

    else:
        print("OK")

def main():
    #kepp asking for username and password until they are correct and manage exceptions
    while True:
        username = input("enter your username-> 3 to 16 characters and must contain english letters numbers and '_': ")
        password = input("enter your password-> 8 to 40 character and must contain upper and lower case english letters, one number and 1 special character: ")
        try:
            check_input(username, password)
        except UsernameContainsIllegalCharacter as e:
            print(e)
        except UsernameTooShort as e:
            print(e)
        except UsernameTooLong as e:
            print(e)
        except PasswordTooShort as e:
            print(e)
        except PasswordTooLong as e:
            print(e)
        except PasswordMissingCharacter as e:
            print(e)
        else:
            break
if __name__ == "__main__":
    main()
