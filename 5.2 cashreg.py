class CashRegister:
    def __init__(self):
        self.products = {
            "хлеб": 35,
            "молоко": 60,
            "яйца": 70,
            "бананы": 130,
            "яблоки": 150,
            "вода": 25,
            "шоколад": 15,
            "чипсы": 120,
            "йогурт": 50,
            "сок": 90
        }

        self.coins = {1: 10, 5: 10, 10: 10, 15: 10, 20: 10}

    def display_cash_status(self):
        total_money = sum(coin * count for coin, count in self.coins.items())
        print("Состояние кассы:")
        print(f"Общая сумма денег: {total_money} рублей")
        print("Количество монет по номиналам:")
        for coin, count in self.coins.items():
            print(f"{coin} рублей: {count} шт.")
        print()

    def select_products(self):
        selected_products = {}
        print("Доступные продукты:")
        for product, price in self.products.items():
            print(f"{product}: {price} рублей")
        print()
        print("Введите название продукта или 'готово', чтобы завершить выбор и перейти к оплате.")
        while True:
            product = input("Введите продукт: ").lower()
            if product == "готово":
                print()
                if not selected_products:
                    print("Покинув магазин, вы ничего не приобрели и ощущали взгляды окружающих, словно они подозревали вас в чём-то нехорошем.")
                    exit()
                break
            if product in self.products:
                if product in selected_products:
                    selected_products[product] += 1
                else:
                    selected_products[product] = 1
            else:
                print("Продукт не найден.")
        return selected_products

    def calculate_total(self, selected_products):
        total = sum(self.products[product] * quantity for product, quantity in selected_products.items())
        return total

    def input_payment(self, total):
        print(f"Общая стоимость: {total} рублей")
        payment_coins = {1: 0, 5: 0, 10: 0, 15: 0, 20: 0}
        payment = 0

        while payment < total:
            coin = int(input(f"Введите номинал монеты для оплаты (осталось {total - payment} рублей): "))
            if coin in payment_coins:
                count = int(input(f"Введите количество монет номиналом {coin} рублей: "))
                payment_coins[coin] += count
                payment += coin * count
            else:
                print("Неправильный номинал монеты.")

        return payment, payment_coins

    def add_payment_to_cash_register(self, payment_coins):
        for coin, count in payment_coins.items():
            self.coins[coin] += count

    def calculate_change(self, total, payment):
        change = payment - total
        change_coins = {1: 0, 5: 0, 10: 0, 15: 0, 20: 0}

        sorted_coins = sorted(self.coins.items(), key=lambda x: (-x[0], -x[1]))

        for coin, count in sorted_coins:
            while change >= coin and self.coins[coin] > 0:
                change_coins[coin] += 1
                self.coins[coin] -= 1
                change -= coin

        if change > 0:
            print("Недостаточно монет для сдачи.")
            return None

        return change_coins

    def display_receipt(self, selected_products, total, payment, change_coins):
        print(f"Общая стоимость: {total} рублей")
        print(f"Оплачено: {payment} рублей")
        print("Сдача:")
        for coin, count in change_coins.items():
            if count > 0:
                print(f"{coin} рублей: {count} шт.")
        print()
        print("Спасибо за покупку!")

def main():
    cash_register = CashRegister()

    while True:
        cash_register.display_cash_status()

        selected_products = cash_register.select_products()
        total = cash_register.calculate_total(selected_products)
        print("Чек:")
        for product, quantity in selected_products.items():
            print(f"{product}: {quantity}")
        print()
        print(f"Общая стоимость: {total} рублей")

        payment, payment_coins = cash_register.input_payment(total)
        cash_register.add_payment_to_cash_register(payment_coins)

        change_coins = cash_register.calculate_change(total, payment)
        if change_coins is None:
            print("Ошибка при расчёте сдачи.")
            continue

        cash_register.display_receipt(selected_products, total, payment, change_coins)

        exit_program = input("Хотите завершить работу? (да/нет): ").lower()
        if exit_program == 'да':
            print("Работа кассы завершена.")
            break

if __name__ == "__main__":
    main()
