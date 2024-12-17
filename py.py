
import random
import sys


class Account:
    def init(self, user_id, name, address, login, password):
        self.user_id = user_id
        self.name = name
        self.address = address
        self.login = login
        self.password = password
        self.balance = 0

    def change_password(self):
        new_password = input("Введіть новий пароль: ")
        self.password = new_password
        print("Пароль успішно змінено.")

    def withdraw_money(self):
        try:
            amount = float(input("Введіть суму для зняття: "))
            if amount <= 0:
                print("Сума має бути більше нуля.")
            elif amount > self.balance:
                print("Недостатньо коштів на рахунку.")
            else:
                self.balance -= amount
                print(f"Ви зняли {amount}. Поточний баланс: {self.balance}")
        except ValueError:
            print("Невірний формат суми.")

    def transfer_money(self, other_account):
        try:
            amount = float(input("Введіть суму для переказу: "))
            if amount <= 0:
                print("Сума має бути більше нуля.")
            elif amount > self.balance:
                print("Недостатньо коштів для переказу.")
            else:
                self.balance -= amount
                other_account.balance += amount
                print(f"Ви переказали {amount}. Ваш баланс: {self.balance}")
        except ValueError:
            print("Невірний формат суми.")

    def work(self):
        earned = random.randint(50, 500)
        self.balance += earned
        print(f"Ви заробили {earned}. Поточний баланс: {self.balance}")

    def rob_bank(self):
        if random.randint(1, 10) > 7:
            stolen = random.randint(1000, 5000)
            self.balance += stolen
            print(f"Вам вдалося пограбувати банк і отримати {stolen}!")
        else:
            self.balance = 0
            print("Пограбування провалилося! Ваш баланс обнулено.")

    def take_credit(self):
        try:
            amount = float(input("Введіть суму кредиту: "))
            if amount <= 0:
                print("Сума має бути більше нуля.")
            else:
                self.balance += amount
                print(f"Ви взяли кредит на суму {amount}. Ваш баланс: {self.balance}")
        except ValueError:
            print("Невірний формат суми.")


def login(accounts):
    login_input = input("Введіть логін: ")
    password_input = input("Введіть пароль: ")
    for account in accounts:
        if account.login == login_input and account.password == password_input:
            print(f"Ласкаво просимо, {account.name}!")
            return account
    print("Неправильний логін або пароль.")
    return None


def main_menu():
    print("\nГоловне меню:")
    print("1. Ввійти в акаунт")
    print("2. Вийти")


def account_menu():
    print("\nМеню акаунта:")
    print("1. Змінити пароль")
    print("2. Зняти гроші")
    print("3. Робота")
    print("4. Пограбувати банк")
    print("5. Переказати гроші")
    print("6. Взяти кредит")
    print("7. Вийти з акаунту")


def main():
    nik = (1, "Іван", "1237537802541234", "pushkina", "user123", "pass123")
    nik2 = (1, "Іван", "1237537802541234", "pushkina", "user123", "pass123")
    accounts = [nik, nik2]

    while True:
        main_menu()
        choice = input("Виберіть опцію: ")
        if choice == "1":
            current_account = login(accounts)
            if current_account:
                while True:
                    account_menu()
                    option = input("Виберіть дію: ")
                    if option == "1":
                        current_account.change_password()
                    elif option == "2":
                        current_account.withdraw_money()
                    elif option == "3":
                        current_account.work()

                    elif option == "4":
                        current_account.rob_bank()
                    elif option == "5":
                        try:
                            other_id = int(input("Введіть ID акаунта для переказу: "))
                            other_account = next((acc for acc in accounts if acc.user_id == other_id), None)
                            if other_account and other_account != current_account:
                                current_account.transfer_money(other_account)
                            elif other_account == current_account:
                                print("Ви не можете переказати гроші самому собі.")
                            else:
                                print("Акаунт не знайдено.")
                        except ValueError:
                            print("Невірний формат ID.")
                    elif option == "6":
                        current_account.take_credit()
                    elif option == "7":
                        print("Вихід з акаунту...")
                        break
                    else:
                        print("Невірна опція. Спробуйте ще раз.")
        elif choice == "2":
            print("Завершення програми...")
            sys.exit()
        else:
            print("Невірна опція. Спробуйте ще раз.")

if __name__ == "__main__":
    main()