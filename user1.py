class User:
    def init(self, username, password):
        # مقداردهی اولیه نام کاربری و رمز عبور
        self.username = username
        self._password = password
        self.transactions = []

    def check_password(self, password):
        # بررسی رمز عبور
        return self._password == password

    def add_transaction(self, transaction):
        # افزودن تراکنش جدید
        self.transactions.append(transaction)

    def generate_report(self):
        # تولید گزارش مالی
        income = sum(t.amount for t in self.transactions if t.t_type == "income")
        expenses = sum(t.amount for t in self.transactions if t.t_type == "expense")
        balance = income - expenses
        report = {
            "username": self.username,
            "total_income": income,
            "total_expenses": expenses,
            "balance": balance,
            "transactions": [t.to_dict() for t in self.transactions]
        }
        return report