from calculator import operations
from calculator.history import History


def show_menu():
    """Kullanıcıya işlem seçeneklerini gösterir."""
    print("\n===== PYTHON HESAP MAKİNESİ =====")
    print("1. Toplama (+)")
    print("2. Çıkarma (-)")
    print("3. Çarpma (*)")
    print("4. Bölme (/)")
    print("5. Üs alma (^)")
    print("6. Mod alma (%)")
    print("7. İşlem Geçmişini Göster")
    print("8. Çıkış")
    print("==================================")


def get_number(prompt):
    """
    Kullanıcıdan sayı ister. Kullanıcı sayı yerine harf gibi
    geçersiz bir şey girerse programı çökertmeden tekrar sorar.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Hata: Lütfen geçerli bir sayı girin.\n")


def main():
    """Programın ana döngüsü. Kullanıcı çıkış yapana kadar çalışır."""
    history = History()

    operation_symbols = {
        "1": "+",
        "2": "-",
        "3": "*",
        "4": "/",
        "5": "^",
        "6": "%",
    }

    while True:
        show_menu()
        choice = input("Bir seçenek girin (1-8): ")

        if choice == "8":
            print("Programdan çıkılıyor. İyi günler!")
            break

        if choice == "7":
            history.show_history()
            continue

        if choice not in operation_symbols:
            print("Hata: Geçersiz seçenek. Lütfen 1-8 arasında bir sayı girin.\n")
            continue

        num1 = get_number("Birinci sayıyı girin: ")
        num2 = get_number("İkinci sayıyı girin: ")

        try:
            if choice == "1":
                result = operations.add(num1, num2)
            elif choice == "2":
                result = operations.subtract(num1, num2)
            elif choice == "3":
                result = operations.multiply(num1, num2)
            elif choice == "4":
                result = operations.divide(num1, num2)
            elif choice == "5":
                result = operations.power(num1, num2)
            elif choice == "6":
                result = operations.modulus(num1, num2)

            print(f"Sonuç: {result}")
            symbol = operation_symbols[choice]
            history.add_record(num1, symbol, num2, result)

        except ValueError as error:
         print(f"Hata: {error}")

if __name__ == "__main__":
    main()
