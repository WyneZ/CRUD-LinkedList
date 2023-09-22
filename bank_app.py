import atexit

from bank_db import Linked_List


# Data Storing when program crush/exit
@atexit.register
def storing():
    while db.head is not None:
        print("11[BA]", type(db.head.data))
        db.storeIN_DB(db.head.data)
        db.head = db.head.next

    print(11, "Storing Successfully!!")


class Bank_App:
    def __init__(self):
        self.user_menu()

    def user_menu(self):
        print("Welcome From Bank App")

        while True:
            option = input("1. Reg\n2. Login\n>")
            if option == '1':
                self.user_registration()
                break

            elif option == '2':
                self.user_login()
                break

            elif option == '3':
                # exit(db.storeIN_DB())
                exit()

            elif option == '4':
                for i in db.get_all():
                    print(43, i['email'])

            else:
                print("Invalid Option")

    def user_registration(self):
        print("_____This is User Registration Section_____")
        while True:
            while True:
                r_email = input("Enter email for User registration: ")
                flag = self.email_checking(r_email)  # 1 or -1
                if flag == 1:
                    break
                else:
                    print("Email Form Invalid!\n")
            print("Email Form Valid ")

            if self.isExisting_email(r_email):
                try:
                    pass1 = input("Enter your password to register: ")
                    pass2 = input("Enter your password again to register: ")

                    if pass1 == pass2:
                        print("Password Was match!\n")
                        name = input("Enter your name: ")
                        ph = input("Enter your phone number: ")
                        amount = input("Enter your amount to deposit: ")
                        # var = vars(self.user)
                        # pprint(var)
                        # print(type(var))
                        user_dict: dict = {'email': r_email, 'password': pass2,
                                           'name': name, 'phone': ph, 'money': amount}
                        print(db.insert(user_dict))

                        self.user_menu()
                        # self.user_function(user_dict)

                    else:
                        print("Password not match!")

                except Exception as err:
                    print(53, err)

            return False

    def user_login(self):
        print("_____This is User Login Section_____")
        while True:
            l_email = input("Enter your email to login: ")
            if not self.isExisting_email(l_email):
                user_dict: dict = db.retrieve(l_email)
                while True:
                    l_pw = input("Enter your password to login: ")
                    if user_dict['password'] == l_pw:
                        print("Login Successful!\n")
                        # self.user_menu()
                        self.user_function(user_dict)
                        return False

    # This is Email Format Checking Section
    def email_checking(self, r_email: str):
        name_counter = 0
        for i in range(len(r_email)):
            if r_email[i] == '@':
                # print("Name End Here")
                break
            name_counter += 1

        email_name = r_email[0:name_counter]
        email_form = r_email[name_counter:]

        # checking for name
        name_flag = 0
        email_flag = 0
        for i in range(len(email_name)):
            aChar = email_name[i]
            if (31 < ord(aChar) < 48) or (57 < ord(aChar) < 65) or (
                    90 < ord(aChar) < 97) or (122 < ord(aChar) < 128):
                name_flag = -1
                break

        domain_form = ["@facebook.com", "@ncc.com", "@mail.ru", "@yahoo.com", "@outlook.com", "@apple.com", "@zoho.com",
                       "@gmail.com"]

        for i in range(len(domain_form)):

            if domain_form[i] == email_form:
                email_flag = 1
                break

        if name_flag == -1 or email_flag == 0:
            return -1

        else:
            return 1

    # Check the registered email is already existed or not
    def isExisting_email(self, r_email):
        data_list: list = db.get_all()
        for i in data_list:
            if r_email == i['email']:
                print("!!!Email is already existed!!!")
                return False
        return True

    # User can do Bank Operations in this section
    def user_function(self, user_dict: dict):

        while True:
            print("_____This is User Function Section_____")
            user_choice: str = input(f"1. Transfer money\n"
                                     f"> ")
            if user_choice == '1':
                self.transfer_money(user_dict)

    def transfer_money(self, user_dict):
        t = True
        while t:
            print("___This is Transfer Money Section___")
            recv_email: str = input("Enter Receiver Email: ")

            for i in db.get_all():
                if i['email'] == recv_email:
                    print(f"Receiver Email: {i['email']}\n"
                          f"Receiver Phone: {i['phone']}\n\n"
                          f"Your Existing Balance is {int(user_dict['money'])}\n")

                    recv_dict: dict = db.retrieve(recv_email)

                    while True:
                        remain_amount: int = int(user_dict['money'])
                        transfer_amount: int = int(input("Amount> "))
                        if remain_amount > transfer_amount:
                            while True:
                                pw = input("Confirm Password to Transfer: ")
                                if pw == user_dict['password']:
                                    sender_amount: int = remain_amount - transfer_amount
                                    user_dict['money'] = str(sender_amount)

                                    recv_amount: int = transfer_amount + int(recv_dict['money'])
                                    recv_dict['money'] = str(recv_amount)
                                    print(f"User amount: {user_dict['money']}\n"
                                          f"Recv amount: {recv_dict['money']}")
                                    db.update(user_dict)
                                    db.update(recv_dict)
                                    break
                                else:
                                    print("Wrong Password!")
                            t = False
                            break
                        else:
                            print("Please Enter Valid Amount!\n")
                    break
                else:
                    print("User Not Found!\n")


if __name__ == "__main__":
    db = Linked_List()
    app = Bank_App()
    storing()
