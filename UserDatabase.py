class UserDatabase:

    def __init__(self):
        self.user_db = {}

    def get_user(self, user_cpf: str) -> dict | None:
        return self.user_db.get(user_cpf)

    def add_new_user(self, user_data: dict) -> None:
        if "cpf" not in user_data:
            name = user_data.get("name", "UNKNOWN")
            raise ValueError(f"Error while trying to add user: {name} due to missing 'CPF' field.")
        if "name" not in user_data:
            cpf = user_data.get("cpf", "UNKNOWN")
            raise ValueError(f"Error while trying to add user: {cpf} due to missing 'NAME' field.")
        self.user_db[user_data['cpf']] = user_data
