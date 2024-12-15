class UserDatabase:

    def __init__(self):
        self.user_db = {}

    def get_user(self, user_cpf: str) -> dict | None:
        user = self.user_db.get(user_cpf)
        if user is not None:
            return user
        return None

    def add_new_user(self, user_data: dict) -> None:
        self.user_db[user_data['cpf']] = user_data
