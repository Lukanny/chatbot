import unittest

from UserDatabase import UserDatabase

class TestUserDatabase(unittest.TestCase):

    def test_add_new_user(self):
        user_db = UserDatabase()
        new_user_joao = {"name": "João", "cpf": "12345678912"}

        user_db.add_new_user(new_user_joao)

        self.assertEqual(user_db.get_user('12345678912'), new_user_joao)

    def test_add_new_user_missing_name(self):
        user_db = UserDatabase()
        new_user_joao = {"cpf": "12345678912"}

        with self.assertRaises(ValueError) as context:
            user_db.add_new_user(new_user_joao)
        self.assertEqual(str(context.exception), "Error while trying to add user: 12345678912 due to missing 'NAME' field.")

    def test_add_new_user_missing_cpf(self):
        user_db = UserDatabase()
        new_user_joao = {"name": "João"}

        with self.assertRaises(ValueError) as context:
            user_db.add_new_user(new_user_joao)
        self.assertEqual(str(context.exception), "Error while trying to add user: João due to missing 'CPF' field.")

    def test_add_new_user_no_user_added(self):
        user_db = UserDatabase()
        new_user_invalid = {"cpf": "12345678912"}

        with self.assertRaises(ValueError):
            user_db.add_new_user(new_user_invalid)
        self.assertIsNone(user_db.get_user("12345678912"))

    def test_get_user(self):
        user_db = UserDatabase()
        new_user_joao = {"name": "João", "cpf": "12345678912"}
        new_user_pedro = {"name": "Pedro", "cpf": "12345678913"}

        user_db.add_new_user(new_user_joao)
        user_joao = user_db.get_user(new_user_joao["cpf"])

        self.assertEqual(user_joao, new_user_joao)
        self.assertIsNone(user_db.get_user(new_user_pedro["cpf"]))
