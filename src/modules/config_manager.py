"""
配置管理模組
負責讀取和管理配置文件
"""

import json
import os


class ConfigManager:
    """配置管理器類別"""
    
    def __init__(self, config_path=None):
        """
        初始化配置管理器
        
        參數:
            config_path: 配置文件路徑，預設為 config/config.json
        """
        if config_path is None:
            # 獲取專案根目錄
            current_dir = os.path.dirname(os.path.abspath(__file__))
            project_root = os.path.dirname(os.path.dirname(current_dir))
            config_path = os.path.join(project_root, 'config', 'config.json')
        
        self.config_path = config_path
        self.config = self.load_config()
    
    def load_config(self):
        """
        讀取配置文件
        
        返回:
            dict: 配置字典
        """
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"配置文件不存在: {self.config_path}")
            return {}
        except json.JSONDecodeError as e:
            print(f"配置文件格式錯誤: {e}")
            return {}
    
    def save_config(self):
        """
        保存配置到文件
        """
        try:
            with open(self.config_path, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=4, ensure_ascii=False)
            print("配置已保存")
            return True
        except Exception as e:
            print(f"保存配置時發生錯誤: {e}")
            return False
    
    def get(self, key, default=None):
        """
        獲取配置值
        
        參數:
            key: 配置鍵（支援點號分隔的嵌套鍵，例如 'user.name'）
            default: 預設值
        
        返回:
            配置值
        """
        keys = key.split('.')
        value = self.config
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def set(self, key, value):
        """
        設置配置值
        
        參數:
            key: 配置鍵（支援點號分隔的嵌套鍵）
            value: 配置值
        """
        keys = key.split('.')
        config = self.config
        
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        
        config[keys[-1]] = value
    
    def get_user_name(self):
        """獲取用戶名稱"""
        return self.get('user.name', 'Unknown')
    
    def get_user_email(self):
        """獲取用戶郵箱"""
        return self.get('user.email', 'unknown@example.com')
    
    def set_user_info(self, name, email):
        """
        設置用戶信息
        
        參數:
            name: 用戶名稱
            email: 用戶郵箱
        """
        self.set('user.name', name)
        self.set('user.email', email)
    
    def display_config(self):
        """顯示所有配置"""
        print("=" * 50)
        print("當前配置:")
        print("=" * 50)
        print(json.dumps(self.config, indent=2, ensure_ascii=False))
        print("=" * 50)


# 使用範例
if __name__ == "__main__":
    # 創建配置管理器實例
    config_manager = ConfigManager()
    
    # 顯示配置
    config_manager.display_config()
    
    # 獲取用戶信息
    print(f"\n用戶名稱: {config_manager.get_user_name()}")
    print(f"用戶郵箱: {config_manager.get_user_email()}")
    
    # 設置用戶信息
    config_manager.set_user_info("張三", "zhangsan@example.com")
    
    # 保存配置
    config_manager.save_config()
