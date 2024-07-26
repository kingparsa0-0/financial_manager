from user1 import User

class FinanceManager:
    def init(self):
        # ایجاد یک دیکشنری برای ذخیره کاربران
        self.users = {}

    def add_user(self, username, password):
        # اضافه کردن یک نفر جدید
        if username in self.users:
            print("User already exists.")
        else:
            self.users[username] = User(username, password)
            print(f"User {username} added successfully.")

    def login(self, username, password):
        # ورود نفر با بررسی نام کاربری و رمز عبور
        if username in self.users and self.users[username].check_password(password):
            print(f"User {username} وارد شد.")
            return self.users[username]
        else:
            print("Invalid credentials.")
            return None