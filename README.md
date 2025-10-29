# Python 模組化專案

這是一個適合小白使用GitHub上傳的模組化專案，適合使用 Spyder 6 進行開發。

## 📁 專案結構

```
GitHub_UploadSystem/
├── config/                 # 配置文件目錄
│   └── config.json        # 主配置文件
├── src/                   # 源代碼目錄
│   ├── main.py           # 主程式入口
│   └── modules/          # 功能模組
│       ├── __init__.py
│       ├── config_manager.py  # 配置管理模組
│       └── utils.py      # 工具函數模組
├── tests/                 # 測試目錄
│   └── test_all.py       # 單元測試
├── .gitignore            # Git 忽略文件
├── requirements.txt      # 依賴套件列表
└── README.md            # 專案說明文件
```

## 🚀 快速開始

### 1. 配置環境

本專案使用純 Python 開發，無需 Anaconda，僅需安裝 Python 3.7+。

```bash
# 安裝依賴（目前無外部依賴）
pip install -r requirements.txt
```

### 2. 配置設定

編輯 `config/config.json` 文件，設置你的用戶信息：

```json
{
    "user": {
        "name": "UserName",                    // 你的名字
        "email": "useremail@example.com"         // 你的郵箱
    },
    "project": {
        "name": "專案管理系統",          // 改成你的專案名稱
        "version": "1.0.0",                 // 初版就是 1.0.0
        "description": "管理專案記錄"  // 改成你的專案描述
    }
}
```

### 3. 運行程式

#### 在 Spyder 6 中運行：
1. 打開 Spyder 6
2. 開啟 `src/main.py` 文件
3. 按 F5 或點擊運行按鈕

#### 在命令行中運行：
```bash
cd src
python main.py
```

## 📚 模組說明

### ConfigManager（配置管理器）

負責讀取和管理配置文件。

```python
from modules import ConfigManager

# 創建配置管理器
config = ConfigManager()

# 獲取配置
name = config.get_user_name()
email = config.get_user_email()

# 設置配置
config.set_user_info("新名字", "newemail@example.com")
config.save_config()
```

### Utils（工具模組）

提供常用的工具函數。

```python
from modules import validate_email, get_timestamp, format_output

# 驗證郵箱
is_valid = validate_email("test@example.com")

# 獲取時間戳
timestamp = get_timestamp()

# 格式化輸出
format_output("標題", "內容")
```

## 🧪 測試

運行單元測試：

```bash
cd tests
python test_all.py
```

## 🔧 在 Spyder 6 中使用

### 推薦設置

1. **工作目錄設置**：
   - 在 Spyder 中，將工作目錄設置為 `GitHubUploadSystem/src`
   - 工具 → 偏好設置 → 當前工作目錄

2. **運行配置**：
   - 直接打開 `main.py` 並按 F5 運行
   - 或在 IPython 控制台中導入模組使用

3. **調試**：
   - 使用 Spyder 的調試功能（Ctrl+F5）
   - 設置斷點進行逐行調試

### 使用範例

在 Spyder 的 IPython 控制台中：

```python
# 切換到 src 目錄
cd src

# 導入模組
from modules import ConfigManager

# 使用配置管理器
config = ConfigManager()
config.display_config()
```

## 📤 上傳到 GitHub

### 初始化 Git 倉庫

```bash
# 初始化 Git
cd GitHubUploadSystem
git init

# 添加文件
git add .

# 提交
git commit -m "Initial commit: 建立模組化專案結構"

# 連接到遠端倉庫
git remote add origin https://github.com/你的用戶名/你的專案名稱.git

# 推送到 GitHub
git push -u origin main
```

### 或使用 GitHub Desktop

1. 打開 GitHub Desktop
2. File → Add Local Repository
3. 選擇 `GitHubUploadSystem` 資料夾
4. 填寫提交訊息並 Commit
5. Publish repository

## 📝 功能特點

- ✅ 模組化設計，代碼結構清晰
- ✅ 配置文件外部化，易於管理
- ✅ 完整的錯誤處理機制
- ✅ 包含單元測試
- ✅ 適配 Spyder 6 開發環境
- ✅ 遵循 PEP 8 編碼規範
- ✅ 完整的中文註釋

## 🛠️ 擴展開發

### 添加新模組

1. 在 `src/modules/` 目錄下創建新的 `.py` 文件
2. 在 `src/modules/__init__.py` 中導入新模組
3. 在主程式中使用新模組

### 添加新配置項

在 `config/config.json` 中添加新的配置項，然後使用 `ConfigManager` 讀取。

## 📄 授權

本專案採用 MIT 授權條款。

## 🤝 貢獻

歡迎提交 Issue 和 Pull Request！

## 📧 聯繫方式

如有問題，請通過配置文件中的郵箱聯繫。
