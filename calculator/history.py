class History:
    """İşlem geçmişini saklayan ve gösteren sınıf."""

    def __init__(self):
        self.records = []

    def add_record(self, num1, operator_symbol, num2, result):
        """Yeni bir işlemi geçmişe ekler."""
        record = f"{num1} {operator_symbol} {num2} = {result}"
        self.records.append(record)

    def show_history(self):
        """Geçmişteki tüm işlemleri ekrana yazdırır."""
        if not self.records:
            print("Henüz herhangi bir işlem yapılmadı.")
            return

        print("\n--- İşlem Geçmişi ---")
        for index, record in enumerate(self.records, start=1):
            print(f"{index}. {record}")
        print("---------------------\n")