# SOP：由教學簡報建立教學網頁

適用：高一第二/三學期、七年級、八年級課程網站（與本站同架構）。
搭配 Cowork 技能 `course-web-builder`（安裝後對 Claude 說出下方指令即可）。

## 一、快速指令（複製貼上給 Claude）

> 請用 course-web-builder 技能，依照我上傳的簡報建立「＿＿＿＿（課程名）」教學網站。
> 對象：＿年級；共＿週、每週＿節。課程計畫表也一併上傳，請把各週單元與
> 形成性評量對應到章節，做完先跑驗證再給我。

新增單一章節時：

> 請用 course-web-builder 技能，把這份簡報做成第＿週章節，加入現有網站
> （資料夾：AI數位創作者_flask 同架構），並更新首頁章節卡片。

## 二、Claude 會做的事（你只需確認）
1. 解析簡報 → 提出「週次×小章」大綱給你確認
2. 產生 content/chXX.py（投影片＋隨堂測驗＋分組實作）
3. 更新首頁章節卡片與評量規準頁
4. 跑 `validate_site.py` ＋ 啟動網站逐頁檢查

## 三、你的驗收清單
- [ ] `python validate_site.py .` 顯示「通過 ✅」
- [ ] `python app.py` 後開 http://localhost:5000 逐章點開
- [ ] 抽查 2 章：數字有年份、案例正確、測驗答案與解析無誤
- [ ] 評量規準頁（/rubric）配分與課程計畫一致

## 四、本站架構備忘
```
app.py                 主程式（章節數改 N_CHAPTERS）
content/chXX.py        每週一章：SLIDES / CHAPTERS / QUIZZES
content/enhancements.py 影片與補充內容（依章節/投影片 id 疊加）
templates/home.html    課程首頁（章節卡片）
templates/slides.html  投影片播放器（勿改）
templates/rubric.html  評量規準頁
validate_site.py       結構驗證腳本
```
啟動：`pip install flask` → `python app.py` → 瀏覽器開 http://localhost:5000
發布給學生：`python make_static.py` 產生 docs/ → push 到 GitHub（詳見 README_上架GitHub.md）
（各章舊版獨立資料夾 ch01~ch10/ 與 week10_app.py、content.py 為歷史檔案，可留可刪。）
