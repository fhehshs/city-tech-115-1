# 讓學生看到網站：GitHub Pages 上架步驟

網站已轉成靜態版（`docs/` 資料夾）。只要做一次以下設定，之後更新內容
只需「重跑一個指令 → push」。

## 第一次上架（約 10 分鐘）

1. 到 github.com 登入 → 右上「＋」→ New repository
   - 名稱例如 `city-tech-115-1`，選 **Public**，按 Create
2. 在本機 `115-1` 資料夾開啟終端機（資料夾按右鍵 → 在終端機開啟）：
   ```
   git init
   git add .
   git commit -m "城市科技 115-1 課程網站"
   git branch -M main
   git remote add origin https://github.com/你的帳號/city-tech-115-1.git
   git push -u origin main
   ```
3. GitHub 網頁 → 該 repo → Settings → Pages
   - Source 選 **Deploy from a branch**
   - Branch 選 `main`、資料夾選 **/docs** → Save
4. 等 1-2 分鐘，學生網址就是：
   `https://你的帳號.github.io/city-tech-115-1/`

## 之後更新內容

1. 修改 `content/chXX.py` 等檔案（或請 Claude 修改）
2. 執行 `python make_static.py`（重新產生 docs/）
3. ```
   git add . && git commit -m "更新內容" && git push
   ```
   push 後 1-2 分鐘網站自動更新。

## 注意事項
- 學生只會看到 docs/ 產出的網頁；repo 是 Public，程式碼任何人可見（教材本來就要公開，沒問題）
- 隨堂測驗成績只在學生自己的瀏覽器裡，不會回傳——要收成績請照常用 Google 表單
- 想在課堂用互動版（Flask）也可以：`python app.py` → http://localhost:5000
