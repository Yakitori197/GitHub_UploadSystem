"""
主程式
專案的入口點
"""

import sys
import os

# 將 src 目錄添加到 Python 路徑中
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from modules import ConfigManager, get_timestamp, validate_email, format_output, safe_input


def main():
    """主函數"""
    print("\n" + "=" * 60)
    print("  歡迎使用 GitHub專案上傳系統 ")
    print("=" * 60)
    
    # 初始化配置管理器
    config = ConfigManager()
    
    while True:
        print("\n請選擇功能:")
        print("1. 查看配置")
        print("2. 修改用戶信息")
        print("3. 查看當前時間")
        print("4. 驗證郵箱格式")
        print("0. 退出")
        
        choice = input("\n請輸入選項 (0-4): ").strip()
        
        if choice == '1':
            # 查看配置
            config.display_config()
            
        elif choice == '2':
            # 修改用戶信息
            print("\n--- 修改用戶信息 ---")
            current_name = config.get_user_name()
            current_email = config.get_user_email()
            
            print(f"當前用戶名稱: {current_name}")
            print(f"當前用戶郵箱: {current_email}")
            
            new_name = safe_input("請輸入新的用戶名稱", current_name)
            new_email = safe_input("請輸入新的用戶郵箱", current_email)
            
            # 驗證郵箱
            if not validate_email(new_email):
                print("\n⚠️  警告: 郵箱格式可能不正確")
                confirm = input("是否仍要保存? (y/n): ").strip().lower()
                if confirm != 'y':
                    print("已取消修改")
                    continue
            
            # 更新配置
            config.set_user_info(new_name, new_email)
            
            # 保存配置
            if config.save_config():
                print("✓ 用戶信息已更新")
            
        elif choice == '3':
            # 查看當前時間
            format_output("當前時間", get_timestamp())
            
        elif choice == '4':
            # 驗證郵箱
            email = input("\n請輸入要驗證的郵箱地址: ").strip()
            if validate_email(email):
                print(f"✓ {email} 是有效的郵箱地址")
            else:
                print(f"✗ {email} 不是有效的郵箱地址")
        
        elif choice == '0':
            # 退出
            print("\n感謝使用，再見！")
            break
        
        else:
            print("\n⚠️  無效的選項，請重新輸入")


def show_info():
    """顯示專案信息"""
    config = ConfigManager()
    
    print("\n專案信息:")
    print(f"名稱: {config.get('project.name', 'Unknown')}")
    print(f"版本: {config.get('project.version', 'Unknown')}")
    print(f"描述: {config.get('project.description', 'Unknown')}")
    print(f"\n用戶信息:")
    print(f"名稱: {config.get_user_name()}")
    print(f"郵箱: {config.get_user_email()}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n程式已被用戶中斷")
    except Exception as e:
        print(f"\n發生錯誤: {e}")
        import traceback
        traceback.print_exc()
