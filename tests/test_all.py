"""
測試模組
用於測試專案的各個功能
"""

import unittest
import sys
import os

# 將 src 目錄添加到路徑
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from modules import ConfigManager, validate_email, get_timestamp


class TestConfigManager(unittest.TestCase):
    """測試配置管理器"""
    
    def setUp(self):
        """測試前準備"""
        self.config = ConfigManager()
    
    def test_get_user_name(self):
        """測試獲取用戶名稱"""
        name = self.config.get_user_name()
        self.assertIsNotNone(name)
        self.assertIsInstance(name, str)
    
    def test_get_user_email(self):
        """測試獲取用戶郵箱"""
        email = self.config.get_user_email()
        self.assertIsNotNone(email)
        self.assertIsInstance(email, str)
    
    def test_set_and_get(self):
        """測試設置和獲取配置"""
        self.config.set('test.key', 'test_value')
        value = self.config.get('test.key')
        self.assertEqual(value, 'test_value')


class TestUtils(unittest.TestCase):
    """測試工具函數"""
    
    def test_validate_email_valid(self):
        """測試有效的郵箱"""
        valid_emails = [
            'test@example.com',
            'user.name@domain.co.uk',
            'user+tag@example.com'
        ]
        for email in valid_emails:
            self.assertTrue(validate_email(email), f"{email} 應該是有效的")
    
    def test_validate_email_invalid(self):
        """測試無效的郵箱"""
        invalid_emails = [
            'invalid.email',
            '@example.com',
            'user@',
            'user@domain',
            ''
        ]
        for email in invalid_emails:
            self.assertFalse(validate_email(email), f"{email} 應該是無效的")
    
    def test_get_timestamp(self):
        """測試時間戳生成"""
        timestamp = get_timestamp()
        self.assertIsNotNone(timestamp)
        self.assertIsInstance(timestamp, str)
        self.assertGreater(len(timestamp), 0)


if __name__ == '__main__':
    print("開始運行測試...\n")
    unittest.main(verbosity=2)
