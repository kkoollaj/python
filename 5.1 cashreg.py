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

        self.coins = [1, 5, 7, 10, 15]

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
            for available_product in self.products.keys():
                if product == available_product.lower():
                    if available_product in selected_products:
                        selected_products[available_product] += 1
                    else:
                        selected_products[available_product] = 1
                    break
            else:
                print("Продукт не найден.")
        return selected_products

    def calculate_total(self, selected_products):
        total = sum(self.products[product] * quantity for product, quantity in selected_products.items())
        return total

    def calculate_change(self, total, payment):
        change = payment - total
        change_coins = []
        coin_counts = {}

        for coin in self.coins:
            coin_counts[coin] = 0

        while change > 0:
            for coin in sorted(self.coins, reverse=True):
                while change >= coin:
                    change_coins.append(coin)
                    coin_counts[coin] += 1
                    change -= coin

        min_coins = sum(coin_counts.values())
        coin_details = " ".join([f"{count}({coin})" for coin, count in coin_counts.items() if count > 0])

        return change_coins, min_coins, coin_details

    def display_receipt(self, selected_products, total, change_coins, min_coins, coin_details):
        print(f"Общая стоимость: {total} рублей")
        print(f"Сдача: {sum(change_coins)} рублей. Минимальное количество монет: {min_coins} – {coin_details}")
        print()
        print("Спасибо за покупку!")

def main():
    cash_register = CashRegister()
    selected_products = cash_register.select_products()
    total = cash_register.calculate_total(selected_products)
    print("Чек:")
    for product, quantity in selected_products.items():
        print(f"{product}: {quantity}")
    print()
    print(f"Общая стоимость: {total} рублей")

    while True:
        payment = int(input("Введите сумму для оплаты: "))
        if payment < total:
            print("Недостаточно средств.")
        else:
            change_coins, min_coins, coin_details = cash_register.calculate_change(total, payment)
            cash_register.display_receipt(selected_products, total, change_coins, min_coins, coin_details)
            break

if __name__ == "__main__":
    main()
