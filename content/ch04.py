# -*- coding: utf-8 -*-
# Ch.4: 文書工具 × 小論文寫作
#   目標：Google Docs 與 Microsoft Word 雙軌，聚焦「產出一份合格小論文」

CHAPTERS = [
    {'name': '封面', 'start': 1},
    {'name': '第一章：文書工具巡禮', 'start': 2},
    {'name': '第二章：文書進階排版（寫論文必備）', 'start': 6},
    {'name': '第三章：共同編輯與版本控制', 'start': 11},
    {'name': '第四章：小論文寫作實戰', 'start': 15},
    {'name': '第五章：電腦軟體應用丙級', 'start': 22},
    {'name': '個人實作', 'start': 24},
]

QUIZZES = {
    'q1': {
        'title': '第一章 隨堂測驗',
        'questions': [
            {
                'q': '關於 Google Docs 和 Microsoft Word，下列敘述何者「錯誤」？',
                'options': [
                    '兩者都支援即時多人協作',
                    'Google Docs 完全免費、Word 需買 Office 365 或授權',
                    '兩者互相不能開啟對方的檔案',
                    '學生用學校 email 通常可以免費申請 Office 365'
                ],
                'answer': 2,
                'explain': 'Word 可以開啟 .docx 也可以開啟 Google Docs 匯出的檔案；Google Docs 也可以匯入 .docx。兩者其實高度相容——這是為什麼你要「兩個都會用」的原因。'
            },
            {
                'q': '你要寫小論文（10 頁 A4），電腦教室桌機沒裝 Word 但可上網，最實際的做法是？',
                'options': [
                    '請老師買一台裝有 Word 的筆電',
                    '直接用瀏覽器打開 Google Docs 或 Word Online 寫',
                    '把文件寫在記事本再套 Word 排版',
                    '手寫掃描'
                ],
                'answer': 1,
                'explain': 'Google Docs 和 Word 都有網頁版，任何有瀏覽器的電腦都能用，寫完直接匯出 PDF 上傳投稿。學校 Google 帳號和 Office 365 學生帳號都免費。'
            },
        ]
    },
    'q2': {
        'title': '第二章 隨堂測驗',
        'questions': [
            {
                'q': '為什麼寫小論文一定要用「段落樣式」（如標題 1、標題 2）？',
                'options': [
                    '只是讓字比較大',
                    '之後才能自動產生目錄、也讓格式全文一致',
                    '沒有一定要用',
                    '樣式只是裝飾用途'
                ],
                'answer': 1,
                'explain': '段落樣式有兩個關鍵作用：① 一改樣式，全文標題同步更新，不用一個個手動改；② 自動目錄只認得「套過樣式」的段落，沒有樣式就沒有目錄。'
            },
            {
                'q': '小論文比賽規定「全篇要有頁首」，最正確的做法是？',
                'options': [
                    '在每一頁最上方手動輸入篇名',
                    '插入頁首功能一次設定，每頁自動顯示',
                    '把篇名放在文件開頭',
                    '不用頁首，讀者自己會看標題'
                ],
                'answer': 1,
                'explain': '「頁首」是專門的功能：Word「插入 → 頁首」、Google Docs「插入 → 頁首和頁尾」，設定一次全文自動套用。手動輸入既費時又容易在編輯時跑掉。'
            },
        ]
    },
    'q3': {
        'title': '第三章 隨堂測驗',
        'questions': [
            {
                'q': '小組 3 人共寫小論文，最推薦的協作方式是？',
                'options': [
                    'A 寫完 email 給 B，B 改完再傳 C，C 統整',
                    '用 Google Docs 共用，3 人同時線上編輯',
                    '3 人分別寫在自己電腦，最後由組長剪貼合併',
                    '用 LINE 傳文字給組長彙整'
                ],
                'answer': 1,
                'explain': '共用 Google Docs（或 Word Online）可同時編輯、看到彼此游標與修改、有版本歷史。傳來傳去的檔案版本會很混亂，也容易漏改。'
            },
            {
                'q': '不小心刪掉了辛苦寫的一整段，存檔後才發現，最快的救援方式？',
                'options': [
                    '重新回想寫過的內容',
                    'Ctrl+Z（但已存檔可能沒用）',
                    '檔案 → 版本歷史，找到刪除前的版本還原',
                    '重灌電腦'
                ],
                'answer': 2,
                'explain': 'Google Docs 和 Word Online 都有「版本歷史」，會自動保留每次修改的紀錄。找到刪除前的版本一鍵還原，這是雲端文書相對本機檔案最大的優勢之一。'
            },
        ]
    },
    'q4': {
        'title': '第四章 隨堂測驗（小論文重點）',
        'questions': [
            {
                'q': '關於小論文的「六大架構」，下列哪一項「不是」正確順序？',
                'options': [
                    '前言 → 文獻探討 → 研究方法 → 分析結果 → 結論建議 → 參考文獻',
                    '文獻探討 → 前言 → 研究方法 → 結論 → 分析結果 → 參考文獻',
                    '研究是為了回答「前言的問題」，所以前言擺最前',
                    '參考文獻永遠是最後一章'
                ],
                'answer': 1,
                'explain': '正確順序：壹.前言 → 貳.文獻探討 → 參.研究方法 → 肆.研究分析與結果 → 伍.研究結論與建議 → 陸.參考文獻。順序錯或缺任何一項都會被退件。'
            },
            {
                'q': '關於小論文比賽的「AI 使用界線」，下列何者正確？',
                'options': [
                    'AI 生成的文字只要重寫過就可以用',
                    'AI 可以用來「發想主題」，但摘要、改寫、圖表都禁止 AI 生成',
                    '整篇用 ChatGPT 寫，改幾個字就沒問題',
                    '只要不被抓到都可以'
                ],
                'answer': 1,
                'explain': '115 學年比賽規則明訂：可用 AI 進行主題發想，但文章內容（含摘要、改寫、圖表等）不得由 AI 生成。違規會被取消資格並下屆停權。'
            },
        ]
    },
}


# ═══════════════════════════════════════════════════════════════════════
# SLIDES
# ═══════════════════════════════════════════════════════════════════════

SLIDES = [

# ─── 1. 封面 ───
{
    'id': 1, 'chapter': '封面', 'title': '文書工具 × 小論文寫作',
    'bg': 'navy', 'quiz': None, 'chart': None, 'video': None,
    'html': """
<div style='text-align:center;padding:30px 20px;'>
  <div style='font-size:72px;margin-bottom:20px;'>📝</div>
  <h1 style='font-size:2.6rem;font-weight:900;color:#fff;margin-bottom:12px;'>文書工具 × 小論文寫作</h1>
  <h2 style='font-size:1.4rem;font-weight:400;color:#93c5fd;margin-bottom:26px;'>Google Docs · Microsoft Word · 全國小論文比賽</h2>
  <div style='display:flex;justify-content:center;gap:16px;flex-wrap:wrap;margin-bottom:24px;'>
    <span style='background:rgba(255,255,255,0.15);color:#e0f2fe;padding:8px 20px;border-radius:20px;font-size:1rem;'>📄 雙軌對照</span>
    <span style='background:rgba(255,255,255,0.15);color:#e0f2fe;padding:8px 20px;border-radius:20px;font-size:1rem;'>🎓 小論文六大架構</span>
    <span style='background:rgba(255,255,255,0.15);color:#e0f2fe;padding:8px 20px;border-radius:20px;font-size:1rem;'>🏆 挑戰全國比賽</span>
  </div>
  <p style='color:#bfdbfe;font-size:1.05rem;'>城市科技 — 第四章</p>
</div>"""
},

# ═══ 第一章：文書工具巡禮 ═══

{
    'id': 2, 'chapter': '第一章：文書工具巡禮', 'title': 'Google Docs vs Microsoft Word',
    'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
    'html': """
<div class='slide-inner'>
  <h2 class='slide-title'>📄 Google Docs vs Microsoft Word</h2>
  <p class='slide-desc'>兩大主流文書工具——高中要會用，未來職場也離不開</p>

  <table class='info-table' style='margin-bottom:12px;font-size:.82rem;'>
    <thead class='table-header'>
      <tr>
        <th>比較項目</th>
        <th style='background:#dbeafe;color:#1e40af;'>Google Docs</th>
        <th style='background:#fef3c7;color:#92400e;'>Microsoft Word</th>
      </tr>
    </thead>
    <tbody>
      <tr><td><strong>取得方式</strong></td><td>Google 帳號 · 完全免費</td><td>買授權 or 學生 Office 365 免費</td></tr>
      <tr class='tr-highlight'><td><strong>使用平台</strong></td><td>瀏覽器（任何電腦、平板、手機）</td><td>Windows/Mac 桌機 + 網頁版 + App</td></tr>
      <tr><td><strong>離線編輯</strong></td><td>需先開離線模式</td><td>桌機版天生就是離線編輯</td></tr>
      <tr class='tr-highlight'><td><strong>即時協作</strong></td><td>✅ 業界最強</td><td>✅ Word Online / OneDrive</td></tr>
      <tr><td><strong>檔案格式</strong></td><td>.gdoc / 可匯出 .docx .pdf</td><td>.docx（業界標準）· 可存 .pdf</td></tr>
      <tr class='tr-highlight'><td><strong>台灣市占</strong></td><td>78% 高中職愛用</td><td>85% 企業標準</td></tr>
    </tbody>
  </table>

  <div class='tip-box'>
    💡 <strong>結論</strong>：兩個都會用，未來走到哪都不怕。它們互相相容——Word 可以開啟 Google 匯出的 .docx，Google Docs 也可以上傳 Word 檔繼續編輯。
  </div>
</div>"""
},

{
    'id': 3, 'chapter': '第一章：文書工具巡禮', 'title': 'Office 365 學生帳號免費申請',
    'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
    'html': """
<div class='slide-inner'>
  <h2 class='slide-title'>🎓 Office 365 學生帳號怎麼領？</h2>
  <p class='slide-desc'>只要有學校 email，Microsoft 送你完整的 Office 一整套</p>

  <div class='card-grid-2' style='margin-bottom:12px;'>
    <div style='background:linear-gradient(135deg,#fef3c7,#fde68a);border:1px solid #fbbf24;border-radius:12px;padding:14px;'>
      <div style='font-weight:700;color:#78350f;font-size:.95rem;margin-bottom:8px;'>📥 3 步驟取得帳號</div>
      <div style='font-size:.82rem;color:#78350f;line-height:1.7;'>
        <strong>①</strong> 去 <a href='https://www.microsoft.com/zh-tw/education/products/office' target='_blank' style='color:#c2410c;'>Microsoft 教育版申請頁</a><br>
        <strong>②</strong> 輸入你的<strong>學校 email</strong>（如 s1234@school.edu.tw）<br>
        <strong>③</strong> 收信、驗證 → 完成！
      </div>
      <p style='font-size:.75rem;color:#92400e;margin-top:10px;'>
        💡 沒收到驗證信？先確認學校 email 是否已啟用，或問資訊組。
      </p>
    </div>

    <div style='background:linear-gradient(135deg,#dbeafe,#bfdbfe);border:1px solid #60a5fa;border-radius:12px;padding:14px;'>
      <div style='font-weight:700;color:#1e40af;font-size:.95rem;margin-bottom:8px;'>🎁 學生方案免費包含</div>
      <div style='font-size:.82rem;color:#1e3a8a;line-height:1.6;'>
        ✅ Word / Excel / PowerPoint / OneNote<br>
        ✅ OneDrive <strong>1 TB</strong> 雲端空間<br>
        ✅ Teams 視訊會議<br>
        ✅ 電腦、平板、手機各 5 台裝置
      </div>
      <p style='font-size:.75rem;color:#1e40af;margin-top:10px;'>
        💰 一般成人授權每年約 NT$2,190，學生 <strong>0 元</strong>！
      </p>
    </div>
  </div>

  <div class='tip-box'>
    🏫 <strong>電腦教室桌機</strong>通常已裝好 Word，直接用即可；<strong>自己筆電</strong>建議申請學生 Office 365 或用 Google Docs 都好。
  </div>
</div>"""
},

{
    'id': 4, 'chapter': '第一章：文書工具巡禮', 'title': '雲端硬碟：Google Drive vs OneDrive',
    'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
    'html': """
<div class='slide-inner'>
  <h2 class='slide-title'>☁️ 雲端硬碟：Google Drive vs OneDrive</h2>

  <div class='card-grid-2' style='margin-bottom:12px;'>
    <div style='background:#eff6ff;border:1px solid #93c5fd;border-radius:12px;padding:14px;'>
      <div style='display:flex;align-items:center;gap:10px;margin-bottom:8px;'>
        <span style='font-size:1.5rem;'>🗂️</span>
        <div>
          <div style='font-weight:700;color:#1e40af;font-size:.95rem;'>Google Drive</div>
          <div style='font-size:.72rem;color:#6b7280;'>drive.google.com</div>
        </div>
      </div>
      <ul style='font-size:.8rem;color:#1e3a8a;line-height:1.7;padding-left:16px;margin:0;'>
        <li>免費 <strong>15 GB</strong>（含 Gmail、Photos）</li>
        <li>學校版 <strong>100 GB+</strong>（依學校方案）</li>
        <li>自動同步 Google Docs / Sheets / Slides</li>
        <li>檔案共用：連結加權限一鍵搞定</li>
      </ul>
    </div>

    <div style='background:#fef3c7;border:1px solid #fbbf24;border-radius:12px;padding:14px;'>
      <div style='display:flex;align-items:center;gap:10px;margin-bottom:8px;'>
        <span style='font-size:1.5rem;'>☁️</span>
        <div>
          <div style='font-weight:700;color:#92400e;font-size:.95rem;'>Microsoft OneDrive</div>
          <div style='font-size:.72rem;color:#6b7280;'>onedrive.live.com</div>
        </div>
      </div>
      <ul style='font-size:.8rem;color:#78350f;line-height:1.7;padding-left:16px;margin:0;'>
        <li>免費 <strong>5 GB</strong></li>
        <li>學生 Office 365 <strong>1 TB</strong>（超大！）</li>
        <li>自動同步 Word / Excel / PowerPoint</li>
        <li>整合 Windows 檔案總管</li>
      </ul>
    </div>
  </div>

  <div style='background:#f0fdf4;border:1px dashed #22c55e;border-radius:10px;padding:10px 14px;font-size:.85rem;color:#15803d;'>
    💡 <strong>寫小論文的實務建議</strong>：主檔放雲端（任何電腦都能開）+ 完成時另存 PDF 上傳投稿系統。<strong>絕對不要只存本機硬碟</strong>——電腦壞掉就沒了！
  </div>
</div>"""
},

{
    'id': 5, 'chapter': '第一章：文書工具巡禮', 'title': '🎯 第一章 隨堂測驗',
    'bg': 'teal', 'quiz': 'q1', 'chart': None, 'video': None,
    'html': """
<div style='text-align:center;padding:40px 20px;'>
  <div style='font-size:64px;margin-bottom:20px;'>🎯</div>
  <h1 style='font-size:2rem;font-weight:900;color:#fff;margin-bottom:12px;'>第一章 隨堂測驗</h1>
  <h2 style='font-size:1.1rem;font-weight:400;color:#a7f3d0;margin-bottom:24px;'>文書工具巡禮</h2>
  <p style='color:#e0f7fa;font-size:1rem;'>2 道題目，按「下一頁」開始作答！</p>
</div>"""
},

# ═══ 第二章：文書進階排版 ═══

{
    'id': 6, 'chapter': '第二章：文書進階排版（寫論文必備）', 'title': '段落樣式：一切自動化的起點',
    'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
    'html': """
<div class='slide-inner'>
  <h2 class='slide-title'>🏷️ 段落樣式：一切自動化的起點</h2>
  <p class='slide-desc'>套用「標題 1、標題 2」不只讓字變大——是後面所有自動化功能的基礎</p>

  <div class='card-grid-2' style='margin-bottom:12px;'>
    <div style='background:#eff6ff;border:1px solid #93c5fd;border-radius:12px;padding:14px;'>
      <div style='font-weight:700;color:#1e40af;font-size:.9rem;margin-bottom:8px;'>📄 Microsoft Word</div>
      <div style='font-size:.8rem;color:#1e3a8a;line-height:1.6;'>
        <strong>路徑</strong>：常用 → 樣式區<br>
        <strong>快捷鍵</strong>：<br>
        &nbsp;&nbsp;<code style='background:#fff;padding:1px 6px;border-radius:4px;'>Ctrl + Alt + 1</code> → 標題 1<br>
        &nbsp;&nbsp;<code style='background:#fff;padding:1px 6px;border-radius:4px;'>Ctrl + Alt + 2</code> → 標題 2<br>
        &nbsp;&nbsp;<code style='background:#fff;padding:1px 6px;border-radius:4px;'>Ctrl + Shift + N</code> → 內文
      </div>
    </div>

    <div style='background:#fef3c7;border:1px solid #fbbf24;border-radius:12px;padding:14px;'>
      <div style='font-weight:700;color:#92400e;font-size:.9rem;margin-bottom:8px;'>📗 Google Docs</div>
      <div style='font-size:.8rem;color:#78350f;line-height:1.6;'>
        <strong>路徑</strong>：工具列「一般文字」下拉選單<br>
        <strong>快捷鍵</strong>：<br>
        &nbsp;&nbsp;<code style='background:#fff;padding:1px 6px;border-radius:4px;'>Ctrl + Alt + 1</code> → 標題 1<br>
        &nbsp;&nbsp;<code style='background:#fff;padding:1px 6px;border-radius:4px;'>Ctrl + Alt + 2</code> → 標題 2<br>
        &nbsp;&nbsp;<code style='background:#fff;padding:1px 6px;border-radius:4px;'>Ctrl + Alt + 0</code> → 內文
      </div>
    </div>
  </div>

  <div style='background:#f0fdf4;border-left:4px solid #22c55e;padding:10px 14px;border-radius:8px;font-size:.85rem;color:#15803d;'>
    ✨ <strong>神奇之處</strong>：全文所有「標題 1」外觀可以一次改（改樣式定義即可）；<strong>而且</strong>之後「自動目錄」會抓出所有標題，不套樣式就不會被抓到！
  </div>

  <div class='tip-box' style='margin-top:10px;'>
    💡 <strong>小論文六大架構每一章都用「標題 1」</strong>，之後只要按「插入目錄」，目錄就自動長出來。
  </div>
</div>"""
},

{
    'id': 7, 'chapter': '第二章：文書進階排版（寫論文必備）', 'title': '自動目錄：0.1 秒生成',
    'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
    'html': """
<div class='slide-inner'>
  <h2 class='slide-title'>📑 自動目錄：0.1 秒生成</h2>

  <div class='card-grid-2' style='margin-bottom:12px;'>
    <div style='background:#eff6ff;border:1px solid #93c5fd;border-radius:12px;padding:14px;'>
      <div style='font-weight:700;color:#1e40af;font-size:.9rem;margin-bottom:8px;'>📄 Word</div>
      <div style='font-size:.8rem;color:#1e3a8a;line-height:1.7;'>
        <strong>步驟</strong>：<br>
        ① 游標點到要插入目錄的位置<br>
        ② 「<strong>參考資料</strong>」分頁 →「目錄」→ 選樣式<br>
        ③ 完成！
      </div>
      <div style='background:#fff;border:1px solid #bfdbfe;border-radius:8px;padding:8px 10px;margin-top:8px;font-size:.72rem;color:#6b7280;'>
        📌 修改標題後：右鍵目錄 → 更新功能變數
      </div>
    </div>

    <div style='background:#fef3c7;border:1px solid #fbbf24;border-radius:12px;padding:14px;'>
      <div style='font-weight:700;color:#92400e;font-size:.9rem;margin-bottom:8px;'>📗 Google Docs</div>
      <div style='font-size:.8rem;color:#78350f;line-height:1.7;'>
        <strong>步驟</strong>：<br>
        ① 游標點到要插入目錄的位置<br>
        ② 「<strong>插入</strong>」→「目錄」→ 選樣式<br>
        ③ 完成！
      </div>
      <div style='background:#fff;border:1px solid #fde68a;border-radius:8px;padding:8px 10px;margin-top:8px;font-size:.72rem;color:#6b7280;'>
        📌 修改標題後：點目錄旁的「重新整理」小圖示
      </div>
    </div>
  </div>

  <div style='background:#fef2f2;border-left:4px solid #ef4444;padding:10px 14px;border-radius:8px;font-size:.85rem;color:#991b1b;'>
    ⚠️ <strong>常見錯誤</strong>：目錄空空的？→ 你沒套「標題 1、標題 2」樣式，只是把字放大。修：把每章章名選起來 → 點樣式「標題 1」。
  </div>
</div>"""
},

{
    'id': 8, 'chapter': '第二章：文書進階排版（寫論文必備）', 'title': '頁首、頁尾與頁碼（小論文必要！）',
    'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
    'html': """
<div class='slide-inner'>
  <h2 class='slide-title'>📌 頁首、頁尾與頁碼</h2>
  <p class='slide-desc'>115 小論文比賽規則明訂：<strong>全篇需有頁首</strong>，且與投稿篇名一致</p>

  <div class='card-grid-2' style='margin-bottom:12px;'>
    <div style='background:#eff6ff;border:1px solid #93c5fd;border-radius:12px;padding:14px;'>
      <div style='font-weight:700;color:#1e40af;font-size:.9rem;margin-bottom:8px;'>📄 Word</div>
      <div style='font-size:.8rem;color:#1e3a8a;line-height:1.7;'>
        <strong>頁首</strong>：插入 → 頁首 → 選樣式 → 打篇名<br>
        <strong>頁碼</strong>：插入 → 頁碼 → 頁面底端 → 置中<br>
        <br>
        💡 <strong>技巧</strong>：首頁不同（封面不編碼）：<br>
        版面配置 → 版面設定 → 首頁不同
      </div>
    </div>

    <div style='background:#fef3c7;border:1px solid #fbbf24;border-radius:12px;padding:14px;'>
      <div style='font-weight:700;color:#92400e;font-size:.9rem;margin-bottom:8px;'>📗 Google Docs</div>
      <div style='font-size:.8rem;color:#78350f;line-height:1.7;'>
        <strong>頁首</strong>：插入 → 頁首和頁尾 → 頁首<br>
        <strong>頁碼</strong>：插入 → 頁碼 → 選位置<br>
        <br>
        💡 <strong>技巧</strong>：不同首頁：<br>
        頁首中點「選項」→ 勾「不同首頁」
      </div>
    </div>
  </div>

  <div style='background:#f3e8ff;border:1px dashed #8b5cf6;border-radius:10px;padding:10px 14px;font-size:.83rem;color:#6d28d9;'>
    🏆 <strong>小論文比賽退件常見原因 (5)</strong>：全篇無頁首、學生報名的篇名跟內文頁首篇名不一致（14 條退件中的 2 條！）。
  </div>
</div>"""
},

{
    'id': 9, 'chapter': '第二章：文書進階排版（寫論文必備）', 'title': '表格、圖片、圖說編號',
    'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
    'html': """
<div class='slide-inner'>
  <h2 class='slide-title'>🖼️ 表格、圖片、圖說編號</h2>

  <div class='card-grid-2' style='margin-bottom:10px;'>
    <div style='background:#f0fdf4;border:1px solid #86efac;border-radius:12px;padding:14px;'>
      <div style='font-weight:700;color:#166534;font-size:.9rem;margin-bottom:8px;'>📊 表格：什麼時候用？</div>
      <div style='font-size:.8rem;color:#14532d;line-height:1.6;'>
        比較多項目、呈現數據時用。<br>
        <strong>操作</strong>：Word/Docs 都是「插入 → 表格 → 選欄列數」。<br>
        小論文中：研究方法列步驟、結果列數字。
      </div>
    </div>

    <div style='background:#eff6ff;border:1px solid #93c5fd;border-radius:12px;padding:14px;'>
      <div style='font-weight:700;color:#1e40af;font-size:.9rem;margin-bottom:8px;'>🖼️ 圖片：怎麼配文字？</div>
      <div style='font-size:.8rem;color:#1e3a8a;line-height:1.6;'>
        Word：插入圖片後選「文繞圖」→ 上下型或緊密型<br>
        Docs：插入圖片後選「內嵌／文字環繞／隔行」<br>
        小論文常用「上下型」較不會版面跑掉。
      </div>
    </div>
  </div>

  <div style='background:#fff7ed;border:1px solid #fdba74;border-radius:12px;padding:12px 14px;font-size:.85rem;color:#9a3412;line-height:1.6;'>
    <div style='font-weight:700;margin-bottom:6px;'>📌 圖說 & 表格編號（學術寫作標準）</div>
    <div>
      • 表格上方標「<strong>表 1</strong>：實驗組別分配」<br>
      • 圖片下方標「<strong>圖 1</strong>：實驗流程示意」<br>
      • 內文引用時要寫「（如表 1 所示）」——這樣讀者才知道你在講哪個圖表。
    </div>
    <div style='margin-top:6px;font-size:.75rem;color:#78350f;'>
      💡 Word 有「參考資料 → 插入標號」自動編號功能，比手動輸入好用。
    </div>
  </div>
</div>"""
},

{
    'id': 10, 'chapter': '第二章：文書進階排版（寫論文必備）', 'title': '🎯 第二章 隨堂測驗',
    'bg': 'teal', 'quiz': 'q2', 'chart': None, 'video': None,
    'html': """
<div style='text-align:center;padding:40px 20px;'>
  <div style='font-size:64px;margin-bottom:20px;'>🎯</div>
  <h1 style='font-size:2rem;font-weight:900;color:#fff;margin-bottom:12px;'>第二章 隨堂測驗</h1>
  <h2 style='font-size:1.1rem;font-weight:400;color:#a7f3d0;margin-bottom:24px;'>文書進階排版</h2>
  <p style='color:#e0f7fa;font-size:1rem;'>2 道題目，按「下一頁」開始作答！</p>
</div>"""
},

# ═══ 第三章：共同編輯與版本控制 ═══

{
    'id': 11, 'chapter': '第三章：共同編輯與版本控制', 'title': '即時協作：3 人同編一份文件',
    'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
    'html': """
<div class='slide-inner'>
  <h2 class='slide-title'>👥 即時協作：3 人同編一份文件</h2>
  <p class='slide-desc'>小組小論文寫作的救星——不再有「哪個是最新版」的困擾</p>

  <div style='background:#fef2f2;padding:10px 14px;border-radius:10px;margin-bottom:8px;border-left:4px solid #ef4444;'>
    <p style='color:#991b1b;font-weight:700;margin:0 0 4px;font-size:.85rem;'>😫 舊方法（傳統 Word 檔案傳來傳去）</p>
    <p style='color:#7f1d1d;font-size:.8rem;margin:0;'>小明改完傳給小華 → 小華改完再傳小美 → 最後搞不清楚「論文_v3_final_真的最終.docx」是哪一份 → 花 2 小時合併</p>
  </div>

  <div style='background:#f0fdf4;padding:10px 14px;border-radius:10px;margin-bottom:10px;border-left:4px solid #22c55e;'>
    <p style='color:#166534;font-weight:700;margin:0 0 4px;font-size:.85rem;'>✅ 新方法（Google Docs / Word Online 共用）</p>
    <p style='color:#14532d;font-size:.8rem;margin:0;'>3 人同時在同一份文件編輯，看到彼此游標顏色、留言討論、只有一份最新檔</p>
  </div>

  <div class='card-grid-2' style='margin-bottom:8px;'>
    <div style='background:#eff6ff;border:1px solid #93c5fd;border-radius:10px;padding:12px;'>
      <div style='font-weight:700;color:#1e40af;font-size:.85rem;margin-bottom:6px;'>📗 Google Docs 共用</div>
      <div style='font-size:.78rem;color:#1e3a8a;line-height:1.6;'>
        右上「共用」按鈕 → 加 email 或用連結<br>
        3 種權限：<strong>檢視 / 留言 / 編輯</strong>
      </div>
    </div>
    <div style='background:#fef3c7;border:1px solid #fbbf24;border-radius:10px;padding:12px;'>
      <div style='font-weight:700;color:#92400e;font-size:.85rem;margin-bottom:6px;'>📄 Word（要先存到 OneDrive）</div>
      <div style='font-size:.78rem;color:#78350f;line-height:1.6;'>
        右上「共用」按鈕 → 加 email 或連結<br>
        3 種權限：<strong>可檢視 / 可留言 / 可編輯</strong>
      </div>
    </div>
  </div>

  <div class='tip-box'>
    💡 <strong>共用給老師時</strong>選「可留言」而不是「可編輯」——老師能給建議但不會不小心動到你的原稿。
  </div>
</div>"""
},

{
    'id': 12, 'chapter': '第三章：共同編輯與版本控制', 'title': '版本歷史：救回誤刪的救命功能',
    'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
    'html': """
<div class='slide-inner'>
  <h2 class='slide-title'>🕰️ 版本歷史：救回誤刪的救命功能</h2>

  <div style='background:#fef2f2;border:1px solid #fca5a5;border-radius:10px;padding:12px 14px;margin-bottom:10px;'>
    <p style='color:#991b1b;font-weight:700;margin:0 0 4px;font-size:.88rem;'>📖 真實情境</p>
    <p style='color:#7f1d1d;font-size:.82rem;margin:0;line-height:1.6;'>
      期末小論文寫到一半，不小心選取整段刪掉、按了 Ctrl+S 儲存 → 5 秒後才發現 → 崩潰...
      沒關係，<strong>版本歷史</strong>可以救你！
    </p>
  </div>

  <div class='card-grid-2' style='margin-bottom:10px;'>
    <div style='background:#fef3c7;border:1px solid #fbbf24;border-radius:12px;padding:14px;'>
      <div style='font-weight:700;color:#92400e;font-size:.9rem;margin-bottom:6px;'>📄 Word（雲端版）</div>
      <div style='font-size:.8rem;color:#78350f;line-height:1.7;'>
        <strong>路徑</strong>：檔案 → 資訊 → 版本歷程記錄<br>
        <strong>特色</strong>：Word Online 每次自動存版本<br>
        <strong>限制</strong>：桌機純本機檔沒有此功能
      </div>
    </div>

    <div style='background:#eff6ff;border:1px solid #93c5fd;border-radius:12px;padding:14px;'>
      <div style='font-weight:700;color:#1e40af;font-size:.9rem;margin-bottom:6px;'>📗 Google Docs</div>
      <div style='font-size:.8rem;color:#1e3a8a;line-height:1.7;'>
        <strong>路徑</strong>：檔案 → 版本記錄 → 查看版本記錄<br>
        <strong>特色</strong>：每幾分鐘自動存一次<br>
        <strong>優點</strong>：可命名重要版本、還原一鍵完成
      </div>
    </div>
  </div>

  <div class='tip-box'>
    💡 <strong>寫完前建議</strong>：每完成一個章節，右鍵「命名此版本」，例如「文獻探討 v1 完成」——之後方便找回特定版本。
  </div>
</div>"""
},

{
    'id': 13, 'chapter': '第三章：共同編輯與版本控制', 'title': '建議模式 vs 追蹤修訂（老師改稿神器）',
    'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
    'html': """
<div class='slide-inner'>
  <h2 class='slide-title'>✏️ 建議模式 vs 追蹤修訂</h2>
  <p class='slide-desc'>老師改你的論文時，你想不想知道「他改了哪些字」？</p>

  <div class='card-grid-2' style='margin-bottom:12px;'>
    <div style='background:#eff6ff;border:1px solid #93c5fd;border-radius:12px;padding:14px;'>
      <div style='font-weight:700;color:#1e40af;font-size:.9rem;margin-bottom:8px;'>📗 Google Docs：建議模式</div>
      <div style='font-size:.8rem;color:#1e3a8a;line-height:1.7;'>
        右上角<strong>「編輯 → 建議」</strong>模式切換<br>
        修改文字會以 <span style='background:#fef3c7;padding:1px 4px;'>綠色建議</span> 顯示<br>
        原作者可 <strong>接受✓ / 拒絕✗</strong> 各項建議
      </div>
    </div>

    <div style='background:#fef3c7;border:1px solid #fbbf24;border-radius:12px;padding:14px;'>
      <div style='font-weight:700;color:#92400e;font-size:.9rem;margin-bottom:8px;'>📄 Word：追蹤修訂</div>
      <div style='font-size:.8rem;color:#78350f;line-height:1.7;'>
        「<strong>校閱</strong>」分頁 →「追蹤修訂」<br>
        修改內容以 <span style='background:#fee2e2;padding:1px 4px;'>紅色標記</span> 顯示<br>
        接受/拒絕修訂功能一模一樣
      </div>
    </div>
  </div>

  <div style='background:#f0fdf4;border-left:4px solid #22c55e;padding:10px 14px;border-radius:8px;font-size:.85rem;color:#15803d;'>
    💡 <strong>寫小論文時的最佳流程</strong>：
    <br>① 你自己寫初稿 → ② 開啟建議模式，共用給老師/同學 → ③ 他們給建議、你接受或拒絕 → ④ 全部處理完關閉建議模式，送出投稿。
  </div>
</div>"""
},

{
    'id': 14, 'chapter': '第三章：共同編輯與版本控制', 'title': '🎯 第三章 隨堂測驗',
    'bg': 'teal', 'quiz': 'q3', 'chart': None, 'video': None,
    'html': """
<div style='text-align:center;padding:40px 20px;'>
  <div style='font-size:64px;margin-bottom:20px;'>🎯</div>
  <h1 style='font-size:2rem;font-weight:900;color:#fff;margin-bottom:12px;'>第三章 隨堂測驗</h1>
  <h2 style='font-size:1.1rem;font-weight:400;color:#a7f3d0;margin-bottom:24px;'>共同編輯與版本控制</h2>
  <p style='color:#e0f7fa;font-size:1rem;'>2 道題目，按「下一頁」開始作答！</p>
</div>"""
},

# ═══ 第四章：小論文寫作實戰 ═══

{
    'id': 15, 'chapter': '第四章：小論文寫作實戰', 'title': '認識全國小論文比賽',
    'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
    'html': """
<div class='slide-inner'>
  <h2 class='slide-title'>🏆 認識 115 學年度全國高中小論文寫作比賽</h2>

  <div class='card-grid-3' style='margin-bottom:10px;'>
    <div style='background:linear-gradient(135deg,#eff6ff,#dbeafe);border:1px solid #93c5fd;border-radius:12px;padding:12px;'>
      <div style='font-size:1.5rem;margin-bottom:6px;text-align:center;'>📅</div>
      <div style='font-weight:700;color:#1e40af;text-align:center;font-size:.88rem;margin-bottom:4px;'>投稿時程</div>
      <div style='font-size:.75rem;color:#1e3a8a;line-height:1.6;'>
        <strong>第一學期</strong>：<br>115.09.01 – 10.15 中午 12 時<br>
        <strong>第二學期</strong>：<br>116.02.01 – 03.15 中午 12 時
      </div>
    </div>

    <div style='background:linear-gradient(135deg,#f0fdf4,#dcfce7);border:1px solid #86efac;border-radius:12px;padding:12px;'>
      <div style='font-size:1.5rem;margin-bottom:6px;text-align:center;'>🎓</div>
      <div style='font-weight:700;color:#166534;text-align:center;font-size:.88rem;margin-bottom:4px;'>21 個主題</div>
      <div style='font-size:.72rem;color:#14532d;line-height:1.6;'>
        工程技術、化學、文學、史地、生物、地球科學、法政、物理、英文寫作、家事、健康與護理、商業、國防、教育、資訊、農業、數學、藝術、體育、觀光餐旅、海事水產
      </div>
    </div>

    <div style='background:linear-gradient(135deg,#fef3c7,#fde68a);border:1px solid #fbbf24;border-radius:12px;padding:12px;'>
      <div style='font-size:1.5rem;margin-bottom:6px;text-align:center;'>🏅</div>
      <div style='font-weight:700;color:#92400e;text-align:center;font-size:.88rem;margin-bottom:4px;'>獎勵</div>
      <div style='font-size:.75rem;color:#78350f;line-height:1.6;'>
        依<strong>年級評分</strong>（高一有高一組）<br>
        分 <strong>特優 / 優等 / 甲等</strong><br>
        頒發獎狀，適合放學習歷程！
      </div>
    </div>
  </div>

  <div class='tip-box'>
    🌐 投稿網站：<a href='https://www.shs.edu.tw' target='_blank' style='color:#0d9488;font-weight:700;'>中學生網站 shs.edu.tw</a>　·　個人或小組（1–3 人同校同年級）皆可
  </div>
</div>"""
},

{
    'id': 16, 'chapter': '第四章：小論文寫作實戰', 'title': '小論文六大架構（必背！）',
    'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
    'html': """
<div class='slide-inner'>
  <h2 class='slide-title'>🏗️ 小論文六大架構（順序不能錯）</h2>
  <p class='slide-desc'>比賽退件的最常見原因之一：<strong>沒按六大架構、順序寫錯</strong></p>

  <div style='display:flex;flex-direction:column;gap:6px;margin-bottom:10px;'>
    <div style='background:#eff6ff;border-left:4px solid #3b82f6;border-radius:6px;padding:8px 12px;'>
      <div style='display:flex;align-items:center;gap:10px;'>
        <div style='background:#3b82f6;color:#fff;width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.85rem;flex-shrink:0;'>壹</div>
        <div style='flex:1;'>
          <div style='font-weight:700;color:#1e40af;font-size:.85rem;'>前言</div>
          <div style='font-size:.75rem;color:#374151;'>研究動機、研究目的、待答問題（<strong>Why 我要研究這個？</strong>）</div>
        </div>
      </div>
    </div>

    <div style='background:#f0fdf4;border-left:4px solid #22c55e;border-radius:6px;padding:8px 12px;'>
      <div style='display:flex;align-items:center;gap:10px;'>
        <div style='background:#22c55e;color:#fff;width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.85rem;flex-shrink:0;'>貳</div>
        <div style='flex:1;'>
          <div style='font-weight:700;color:#166534;font-size:.85rem;'>文獻探討</div>
          <div style='font-size:.75rem;color:#374151;'>別人做過的相關研究、目前知識現況（<strong>What 我知道什麼？</strong>）</div>
        </div>
      </div>
    </div>

    <div style='background:#fef3c7;border-left:4px solid #f59e0b;border-radius:6px;padding:8px 12px;'>
      <div style='display:flex;align-items:center;gap:10px;'>
        <div style='background:#f59e0b;color:#fff;width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.85rem;flex-shrink:0;'>參</div>
        <div style='flex:1;'>
          <div style='font-weight:700;color:#92400e;font-size:.85rem;'>研究方法</div>
          <div style='font-size:.75rem;color:#374151;'>你怎麼做這個研究：實驗/問卷/訪談/文獻分析（<strong>How 我怎麼做？</strong>）</div>
        </div>
      </div>
    </div>

    <div style='background:#faf5ff;border-left:4px solid #8b5cf6;border-radius:6px;padding:8px 12px;'>
      <div style='display:flex;align-items:center;gap:10px;'>
        <div style='background:#8b5cf6;color:#fff;width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.85rem;flex-shrink:0;'>肆</div>
        <div style='flex:1;'>
          <div style='font-weight:700;color:#6b21a8;font-size:.85rem;'>研究分析與結果</div>
          <div style='font-size:.75rem;color:#374151;'>資料整理、圖表呈現、找出模式（<strong>What 我發現了什麼？</strong>）</div>
        </div>
      </div>
    </div>

    <div style='background:#fef2f2;border-left:4px solid #ef4444;border-radius:6px;padding:8px 12px;'>
      <div style='display:flex;align-items:center;gap:10px;'>
        <div style='background:#ef4444;color:#fff;width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.85rem;flex-shrink:0;'>伍</div>
        <div style='flex:1;'>
          <div style='font-weight:700;color:#991b1b;font-size:.85rem;'>研究結論與建議</div>
          <div style='font-size:.75rem;color:#374151;'>回答前言的問題、給後續研究建議（<strong>So What 這代表什麼？</strong>）</div>
        </div>
      </div>
    </div>

    <div style='background:#f1f5f9;border-left:4px solid #64748b;border-radius:6px;padding:8px 12px;'>
      <div style='display:flex;align-items:center;gap:10px;'>
        <div style='background:#64748b;color:#fff;width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.85rem;flex-shrink:0;'>陸</div>
        <div style='flex:1;'>
          <div style='font-weight:700;color:#334155;font-size:.85rem;'>參考文獻</div>
          <div style='font-size:.75rem;color:#374151;'>列出所有引用過的資料，<strong>至少 3 篇</strong>（<strong>Who 我參考了誰？</strong>）</div>
        </div>
      </div>
    </div>
  </div>

  <div style='background:#fef2f2;border:1px solid #fca5a5;padding:8px 12px;border-radius:8px;font-size:.8rem;color:#991b1b;'>
    ⚠️ <strong>順序錯誤或缺一項</strong> → 校內初選就會被刪除，連參賽資格都沒有！
  </div>
</div>"""
},

{
    'id': 17, 'chapter': '第四章：小論文寫作實戰', 'title': '格式規範一覽',
    'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
    'html': """
<div class='slide-inner'>
  <h2 class='slide-title'>📐 格式規範一覽（看仔細！）</h2>

  <table class='info-table' style='font-size:.82rem;margin-bottom:10px;'>
    <thead class='table-header'>
      <tr><th style='width:26%;'>項目</th><th>規定</th></tr>
    </thead>
    <tbody>
      <tr><td><strong>紙張</strong></td><td>A4 直式</td></tr>
      <tr class='tr-highlight'><td><strong>篇幅</strong></td><td><strong>4–10 頁</strong>（少於 4 頁或多於 10 頁都退件）</td></tr>
      <tr><td><strong>檔案格式</strong></td><td><strong>PDF</strong>（Word/Docs 寫完匯出）</td></tr>
      <tr class='tr-highlight'><td><strong>檔案大小</strong></td><td><strong>不超過 5 MB</strong>（含圖檔）</td></tr>
      <tr><td><strong>封面</strong></td><td><strong>不做封面頁！</strong>（上傳作品「不含」封面）</td></tr>
      <tr class='tr-highlight'><td><strong>頁首</strong></td><td>全篇要有頁首，且與投稿篇名<strong>一致</strong></td></tr>
      <tr><td><strong>語言</strong></td><td>中文或英文皆可（英文請用 I. Introduction 等六大架構）</td></tr>
      <tr class='tr-highlight'><td><strong>參與者</strong></td><td>個人 or 小組（1–3 人，須同校同年級）</td></tr>
      <tr><td><strong>身分揭露</strong></td><td>題目、內文、附錄<strong>不得</strong>出現作者姓名、學號（校名 OK）</td></tr>
      <tr class='tr-highlight'><td><strong>每人上限</strong></td><td>每人每次限投稿 <strong>1 篇</strong></td></tr>
    </tbody>
  </table>

  <div style='background:#fff7ed;border:1px solid #fdba74;border-radius:8px;padding:8px 12px;font-size:.8rem;color:#9a3412;'>
    💡 <strong>技巧</strong>：Word 有「檢查文件」功能可以自動找出格式問題；投稿前務必<strong>用 PDF 開一次</strong>確認頁首/頁碼/字體正確顯示。
  </div>
</div>"""
},

{
    'id': 18, 'chapter': '第四章：小論文寫作實戰', 'title': '引註與 APA 參考文獻格式',
    'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
    'html': """
<div class='slide-inner'>
  <h2 class='slide-title'>📚 引註與 APA 參考文獻格式</h2>

  <div class='card-grid-2' style='margin-bottom:10px;'>
    <div style='background:#eff6ff;border:1px solid #93c5fd;border-radius:10px;padding:12px;'>
      <div style='font-weight:700;color:#1e40af;font-size:.88rem;margin-bottom:6px;'>✅ 可以引用</div>
      <ul style='font-size:.78rem;color:#1e3a8a;line-height:1.7;padding-left:16px;margin:0;'>
        <li>學術期刊論文</li>
        <li>學位論文（碩博士）</li>
        <li>正式出版書籍</li>
        <li>政府機關研究報告</li>
        <li>新聞媒體、專業網站</li>
      </ul>
    </div>
    <div style='background:#fef2f2;border:1px solid #fca5a5;border-radius:10px;padding:12px;'>
      <div style='font-weight:700;color:#991b1b;font-size:.88rem;margin-bottom:6px;'>❌ 禁止引用</div>
      <ul style='font-size:.78rem;color:#7f1d1d;line-height:1.7;padding-left:16px;margin:0;'>
        <li>PTT、Dcard 等討論區</li>
        <li>Yahoo 知識家等問答網站</li>
        <li>LINE 群組、聊天訊息</li>
        <li>ChatGPT 對話內容</li>
        <li>維基百科（可引用其「參考資料」）</li>
      </ul>
    </div>
  </div>

  <div style='background:#f0fdf4;border:1px solid #86efac;border-radius:10px;padding:10px 14px;font-size:.78rem;color:#14532d;margin-bottom:8px;'>
    <div style='font-weight:700;color:#166534;margin-bottom:6px;'>📖 APA 格式範例（參考文獻至少 3 篇）</div>
    <div style='background:#fff;padding:8px 10px;border-radius:6px;margin-bottom:4px;font-family:monospace;font-size:.7rem;line-height:1.6;'>
      <strong>期刊</strong>：陳志明（2023）。生成式 AI 對高中生學習的影響。<em>教育研究月刊</em>，350，1-15。
    </div>
    <div style='background:#fff;padding:8px 10px;border-radius:6px;margin-bottom:4px;font-family:monospace;font-size:.7rem;line-height:1.6;'>
      <strong>書籍</strong>：林秀華（2022）。<em>資訊素養教學實務</em>。台北：五南。
    </div>
    <div style='background:#fff;padding:8px 10px;border-radius:6px;font-family:monospace;font-size:.7rem;line-height:1.6;'>
      <strong>網頁</strong>：教育部（2024）。<em>115 學年度小論文比賽實施計畫</em>。取自 https://www.shs.edu.tw
    </div>
  </div>

  <div class='tip-box'>
    💡 <strong>內文引註</strong>：寫「陳志明（2023）指出...」或「有研究發現...（陳志明，2023）」——把作者和年份標出來。
  </div>
</div>"""
},

{
    'id': 19, 'chapter': '第四章：小論文寫作實戰', 'title': 'AI 使用界線（重要！）',
    'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
    'html': """
<div class='slide-inner'>
  <h2 class='slide-title'>🤖 AI 使用界線</h2>
  <p class='slide-desc'>115 學年比賽明訂：<strong>文章內容不得由 AI 生成</strong>，違規會被停權</p>

  <div class='card-grid-2' style='margin-bottom:10px;'>
    <div style='background:linear-gradient(135deg,#f0fdf4,#dcfce7);border:2px solid #22c55e;border-radius:12px;padding:14px;'>
      <div style='font-weight:700;color:#166534;font-size:.95rem;margin-bottom:8px;'>✅ 可以用 AI 做這些</div>
      <ul style='font-size:.82rem;color:#14532d;line-height:1.8;padding-left:16px;margin:0;'>
        <li><strong>發想主題</strong>：「請給我 5 個關於水質檢測的研究方向」</li>
        <li><strong>找關鍵字</strong>幫你搜文獻</li>
        <li><strong>解釋概念</strong>：不懂的專業詞問 AI</li>
        <li><strong>檢查文法錯字</strong>（不含改寫段落）</li>
      </ul>
    </div>

    <div style='background:linear-gradient(135deg,#fef2f2,#fee2e2);border:2px solid #ef4444;border-radius:12px;padding:14px;'>
      <div style='font-weight:700;color:#991b1b;font-size:.95rem;margin-bottom:8px;'>❌ 絕對禁止用 AI</div>
      <ul style='font-size:.82rem;color:#7f1d1d;line-height:1.8;padding-left:16px;margin:0;'>
        <li>AI 生成<strong>摘要</strong>、內文段落</li>
        <li>AI <strong>改寫</strong>你的文字（洗稿）</li>
        <li>AI 生成<strong>圖表、圖片</strong></li>
        <li>AI 生成<strong>參考文獻</strong>（會編假的）</li>
      </ul>
    </div>
  </div>

  <div style='background:#fff7ed;border:1px solid #fdba74;border-radius:10px;padding:10px 14px;font-size:.82rem;color:#9a3412;'>
    <div style='font-weight:700;color:#7c2d12;margin-bottom:4px;'>🚨 違規後果</div>
    <div style='line-height:1.6;'>
      1. 校內初選就會被刪除，無法參加全國賽<br>
      2. 得獎後被發現 → 取消得獎資格、追回獎狀<br>
      3. 累積 <strong>2 次違規 → 永久停權</strong>（未來所有屆都不能投稿）<br>
      4. 學校可能記過處分
    </div>
  </div>
</div>"""
},

{
    'id': 20, 'chapter': '第四章：小論文寫作實戰', 'title': '14 條常見退件原因',
    'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
    'html': """
<div class='slide-inner'>
  <h2 class='slide-title'>⚠️ 14 條常見退件原因（附件 1 摘要）</h2>
  <p class='slide-desc'>投稿前用這個清單自我檢查——很多同學就是因為這些小地方被刷掉！</p>

  <div style='display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:10px;font-size:.75rem;'>
    <div style='background:#fef2f2;padding:6px 10px;border-radius:6px;border-left:3px solid #ef4444;'>❌ 1. 檔案無法開啟</div>
    <div style='background:#fef2f2;padding:6px 10px;border-radius:6px;border-left:3px solid #ef4444;'>❌ 2. 作者資料錯（超過 3 人 or 不同年級）</div>
    <div style='background:#fef2f2;padding:6px 10px;border-radius:6px;border-left:3px solid #ef4444;'>❌ 3. 年級錯誤</div>
    <div style='background:#fef2f2;padding:6px 10px;border-radius:6px;border-left:3px solid #ef4444;'>❌ 4. 上傳作品含封面頁</div>
    <div style='background:#fef2f2;padding:6px 10px;border-radius:6px;border-left:3px solid #ef4444;'>❌ 5. 全篇無頁首</div>
    <div style='background:#fef2f2;padding:6px 10px;border-radius:6px;border-left:3px solid #ef4444;'>❌ 6. 報名篇名與內文頁首不一致</div>
    <div style='background:#fef2f2;padding:6px 10px;border-radius:6px;border-left:3px solid #ef4444;'>❌ 7. 沒按六大架構順序寫</div>
    <div style='background:#fef2f2;padding:6px 10px;border-radius:6px;border-left:3px solid #ef4444;'>❌ 8. 一人投稿超過 1 篇</div>
    <div style='background:#fef2f2;padding:6px 10px;border-radius:6px;border-left:3px solid #ef4444;'>❌ 9. 篇幅少於 4 頁 or 超過 10 頁</div>
    <div style='background:#fef2f2;padding:6px 10px;border-radius:6px;border-left:3px solid #ef4444;'>❌ 10. 參考文獻少於 3 篇</div>
    <div style='background:#fef2f2;padding:6px 10px;border-radius:6px;border-left:3px solid #ef4444;'>❌ 11. 已在校外出版、獲獎、一稿多投</div>
    <div style='background:#fef2f2;padding:6px 10px;border-radius:6px;border-left:3px solid #ef4444;'>❌ 12. 內容由 AI 工具生成</div>
    <div style='background:#fef2f2;padding:6px 10px;border-radius:6px;border-left:3px solid #ef4444;'>❌ 13. 涉及抄襲</div>
    <div style='background:#fef2f2;padding:6px 10px;border-radius:6px;border-left:3px solid #ef4444;'>❌ 14. 出現作者身分資料（含照片，校名例外）</div>
  </div>

  <div class='tip-box'>
    💡 用「校內初選檢核表」逐條打勾，投稿前一定要自己確認過一遍！
  </div>
</div>"""
},

{
    'id': 21, 'chapter': '第四章：小論文寫作實戰', 'title': '🎯 第四章 隨堂測驗',
    'bg': 'teal', 'quiz': 'q4', 'chart': None, 'video': None,
    'html': """
<div style='text-align:center;padding:40px 20px;'>
  <div style='font-size:64px;margin-bottom:20px;'>🎯</div>
  <h1 style='font-size:2rem;font-weight:900;color:#fff;margin-bottom:12px;'>第四章 隨堂測驗</h1>
  <h2 style='font-size:1.1rem;font-weight:400;color:#a7f3d0;margin-bottom:24px;'>小論文寫作重點</h2>
  <p style='color:#e0f7fa;font-size:1rem;'>2 道題目，按「下一頁」開始作答！</p>
</div>"""
},

# ═══ 第五章：電腦軟體應用丙級 ═══

{
    'id': 22, 'chapter': '第五章：電腦軟體應用丙級', 'title': '電腦軟體應用丙級是什麼？',
    'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
    'html': """
<div class='slide-inner'>
  <h2 class='slide-title'>🏅 電腦軟體應用丙級技術士</h2>
  <p class='slide-desc'>勞動部發的<strong>國家級證照</strong>，高中生就能考、通過率約 60-70%</p>

  <div class='card-grid-3' style='margin-bottom:10px;'>
    <div style='background:#eff6ff;border:1px solid #93c5fd;border-radius:12px;padding:12px;'>
      <div style='font-size:1.5rem;margin-bottom:6px;text-align:center;'>📚</div>
      <div style='font-weight:700;color:#1e40af;text-align:center;font-size:.88rem;margin-bottom:4px;'>考什麼</div>
      <div style='font-size:.72rem;color:#1e3a8a;line-height:1.6;'>
        <strong>學科</strong>：80 題選擇題（80 分及格）<br>
        &nbsp;&nbsp;· 電腦基本知識<br>
        &nbsp;&nbsp;· 資訊倫理與安全<br>
        &nbsp;&nbsp;· Office 操作原理<br>
        <strong>術科</strong>：4 題實作（60 分及格）<br>
        &nbsp;&nbsp;· Windows 操作<br>
        &nbsp;&nbsp;· Word 排版<br>
        &nbsp;&nbsp;· Excel 試算<br>
        &nbsp;&nbsp;· PowerPoint 簡報
      </div>
    </div>

    <div style='background:#f0fdf4;border:1px solid #86efac;border-radius:12px;padding:12px;'>
      <div style='font-size:1.5rem;margin-bottom:6px;text-align:center;'>💰</div>
      <div style='font-weight:700;color:#166534;text-align:center;font-size:.88rem;margin-bottom:4px;'>報名資訊</div>
      <div style='font-size:.72rem;color:#14532d;line-height:1.6;'>
        <strong>報名費</strong>：約 NT$ 1,470<br>
        <strong>年紀限制</strong>：無（國中以上都可）<br>
        <strong>報名網址</strong>：<br>
        技能檢定中心 <a href='https://skill.tcte.edu.tw/' target='_blank' style='color:#166534;font-size:.72rem;'>skill.tcte.edu.tw</a><br>
        <strong>考試日期</strong>：<br>
        每年 3 月、7 月、11 月<br>
        <strong>成績公告</strong>：<br>
        考後約 4-6 週
      </div>
    </div>

    <div style='background:#fef3c7;border:1px solid #fbbf24;border-radius:12px;padding:12px;'>
      <div style='font-size:1.5rem;margin-bottom:6px;text-align:center;'>🎯</div>
      <div style='font-weight:700;color:#92400e;text-align:center;font-size:.88rem;margin-bottom:4px;'>對高中生的價值</div>
      <div style='font-size:.72rem;color:#78350f;line-height:1.6;'>
        ✅ <strong>學習歷程檔案</strong>加分項<br>
        ✅ <strong>四技二專推甄</strong>證照可加分<br>
        ✅ <strong>統測</strong>資訊類考試打底<br>
        ✅ <strong>履歷</strong>基本標配<br>
        ✅ 打工也用得到<br>
        <br>
        📈 全國每年考生<br>&nbsp;&nbsp;<strong>超過 4 萬人</strong>
      </div>
    </div>
  </div>

  <div class='tip-box'>
    💡 <strong>好消息</strong>：Ch04 你已經學了 Word 段落樣式、頁首頁碼、目錄——這些都是丙級 Word 術科的必考技能！接下來看看實際題型長什麼樣。
  </div>
</div>"""
},

{
    'id': 23, 'chapter': '第五章：電腦軟體應用丙級', 'title': '丙級術科 Word 題型範例',
    'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
    'html': """
<div class='slide-inner'>
  <h2 class='slide-title'>📝 丙級術科 Word 題型範例</h2>
  <p class='slide-desc'>術科題目會給你一份文件檔和範本圖，要你在時間內排出跟範本一模一樣的文件</p>

  <div class='card-grid-2' style='margin-bottom:10px;'>
    <div style='background:#eff6ff;border:1px solid #93c5fd;border-radius:12px;padding:14px;'>
      <div style='font-weight:700;color:#1e40af;font-size:.9rem;margin-bottom:8px;'>🎯 常見要求（要能做到）</div>
      <ul style='font-size:.78rem;color:#1e3a8a;line-height:1.7;padding-left:18px;margin:0;'>
        <li>指定<strong>字型、字級、行距</strong>（中/英文分別設定）</li>
        <li>套用<strong>段落樣式</strong>（標題 1、標題 2）</li>
        <li>插入<strong>頁首、頁尾與頁碼</strong></li>
        <li>製作<strong>自動目錄</strong>（含更新）</li>
        <li>插入<strong>表格</strong>並套用格式</li>
        <li>插入<strong>圖片</strong>與文繞圖設定</li>
        <li>插入<strong>頁次分隔</strong>與<strong>分欄</strong></li>
        <li>使用<strong>項目符號</strong>或編號清單</li>
      </ul>
    </div>

    <div style='background:#fef3c7;border:1px solid #fbbf24;border-radius:12px;padding:14px;'>
      <div style='font-weight:700;color:#92400e;font-size:.9rem;margin-bottom:8px;'>⏱️ 考試技巧</div>
      <ul style='font-size:.78rem;color:#78350f;line-height:1.7;padding-left:18px;margin:0;'>
        <li>術科每題約 <strong>30-40 分鐘</strong>，時間很緊</li>
        <li>熟記<strong>常用快捷鍵</strong>（Ctrl+B/I/U/S、Ctrl+Alt+1/2）</li>
        <li>先做好<strong>樣式定義</strong>，全文才會一致</li>
        <li>先套目錄樣式再做其他，最後更新目錄</li>
        <li><strong>存檔頻繁！</strong>Ctrl+S 每 5 分鐘按一次</li>
        <li>邊做邊<strong>對照範本圖</strong>（不要漏做任何一項）</li>
      </ul>
    </div>
  </div>

  <div style='background:linear-gradient(135deg,#faf5ff,#ede9fe);border:1px solid #c4b5fd;border-radius:10px;padding:10px 14px;font-size:.82rem;color:#6d28d9;'>
    📚 <strong>術科題目公開！</strong>技能檢定中心會公布歷屆題目，可到
    <a href='https://skill.tcte.edu.tw/' target='_blank' style='color:#6d28d9;font-weight:700;'>skill.tcte.edu.tw</a>
    的「學/術科題庫」下載練習。<strong>術科題目考前就會公開範圍</strong>，準備得夠熟就能過。
  </div>

  <div class='tip-box'>
    🎓 <strong>加分挑戰</strong>：這學期把 Word 部分練熟 → 期末大報告用得到 → 高一結束後暑假報名 3 月考試 → 高二上手拿證書！
  </div>
</div>"""
},

# ═══ 個人實作 ═══

{
    'id': 24, 'chapter': '個人實作', 'title': '個人實作：丙級 Word 術科模擬',
    'bg': 'teal', 'quiz': None, 'chart': None, 'video': None,
    'html': """
<h2 style='font-size:1.6rem;font-weight:800;color:#fff;margin-bottom:10px;text-align:center;'>📝 個人實作：丙級 Word 術科模擬題</h2>
<p style='color:#cffafe;text-align:center;font-size:.88rem;margin-bottom:12px;'>
  每人獨立完成一份 Word 排版作品（3-4 頁）· 用 <strong>電腦教室桌機 Word</strong> 或自己的 <strong>Office 365 / Google Docs</strong> 都可
</p>

<div style='display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:8px;'>
  <div style='background:rgba(255,255,255,0.12);padding:12px;border-radius:12px;'>
    <h3 style='color:#fff;font-size:.92rem;margin-bottom:8px;'>📋 題目：仿照範本排版</h3>
    <p style='color:#cffafe;font-size:.75rem;margin:0 0 8px;line-height:1.5;'>
      老師會發一份「原始文字檔」+「範本 PDF」，你要把文字檔排成跟範本一模一樣。
    </p>

    <p style='color:#fde68a;font-size:.75rem;margin:6px 0 4px;font-weight:700;'>🎯 必做項目（每項都要有）：</p>
    <div style='display:flex;flex-direction:column;gap:4px;font-size:.72rem;'>
      <div style='background:rgba(34,197,94,0.25);border-left:3px solid #86efac;padding:6px 9px;border-radius:5px;color:#fff;'>① 標題套「<strong>標題 1</strong>」樣式</div>
      <div style='background:rgba(34,197,94,0.25);border-left:3px solid #86efac;padding:6px 9px;border-radius:5px;color:#fff;'>② 次標題套「<strong>標題 2</strong>」樣式</div>
      <div style='background:rgba(34,197,94,0.25);border-left:3px solid #86efac;padding:6px 9px;border-radius:5px;color:#fff;'>③ 插入<strong>自動目錄</strong>於首頁</div>
      <div style='background:rgba(34,197,94,0.25);border-left:3px solid #86efac;padding:6px 9px;border-radius:5px;color:#fff;'>④ 加<strong>頁首</strong>（打自己的名字或指定文字）</div>
      <div style='background:rgba(34,197,94,0.25);border-left:3px solid #86efac;padding:6px 9px;border-radius:5px;color:#fff;'>⑤ 加<strong>頁碼</strong>（頁底置中）</div>
      <div style='background:rgba(34,197,94,0.25);border-left:3px solid #86efac;padding:6px 9px;border-radius:5px;color:#fff;'>⑥ 至少 1 個<strong>表格</strong>（3 欄 3 列以上）</div>
      <div style='background:rgba(34,197,94,0.25);border-left:3px solid #86efac;padding:6px 9px;border-radius:5px;color:#fff;'>⑦ 至少 1 張<strong>圖片</strong>（含圖說）</div>
      <div style='background:rgba(34,197,94,0.25);border-left:3px solid #86efac;padding:6px 9px;border-radius:5px;color:#fff;'>⑧ 使用<strong>項目符號</strong>或<strong>編號清單</strong></div>
      <div style='background:rgba(34,197,94,0.25);border-left:3px solid #86efac;padding:6px 9px;border-radius:5px;color:#fff;'>⑨ 中文<strong>細明體 12pt</strong>、英文 <strong>Times New Roman 12pt</strong>、行距 1.5</div>
      <div style='background:rgba(34,197,94,0.25);border-left:3px solid #86efac;padding:6px 9px;border-radius:5px;color:#fff;'>⑩ 匯出為 <strong>PDF</strong> 上傳</div>
    </div>
  </div>

  <div>
    <div style='background:rgba(255,255,255,0.12);padding:12px;border-radius:12px;margin-bottom:8px;'>
      <h3 style='color:#fff;font-size:.92rem;margin-bottom:6px;'>📊 評分規準（100 分）</h3>
      <table style='width:100%;font-size:.72rem;color:#e0f7fa;border-collapse:collapse;'>
        <tr style='background:rgba(255,255,255,0.15);'><th style='padding:4px 6px;text-align:left;'>項目</th><th style='padding:4px 6px;text-align:center;'>配分</th></tr>
        <tr><td style='padding:4px 6px;'>段落樣式 + 目錄</td><td style='padding:4px 6px;text-align:center;color:#fde68a;font-weight:700;'>25</td></tr>
        <tr><td style='padding:4px 6px;'>頁首 + 頁碼</td><td style='padding:4px 6px;text-align:center;color:#fde68a;font-weight:700;'>15</td></tr>
        <tr><td style='padding:4px 6px;'>表格 + 圖片圖說</td><td style='padding:4px 6px;text-align:center;color:#fde68a;font-weight:700;'>20</td></tr>
        <tr><td style='padding:4px 6px;'>字型/字級/行距正確</td><td style='padding:4px 6px;text-align:center;color:#fde68a;font-weight:700;'>15</td></tr>
        <tr><td style='padding:4px 6px;'>項目符號/清單</td><td style='padding:4px 6px;text-align:center;color:#fde68a;font-weight:700;'>10</td></tr>
        <tr><td style='padding:4px 6px;'>PDF 匯出正確</td><td style='padding:4px 6px;text-align:center;color:#fde68a;font-weight:700;'>10</td></tr>
        <tr><td style='padding:4px 6px;'>整體版面美觀</td><td style='padding:4px 6px;text-align:center;color:#fde68a;font-weight:700;'>5</td></tr>
        <tr><td style='padding:4px 6px;'>加分：小論文主題發想單</td><td style='padding:4px 6px;text-align:center;color:#a7f3d0;font-weight:700;'>+5</td></tr>
      </table>
    </div>

    <div style='background:rgba(255,255,255,0.12);padding:10px 12px;border-radius:10px;font-size:.75rem;color:#cffafe;line-height:1.6;margin-bottom:6px;'>
      <p style='color:#fff;font-weight:700;margin:0 0 3px;font-size:.82rem;'>🗓️ 時程</p>
      第 1 節：老師發題目 + 個人開始排版<br>
      第 2 節：完成 → 匯出 PDF → 上傳 Google Classroom
    </div>

    <div style='background:rgba(168,85,247,0.25);border-left:3px solid #d8b4fe;padding:8px 12px;border-radius:8px;font-size:.75rem;color:#f3e8ff;line-height:1.6;'>
      <p style='color:#fff;font-weight:700;margin:0 0 3px;font-size:.82rem;'>⭐ 加分挑戰（+5 分）</p>
      交一份 <strong>「我想寫的小論文主題發想單」</strong>（1 頁）：
      主題方向、想解決什麼問題、初步想到的做法。
      <strong>期末大報告會做完整小論文</strong>，先想早點準備。
    </div>
  </div>
</div>

<div style='background:rgba(255,255,255,0.08);padding:8px 12px;border-radius:8px;margin-top:8px;font-size:.75rem;color:#cffafe;'>
  💡 <strong>期末預告</strong>：學完 Ch08 大數據、Ch09 資料分析後，期末個人大報告會寫一篇<strong>真正的小論文</strong>——用到今天學的六大架構、格式規範，加上你會的數據分析技能。今天先把工具練熟！
</div>"""
},

{
    'id': 25, 'chapter': '個人實作', 'title': 'Word / Docs 匯出 PDF 教學',
    'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
    'html': """
<div class='slide-inner'>
  <h2 class='slide-title'>💾 Word / Docs 匯出 PDF 教學</h2>
  <p class='slide-desc'>小論文比賽只接受 <strong>PDF 檔</strong>，其他格式一律退件</p>

  <div class='card-grid-2' style='margin-bottom:10px;'>
    <div style='background:#eff6ff;border:1px solid #93c5fd;border-radius:12px;padding:14px;'>
      <div style='font-weight:700;color:#1e40af;font-size:.9rem;margin-bottom:8px;'>📄 Microsoft Word</div>
      <div style='font-size:.8rem;color:#1e3a8a;line-height:1.7;'>
        <strong>步驟</strong>：<br>
        ① 檔案 → 另存新檔<br>
        ② 選存檔位置<br>
        ③ 「存檔類型」下拉選 <strong>PDF (*.pdf)</strong><br>
        ④ 點「儲存」
      </div>
      <div style='background:#fff;border:1px solid #bfdbfe;border-radius:6px;padding:6px 10px;margin-top:8px;font-size:.72rem;color:#6b7280;'>
        💡 快捷鍵：<code>F12</code> → 快速另存新檔
      </div>
    </div>

    <div style='background:#fef3c7;border:1px solid #fbbf24;border-radius:12px;padding:14px;'>
      <div style='font-weight:700;color:#92400e;font-size:.9rem;margin-bottom:8px;'>📗 Google Docs</div>
      <div style='font-size:.8rem;color:#78350f;line-height:1.7;'>
        <strong>步驟</strong>：<br>
        ① 檔案 → 下載<br>
        ② 選 <strong>PDF 文件 (.pdf)</strong><br>
        ③ 自動下載到你的下載資料夾
      </div>
      <div style='background:#fff;border:1px solid #fde68a;border-radius:6px;padding:6px 10px;margin-top:8px;font-size:.72rem;color:#6b7280;'>
        💡 想再改？回到 Google Docs 就好，下載出去的 PDF 就是完成品
      </div>
    </div>
  </div>

  <div style='background:#f0fdf4;border-left:4px solid #22c55e;padding:10px 14px;border-radius:8px;font-size:.85rem;color:#15803d;'>
    ✅ <strong>檢查清單</strong>：
    <div style='display:grid;grid-template-columns:1fr 1fr;gap:4px;margin-top:6px;font-size:.78rem;'>
      <div>☐ 頁首出現在每一頁</div>
      <div>☐ 頁碼連續正確</div>
      <div>☐ 目錄顯示無誤</div>
      <div>☐ 圖表沒有跑版</div>
      <div>☐ 中文沒有變亂碼</div>
      <div>☐ 總頁數 4-10 頁</div>
    </div>
  </div>

  <div class='tip-box' style='margin-top:8px;'>
    ⚠️ 匯出後<strong>一定要用 PDF 開一次</strong>檢查！有時候字型、圖片位置在 PDF 會跑掉。
  </div>
</div>"""
},

{
    'id': 26, 'chapter': '個人實作', 'title': '結尾：從工具到創作',
    'bg': 'navy', 'quiz': None, 'chart': None, 'video': None,
    'html': """
<div style='text-align:center;padding:30px 20px;'>
  <div style='font-size:64px;margin-bottom:20px;'>🎓</div>
  <h1 style='font-size:2.2rem;font-weight:900;color:#fff;margin-bottom:12px;'>從工具到創作</h1>
  <h2 style='font-size:1.2rem;font-weight:400;color:#93c5fd;margin-bottom:24px;'>你已具備寫出一篇小論文的所有技能</h2>

  <div style='display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:12px;max-width:700px;margin:0 auto 24px;'>
    <div style='background:rgba(255,255,255,0.1);padding:12px;border-radius:10px;'>
      <div style='font-size:1.8rem;margin-bottom:4px;'>📄</div>
      <div style='color:#e0f2fe;font-size:.85rem;'>Word / Docs 雙軌</div>
    </div>
    <div style='background:rgba(255,255,255,0.1);padding:12px;border-radius:10px;'>
      <div style='font-size:1.8rem;margin-bottom:4px;'>🏷️</div>
      <div style='color:#e0f2fe;font-size:.85rem;'>段落樣式 + 自動目錄</div>
    </div>
    <div style='background:rgba(255,255,255,0.1);padding:12px;border-radius:10px;'>
      <div style='font-size:1.8rem;margin-bottom:4px;'>👥</div>
      <div style='color:#e0f2fe;font-size:.85rem;'>共同編輯與版本控制</div>
    </div>
    <div style='background:rgba(255,255,255,0.1);padding:12px;border-radius:10px;'>
      <div style='font-size:1.8rem;margin-bottom:4px;'>🏆</div>
      <div style='color:#e0f2fe;font-size:.85rem;'>小論文六大架構</div>
    </div>
  </div>

  <div style='background:rgba(255,255,255,0.1);padding:16px 20px;border-radius:12px;max-width:640px;margin:0 auto 20px;'>
    <p style='color:#fef3c7;font-size:1.1rem;font-weight:700;margin:0 0 6px;'>🚀 挑戰自己：報名 115 學年小論文比賽</p>
    <p style='color:#e2e8f0;font-size:.9rem;margin:0;line-height:1.6;'>
      第一學期截止：<strong>115.10.15 中午 12 時</strong><br>
      投稿網站：<a href='https://www.shs.edu.tw' target='_blank' style='color:#93c5fd;'>shs.edu.tw</a><br>
      得獎可放進學習歷程，是升學備審的加分武器！
    </p>
  </div>

  <p style='color:#94a3b8;font-size:.9rem;font-style:italic;'>
    「文書工具是骨架，思考與研究才是靈魂。」
  </p>
</div>"""
},

]
