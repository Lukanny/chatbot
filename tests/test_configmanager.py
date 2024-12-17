from ConfigManager import ConfigManager
from unittest.mock import patch

import unittest


class TestConfigManager(unittest.TestCase):

    @patch.dict('os.environ', {
        'TWILIO_ACCOUNT_SID': 'test_sid',
        'TWILIO_ACCOUNT_TOKEN': 'test_token'
    })
    def test_get_twilio_credentials(self):
        config_manager = ConfigManager()
        
        credentials = config_manager.get_twilio_credential()
        
        self.assertEqual(credentials['account_id'], 'test_sid')
        self.assertEqual(credentials['account_token'], 'test_token')
        