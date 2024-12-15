from UserDatabase import UserDatabase

class UserCreator:

    def __init__(self, user_db: UserDatabase):
        self.user_database = user_db

    def is_user_registered(self, cpf: str) -> bool:
        return self.user_database.get_user(cpf) is not None

    def register_new_user(self, user_data: dict) -> dict:
        if self.is_user_registered(user_data["cpf"]):
            raise ValueError('User already registered')
        self.user_database.add_new_user(user_data)
        return {"status": "success", "message": f"User {user_data['name']} with CPF: {user_data['cpf']} registered with success!"}
