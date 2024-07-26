import user1
import finance_manager
from datetime import datetime

class Transaction:
    def init(self, amount, date, description):
        self.amount = amount
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.description = description

    def str(self):
        return f"Transaction(amount={self.amount}, date={self.date}, description='{self.description}')"