import json
import user1
from finance_manager import FinanceManager
from transaction import Transaction

def main():
    fm = FinanceManager()

    # افزودن یک کاربر جدید
    fm.add_user("Alice", "password123")

    # ورود کاربر
    user = fm.login("Alice", "password123")

    if user:
        # افزودن تراکنش‌ها
        user.add_transaction(Transaction("2024-07-19", "income", 1000, "Salary"))
        user.add_transaction(Transaction("2024-07-20", "expense", 50, "Groceries"))

        # تولید و نمایش گزارش به حالت یک فایل json
        report = user.generate_report()
        print(json.dumps(report, indent=4, ensure_ascii=False))

if name == "main":
    main()