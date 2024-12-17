from dotenv import load_dotenv

import os

class ConfigManager:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigManager, cls).__new__(cls)
            cls._instance._load_env()
        return cls._instance

    def _load_env(self):
        load_dotenv()
        self.twilio_account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        self.twilio_account_token = os.getenv('TWILIO_ACCOUNT_TOKEN')

    def get_twilio_credential(self):
        return {
            'account_sid': self.twilio_account_sid,
            'account_token': self.twilio_account_token
        }
    