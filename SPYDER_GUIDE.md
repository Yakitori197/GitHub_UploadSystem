# Spyder 6 使用指南

## 🎯 在 Spyder 6 中開始使用本專案

### 第一步：開啟專案

1. 啟動 Spyder 6
2. **檔案（File）** → **開啟專案（Open Project）** → 選擇 `my_project` 資料夾
3. 或者直接開啟 `src/main.py` 文件

### 第二步：設定工作目錄

在 Spyder 右上角的工作目錄選擇器中，設定為 `my_project/src`

或在 IPython 控制台中執行：
```python
cd /path/to/my_project/src
```

### 第三步：執行程式

#### 方法 1：直接執行主程式
1. 開啟 `src/main.py`
2. 按 **F5** 或點擊綠色的執行按鈕
3. 在控制台中查看輸出並進行互動

#### 方法 2：在控制台中使用模組
```python
# 匯入模組
from modules import ConfigManager, validate_email, get_timestamp

# 使用配置管理器
config = ConfigManager()
print(config.get_user_name())
print(config.get_user_email())

# 測試工具函數
print(get_timestamp())
print(validate_email("test@example.com"))
```

#### 方法 3：執行測試
1. 開啟 `tests/test_all.py`
2. 按 F5 執行測試

### 第四步：修改配置

1. 在 Spyder 的文件瀏覽器中找到 `config/config.json`
2. 雙擊開啟並編輯
3. 修改 `user.name` 和 `user.email`
4. 儲存文件（Ctrl+S）

### 第五步：調試程式

1. 在想要設置斷點的行號左側點擊，出現紅點
2. 按 **Ctrl+F5** 進入調試模式
3. 使用調試工具列：
   - 繼續（Continue）：F5
   - 下一步（Step）：F10
   - 進入函數（Step Into）：F11
   - 跳出函數（Step Out）：Shift+F11

## 📝 常用操作

### 查看變數
在調試時，右側的「變數瀏覽器」會顯示所有變數的值

### 查看幫助
在控制台中輸入：
```python
help(ConfigManager)
help(validate_email)
```

### 重新載入模組
如果修改了模組代碼，需要重新載入：
```python
import importlib
import modules
importlib.reload(modules)
```

或者重啟內核（Ctrl+.）

## 🔧 Spyder 快捷鍵

- **F5**：執行文件
- **Ctrl+F5**：調試文件
- **F9**：執行選中的代碼
- **Ctrl+1**：註解/取消註解
- **Ctrl+Space**：自動補全
- **Ctrl+I**：檢查對象
- **Ctrl+Shift+F**：格式化代碼

## 💡 提示

1. **自動補全**：輸入 `config.` 後按 Tab 鍵，會顯示所有可用的方法
2. **即時幫助**：在編輯器中選中函數名，右側的幫助面板會顯示文檔
3. **代碼分析**：Spyder 會即時顯示語法錯誤和警告
4. **多文件編輯**：可以同時開啟多個文件進行編輯

## 🐛 常見問題

### 問題：找不到模組
**解決**：確認工作目錄設定正確，應該是 `my_project/src`

### 問題：配置文件讀取失敗
**解決**：檢查 `config/config.json` 是否存在且格式正確

### 問題：修改代碼後沒有生效
**解決**：重新執行程式（F5）或重啟內核（Ctrl+.）

## 📚 進階使用

### 整合 Git
1. 在 Spyder 中：**檢視（View）** → **Panes** → **Git**
2. 或在終端機中使用 Git 命令

### 使用虛擬環境
```bash
# 創建虛擬環境
python -m venv venv

# 啟動虛擬環境
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 在 Spyder 中使用虛擬環境
# 工具 → 偏好設置 → Python 解釋器 → 使用自定義 Python 解釋器
```

## 🎓 學習資源

- [Spyder 官方文檔](https://docs.spyder-ide.org/)
- [Python 官方教程](https://docs.python.org/zh-tw/3/tutorial/)
- 本專案的 README.md

---

祝你使用愉快！如有問題歡迎查看專案的 README.md 或提交 Issue。
