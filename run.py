#!/usr/bin/env python3
"""
快速啟動腳本
可以直接在專案根目錄運行此腳本
"""

import os
import sys

# 添加 src 目錄到路徑
project_root = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(project_root, 'src')
sys.path.insert(0, src_path)

# 導入並運行主程式
if __name__ == "__main__":
    os.chdir(src_path)
    from main import main
    main()
