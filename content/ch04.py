# -*- coding: utf-8 -*-
# Ch.4: Google Workspace 文書應用

CHAPTERS = [
    {'name': '封面', 'start': 1},
    {'name': '第一章：Google Workspace 概覽', 'start': 2},
    {'name': '第二章：Google 文件進階排版', 'start': 8},
    {'name': '第三章：共同編輯與版本控制', 'start': 14},
    {'name': '第四章：雲端辦公應用', 'start': 19},
    {'name': '分組實作', 'start': 23},
]

QUIZZES = {
    'q1': {
        'title': '第一章 隨堂測驗',
        'questions': [
            {
                'q': 'Google Workspace 的最大優勢是什麼？',
                'options': ['比 Microsoft Office 功能更強大', '多人可同時在同一份文件上即時協作', '完全免費，沒有任何限制', '只能在 Chrome 瀏覽器使用'],
                'answer': 1,
                'explain': 'Google Workspace 最核心的優勢是「即時多人協作」：多位使用者可以同時編輯同一份文件，看到彼此的游標和修改，不需要來回傳送檔案。這改變了團隊合作的方式。'
            },
            {
                'q': 'Google 雲端硬碟的免費儲存空間是多少？',
                'options': ['100 GB', '無限制', '5 GB', '15 GB（共享 Gmail、雲端硬碟、相片）'],
                'answer': 3,
                'explain': 'Google 帳號免費提供 15 GB 儲存空間，由 Gmail、Google 雲端硬碟和 Google 相片共用。需要更多空間可購買 Google One 方案（100GB 約 NT$65/月）。'
            },
        ]
    },
    'q2': {
        'title': '第二章 隨堂測驗',
        'questions': [
            {
                'q': 'Google 文件中，「段落樣式」最主要的用途是什麼？',
                'options': ['改變字體顏色', '插入圖片', '快速套用一致的格式，並自動產生目錄', '加入頁碼'],
                'answer': 2,
                'explain': '段落樣式（標題1、標題2、內文等）有兩個主要功能：(1) 讓全文格式一致，改一個樣式全文同步更新；(2) 自動產生目錄功能會掃描這些標題樣式。這是專業文件排版的核心技巧。'
            },
            {
                'q': '在 Google 文件插入目錄，以下敘述何者正確？',
                'options': ['插入目錄後，若文章標題有修改，需手動更新目錄', '目錄插入後永遠不需要更新', '目錄只能放在文件開頭', '手動輸入的段落也會自動出現在目錄'],
                'answer': 0,
                'explain': '插入目錄後，如果你修改了標題文字或新增段落，目錄不會即時自動更新。需要點擊目錄旁的「更新」按鈕或從選單更新。只有套用了「標題」樣式的段落才會出現在目錄中。'
            },
        ]
    },
    'q3': {
        'title': '第三章 隨堂測驗',
        'questions': [
            {
                'q': 'Google 文件的「建議模式」功能主要用於？',
                'options': ['讓修改以追蹤方式顯示，方便審閱者接受或拒絕', '自動糾正文法錯誤', '提供 AI 撰寫建議', '自動備份文件到雲端'],
                'answer': 0,
                'explain': '建議模式（Suggestion mode）類似 Word 的「追蹤修訂」：你的每個修改都以彩色標示，原作者可以選擇「接受」或「拒絕」各項建議。適合多人審閱文件時使用。'
            },
            {
                'q': '共用 Google 文件時，設定為「可以檢視」的使用者能做什麼？',
                'options': ['可以留言但不能直接編輯', '只能閱讀，無法修改或留言', '可以完整編輯', '可以刪除他人的修改'],
                'answer': 1,
                'explain': 'Google 文件有三種共用權限：「可以檢視」（只能讀）、「可以留言」（可加留言但不能直接修改文字）、「可以編輯」（完整編輯權限）。選擇正確的權限對文件安全很重要。'
            },
        ]
    },
    'q4': {
        'title': '第四章 隨堂測驗',
        'questions': [
            {
                'q': 'Google 試算表中，VLOOKUP 函數的功能是什麼？',
                'options': ['計算一組數字的平均值', '統計儲存格中的數字個數', '將文字轉換為大寫', '在指定範圍中搜尋特定值，並回傳同一列中對應欄的資料'],
                'answer': 3,
                'explain': 'VLOOKUP（垂直查找）是試算表最重要的函數之一：在第一欄搜尋你指定的值，找到後回傳同一列中你想要的欄位資料。例如輸入學號，自動找到對應的學生姓名。語法：=VLOOKUP(搜尋值, 範圍, 欄數, 0)'
            },
            {
                'q': 'Google 簡報中，「主題」（Theme）的作用是什麼？',
                'options': ['限制簡報只能使用特定的版面配置', '自動播放簡報', '套用統一的配色、字體和背景設計，讓整份簡報風格一致', '加入動畫效果'],
                'answer': 2,
                'explain': '主題（Theme）讓你一鍵套用設計師預設的配色、字體和背景，確保整份簡報視覺一致。改主題後，所有投影片都會同步更新。這比逐張修改格式節省大量時間。'
            },
        ]
    },
}

SLIDES = [
    {
        'id': 1, 'chapter': '封面', 'title': 'Google Workspace 文書應用',
        'bg': 'navy', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<div style='text-align:center;padding:30px 20px;'>
  <div style='font-size:72px;margin-bottom:20px;'>📝</div>
  <h1 style='font-size:2.8rem;font-weight:900;color:#fff;margin-bottom:12px;'>Google Workspace<br>文書應用</h1>
  <h2 style='font-size:1.5rem;font-weight:400;color:#93c5fd;margin-bottom:30px;'>Productivity &amp; Collaboration Tools</h2>
  <div style='display:flex;justify-content:center;gap:20px;flex-wrap:wrap;margin-bottom:30px;'>
    <span style='background:rgba(255,255,255,0.15);color:#e0f2fe;padding:8px 20px;border-radius:20px;font-size:1rem;'>📄 文件排版</span>
    <span style='background:rgba(255,255,255,0.15);color:#e0f2fe;padding:8px 20px;border-radius:20px;font-size:1rem;'>🤝 共同協作</span>
    <span style='background:rgba(255,255,255,0.15);color:#e0f2fe;padding:8px 20px;border-radius:20px;font-size:1rem;'>☁️ 雲端辦公</span>
  </div>
  <p style='color:#bfdbfe;font-size:1.1rem;'>城市科技 — 第四章</p>
</div>"""
    },
    {
        'id': 2, 'chapter': '第一章：Google Workspace 概覽', 'title': 'Google Workspace 是什麼？',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>Google Workspace：雲端辦公室</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>🌐 核心應用</h3>
      <div style='display:grid;grid-template-columns:1fr 1fr;gap:8px;'>
        <div style='background:#fff;padding:10px;border-radius:8px;text-align:center;'>
          <div style='font-size:1.8rem;'>📄</div>
          <p style='color:#374151;font-size:.8rem;margin-top:4px;font-weight:600;'>Google 文件</p>
          <p style='color:#6b7280;font-size:.7rem;'>文字處理</p>
        </div>
        <div style='background:#fff;padding:10px;border-radius:8px;text-align:center;'>
          <div style='font-size:1.8rem;'>📊</div>
          <p style='color:#374151;font-size:.8rem;margin-top:4px;font-weight:600;'>Google 試算表</p>
          <p style='color:#6b7280;font-size:.7rem;'>資料分析</p>
        </div>
        <div style='background:#fff;padding:10px;border-radius:8px;text-align:center;'>
          <div style='font-size:1.8rem;'>📑</div>
          <p style='color:#374151;font-size:.8rem;margin-top:4px;font-weight:600;'>Google 簡報</p>
          <p style='color:#6b7280;font-size:.7rem;'>投影片製作</p>
        </div>
        <div style='background:#fff;padding:10px;border-radius:8px;text-align:center;'>
          <div style='font-size:1.8rem;'>📝</div>
          <p style='color:#374151;font-size:.8rem;margin-top:4px;font-weight:600;'>Google 表單</p>
          <p style='color:#6b7280;font-size:.7rem;'>問卷調查</p>
        </div>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:10px;'>✨ 最大優勢</h3>
      <div style='display:flex;flex-direction:column;gap:8px;font-size:.85rem;'>
        <div style='background:#dcfce7;padding:8px;border-radius:6px;color:#15803d;'>🤝 多人即時協作，看見彼此游標</div>
        <div style='background:#dcfce7;padding:8px;border-radius:6px;color:#15803d;'>☁️ 雲端儲存，任何裝置開啟</div>
        <div style='background:#dcfce7;padding:8px;border-radius:6px;color:#15803d;'>🔄 自動儲存，不怕當機遺失</div>
        <div style='background:#dcfce7;padding:8px;border-radius:6px;color:#15803d;'>📋 版本歷史，可還原任何時間點</div>
        <div style='background:#dcfce7;padding:8px;border-radius:6px;color:#15803d;'>🆓 免費使用（15GB 儲存空間）</div>
      </div>
    </div>
  </div>
</div>"""
    },
    {
        'id': 3, 'chapter': '第一章：Google Workspace 概覽', 'title': 'Google vs Microsoft Office',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>Google Workspace vs Microsoft 365</h2>
<div style='overflow-x:auto;'>
  <table style='width:100%;border-collapse:collapse;font-size:.85rem;'>
    <thead>
      <tr style='background:#1e293b;color:#fff;'>
        <th style='padding:10px;text-align:left;'>比較項目</th>
        <th style='padding:10px;text-align:center;'>📝 Google Workspace</th>
        <th style='padding:10px;text-align:center;'>💙 Microsoft 365</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style='padding:9px;color:#374151;font-weight:600;'>費用</td>
        <td style='padding:9px;text-align:center;color:#15803d;font-weight:700;'>個人免費（15GB）</td>
        <td style='padding:9px;text-align:center;color:#374151;'>個人版 約 NT$219/月</td>
      </tr>
      <tr style='background:#f8fafc;'>
        <td style='padding:9px;color:#374151;font-weight:600;'>協作功能</td>
        <td style='padding:9px;text-align:center;color:#15803d;font-weight:700;'>即時多人協作 ⭐⭐⭐⭐⭐</td>
        <td style='padding:9px;text-align:center;color:#374151;'>需 SharePoint ⭐⭐⭐</td>
      </tr>
      <tr>
        <td style='padding:9px;color:#374151;font-weight:600;'>離線使用</td>
        <td style='padding:9px;text-align:center;color:#374151;'>需設定</td>
        <td style='padding:9px;text-align:center;color:#15803d;font-weight:700;'>原生支援 ✅</td>
      </tr>
      <tr style='background:#f8fafc;'>
        <td style='padding:9px;color:#374151;font-weight:600;'>功能完整度</td>
        <td style='padding:9px;text-align:center;color:#374151;'>基礎~中階</td>
        <td style='padding:9px;text-align:center;color:#15803d;font-weight:700;'>功能最完整 ✅</td>
      </tr>
      <tr>
        <td style='padding:9px;color:#374151;font-weight:600;'>學校/企業採用</td>
        <td style='padding:9px;text-align:center;color:#374151;'>教育界廣泛使用</td>
        <td style='padding:9px;text-align:center;color:#374151;'>企業主流</td>
      </tr>
    </tbody>
  </table>
</div>
<div style='background:#fef9c3;padding:10px;border-radius:8px;margin-top:10px;'>
  <p style='color:#854d0e;font-size:.85rem;margin:0;'>💡 <strong>建議</strong>：學校作業用 Google Workspace（協作方便），職場文件用 Microsoft 365（功能最完整）。兩種都要會！</p>
</div>"""
    },
    {
        'id': 4, 'chapter': '第一章：Google Workspace 概覽', 'title': 'Google 雲端硬碟',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>Google 雲端硬碟：整理你的數位空間</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>📁 有效率的整理方式</h3>
      <div style='background:#f8fafc;padding:12px;border-radius:8px;font-family:monospace;font-size:.8rem;color:#374151;'>
        <p style='margin:0;'>📁 我的雲端硬碟</p>
        <p style='margin:0;padding-left:16px;'>📁 學校作業</p>
        <p style='margin:0;padding-left:32px;'>📁 一年級</p>
        <p style='margin:0;padding-left:48px;'>📄 城市科技期末報告</p>
        <p style='margin:0;padding-left:48px;'>📊 資料分析作業</p>
        <p style='margin:0;padding-left:32px;'>📁 二年級</p>
        <p style='margin:0;padding-left:16px;'>📁 課外活動</p>
        <p style='margin:0;padding-left:32px;'>📸 社團照片</p>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:10px;'>⚡ 常用技巧</h3>
      <div style='display:flex;flex-direction:column;gap:6px;font-size:.83rem;'>
        <div style='background:#dcfce7;padding:7px;border-radius:6px;color:#374151;'><strong style='color:#15803d;'>搜尋功能</strong>：支援 OCR，可搜尋圖片和 PDF 中的文字</div>
        <div style='background:#dcfce7;padding:7px;border-radius:6px;color:#374151;'><strong style='color:#15803d;'>分享連結</strong>：設定「任何人都可以檢視」快速分享</div>
        <div style='background:#dcfce7;padding:7px;border-radius:6px;color:#374151;'><strong style='color:#15803d;'>加星號</strong>：重要文件加星號方便快速找到</div>
        <div style='background:#dcfce7;padding:7px;border-radius:6px;color:#374151;'><strong style='color:#15803d;'>右鍵轉換</strong>：上傳 Word 檔後右鍵可轉為 Google 文件</div>
        <div style='background:#dcfce7;padding:7px;border-radius:6px;color:#374151;'><strong style='color:#15803d;'>鍵盤快捷鍵</strong>：N 新建資料夾、/ 搜尋</div>
      </div>
    </div>
  </div>
</div>"""
    },
    {
        'id': 5, 'chapter': '第一章：Google Workspace 概覽', 'title': 'Google 帳號安全設定',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>Google 帳號安全管理</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#fef2f2;padding:15px;border-radius:10px;border:1px solid #fecaca;margin-bottom:12px;'>
      <h3 style='color:#dc2626;font-size:1rem;margin-bottom:10px;'>⚠️ 常見安全威脅</h3>
      <ul style='color:#374151;font-size:.85rem;padding-left:16px;'>
        <li>帳號被盜後，雲端硬碟資料也被存取</li>
        <li>在他人電腦登入後忘記登出</li>
        <li>在公用電腦儲存密碼</li>
        <li>被釣魚網站騙走帳密</li>
      </ul>
    </div>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:10px;'>🛡️ 安全強化步驟</h3>
      <div style='display:flex;flex-direction:column;gap:6px;font-size:.83rem;'>
        <div style='background:#dcfce7;padding:7px;border-radius:6px;color:#374151;'>① 前往 myaccount.google.com 進行安全檢查</div>
        <div style='background:#dcfce7;padding:7px;border-radius:6px;color:#374151;'>② 啟用兩步驟驗證（2FA）</div>
        <div style='background:#dcfce7;padding:7px;border-radius:6px;color:#374151;'>③ 查看「帳號活動」確認有無異常登入</div>
        <div style='background:#dcfce7;padding:7px;border-radius:6px;color:#374151;'>④ 定期清除已授權的第三方應用程式</div>
        <div style='background:#dcfce7;padding:7px;border-radius:6px;color:#374151;'>⑤ 使用 Gmail 的「機密模式」傳送敏感郵件</div>
      </div>
    </div>
  </div>
</div>"""
    },
    {
        'id': 6, 'chapter': '第一章：Google Workspace 概覽', 'title': 'Gmail 進階使用',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>Gmail 進階使用技巧</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>🔍 Gmail 搜尋語法</h3>
      <div style='display:flex;flex-direction:column;gap:5px;font-size:.82rem;'>
        <div style='background:#fff;padding:7px;border-radius:5px;border-left:3px solid #2563eb;'><code style='color:#1e40af;'>from:teacher@school.edu</code><span style='color:#6b7280;'> — 來自特定寄件人</span></div>
        <div style='background:#fff;padding:7px;border-radius:5px;border-left:3px solid #2563eb;'><code style='color:#1e40af;'>has:attachment</code><span style='color:#6b7280;'> — 含附件</span></div>
        <div style='background:#fff;padding:7px;border-radius:5px;border-left:3px solid #2563eb;'><code style='color:#1e40af;'>is:unread</code><span style='color:#6b7280;'> — 未讀郵件</span></div>
        <div style='background:#fff;padding:7px;border-radius:5px;border-left:3px solid #2563eb;'><code style='color:#1e40af;'>after:2024/1/1</code><span style='color:#6b7280;'> — 特定日期後</span></div>
        <div style='background:#fff;padding:7px;border-radius:5px;border-left:3px solid #2563eb;'><code style='color:#1e40af;'>larger:5m</code><span style='color:#6b7280;'> — 大於5MB</span></div>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:10px;'>⚡ Gmail 快捷鍵</h3>
      <div style='display:flex;flex-direction:column;gap:5px;font-size:.82rem;'>
        <div style='display:flex;justify-content:space-between;background:#fff;padding:7px;border-radius:5px;'><code style='color:#15803d;'>C</code><span style='color:#374151;'>撰寫新郵件</span></div>
        <div style='display:flex;justify-content:space-between;background:#f0fdf4;padding:7px;border-radius:5px;'><code style='color:#15803d;'>R</code><span style='color:#374151;'>回覆</span></div>
        <div style='display:flex;justify-content:space-between;background:#fff;padding:7px;border-radius:5px;'><code style='color:#15803d;'>A</code><span style='color:#374151;'>全部回覆</span></div>
        <div style='display:flex;justify-content:space-between;background:#f0fdf4;padding:7px;border-radius:5px;'><code style='color:#15803d;'>E</code><span style='color:#374151;'>封存</span></div>
        <div style='display:flex;justify-content:space-between;background:#fff;padding:7px;border-radius:5px;'><code style='color:#15803d;'>/ </code><span style='color:#374151;'>搜尋</span></div>
      </div>
      <p style='color:#6b7280;font-size:.75rem;margin-top:8px;'>需先在設定中啟用鍵盤快捷鍵</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 7, 'chapter': '第一章：Google Workspace 概覽', 'title': '🎯 第一章 隨堂測驗',
        'bg': 'purple', 'quiz': 'q1', 'chart': None, 'video': None,
        'html': """
<div style='text-align:center;padding:20px;'>
  <div style='font-size:56px;margin-bottom:15px;'>🎯</div>
  <h2 style='color:#fff;font-size:2rem;font-weight:800;margin-bottom:10px;'>第一章 隨堂測驗</h2>
  <p style='color:#e9d5ff;font-size:1.1rem;'>Google Workspace 概覽 ── 2 道題目，點擊作答！</p>
</div>"""
    },
    {
        'id': 8, 'chapter': '第二章：Google 文件進階排版', 'title': '段落樣式',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>段落樣式：專業排版的關鍵</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>📐 樣式層次</h3>
      <div style='display:flex;flex-direction:column;gap:5px;'>
        <div style='background:#1e3a5f;color:#fff;padding:10px;border-radius:6px;font-size:1.1rem;font-weight:900;'>標題（文件名稱）</div>
        <div style='background:#2563eb;color:#fff;padding:8px;border-radius:6px;font-size:.95rem;font-weight:700;padding-left:20px;'>標題 1（大章節）</div>
        <div style='background:#3b82f6;color:#fff;padding:7px;border-radius:6px;font-size:.85rem;font-weight:600;padding-left:32px;'>標題 2（小節）</div>
        <div style='background:#93c5fd;color:#1e3a5f;padding:6px;border-radius:6px;font-size:.8rem;padding-left:44px;'>標題 3（子節）</div>
        <div style='background:#f1f5f9;color:#374151;padding:6px;border-radius:6px;font-size:.78rem;padding-left:44px;border:1px solid #e2e8f0;'>內文（正文）</div>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:10px;'>✨ 使用樣式的好處</h3>
      <ul style='color:#374151;font-size:.85rem;padding-left:16px;'>
        <li>一鍵套用，格式全文一致</li>
        <li>修改樣式後全文同步更新</li>
        <li>自動產生目錄</li>
        <li>文件導覽窗格可快速跳頁</li>
        <li>方便閱讀，結構清晰</li>
      </ul>
    </div>
    <div style='background:#fef9c3;padding:10px;border-radius:8px;'>
      <p style='color:#854d0e;font-size:.85rem;margin:0;'>💡 使用方式：格式 → 段落樣式，或用工具列左側下拉選單</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 9, 'chapter': '第二章：Google 文件進階排版', 'title': '自動目錄',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>自動目錄：讓文件更專業</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>📋 插入目錄步驟</h3>
      <div style='display:flex;flex-direction:column;gap:6px;font-size:.83rem;'>
        <div style='background:#dbeafe;padding:7px;border-radius:5px;display:flex;gap:8px;align-items:center;'><span style='background:#2563eb;color:#fff;width:20px;height:20px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:.7rem;font-weight:700;flex-shrink:0;'>1</span><span style='color:#374151;'>先用「段落樣式」套用標題</span></div>
        <div style='background:#dbeafe;padding:7px;border-radius:5px;display:flex;gap:8px;align-items:center;'><span style='background:#2563eb;color:#fff;width:20px;height:20px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:.7rem;font-weight:700;flex-shrink:0;'>2</span><span style='color:#374151;'>將游標放到要插入目錄的位置</span></div>
        <div style='background:#dbeafe;padding:7px;border-radius:5px;display:flex;gap:8px;align-items:center;'><span style='background:#2563eb;color:#fff;width:20px;height:20px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:.7rem;font-weight:700;flex-shrink:0;'>3</span><span style='color:#374151;'>插入 → 目錄，選擇帶頁碼或帶連結</span></div>
        <div style='background:#dbeafe;padding:7px;border-radius:5px;display:flex;gap:8px;align-items:center;'><span style='background:#2563eb;color:#fff;width:20px;height:20px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:.7rem;font-weight:700;flex-shrink:0;'>4</span><span style='color:#374151;'>標題修改後，按目錄上的「更新」按鈕</span></div>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#f8fafc;border:2px solid #e2e8f0;padding:15px;border-radius:10px;'>
      <h3 style='color:#374151;font-size:.9rem;margin-bottom:10px;'>📖 目錄範例預覽</h3>
      <div style='font-size:.82rem;color:#374151;'>
        <div style='display:flex;justify-content:space-between;border-bottom:1px dotted #e2e8f0;padding:4px 0;font-weight:700;color:#1e40af;'>第一章　城市科技概覽<span>1</span></div>
        <div style='display:flex;justify-content:space-between;border-bottom:1px dotted #e2e8f0;padding:4px 0;padding-left:12px;'>1.1 什麼是城市科技<span>2</span></div>
        <div style='display:flex;justify-content:space-between;border-bottom:1px dotted #e2e8f0;padding:4px 0;padding-left:12px;'>1.2 台灣科技產業現況<span>5</span></div>
        <div style='display:flex;justify-content:space-between;border-bottom:1px dotted #e2e8f0;padding:4px 0;font-weight:700;color:#1e40af;'>第二章　數位工具應用<span>8</span></div>
        <div style='display:flex;justify-content:space-between;padding:4px 0;padding-left:12px;'>2.1 Google Workspace<span>9</span></div>
      </div>
    </div>
  </div>
</div>"""
    },
    {
        'id': 10, 'chapter': '第二章：Google 文件進階排版', 'title': '頁首頁尾與頁碼',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>頁首、頁尾與頁碼</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>📃 頁首頁尾設定</h3>
      <p style='color:#374151;font-size:.88rem;margin-bottom:8px;'>插入 → 頁首與頁尾</p>
      <ul style='color:#374151;font-size:.83rem;padding-left:16px;'>
        <li>頁首：通常放文件標題或學校名稱</li>
        <li>頁尾：通常放頁碼</li>
        <li>可設定第一頁不同（封面不顯示頁碼）</li>
        <li>奇偶頁可設定不同頁首頁尾</li>
      </ul>
    </div>
    <div style='background:#f0fdf4;padding:10px;border-radius:8px;'>
      <h3 style='color:#15803d;font-size:.9rem;margin-bottom:6px;'>🔢 插入頁碼</h3>
      <p style='color:#374151;font-size:.83rem;margin:0;'>插入 → 頁碼，可選擇位置（左/中/右）和格式（阿拉伯數字/羅馬數字）</p>
    </div>
  </div>
  <div>
    <div style='background:#f8fafc;border:2px solid #e2e8f0;padding:0;border-radius:10px;overflow:hidden;'>
      <div style='background:#dbeafe;padding:8px 12px;border-bottom:1px solid #e2e8f0;text-align:center;font-size:.78rem;color:#1e40af;font-weight:600;'>頁首示範</div>
      <div style='padding:15px;'>
        <div style='display:flex;justify-content:space-between;font-size:.78rem;color:#94a3b8;border-bottom:1px solid #e2e8f0;padding-bottom:6px;margin-bottom:10px;'>
          <span>芳和實驗中學</span>
          <span>城市科技期末報告</span>
        </div>
        <p style='color:#374151;font-size:.83rem;line-height:1.6;'>在數位時代，科技改變了我們生活的每個層面。從早晨起床查看手機通知，到晚上使用串流服務觀看影片...</p>
        <div style='display:flex;justify-content:center;font-size:.78rem;color:#94a3b8;border-top:1px solid #e2e8f0;padding-top:6px;margin-top:10px;'>第 1 頁</div>
      </div>
      <div style='background:#dcfce7;padding:6px 12px;border-top:1px solid #e2e8f0;text-align:center;font-size:.78rem;color:#15803d;font-weight:600;'>頁尾示範</div>
    </div>
  </div>
</div>"""
    },
    {
        'id': 11, 'chapter': '第二章：Google 文件進階排版', 'title': '表格與圖片排版',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>表格與圖片的專業排版</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>📊 表格使用技巧</h3>
      <ul style='color:#374151;font-size:.85rem;padding-left:16px;'>
        <li>插入 → 表格，選擇欄/列數</li>
        <li>可合併儲存格（選取後右鍵）</li>
        <li>表格樣式：格式 → 段落樣式</li>
        <li>表格寬度：拖曳邊框調整</li>
        <li>固定欄寬：右鍵 → 表格屬性</li>
      </ul>
    </div>
    <div style='background:#f0fdf4;padding:10px;border-radius:8px;'>
      <h3 style='color:#15803d;font-size:.9rem;margin-bottom:6px;'>🖼️ 圖片排版選項</h3>
      <ul style='color:#374151;font-size:.82rem;padding-left:14px;'>
        <li>與文字一起：圖片在文字行內</li>
        <li>文繞圖：文字環繞圖片四周</li>
        <li>突破文字：圖片蓋在文字上</li>
      </ul>
    </div>
  </div>
  <div>
    <div style='background:#fef9c3;padding:15px;border-radius:10px;'>
      <h3 style='color:#854d0e;font-size:1rem;margin-bottom:10px;'>💡 常用快捷鍵</h3>
      <div style='display:flex;flex-direction:column;gap:5px;font-size:.82rem;'>
        <div style='display:flex;justify-content:space-between;background:#fff;padding:7px;border-radius:5px;'><code style='color:#854d0e;'>Ctrl+B</code><span style='color:#374151;'>粗體</span></div>
        <div style='display:flex;justify-content:space-between;background:#fef9c3;padding:7px;border-radius:5px;'><code style='color:#854d0e;'>Ctrl+I</code><span style='color:#374151;'>斜體</span></div>
        <div style='display:flex;justify-content:space-between;background:#fff;padding:7px;border-radius:5px;'><code style='color:#854d0e;'>Ctrl+U</code><span style='color:#374151;'>底線</span></div>
        <div style='display:flex;justify-content:space-between;background:#fef9c3;padding:7px;border-radius:5px;'><code style='color:#854d0e;'>Ctrl+Z</code><span style='color:#374151;'>復原</span></div>
        <div style='display:flex;justify-content:space-between;background:#fff;padding:7px;border-radius:5px;'><code style='color:#854d0e;'>Ctrl+Shift+C</code><span style='color:#374151;'>複製格式</span></div>
        <div style='display:flex;justify-content:space-between;background:#fef9c3;padding:7px;border-radius:5px;'><code style='color:#854d0e;'>Ctrl+Shift+V</code><span style='color:#374151;'>貼上格式</span></div>
      </div>
    </div>
  </div>
</div>"""
    },
    {
        'id': 12, 'chapter': '第二章：Google 文件進階排版', 'title': '🎯 第二章 隨堂測驗',
        'bg': 'purple', 'quiz': 'q2', 'chart': None, 'video': None,
        'html': """
<div style='text-align:center;padding:20px;'>
  <div style='font-size:56px;margin-bottom:15px;'>🎯</div>
  <h2 style='color:#fff;font-size:2rem;font-weight:800;margin-bottom:10px;'>第二章 隨堂測驗</h2>
  <p style='color:#e9d5ff;font-size:1.1rem;'>Google 文件排版 ── 2 道題目，點擊作答！</p>
</div>"""
    },
    {
        'id': 13, 'chapter': '第三章：共同編輯與版本控制', 'title': '即時協作',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>即時協作：一起工作的革命</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>🔄 傳統 vs 雲端協作</h3>
      <div style='display:flex;flex-direction:column;gap:8px;font-size:.83rem;'>
        <div style='background:#fef2f2;padding:10px;border-radius:8px;border-left:3px solid #dc2626;'>
          <p style='color:#dc2626;font-weight:700;margin:0 0 3px;'>❌ 傳統方式</p>
          <p style='color:#374151;margin:0;'>A 存檔 → 傳給 B → B 修改 → 傳回 A → A 修改……版本混亂，哪個是最新版？</p>
        </div>
        <div style='background:#f0fdf4;padding:10px;border-radius:8px;border-left:3px solid #16a34a;'>
          <p style='color:#15803d;font-weight:700;margin:0 0 3px;'>✅ Google 文件</p>
          <p style='color:#374151;margin:0;'>所有人同時在同一份文件上編輯，看到彼此游標，永遠只有一個版本。</p>
        </div>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:10px;'>💬 協作功能</h3>
      <div style='display:flex;flex-direction:column;gap:6px;font-size:.83rem;'>
        <div style='background:#dcfce7;padding:7px;border-radius:6px;color:#374151;'><strong style='color:#15803d;'>留言（Comment）</strong>：選取文字 → 右鍵 → 加入留言</div>
        <div style='background:#dcfce7;padding:7px;border-radius:6px;color:#374151;'><strong style='color:#15803d;'>建議（Suggesting）</strong>：工具列切換編輯模式</div>
        <div style='background:#dcfce7;padding:7px;border-radius:6px;color:#374151;'><strong style='color:#15803d;'>@提及</strong>：留言中 @同學名字，他會收到通知</div>
        <div style='background:#dcfce7;padding:7px;border-radius:6px;color:#374151;'><strong style='color:#15803d;'>即時聊天</strong>：右上角聊天圖示，不需切換 LINE</div>
      </div>
    </div>
  </div>
</div>"""
    },
    {
        'id': 14, 'chapter': '第三章：共同編輯與版本控制', 'title': '版本歷史',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>版本歷史：時光機功能</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>⏰ 版本歷史功能</h3>
      <p style='color:#374151;font-size:.88rem;margin-bottom:8px;'>Google 文件會自動儲存每次修改的快照，你可以：</p>
      <ul style='color:#374151;font-size:.83rem;padding-left:16px;'>
        <li>查看任何時間點的文件狀態</li>
        <li>還原到過去某個版本</li>
        <li>查看是誰做了哪些修改（不同顏色標示）</li>
        <li>為重要版本命名（如「定稿版」）</li>
      </ul>
      <div style='background:#dbeafe;padding:8px;border-radius:6px;margin-top:8px;'>
        <p style='color:#1e40af;font-size:.8rem;margin:0;'>操作：檔案 → 版本歷史 → 查看版本歷史</p>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:10px;'>🛡️ 共用權限設定</h3>
      <div style='display:flex;flex-direction:column;gap:6px;font-size:.83rem;'>
        <div style='background:#dcfce7;padding:8px;border-radius:6px;'>
          <p style='color:#15803d;font-weight:700;margin:0 0 2px;'>擁有者</p>
          <p style='color:#374151;margin:0;'>完整控制，可以刪除文件、轉移擁有權</p>
        </div>
        <div style='background:#dcfce7;padding:8px;border-radius:6px;'>
          <p style='color:#15803d;font-weight:700;margin:0 0 2px;'>編輯者</p>
          <p style='color:#374151;margin:0;'>可以修改文件，也可以邀請他人</p>
        </div>
        <div style='background:#dcfce7;padding:8px;border-radius:6px;'>
          <p style='color:#15803d;font-weight:700;margin:0 0 2px;'>加入留言</p>
          <p style='color:#374151;margin:0;'>可以留言但不能直接修改文字</p>
        </div>
        <div style='background:#dcfce7;padding:8px;border-radius:6px;'>
          <p style='color:#15803d;font-weight:700;margin:0 0 2px;'>檢視者</p>
          <p style='color:#374151;margin:0;'>只能閱讀，無法任何修改</p>
        </div>
      </div>
    </div>
  </div>
</div>"""
    },
    {
        'id': 15, 'chapter': '第三章：共同編輯與版本控制', 'title': '建議模式',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>建議模式：讓修改更透明</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>✏️ 三種編輯模式</h3>
      <div style='display:flex;flex-direction:column;gap:6px;font-size:.83rem;'>
        <div style='background:#fff;padding:8px;border-radius:6px;border:2px solid #2563eb;'>
          <p style='color:#1e40af;font-weight:700;margin:0 0 2px;'>✏️ 編輯模式</p>
          <p style='color:#374151;margin:0;'>直接修改，適合自己的文件</p>
        </div>
        <div style='background:#fff;padding:8px;border-radius:6px;border:2px solid #16a34a;'>
          <p style='color:#15803d;font-weight:700;margin:0 0 2px;'>💡 建議模式</p>
          <p style='color:#374151;margin:0;'>修改以彩色標示，作者可接受/拒絕</p>
        </div>
        <div style='background:#fff;padding:8px;border-radius:6px;border:2px solid #6b7280;'>
          <p style='color:#6b7280;font-weight:700;margin:0 0 2px;'>👁️ 檢視模式</p>
          <p style='color:#374151;margin:0;'>只能閱讀，無法做任何修改</p>
        </div>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#f8fafc;border:2px solid #e2e8f0;padding:15px;border-radius:10px;'>
      <h3 style='color:#374151;font-size:.9rem;margin-bottom:10px;'>📄 建議模式示範</h3>
      <div style='background:#fff;padding:12px;border-radius:8px;font-size:.85rem;line-height:1.8;border:1px solid #e2e8f0;'>
        <span style='color:#374151;'>台灣是</span>
        <span style='background:#fef2f2;color:#dc2626;text-decoration:line-through;'>全球最重要的</span>
        <span style='background:#f0fdf4;color:#15803d;'>半導體產業</span>
        <span style='color:#374151;'>重要的科技中心</span>
        <span style='background:#f0fdf4;color:#15803d;'>，台積電佔全球先進晶片代工超過 60%</span>
        <span style='color:#374151;'>。</span>
      </div>
      <div style='display:flex;gap:8px;margin-top:8px;font-size:.78rem;'>
        <span style='background:#f0fdf4;color:#15803d;padding:3px 8px;border-radius:4px;'>綠色：新增</span>
        <span style='background:#fef2f2;color:#dc2626;padding:3px 8px;border-radius:4px;'>紅底：刪除</span>
      </div>
    </div>
  </div>
</div>"""
    },
    {
        'id': 16, 'chapter': '第三章：共同編輯與版本控制', 'title': '🎯 第三章 隨堂測驗',
        'bg': 'purple', 'quiz': 'q3', 'chart': None, 'video': None,
        'html': """
<div style='text-align:center;padding:20px;'>
  <div style='font-size:56px;margin-bottom:15px;'>🎯</div>
  <h2 style='color:#fff;font-size:2rem;font-weight:800;margin-bottom:10px;'>第三章 隨堂測驗</h2>
  <p style='color:#e9d5ff;font-size:1.1rem;'>共同編輯與版本控制 ── 2 道題目，點擊作答！</p>
</div>"""
    },
    {
        'id': 17, 'chapter': '第四章：雲端辦公應用', 'title': 'Google 試算表',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>Google 試算表：常用函數</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>📊 基礎函數</h3>
      <table style='width:100%;border-collapse:collapse;font-size:.8rem;'>
        <tr style='background:#1e40af;color:#fff;'><th style='padding:6px;'>函數</th><th style='padding:6px;'>功能</th><th style='padding:6px;'>範例</th></tr>
        <tr><td style='padding:5px;color:#374151;font-family:monospace;'>SUM</td><td style='padding:5px;color:#374151;'>加總</td><td style='padding:5px;color:#1e40af;font-family:monospace;font-size:.75rem;'>=SUM(A1:A10)</td></tr>
        <tr style='background:#f0f9ff;'><td style='padding:5px;color:#374151;font-family:monospace;'>AVERAGE</td><td style='padding:5px;color:#374151;'>平均</td><td style='padding:5px;color:#1e40af;font-family:monospace;font-size:.75rem;'>=AVERAGE(B1:B5)</td></tr>
        <tr><td style='padding:5px;color:#374151;font-family:monospace;'>COUNT</td><td style='padding:5px;color:#374151;'>計數</td><td style='padding:5px;color:#1e40af;font-family:monospace;font-size:.75rem;'>=COUNT(C1:C20)</td></tr>
        <tr style='background:#f0f9ff;'><td style='padding:5px;color:#374151;font-family:monospace;'>IF</td><td style='padding:5px;color:#374151;'>條件判斷</td><td style='padding:5px;color:#1e40af;font-family:monospace;font-size:.75rem;'>=IF(A1>60,"及格","不及格")</td></tr>
        <tr><td style='padding:5px;color:#374151;font-family:monospace;'>VLOOKUP</td><td style='padding:5px;color:#374151;'>垂直查找</td><td style='padding:5px;color:#1e40af;font-family:monospace;font-size:.75rem;'>=VLOOKUP(A1,D:F,2,0)</td></tr>
      </table>
    </div>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:8px;'>📈 製作圖表</h3>
      <div style='display:flex;flex-direction:column;gap:6px;font-size:.83rem;'>
        <div style='background:#dcfce7;padding:7px;border-radius:5px;display:flex;gap:6px;align-items:center;'><span style='background:#15803d;color:#fff;width:18px;height:18px;border-radius:50%;font-size:.65rem;font-weight:700;display:flex;align-items:center;justify-content:center;flex-shrink:0;'>1</span><span style='color:#374151;'>選取要圖表化的資料範圍</span></div>
        <div style='background:#dcfce7;padding:7px;border-radius:5px;display:flex;gap:6px;align-items:center;'><span style='background:#15803d;color:#fff;width:18px;height:18px;border-radius:50%;font-size:.65rem;font-weight:700;display:flex;align-items:center;justify-content:center;flex-shrink:0;'>2</span><span style='color:#374151;'>插入 → 圖表</span></div>
        <div style='background:#dcfce7;padding:7px;border-radius:5px;display:flex;gap:6px;align-items:center;'><span style='background:#15803d;color:#fff;width:18px;height:18px;border-radius:50%;font-size:.65rem;font-weight:700;display:flex;align-items:center;justify-content:center;flex-shrink:0;'>3</span><span style='color:#374151;'>選擇圖表類型（柱狀、折線、圓餅）</span></div>
        <div style='background:#dcfce7;padding:7px;border-radius:5px;display:flex;gap:6px;align-items:center;'><span style='background:#15803d;color:#fff;width:18px;height:18px;border-radius:50%;font-size:.65rem;font-weight:700;display:flex;align-items:center;justify-content:center;flex-shrink:0;'>4</span><span style='color:#374151;'>調整標題、顏色等外觀設定</span></div>
      </div>
    </div>
  </div>
</div>"""
    },
    {
        'id': 18, 'chapter': '第四章：雲端辦公應用', 'title': 'Google 簡報',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>Google 簡報：有效的視覺呈現</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>🎨 好簡報的設計原則</h3>
      <div style='display:flex;flex-direction:column;gap:6px;font-size:.83rem;'>
        <div style='background:#dbeafe;padding:7px;border-radius:5px;color:#374151;'><strong style='color:#1e40af;'>少即是多</strong>：每頁一個重點，文字精簡</div>
        <div style='background:#dbeafe;padding:7px;border-radius:5px;color:#374151;'><strong style='color:#1e40af;'>大字原則</strong>：字體至少 24pt，讓後排看得清楚</div>
        <div style='background:#dbeafe;padding:7px;border-radius:5px;color:#374151;'><strong style='color:#1e40af;'>對比色</strong>：深底淺字或淺底深字，提高可讀性</div>
        <div style='background:#dbeafe;padding:7px;border-radius:5px;color:#374151;'><strong style='color:#1e40af;'>一致性</strong>：整份簡報套用同一主題</div>
        <div style='background:#dbeafe;padding:7px;border-radius:5px;color:#374151;'><strong style='color:#1e40af;'>圖像優先</strong>：一張好圖片勝過一段文字</div>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:10px;'>⚡ 實用功能</h3>
      <ul style='color:#374151;font-size:.85rem;padding-left:16px;'>
        <li>主題（Theme）：一鍵統一設計</li>
        <li>母片（Slide master）：統一版面配置</li>
        <li>動畫與轉場效果</li>
        <li>演講者備忘稿</li>
        <li>發表模式（全螢幕）</li>
        <li>分享為 PDF 或 PowerPoint 格式</li>
      </ul>
    </div>
  </div>
</div>"""
    },
    {
        'id': 19, 'chapter': '第四章：雲端辦公應用', 'title': 'Google Calendar 與 Meet',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>Google Calendar 與 Meet</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>📅 Google Calendar</h3>
      <ul style='color:#374151;font-size:.85rem;padding-left:16px;'>
        <li>建立並邀請他人參加活動</li>
        <li>設定提醒（Email 或手機通知）</li>
        <li>與同學、老師共享行事曆</li>
        <li>自動同步到手機</li>
        <li>整合 Google Meet 視訊連結</li>
      </ul>
    </div>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:10px;'>🎥 Google Meet</h3>
      <ul style='color:#374151;font-size:.85rem;padding-left:16px;'>
        <li>免費視訊會議（最多 100 人）</li>
        <li>即時字幕（支援英文）</li>
        <li>螢幕分享</li>
        <li>分組討論室（Breakout rooms）</li>
        <li>錄製會議（需 Google Workspace）</li>
      </ul>
      <div style='background:#dcfce7;padding:8px;border-radius:6px;margin-top:10px;'>
        <p style='color:#15803d;font-size:.8rem;margin:0;'>💡 學生可以用 Meet 進行線上分組討論</p>
      </div>
    </div>
  </div>
</div>"""
    },
    {
        'id': 20, 'chapter': '第四章：雲端辦公應用', 'title': 'Google 協作平台',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>Google 協作平台與 Classroom</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>🏫 Google Classroom</h3>
      <ul style='color:#374151;font-size:.85rem;padding-left:16px;'>
        <li>老師發布作業、通知</li>
        <li>學生提交作業（可直接提交 Google 文件）</li>
        <li>老師線上批改、評分、留言</li>
        <li>作業截止時間提醒</li>
        <li>整合 Meet 視訊連結</li>
      </ul>
    </div>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:10px;'>🌐 Google 協作平台</h3>
      <p style='color:#374151;font-size:.88rem;margin-bottom:8px;'>類似學校/班級的網站：</p>
      <ul style='color:#374151;font-size:.85rem;padding-left:16px;'>
        <li>建立班級或社團的共用網站</li>
        <li>嵌入 Google 試算表、文件、YouTube</li>
        <li>不需要寫程式即可建立網頁</li>
        <li>可公開或只限校內人員檢視</li>
      </ul>
    </div>
  </div>
</div>"""
    },
    {
        'id': 21, 'chapter': '第四章：雲端辦公應用', 'title': '生產力工作流程',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>打造高效的雲端工作流程</h2>
<div style='background:#1e293b;padding:20px;border-radius:12px;margin-bottom:16px;'>
  <h3 style='color:#94a3b8;font-size:.85rem;text-align:center;margin-bottom:16px;letter-spacing:.05em;'>分組報告的最佳實踐流程</h3>
  <div style='display:grid;grid-template-columns:repeat(5,1fr);gap:8px;'>
    <div style='background:#0f172a;padding:12px;border-radius:8px;text-align:center;border-bottom:3px solid #3b82f6;'>
      <div style='font-size:1.6rem;'>📋</div>
      <p style='color:#93c5fd;font-size:.7rem;margin-top:4px;'>①計畫<br>Calendar 排程</p>
    </div>
    <div style='background:#0f172a;padding:12px;border-radius:8px;text-align:center;border-bottom:3px solid #22c55e;'>
      <div style='font-size:1.6rem;'>📄</div>
      <p style='color:#86efac;font-size:.7rem;margin-top:4px;'>②協作<br>文件共同編輯</p>
    </div>
    <div style='background:#0f172a;padding:12px;border-radius:8px;text-align:center;border-bottom:3px solid #f59e0b;'>
      <div style='font-size:1.6rem;'>📊</div>
      <p style='color:#fcd34d;font-size:.7rem;margin-top:4px;'>③分析<br>試算表整理</p>
    </div>
    <div style='background:#0f172a;padding:12px;border-radius:8px;text-align:center;border-bottom:3px solid #f472b6;'>
      <div style='font-size:1.6rem;'>📑</div>
      <p style='color:#f9a8d4;font-size:.7rem;margin-top:4px;'>④呈現<br>簡報製作</p>
    </div>
    <div style='background:#0f172a;padding:12px;border-radius:8px;text-align:center;border-bottom:3px solid #a78bfa;'>
      <div style='font-size:1.6rem;'>🎥</div>
      <p style='color:#c4b5fd;font-size:.7rem;margin-top:4px;'>⑤分享<br>Meet 發表</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 22, 'chapter': '第四章：雲端辦公應用', 'title': '🎯 第四章 隨堂測驗',
        'bg': 'purple', 'quiz': 'q4', 'chart': None, 'video': None,
        'html': """
<div style='text-align:center;padding:20px;'>
  <div style='font-size:56px;margin-bottom:15px;'>🎯</div>
  <h2 style='color:#fff;font-size:2rem;font-weight:800;margin-bottom:10px;'>第四章 隨堂測驗</h2>
  <p style='color:#e9d5ff;font-size:1.1rem;'>雲端辦公應用 ── 2 道題目，點擊作答！</p>
</div>"""
    },
    {
        'id': 23, 'chapter': '分組實作', 'title': '分組實作：雲端協作報告',
        'bg': 'teal', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 style='font-size:1.8rem;font-weight:800;color:#fff;margin-bottom:20px;text-align:center;'>☁️ 分組實作：雲端協作報告</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div style='background:rgba(255,255,255,0.15);padding:18px;border-radius:12px;'>
    <h3 style='color:#fff;font-size:1rem;margin-bottom:14px;'>📋 實作任務</h3>
    <div style='display:flex;flex-direction:column;gap:10px;'>
      <div style='background:rgba(255,255,255,0.2);padding:12px;border-radius:8px;'>
        <p style='color:#fff;font-weight:700;font-size:.9rem;margin:0 0 4px;'>任務一：共同編輯文件</p>
        <p style='color:#cffafe;font-size:.8rem;margin:0;'>小組成員同時在 Google 文件撰寫「台灣科技產業調查報告」，使用標題樣式和自動目錄</p>
      </div>
      <div style='background:rgba(255,255,255,0.2);padding:12px;border-radius:8px;'>
        <p style='color:#fff;font-weight:700;font-size:.9rem;margin:0 0 4px;'>任務二：試算表分析</p>
        <p style='color:#cffafe;font-size:.8rem;margin:0;'>用 Google 試算表整理調查數據，加入 IF 函數和圖表視覺化</p>
      </div>
      <div style='background:rgba(255,255,255,0.2);padding:12px;border-radius:8px;'>
        <p style='color:#fff;font-weight:700;font-size:.9rem;margin:0 0 4px;'>任務三：簡報製作</p>
        <p style='color:#cffafe;font-size:.8rem;margin:0;'>製作 8 張以上 Google 簡報，套用主題，展示調查結果</p>
      </div>
    </div>
  </div>
  <div>
    <div style='background:rgba(255,255,255,0.15);padding:15px;border-radius:12px;margin-bottom:12px;'>
      <h3 style='color:#fff;font-size:1rem;margin-bottom:10px;'>📊 評分標準</h3>
      <ul style='color:#cffafe;font-size:.85rem;padding-left:16px;'>
        <li>文件：標題樣式、目錄、格式（30分）</li>
        <li>試算表：函數、圖表（20分）</li>
        <li>簡報：設計、內容（30分）</li>
        <li>協作過程：版本歷史、留言（20分）</li>
      </ul>
    </div>
    <div style='background:rgba(255,255,255,0.15);padding:12px;border-radius:8px;'>
      <p style='color:#fff;font-size:.85rem;font-weight:700;margin-bottom:4px;'>🗓️ 繳交方式</p>
      <p style='color:#cffafe;font-size:.82rem;margin:0;'>共用連結上傳至 Google Classroom，確認權限為「任何人可以留言」</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 24, 'chapter': '分組實作', 'title': '雲端改變了工作方式',
        'bg': 'navy', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<div style='text-align:center;padding:30px 20px;'>
  <div style='font-size:64px;margin-bottom:20px;'>☁️</div>
  <h1 style='font-size:2.2rem;font-weight:900;color:#fff;margin-bottom:12px;'>雲端讓合作沒有距離</h1>
  <h2 style='font-size:1.2rem;font-weight:400;color:#93c5fd;margin-bottom:24px;'>任何裝置、任何地點、任何時間，一起工作</h2>
  <div style='background:rgba(255,255,255,0.1);padding:18px;border-radius:12px;margin-bottom:24px;max-width:600px;margin-left:auto;margin-right:auto;'>
    <p style='color:#e2e8f0;font-size:1rem;font-style:italic;line-height:1.7;margin:0;'>
      「The future of work is not about where you work, it's about how you collaborate.」
    </p>
  </div>
  <div style='display:flex;justify-content:center;gap:12px;flex-wrap:wrap;'>
    <span style='background:rgba(255,255,255,0.12);color:#e0f2fe;padding:8px 18px;border-radius:20px;font-size:.9rem;'>掌握 Workspace ✅</span>
    <span style='background:rgba(255,255,255,0.12);color:#e0f2fe;padding:8px 18px;border-radius:20px;font-size:.9rem;'>學會協作 ✅</span>
    <span style='background:rgba(255,255,255,0.12);color:#e0f2fe;padding:8px 18px;border-radius:20px;font-size:.9rem;'>下一章見 👋</span>
  </div>
</div>"""
    },
]
