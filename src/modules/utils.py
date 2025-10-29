"""
工具模組
提供常用的工具函數
"""

from datetime import datetime


def get_timestamp():
    """
    獲取當前時間戳
    
    返回:
        str: 格式化的時間字串
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def validate_email(email):
    """
    驗證郵箱格式
    
    參數:
        email: 郵箱地址
    
    返回:
        bool: 是否為有效郵箱
    """
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def format_output(title, content):
    """
    格式化輸出
    
    參數:
        title: 標題
        content: 內容
    """
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)
    print(content)
    print("=" * 60 + "\n")


def safe_input(prompt, default=""):
    """
    安全的輸入函數
    
    參數:
        prompt: 提示訊息
        default: 預設值
    
    返回:
        str: 用戶輸入或預設值
    """
    try:
        user_input = input(f"{prompt} [{default}]: ").strip()
        return user_input if user_input else default
    except KeyboardInterrupt:
        print("\n\n用戶取消輸入")
        return default


# 使用範例
if __name__ == "__main__":
    # 測試時間戳
    print(f"當前時間: {get_timestamp()}")
    
    # 測試郵箱驗證
    test_emails = [
        "test@example.com",
        "invalid.email",
        "user@domain.co.uk"
    ]
    
    for email in test_emails:
        result = "有效" if validate_email(email) else "無效"
        print(f"{email}: {result}")
    
    # 測試格式化輸出
    format_output("測試標題", "這是測試內容")
