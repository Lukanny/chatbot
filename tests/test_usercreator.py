import unittest

from UserCreator import UserCreator
from UserDatabase import UserDatabase

class TestUserCreator(unittest.TestCase):

    def test_is_user_registered(self):
        user_db = UserDatabase()
        creator = UserCreator(user_db)
        user_not_registered = {"name": "João", "cpf": "12345678901"}

        is_user_registered = creator.is_user_registered(user_not_registered["cpf"])

        self.assertFalse(is_user_registered)

    def test_register_new_user(self):
        user_db = UserDatabase()
        creator = UserCreator(user_db)
        user_to_register = {"name": "João", "cpf": "12345678901"}

        result = creator.register_new_user(user_to_register)

        self.assertEqual(result["status"], "success")
        self.assertTrue(creator.is_user_registered(user_to_register["cpf"]))


    def test_register_new_user_fail(self):
        user_db = UserDatabase()
        creator = UserCreator(user_db)
        user_to_register = {"name": "João", "cpf": "12345678901"}

        creator.register_new_user(user_to_register)

        with self.assertRaises(ValueError) as context:
            creator.register_new_user(user_to_register)
        self.assertEqual(str(context.exception), "User already registered")
