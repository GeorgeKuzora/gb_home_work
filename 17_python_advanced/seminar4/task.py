import decimal

MULTIPLICITY = 50
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
MIN_REMOVAL = decimal.Decimal(30)
MAX_REMOVAL = decimal.Decimal(600)
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
COUNTER4PERCENTAGES = 3
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_SUM = decimal.Decimal(10_000_000)

bank_account = decimal.Decimal(0)
count = 0
operations = []


def check_multiplicity(amount):  # Проверка кратности суммы при пополнении и снятии.
    if amount % MULTIPLICITY == 0:
        return True
    else:
        return False


def deposit(amount):  # Пополнение счёта.
    global operations
    global bank_account
    if check_multiplicity(amount):
        bank_account += amount
        operations.append(
            f"Пополнение карты на {amount} у.е. Итого {bank_account} у.е."
        )
    else:
        print(f"Сумма должна быть кратной {MULTIPLICITY} у.е.")


def withdraw(amount):  # Снятие денег.
    global operations
    global bank_account
    percent = amount * PERCENT_REMOVAL
    if percent > MAX_REMOVAL:
        percent = MAX_REMOVAL
    elif percent < MIN_REMOVAL:
        percent = MIN_REMOVAL
    removal = amount + percent
    good = True
    if not check_multiplicity(amount):
        good = False
        print(f"Сумма должна быть кратной {MULTIPLICITY} у.е.")
    if bank_account < removal:
        operations.append(
            f"Недостаточно средств. Сумма с комиссией {removal:.0f} у.е. На карте {bank_account} у.е."
        )
    elif good:
        bank_account -= removal
        operations.append(
            f"Снятие с карты {amount} у.е. Процент за снятие {percent:.0f} у.е.. Итого {bank_account:.0f} у.е."
        )


def exit():  # Завершение работы и вывод итоговой информации о состоянии счета и проведенных операциях.
    global operations
    global bank_account
    if bank_account > RICHNESS_SUM:
        tax = bank_account * RICHNESS_PERCENT
        bank_account -= tax
        operations.append(
            f"Вычтен налог на богатство {RICHNESS_PERCENT}% в сумме {tax} у.е. Итого {bank_account} у.е."
        )
    operations.append(f"Возьмите карту на которой {bank_account} у.е.")


if __name__ == "__main__":
    deposit(1000000000000000)
    withdraw(200)
    withdraw(300)
    deposit(500)
    withdraw(3000)
    exit()

    print(operations)
