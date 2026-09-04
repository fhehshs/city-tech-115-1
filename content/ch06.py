# -*- coding: utf-8 -*-
# Ch.5: 合併列印與表單應用

CHAPTERS = [
    {'name': '封面', 'start': 1},
    {'name': '第一章：合併列印概念', 'start': 2},
    {'name': '第二章：合併列印實作', 'start': 8},
    {'name': '第三章：Google 表單設計', 'start': 14},
    {'name': '第四章：問卷資料分析', 'start': 19},
    {'name': '分組實作', 'start': 23},
]

QUIZZES = {
    'q1': {
        'title': '第一章 隨堂測驗',
        'questions': [
            {
                'q': '合併列印（Mail Merge）的主要用途是什麼？',
                'options': ['將多份文件合併成一份', '自動寄送電子郵件給所有聯絡人', '將固定格式文件與資料來源結合，批次產生個人化文件', '將試算表資料轉換為文件格式'],
                'answer': 2,
                'explain': '合併列印讓你用一份「範本」文件（含佔位符），加上一份「資料來源」（如 Excel 或 Google 試算表），批次產生幾百份個人化文件。例如：學生成績通知單、活動邀請函、大量信封地址。'
            },
            {
                'q': '合併列印中，「資料來源」通常是什麼格式？',
                'options': ['純文字檔案（.txt）', '試算表或資料庫（如 Excel、Google 試算表）', 'PDF 文件', 'Word 文件本身'],
                'answer': 1,
                'explain': '合併列印的資料來源需要結構化的表格資料，最常用的是 Excel（.xlsx）或 Google 試算表。第一列通常是欄位名稱（如姓名、地址），之後每列是一筆記錄，對應一份輸出文件。'
            },
        ]
    },
    'q2': {
        'title': '第二章 隨堂測驗',
        'questions': [
            {
                'q': '在 Word 合併列印中，「功能變數」（佔位符）的格式是？',
                'options': ['{欄位名稱}', '[欄位名稱]', '${欄位名稱}', '《《欄位名稱》》'],
                'answer': 3,
                'explain': 'Word 合併列印使用《《功能變數》》符號（也稱 «欄位名稱»）作為佔位符。例如在範本中寫「親愛的《《姓名》》同學」，合併時《《姓名》》會被資料來源的實際姓名替換。'
            },
            {
                'q': '使用合併列印產生信封時，需要特別注意什麼？',
                'options': ['收件人地址格式要符合中華郵政規定，包括郵遞區號位置', '信封上不能印彩色圖案', '只能用 A4 紙張列印', '收件人和寄件人欄位必須用不同字體'],
                'answer': 0,
                'explain': '中華郵政規定信封的郵遞區號框需在特定位置，地址書寫格式為「縣市→區→路→號」。合併列印信封時要確認郵遞區號欄位已包含在資料中，且框的位置符合郵政規範。'
            },
        ]
    },
    'q3': {
        'title': '第三章 隨堂測驗',
        'questions': [
            {
                'q': 'Google 表單中，「必填」選項的作用是？',
                'options': ['限制只有特定人才能填寫此題', '若此題未填寫，表單無法提交', '自動顯示提示文字', '限制填寫次數'],
                'answer': 1,
                'explain': '將題目設定為「必填」後，填寫者若跳過此題，點擊提交時會出現錯誤提示，無法送出表單。這確保你能收集到所有必要的資訊。適合用在不可或缺的問題，但不要所有題目都必填，以免降低填寫意願。'
            },
            {
                'q': 'Google 表單的哪種題型最適合讓填寫者「從多個選項中只選一個」？',
                'options': ['核取方塊（可複選）', '下拉式選單（最多選一）', '單選題（選項按鈕）', '線性刻度'],
                'answer': 2,
                'explain': '單選題（Radio button）和下拉式選單都只能選一個，但用途不同：單選題適合選項少（2-5個）、需要一眼看清楚選項的情況；下拉式選單適合選項多（如縣市、年級），不佔版面。核取方塊（Checkbox）可以多選。'
            },
        ]
    },
    'q4': {
        'title': '第四章 隨堂測驗',
        'questions': [
            {
                'q': 'Google 表單收集的資料，可以自動整理到哪裡？',
                'options': ['Google 試算表（可查看所有填寫記錄）', 'Google 文件', 'Google 簡報', 'Gmail 信箱'],
                'answer': 0,
                'explain': 'Google 表單的「回應」標籤中，點擊試算表圖示，可以自動建立一份連結的 Google 試算表。每當有人填寫表單，新資料就會即時出現在試算表中，方便後續統計分析。'
            },
            {
                'q': '以下哪項是設計問卷時的好習慣？',
                'options': ['每題都設定為必填以確保資料完整', '問題越多越好，收集更多資訊', '只使用開放式問題以獲得詳細回答', '問卷長度適中，避免超過 10 分鐘填寫時間'],
                'answer': 3,
                'explain': '問卷設計原則：長度適中（理想 5-7 分鐘，最多 15 分鐘），填寫率會大幅降低。其他好習慣：非關鍵題不必填、選擇題和開放題混合使用、問題清楚不含糊、避免引導性問題、在開頭說明目的和填寫時間。'
            },
        ]
    },
}

SLIDES = [
    {
        'id': 1, 'chapter': '封面', 'title': '合併列印與表單應用',
        'bg': 'navy', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<div style='text-align:center;padding:30px 20px;'>
  <div style='font-size:72px;margin-bottom:20px;'>📋</div>
  <h1 style='font-size:2.8rem;font-weight:900;color:#fff;margin-bottom:12px;'>合併列印與表單應用</h1>
  <h2 style='font-size:1.5rem;font-weight:400;color:#93c5fd;margin-bottom:30px;'>Mail Merge &amp; Google Forms</h2>
  <div style='display:flex;justify-content:center;gap:20px;flex-wrap:wrap;margin-bottom:30px;'>
    <span style='background:rgba(255,255,255,0.15);color:#e0f2fe;padding:8px 20px;border-radius:20px;font-size:1rem;'>✉️ 合併列印</span>
    <span style='background:rgba(255,255,255,0.15);color:#e0f2fe;padding:8px 20px;border-radius:20px;font-size:1rem;'>📝 表單設計</span>
    <span style='background:rgba(255,255,255,0.15);color:#e0f2fe;padding:8px 20px;border-radius:20px;font-size:1rem;'>📊 資料分析</span>
  </div>
  <p style='color:#bfdbfe;font-size:1.1rem;'>城市科技 — 第五章</p>
</div>"""
    },
    {
        'id': 2, 'chapter': '第一章：合併列印概念', 'title': '什麼是合併列印？',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>合併列印：批次產生個人化文件</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>💡 核心概念</h3>
      <div style='background:#f8fafc;padding:15px;border-radius:8px;'>
        <div style='text-align:center;margin-bottom:10px;'>
          <div style='display:flex;align-items:center;justify-content:center;gap:8px;font-size:.85rem;'>
            <div style='background:#dbeafe;padding:8px 12px;border-radius:8px;color:#1e40af;font-weight:700;'>📄 範本文件</div>
            <span style='font-size:1.2rem;color:#6b7280;'>+</span>
            <div style='background:#dcfce7;padding:8px 12px;border-radius:8px;color:#15803d;font-weight:700;'>📊 資料來源</div>
            <span style='font-size:1.2rem;color:#6b7280;'>=</span>
            <div style='background:#fde047;padding:8px 12px;border-radius:8px;color:#854d0e;font-weight:700;'>📑 N 份文件</div>
          </div>
        </div>
        <p style='color:#374151;font-size:.83rem;text-align:center;'>一份範本 × 100 筆資料 = 100 份個人化文件</p>
      </div>
    </div>
    <div style='background:#f0fdf4;padding:10px;border-radius:8px;'>
      <p style='color:#15803d;font-size:.85rem;font-weight:700;margin-bottom:5px;'>🕐 省多少時間？</p>
      <p style='color:#374151;font-size:.83rem;margin:0;'>手動：100 份通知單 × 5 分鐘 = 500 分鐘<br>合併列印：設定完成後，5 分鐘產生全部 100 份</p>
    </div>
  </div>
  <div>
    <div style='background:#fef9c3;padding:15px;border-radius:10px;border:1px solid #fde047;'>
      <h3 style='color:#854d0e;font-size:1rem;margin-bottom:10px;'>📝 常見應用</h3>
      <div style='display:flex;flex-direction:column;gap:7px;font-size:.83rem;'>
        <div style='background:#fff;padding:8px;border-radius:6px;border-left:3px solid #f59e0b;color:#374151;'>✉️ 學生成績通知單（每個家長不同）</div>
        <div style='background:#fff;padding:8px;border-radius:6px;border-left:3px solid #f59e0b;color:#374151;'>🎟️ 活動邀請函（每人姓名不同）</div>
        <div style='background:#fff;padding:8px;border-radius:6px;border-left:3px solid #f59e0b;color:#374151;'>🏷️ 信封地址標籤（大量寄件）</div>
        <div style='background:#fff;padding:8px;border-radius:6px;border-left:3px solid #f59e0b;color:#374151;'>🎓 畢業證書（每人姓名、科系不同）</div>
        <div style='background:#fff;padding:8px;border-radius:6px;border-left:3px solid #f59e0b;color:#374151;'>📧 行銷電子郵件（個人化稱謂）</div>
      </div>
    </div>
  </div>
</div>"""
    },
    {
        'id': 3, 'chapter': '第一章：合併列印概念', 'title': '合併列印的組成',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>合併列印的兩大組成要素</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:18px;border-radius:12px;border:2px solid #2563eb;'>
      <h3 style='color:#1e40af;font-size:1.1rem;margin-bottom:12px;text-align:center;'>📄 範本文件</h3>
      <div style='background:#fff;padding:15px;border-radius:8px;font-size:.85rem;line-height:1.8;border:1px solid #e2e8f0;'>
        <p style='color:#374151;margin:0;'>親愛的 <span style='background:#fde047;padding:2px 5px;border-radius:3px;color:#854d0e;font-weight:700;'>《《姓名》》</span> 同學家長：</p>
        <p style='color:#374151;margin:8px 0;'>您的孩子本學期成績為 <span style='background:#fde047;padding:2px 5px;border-radius:3px;color:#854d0e;font-weight:700;'>《《總分》》</span> 分，名次為全班第 <span style='background:#fde047;padding:2px 5px;border-radius:3px;color:#854d0e;font-weight:700;'>《《名次》》</span> 名。</p>
      </div>
      <p style='color:#6b7280;font-size:.75rem;margin-top:8px;text-align:center;'>黃色部分為功能變數（佔位符）</p>
    </div>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:18px;border-radius:12px;border:2px solid #16a34a;'>
      <h3 style='color:#15803d;font-size:1.1rem;margin-bottom:12px;text-align:center;'>📊 資料來源（試算表）</h3>
      <table style='width:100%;border-collapse:collapse;font-size:.8rem;'>
        <tr style='background:#15803d;color:#fff;'><th style='padding:6px;'>姓名</th><th style='padding:6px;'>總分</th><th style='padding:6px;'>名次</th></tr>
        <tr><td style='padding:5px;color:#374151;'>王小明</td><td style='padding:5px;color:#374151;'>285</td><td style='padding:5px;color:#374151;'>3</td></tr>
        <tr style='background:#f0fdf4;'><td style='padding:5px;color:#374151;'>李小花</td><td style='padding:5px;color:#374151;'>312</td><td style='padding:5px;color:#374151;'>1</td></tr>
        <tr><td style='padding:5px;color:#374151;'>陳大成</td><td style='padding:5px;color:#374151;'>270</td><td style='padding:5px;color:#374151;'>7</td></tr>
      </table>
      <p style='color:#6b7280;font-size:.75rem;margin-top:8px;text-align:center;'>每列資料 → 產生一份文件</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 4, 'chapter': '第一章：合併列印概念', 'title': '生活中的合併列印',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>你不知道這些都用了合併列印？</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:16px;'>
  <div style='display:flex;flex-direction:column;gap:10px;'>
    <div style='background:#eff6ff;padding:12px;border-radius:10px;border-left:4px solid #2563eb;'>
      <h3 style='color:#1e40af;font-size:.9rem;margin-bottom:5px;'>🏦 銀行對帳單</h3>
      <p style='color:#374151;font-size:.82rem;'>每個月你收到的信用卡帳單、存款對帳單，銀行是用合併列印批次產生幾百萬份。</p>
    </div>
    <div style='background:#f0fdf4;padding:12px;border-radius:10px;border-left:4px solid #16a34a;'>
      <h3 style='color:#15803d;font-size:.9rem;margin-bottom:5px;'>📦 包裹收件標籤</h3>
      <p style='color:#374151;font-size:.82rem;'>黑貓宅急便、711 等物流，每個包裹上的姓名地址標籤都是合併列印自動產生的。</p>
    </div>
    <div style='background:#fdf4ff;padding:12px;border-radius:10px;border-left:4px solid #7c3aed;'>
      <h3 style='color:#7c3aed;font-size:.9rem;margin-bottom:5px;'>🎓 學校成績單</h3>
      <p style='color:#374151;font-size:.82rem;'>期末成績單、學期評語，老師或教務處使用合併列印批次印出每個學生的個人成績。</p>
    </div>
  </div>
  <div style='display:flex;flex-direction:column;gap:10px;'>
    <div style='background:#fff7ed;padding:12px;border-radius:10px;border-left:4px solid #ea580c;'>
      <h3 style='color:#ea580c;font-size:.9rem;margin-bottom:5px;'>🎫 活動票券</h3>
      <p style='color:#374151;font-size:.82rem;'>演唱會、展覽的入場票上有你的姓名和座位號碼，是從購票資料庫合併列印。</p>
    </div>
    <div style='background:#fef9c3;padding:12px;border-radius:10px;border-left:4px solid #ca8a04;'>
      <h3 style='color:#854d0e;font-size:.9rem;margin-bottom:5px;'>📧 行銷電子郵件</h3>
      <p style='color:#374151;font-size:.82rem;'>你收到「親愛的 XXX 先生/小姐，我們為您準備了...」，這種個人化郵件就是合併列印的電子版。</p>
    </div>
    <div style='background:#fef2f2;padding:10px;border-radius:8px;'>
      <p style='color:#dc2626;font-size:.83rem;margin:0;'>💡 這些功能每天在全球處理幾十億份文件！</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 5, 'chapter': '第一章：合併列印概念', 'title': 'Word 合併列印工具',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>Word 合併列印：工具列介紹</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>🔧 「郵件」索引標籤功能</h3>
      <div class='layer-stack'>
        <div class='layer layer-user'><div class='layer-num'>1</div><div><div class='layer-name' style='color:#374151;'>開始合併列印</div><div class='layer-detail'>選擇文件類型（信件、信封、標籤）</div></div></div>
        <div class='layer layer-app'><div class='layer-num'>2</div><div><div class='layer-name' style='color:#374151;'>選取收件者</div><div class='layer-detail'>連接 Excel 或 Outlook 聯絡人</div></div></div>
        <div class='layer layer-os'><div class='layer-num'>3</div><div><div class='layer-name' style='color:#374151;'>插入合併欄位</div><div class='layer-detail'>在文件中插入《《欄位》》佔位符</div></div></div>
        <div class='layer layer-hw'><div class='layer-num'>4</div><div><div class='layer-name' style='color:#374151;'>完成與合併</div><div class='layer-detail'>預覽結果並列印或儲存</div></div></div>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:10px;'>📊 資料來源格式要求</h3>
      <table style='width:100%;border-collapse:collapse;font-size:.82rem;'>
        <tr style='background:#15803d;color:#fff;'><th style='padding:6px;'>要求</th><th style='padding:6px;'>說明</th></tr>
        <tr><td style='padding:5px;color:#374151;'>第一列</td><td style='padding:5px;color:#374151;'>欄位名稱（不能有空格）</td></tr>
        <tr style='background:#f0fdf4;'><td style='padding:5px;color:#374151;'>資料列</td><td style='padding:5px;color:#374151;'>從第二列開始，每列一筆</td></tr>
        <tr><td style='padding:5px;color:#374151;'>欄位名稱</td><td style='padding:5px;color:#374151;'>建議用英文或無空格中文</td></tr>
        <tr style='background:#f0fdf4;'><td style='padding:5px;color:#374151;'>空白列</td><td style='padding:5px;color:#374151;'>不要有空白列（會出錯）</td></tr>
      </table>
    </div>
  </div>
</div>"""
    },
    {
        'id': 6, 'chapter': '第一章：合併列印概念', 'title': '規則條件設定',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>合併列印進階：條件規則</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>🔀 IF...THEN...ELSE 規則</h3>
      <p style='color:#374151;font-size:.88rem;margin-bottom:10px;'>根據條件顯示不同文字，讓文件更個人化：</p>
      <div style='background:#f8fafc;padding:12px;border-radius:8px;font-family:monospace;font-size:.82rem;'>
        <p style='color:#1e40af;margin:0 0 4px;font-weight:700;'>IF 性別 = "男"</p>
        <p style='color:#15803d;margin:0 0 4px;padding-left:16px;'>THEN "先生"</p>
        <p style='color:#dc2626;margin:0;padding-left:16px;'>ELSE "小姐"</p>
      </div>
      <p style='color:#374151;font-size:.82rem;margin-top:8px;'>結果：「王小明 先生」或「李小花 小姐」</p>
    </div>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:10px;'>📊 資料篩選</h3>
      <p style='color:#374151;font-size:.88rem;margin-bottom:8px;'>可以篩選特定條件的資料：</p>
      <ul style='color:#374151;font-size:.85rem;padding-left:16px;'>
        <li>只寄給「台北市」的收件人</li>
        <li>只寄給成績低於 60 分的學生</li>
        <li>只處理「已報名」的名單</li>
      </ul>
      <div style='background:#dcfce7;padding:8px;border-radius:6px;margin-top:8px;'>
        <p style='color:#15803d;font-size:.8rem;margin:0;'>操作：選取收件者 → 編輯收件者清單 → 篩選</p>
      </div>
    </div>
  </div>
</div>"""
    },
    {
        'id': 7, 'chapter': '第一章：合併列印概念', 'title': '🎯 第一章 隨堂測驗',
        'bg': 'purple', 'quiz': 'q1', 'chart': None, 'video': None,
        'html': """
<div style='text-align:center;padding:20px;'>
  <div style='font-size:56px;margin-bottom:15px;'>🎯</div>
  <h2 style='color:#fff;font-size:2rem;font-weight:800;margin-bottom:10px;'>第一章 隨堂測驗</h2>
  <p style='color:#e9d5ff;font-size:1.1rem;'>合併列印概念 ── 2 道題目，點擊作答！</p>
</div>"""
    },
    {
        'id': 8, 'chapter': '第二章：合併列印實作', 'title': '成績通知單實作',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>實作一：學生成績通知單</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>📋 準備工作</h3>
      <div style='display:flex;flex-direction:column;gap:6px;font-size:.83rem;'>
        <div style='background:#dbeafe;padding:7px;border-radius:5px;display:flex;gap:8px;align-items:start;'><span style='background:#2563eb;color:#fff;min-width:20px;height:20px;border-radius:50%;font-size:.65rem;font-weight:700;display:flex;align-items:center;justify-content:center;'>1</span><span style='color:#374151;'>準備 Excel 檔：欄位含「學號、姓名、國文、英文、數學、總分、名次」</span></div>
        <div style='background:#dbeafe;padding:7px;border-radius:5px;display:flex;gap:8px;align-items:start;'><span style='background:#2563eb;color:#fff;min-width:20px;height:20px;border-radius:50%;font-size:.65rem;font-weight:700;display:flex;align-items:center;justify-content:center;'>2</span><span style='color:#374151;'>建立 Word 範本：版面配置、學校 logo、固定文字</span></div>
        <div style='background:#dbeafe;padding:7px;border-radius:5px;display:flex;gap:8px;align-items:start;'><span style='background:#2563eb;color:#fff;min-width:20px;height:20px;border-radius:50%;font-size:.65rem;font-weight:700;display:flex;align-items:center;justify-content:center;'>3</span><span style='color:#374151;'>連結資料：郵件 → 選取收件者 → 使用現有清單</span></div>
        <div style='background:#dbeafe;padding:7px;border-radius:5px;display:flex;gap:8px;align-items:start;'><span style='background:#2563eb;color:#fff;min-width:20px;height:20px;border-radius:50%;font-size:.65rem;font-weight:700;display:flex;align-items:center;justify-content:center;'>4</span><span style='color:#374151;'>插入欄位：在對應位置插入《《欄位名稱》》</span></div>
        <div style='background:#dbeafe;padding:7px;border-radius:5px;display:flex;gap:8px;align-items:start;'><span style='background:#2563eb;color:#fff;min-width:20px;height:20px;border-radius:50%;font-size:.65rem;font-weight:700;display:flex;align-items:center;justify-content:center;'>5</span><span style='color:#374151;'>預覽、確認後完成合併，列印或儲存</span></div>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#f8fafc;border:2px solid #e2e8f0;padding:15px;border-radius:10px;font-size:.83rem;'>
      <h3 style='color:#374151;font-size:.9rem;margin-bottom:10px;text-align:center;'>成績通知單範本預覽</h3>
      <div style='background:#fff;padding:12px;border-radius:8px;border:1px solid #e5e7eb;'>
        <p style='color:#374151;text-align:center;font-weight:700;font-size:.85rem;margin-bottom:8px;'>芳和實驗中學 成績通知</p>
        <p style='color:#374151;font-size:.8rem;margin-bottom:6px;'>學號：<span style='background:#fef9c3;padding:1px 4px;border-radius:3px;font-weight:700;color:#854d0e;'>《《學號》》</span></p>
        <p style='color:#374151;font-size:.8rem;margin-bottom:6px;'>姓名：<span style='background:#fef9c3;padding:1px 4px;border-radius:3px;font-weight:700;color:#854d0e;'>《《姓名》》</span> 同學</p>
        <table style='width:100%;border-collapse:collapse;font-size:.75rem;margin-top:8px;'>
          <tr style='background:#1e3a5f;color:#fff;'><th style='padding:4px;'>科目</th><th style='padding:4px;'>成績</th></tr>
          <tr><td style='padding:4px;color:#374151;'>國文</td><td style='padding:4px;color:#854d0e;font-weight:700;'>《《國文》》</td></tr>
          <tr style='background:#f8fafc;'><td style='padding:4px;color:#374151;'>英文</td><td style='padding:4px;color:#854d0e;font-weight:700;'>《《英文》》</td></tr>
          <tr><td style='padding:4px;color:#374151;'>數學</td><td style='padding:4px;color:#854d0e;font-weight:700;'>《《數學》》</td></tr>
          <tr style='background:#dbeafe;'><td style='padding:4px;color:#1e40af;font-weight:700;'>總分</td><td style='padding:4px;color:#1e40af;font-weight:700;'>《《總分》》</td></tr>
        </table>
      </div>
    </div>
  </div>
</div>"""
    },
    {
        'id': 9, 'chapter': '第二章：合併列印實作', 'title': '信封合併列印',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>實作二：大量信封地址列印</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>📮 信封設定步驟</h3>
      <div style='display:flex;flex-direction:column;gap:6px;font-size:.83rem;'>
        <div style='background:#dbeafe;padding:7px;border-radius:5px;color:#374151;'><strong>郵件 → 開始合併列印 → 信封</strong>：設定信封尺寸</div>
        <div style='background:#dbeafe;padding:7px;border-radius:5px;color:#374151;'>台灣常用：<strong>DL（22x11cm）</strong> 或 <strong>6號信封（17.3x12cm）</strong></div>
        <div style='background:#dbeafe;padding:7px;border-radius:5px;color:#374151;'>資料欄位：姓名、地址、郵遞區號（分開欄位）</div>
        <div style='background:#dbeafe;padding:7px;border-radius:5px;color:#374151;'>設定寄件人（固定文字，不合併）</div>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#f8fafc;border:2px solid #e2e8f0;padding:15px;border-radius:10px;'>
      <h3 style='color:#374151;font-size:.9rem;margin-bottom:10px;text-align:center;'>信封範本示意</h3>
      <div style='background:#fff;padding:15px;border-radius:8px;border:1px solid #e5e7eb;min-height:100px;position:relative;font-size:.8rem;'>
        <div style='position:absolute;top:10px;left:10px;'>
          <p style='color:#374151;margin:0;font-size:.75rem;'>芳和實驗中學</p>
          <p style='color:#374151;margin:0;font-size:.75rem;'>台北市大安區和平東路三段</p>
        </div>
        <div style='position:absolute;top:10px;right:10px;width:55px;height:25px;border:1px solid #e2e8f0;display:flex;align-items:center;justify-content:center;'>
          <p style='color:#94a3b8;font-size:.65rem;margin:0;'>郵票</p>
        </div>
        <div style='position:absolute;bottom:15px;right:15px;text-align:right;'>
          <p style='color:#854d0e;font-weight:700;font-size:.8rem;background:#fef9c3;padding:2px 4px;border-radius:3px;display:inline-block;margin-bottom:3px;'>《《郵遞區號》》</p><br>
          <p style='color:#374151;margin:0;font-size:.8rem;'>《《地址》》</p>
          <p style='color:#374151;margin:0;font-size:.8rem;'><span style='background:#fef9c3;padding:1px 4px;border-radius:3px;color:#854d0e;font-weight:700;'>《《姓名》》</span> 收</p>
        </div>
      </div>
    </div>
  </div>
</div>"""
    },
    {
        'id': 10, 'chapter': '第二章：合併列印實作', 'title': '地址標籤',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>實作三：地址標籤批次列印</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>🏷️ 標籤設定步驟</h3>
      <div style='display:flex;flex-direction:column;gap:6px;font-size:.83rem;'>
        <div style='background:#dbeafe;padding:7px;border-radius:5px;color:#374151;'><strong>郵件 → 開始合併列印 → 標籤</strong></div>
        <div style='background:#dbeafe;padding:7px;border-radius:5px;color:#374151;'>選擇標籤廠商和型號（如 Avery A4）</div>
        <div style='background:#dbeafe;padding:7px;border-radius:5px;color:#374151;'>在「第一個標籤」設計版面</div>
        <div style='background:#dbeafe;padding:7px;border-radius:5px;color:#374151;'>點擊「更新標籤」複製到所有標籤</div>
        <div style='background:#dbeafe;padding:7px;border-radius:5px;color:#374151;'>預覽確認後直接列印到標籤貼紙</div>
      </div>
    </div>
    <div style='background:#fef9c3;padding:10px;border-radius:8px;'>
      <p style='color:#854d0e;font-size:.83rem;margin:0;'>💡 一頁 A4 可放 12–24 個標籤，效率極高！</p>
    </div>
  </div>
  <div>
    <div style='background:#f8fafc;border:2px solid #e2e8f0;padding:12px;border-radius:10px;'>
      <h3 style='color:#374151;font-size:.85rem;margin-bottom:10px;text-align:center;'>標籤頁面示意（3×4=12標籤）</h3>
      <div style='display:grid;grid-template-columns:1fr 1fr 1fr;gap:4px;'>
        {labels}
      </div>
    </div>
  </div>
</div>""".replace('{labels}', ''.join([
    f"<div style='background:#fff;border:1px solid #e2e8f0;padding:6px;border-radius:4px;font-size:.65rem;color:#374151;text-align:center;'><span style='color:#854d0e;font-weight:700;'>《《姓名》》</span><br><span style='color:#6b7280;'>《《地址》》</span></div>" if i < 6 else
    f"<div style='background:#f8fafc;border:1px solid #e2e8f0;padding:6px;border-radius:4px;font-size:.65rem;color:#94a3b8;text-align:center;'>（空白）</div>"
    for i in range(12)
])
)
    },
    {
        'id': 11, 'chapter': '第二章：合併列印實作', 'title': '常見問題排除',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>合併列印常見問題 Q&A</h2>
<div style='display:flex;flex-direction:column;gap:10px;'>
  <div style='display:grid;grid-template-columns:1fr 3fr;gap:12px;background:#fef2f2;padding:12px;border-radius:10px;align-items:start;'>
    <div style='background:#dc2626;color:#fff;padding:8px;border-radius:8px;text-align:center;font-size:.82rem;font-weight:700;'>❓ 問題<br>合併後日期格式錯誤（顯示英文格式）</div>
    <div style='background:#fff;padding:10px;border-radius:8px;font-size:.82rem;color:#374151;'>在欄位上右鍵 → 編輯功能變數 → 圖片格式：加入 <code style='color:#1e40af;'>\\@ "yyyy年MM月dd日"</code> 轉換日期格式。</div>
  </div>
  <div style='display:grid;grid-template-columns:1fr 3fr;gap:12px;background:#fff7ed;padding:12px;border-radius:10px;align-items:start;'>
    <div style='background:#ea580c;color:#fff;padding:8px;border-radius:8px;text-align:center;font-size:.82rem;font-weight:700;'>❓ 問題<br>金額出現小數點（如 100.00）</div>
    <div style='background:#fff;padding:10px;border-radius:8px;font-size:.82rem;color:#374151;'>在欄位上右鍵 → 編輯功能變數 → 加入 <code style='color:#1e40af;'>\\# "#,##0"</code> 格式化數字，去除小數並加千分位。</div>
  </div>
  <div style='display:grid;grid-template-columns:1fr 3fr;gap:12px;background:#eff6ff;padding:12px;border-radius:10px;align-items:start;'>
    <div style='background:#2563eb;color:#fff;padding:8px;border-radius:8px;text-align:center;font-size:.82rem;font-weight:700;'>❓ 問題<br>連結資料時找不到 Excel 檔</div>
    <div style='background:#fff;padding:10px;border-radius:8px;font-size:.82rem;color:#374151;'>確認 Excel 檔案已關閉（Word 無法連結開啟中的檔案），且路徑中不要有特殊字元。</div>
  </div>
</div>"""
    },
    {
        'id': 12, 'chapter': '第二章：合併列印實作', 'title': '🎯 第二章 隨堂測驗',
        'bg': 'purple', 'quiz': 'q2', 'chart': None, 'video': None,
        'html': """
<div style='text-align:center;padding:20px;'>
  <div style='font-size:56px;margin-bottom:15px;'>🎯</div>
  <h2 style='color:#fff;font-size:2rem;font-weight:800;margin-bottom:10px;'>第二章 隨堂測驗</h2>
  <p style='color:#e9d5ff;font-size:1.1rem;'>合併列印實作 ── 2 道題目，點擊作答！</p>
</div>"""
    },
    {
        'id': 13, 'chapter': '第三章：Google 表單設計', 'title': '認識 Google 表單',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>Google 表單：免費強大的問卷工具</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>📝 Google 表單能做什麼？</h3>
      <div style='display:flex;flex-direction:column;gap:6px;font-size:.83rem;'>
        <div style='background:#dbeafe;padding:7px;border-radius:5px;color:#374151;'>📋 問卷調查（選項、評分、開放題）</div>
        <div style='background:#dbeafe;padding:7px;border-radius:5px;color:#374151;'>✅ 線上測驗（自動批改、顯示分數）</div>
        <div style='background:#dbeafe;padding:7px;border-radius:5px;color:#374151;'>📅 活動報名（收集姓名聯絡資訊）</div>
        <div style='background:#dbeafe;padding:7px;border-radius:5px;color:#374151;'>📊 資料蒐集（自動整理到試算表）</div>
        <div style='background:#dbeafe;padding:7px;border-radius:5px;color:#374151;'>🔗 分享連結，任何裝置都能填寫</div>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:10px;'>⭐ 為什麼選 Google 表單？</h3>
      <div style='display:flex;flex-direction:column;gap:6px;font-size:.83rem;'>
        <div style='background:#dcfce7;padding:7px;border-radius:5px;color:#15803d;'>✅ 完全免費，無限筆數</div>
        <div style='background:#dcfce7;padding:7px;border-radius:5px;color:#15803d;'>✅ 不需安裝任何軟體</div>
        <div style='background:#dcfce7;padding:7px;border-radius:5px;color:#15803d;'>✅ 即時查看回應統計圖表</div>
        <div style='background:#dcfce7;padding:7px;border-radius:5px;color:#15803d;'>✅ 自動同步到 Google 試算表</div>
        <div style='background:#dcfce7;padding:7px;border-radius:5px;color:#15803d;'>✅ 可設定截止時間和填寫限制</div>
      </div>
    </div>
  </div>
</div>"""
    },
    {
        'id': 14, 'chapter': '第三章：Google 表單設計', 'title': '題型選擇',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>Google 表單題型全覽</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:16px;'>
  <div style='display:flex;flex-direction:column;gap:8px;'>
    <div style='background:#eff6ff;padding:10px;border-radius:8px;border-left:3px solid #2563eb;'>
      <h3 style='color:#1e40af;font-size:.88rem;margin-bottom:4px;'>🔘 單選題（選項按鈕）</h3>
      <p style='color:#374151;font-size:.78rem;margin:0;'>只能選一個答案，適合明確二選一或少數選項</p>
    </div>
    <div style='background:#f0fdf4;padding:10px;border-radius:8px;border-left:3px solid #16a34a;'>
      <h3 style='color:#15803d;font-size:.88rem;margin-bottom:4px;'>☑️ 核取方塊（複選）</h3>
      <p style='color:#374151;font-size:.78rem;margin:0;'>可選多個答案，適合「選出所有符合的」</p>
    </div>
    <div style='background:#fdf4ff;padding:10px;border-radius:8px;border-left:3px solid #7c3aed;'>
      <h3 style='color:#7c3aed;font-size:.88rem;margin-bottom:4px;'>🔽 下拉式選單</h3>
      <p style='color:#374151;font-size:.78rem;margin:0;'>只能選一個，適合選項多（縣市、年級等）</p>
    </div>
    <div style='background:#fff7ed;padding:10px;border-radius:8px;border-left:3px solid #ea580c;'>
      <h3 style='color:#ea580c;font-size:.88rem;margin-bottom:4px;'>📏 線性刻度</h3>
      <p style='color:#374151;font-size:.78rem;margin:0;'>1–5 或 1–10 的滿意度、重要性評分</p>
    </div>
  </div>
  <div style='display:flex;flex-direction:column;gap:8px;'>
    <div style='background:#fef9c3;padding:10px;border-radius:8px;border-left:3px solid #ca8a04;'>
      <h3 style='color:#854d0e;font-size:.88rem;margin-bottom:4px;'>📝 簡答（短文字）</h3>
      <p style='color:#374151;font-size:.78rem;margin:0;'>填寫姓名、電話等短文字，一行內容</p>
    </div>
    <div style='background:#fef2f2;padding:10px;border-radius:8px;border-left:3px solid #dc2626;'>
      <h3 style='color:#dc2626;font-size:.88rem;margin-bottom:4px;'>📄 段落（長文字）</h3>
      <p style='color:#374151;font-size:.78rem;margin:0;'>填寫長段意見、建議，多行文字</p>
    </div>
    <div style='background:#f0fdf4;padding:10px;border-radius:8px;border-left:3px solid #0d9488;'>
      <h3 style='color:#0d9488;font-size:.88rem;margin-bottom:4px;'>📅 日期 / 時間</h3>
      <p style='color:#374151;font-size:.78rem;margin:0;'>選擇日期或時間，顯示日期選擇器</p>
    </div>
    <div style='background:#eff6ff;padding:10px;border-radius:8px;border-left:3px solid #6366f1;'>
      <h3 style='color:#4338ca;font-size:.88rem;margin-bottom:4px;'>🔲 方格（矩陣題）</h3>
      <p style='color:#374151;font-size:.78rem;margin:0;'>多題共用相同選項，節省版面</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 15, 'chapter': '第三章：Google 表單設計', 'title': '表單進階設定',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>Google 表單進階設定</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>⚙️ 常用設定</h3>
      <div style='display:flex;flex-direction:column;gap:6px;font-size:.83rem;'>
        <div style='background:#dbeafe;padding:7px;border-radius:5px;color:#374151;'><strong style='color:#1e40af;'>每人限填一次</strong>：需要 Google 帳號，防止重複填寫</div>
        <div style='background:#dbeafe;padding:7px;border-radius:5px;color:#374151;'><strong style='color:#1e40af;'>顯示進度列</strong>：讓填寫者知道還有幾題</div>
        <div style='background:#dbeafe;padding:7px;border-radius:5px;color:#374151;'><strong style='color:#1e40af;'>填寫後顯示結果</strong>：可讓填寫者看到統計圖</div>
        <div style='background:#dbeafe;padding:7px;border-radius:5px;color:#374151;'><strong style='color:#1e40af;'>確認訊息</strong>：填寫完成後顯示感謝文字</div>
        <div style='background:#dbeafe;padding:7px;border-radius:5px;color:#374151;'><strong style='color:#1e40af;'>截止接受回應</strong>：到期後自動關閉</div>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:10px;'>📊 分區設計</h3>
      <p style='color:#374151;font-size:.88rem;margin-bottom:8px;'>長問卷可分成多個「區段」：</p>
      <ul style='color:#374151;font-size:.83rem;padding-left:16px;'>
        <li>每區段有標題說明，視覺清楚</li>
        <li>可設定根據答案跳至不同區段</li>
        <li>例如：選「是」→ 到第2區；選「否」→ 直接到最後</li>
      </ul>
      <div style='background:#dcfce7;padding:8px;border-radius:6px;margin-top:8px;'>
        <p style='color:#15803d;font-size:.8rem;margin:0;'>新增區段：最下方工具列 → 新增區段圖示</p>
      </div>
    </div>
  </div>
</div>"""
    },
    {
        'id': 16, 'chapter': '第三章：Google 表單設計', 'title': '線上測驗設計',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>Google 表單當測驗：自動批改</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>🎓 啟用測驗模式</h3>
      <div style='display:flex;flex-direction:column;gap:6px;font-size:.83rem;'>
        <div style='background:#dbeafe;padding:7px;border-radius:5px;display:flex;gap:6px;align-items:center;'><span style='background:#2563eb;color:#fff;width:18px;height:18px;border-radius:50%;font-size:.65rem;font-weight:700;display:flex;align-items:center;justify-content:center;flex-shrink:0;'>1</span><span style='color:#374151;'>設定 → 測驗 → 將此表單設為測驗</span></div>
        <div style='background:#dbeafe;padding:7px;border-radius:5px;display:flex;gap:6px;align-items:center;'><span style='background:#2563eb;color:#fff;width:18px;height:18px;border-radius:50%;font-size:.65rem;font-weight:700;display:flex;align-items:center;justify-content:center;flex-shrink:0;'>2</span><span style='color:#374151;'>每題設定正確答案和分數</span></div>
        <div style='background:#dbeafe;padding:7px;border-radius:5px;display:flex;gap:6px;align-items:center;'><span style='background:#2563eb;color:#fff;width:18px;height:18px;border-radius:50%;font-size:.65rem;font-weight:700;display:flex;align-items:center;justify-content:center;flex-shrink:0;'>3</span><span style='color:#374151;'>可加入解釋說明（答完後顯示）</span></div>
        <div style='background:#dbeafe;padding:7px;border-radius:5px;display:flex;gap:6px;align-items:center;'><span style='background:#2563eb;color:#fff;width:18px;height:18px;border-radius:50%;font-size:.65rem;font-weight:700;display:flex;align-items:center;justify-content:center;flex-shrink:0;'>4</span><span style='color:#374151;'>設定何時顯示分數（立即/審閱後）</span></div>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:10px;'>✅ 支援自動批改的題型</h3>
      <div style='display:flex;flex-direction:column;gap:6px;font-size:.83rem;'>
        <div style='background:#dcfce7;padding:6px;border-radius:5px;color:#15803d;'>✅ 單選題（完全自動批改）</div>
        <div style='background:#dcfce7;padding:6px;border-radius:5px;color:#15803d;'>✅ 核取方塊（多選題）</div>
        <div style='background:#dcfce7;padding:6px;border-radius:5px;color:#15803d;'>✅ 下拉式選單</div>
        <div style='background:#fef9c3;padding:6px;border-radius:5px;color:#854d0e;'>⚠️ 簡答題（需設定正確答案，大小寫敏感）</div>
        <div style='background:#fee2e2;padding:6px;border-radius:5px;color:#dc2626;'>❌ 段落（長文字）需人工批改</div>
      </div>
    </div>
  </div>
</div>"""
    },
    {
        'id': 17, 'chapter': '第三章：Google 表單設計', 'title': '🎯 第三章 隨堂測驗',
        'bg': 'purple', 'quiz': 'q3', 'chart': None, 'video': None,
        'html': """
<div style='text-align:center;padding:20px;'>
  <div style='font-size:56px;margin-bottom:15px;'>🎯</div>
  <h2 style='color:#fff;font-size:2rem;font-weight:800;margin-bottom:10px;'>第三章 隨堂測驗</h2>
  <p style='color:#e9d5ff;font-size:1.1rem;'>Google 表單設計 ── 2 道題目，點擊作答！</p>
</div>"""
    },
    {
        'id': 18, 'chapter': '第四章：問卷資料分析', 'title': '表單回應分析',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>Google 表單回應分析</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>📊 內建圖表</h3>
      <p style='color:#374151;font-size:.88rem;margin-bottom:8px;'>點擊「回應」標籤，Google 表單自動產生：</p>
      <ul style='color:#374151;font-size:.83rem;padding-left:16px;'>
        <li>圓餅圖（單選題）</li>
        <li>長條圖（核取方塊）</li>
        <li>統計數字（總回應數）</li>
        <li>各題回應摘要</li>
      </ul>
    </div>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:10px;'>📈 連結 Google 試算表</h3>
      <div style='display:flex;flex-direction:column;gap:6px;font-size:.83rem;'>
        <div style='background:#dcfce7;padding:7px;border-radius:5px;color:#374151;'>回應 → 點擊試算表圖示 → 建立新試算表</div>
        <div style='background:#dcfce7;padding:7px;border-radius:5px;color:#374151;'>每次有人填寫，資料即時出現在試算表</div>
        <div style='background:#dcfce7;padding:7px;border-radius:5px;color:#374151;'>在試算表中可進行進階分析：COUNTIF、排序、篩選</div>
        <div style='background:#dcfce7;padding:7px;border-radius:5px;color:#374151;'>可建立樞紐分析表進行交叉分析</div>
      </div>
    </div>
  </div>
</div>"""
    },
    {
        'id': 19, 'chapter': '第四章：問卷資料分析', 'title': '問卷設計原則',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>好問卷的設計原則</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:10px;'>✅ 好問卷應該...</h3>
      <div style='display:flex;flex-direction:column;gap:6px;font-size:.83rem;'>
        <div style='background:#dcfce7;padding:6px;border-radius:5px;color:#15803d;'>開頭說明目的和預計填寫時間</div>
        <div style='background:#dcfce7;padding:6px;border-radius:5px;color:#15803d;'>問題清楚、不含雙重否定</div>
        <div style='background:#dcfce7;padding:6px;border-radius:5px;color:#15803d;'>選項互斥且完整（有「其他」選項）</div>
        <div style='background:#dcfce7;padding:6px;border-radius:5px;color:#15803d;'>適當長度（5-10分鐘完成）</div>
        <div style='background:#dcfce7;padding:6px;border-radius:5px;color:#15803d;'>最後加「感謝填寫」確認訊息</div>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#fef2f2;padding:15px;border-radius:10px;'>
      <h3 style='color:#dc2626;font-size:1rem;margin-bottom:10px;'>❌ 不好的問卷問題</h3>
      <div style='display:flex;flex-direction:column;gap:8px;font-size:.83rem;'>
        <div style='background:#fee2e2;padding:8px;border-radius:6px;'>
          <p style='color:#dc2626;font-weight:700;margin:0 0 2px;'>引導性問題</p>
          <p style='color:#374151;margin:0;'>「你不覺得我們的服務很棒嗎？」</p>
        </div>
        <div style='background:#fee2e2;padding:8px;border-radius:6px;'>
          <p style='color:#dc2626;font-weight:700;margin:0 0 2px;'>雙重問題</p>
          <p style='color:#374151;margin:0;'>「你喜歡這個產品的品質和價格嗎？」（兩件事一題問）</p>
        </div>
        <div style='background:#fee2e2;padding:8px;border-radius:6px;'>
          <p style='color:#dc2626;font-weight:700;margin:0 0 2px;'>模糊問題</p>
          <p style='color:#374151;margin:0;'>「你常用手機嗎？」（多常算「常」？）</p>
        </div>
      </div>
    </div>
  </div>
</div>"""
    },
    {
        'id': 20, 'chapter': '第四章：問卷資料分析', 'title': '資料清理與分析',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>問卷資料清理與初步分析</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>🧹 資料清理</h3>
      <ul style='color:#374151;font-size:.85rem;padding-left:16px;'>
        <li>移除填寫不完整的問卷</li>
        <li>統一格式（如縣市名稱）</li>
        <li>找出明顯矛盾的回答</li>
        <li>確認無重複填寫</li>
      </ul>
    </div>
    <div style='background:#fef9c3;padding:10px;border-radius:8px;'>
      <p style='color:#854d0e;font-size:.85rem;font-weight:700;margin-bottom:4px;'>常用函數</p>
      <p style='color:#374151;font-size:.82rem;margin:0;'><code style='color:#1e40af;'>COUNTIF</code>：計算特定條件的筆數<br><code style='color:#1e40af;'>AVERAGEIF</code>：條件平均<br><code style='color:#1e40af;'>UNIQUE</code>：取出唯一值</p>
    </div>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:10px;'>📊 資料視覺化</h3>
      <p style='color:#374151;font-size:.88rem;margin-bottom:8px;'>不同資料型態適合不同圖表：</p>
      <div style='display:flex;flex-direction:column;gap:6px;font-size:.82rem;'>
        <div style='background:#dcfce7;padding:6px;border-radius:5px;color:#374151;'><strong style='color:#15803d;'>圓餅圖</strong>：各選項佔比（比例關係）</div>
        <div style='background:#dcfce7;padding:6px;border-radius:5px;color:#374151;'><strong style='color:#15803d;'>長條圖</strong>：各類別數量比較</div>
        <div style='background:#dcfce7;padding:6px;border-radius:5px;color:#374151;'><strong style='color:#15803d;'>折線圖</strong>：隨時間的變化趨勢</div>
        <div style='background:#dcfce7;padding:6px;border-radius:5px;color:#374151;'><strong style='color:#15803d;'>散佈圖</strong>：兩變數的相關性</div>
      </div>
    </div>
  </div>
</div>"""
    },
    {
        'id': 21, 'chapter': '第四章：問卷資料分析', 'title': '調查報告撰寫',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>從資料到報告：說一個好故事</h2>
<div style='background:#1e293b;padding:20px;border-radius:12px;margin-bottom:16px;'>
  <h3 style='color:#94a3b8;font-size:.85rem;text-align:center;margin-bottom:16px;letter-spacing:.05em;'>調查報告的結構</h3>
  <div style='display:grid;grid-template-columns:repeat(5,1fr);gap:8px;'>
    <div style='background:#0f172a;padding:12px;border-radius:8px;text-align:center;border-bottom:3px solid #3b82f6;'>
      <div style='font-size:1.6rem;'>🎯</div>
      <p style='color:#93c5fd;font-size:.7rem;margin-top:4px;'>① 研究目的<br>為何調查？</p>
    </div>
    <div style='background:#0f172a;padding:12px;border-radius:8px;text-align:center;border-bottom:3px solid #22c55e;'>
      <div style='font-size:1.6rem;'>👥</div>
      <p style='color:#86efac;font-size:.7rem;margin-top:4px;'>② 對象與方法<br>誰填？怎麼填？</p>
    </div>
    <div style='background:#0f172a;padding:12px;border-radius:8px;text-align:center;border-bottom:3px solid #f59e0b;'>
      <div style='font-size:1.6rem;'>📊</div>
      <p style='color:#fcd34d;font-size:.7rem;margin-top:4px;'>③ 資料呈現<br>圖表顯示什麼？</p>
    </div>
    <div style='background:#0f172a;padding:12px;border-radius:8px;text-align:center;border-bottom:3px solid #f472b6;'>
      <div style='font-size:1.6rem;'>💡</div>
      <p style='color:#f9a8d4;font-size:.7rem;margin-top:4px;'>④ 分析結論<br>代表什麼意義？</p>
    </div>
    <div style='background:#0f172a;padding:12px;border-radius:8px;text-align:center;border-bottom:3px solid #a78bfa;'>
      <div style='font-size:1.6rem;'>📝</div>
      <p style='color:#c4b5fd;font-size:.7rem;margin-top:4px;'>⑤ 建議<br>可以怎麼改善？</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 22, 'chapter': '第四章：問卷資料分析', 'title': '🎯 第四章 隨堂測驗',
        'bg': 'purple', 'quiz': 'q4', 'chart': None, 'video': None,
        'html': """
<div style='text-align:center;padding:20px;'>
  <div style='font-size:56px;margin-bottom:15px;'>🎯</div>
  <h2 style='color:#fff;font-size:2rem;font-weight:800;margin-bottom:10px;'>第四章 隨堂測驗</h2>
  <p style='color:#e9d5ff;font-size:1.1rem;'>問卷資料分析 ── 2 道題目，點擊作答！</p>
</div>"""
    },
    {
        'id': 23, 'chapter': '分組實作', 'title': '分組實作：校園調查與合併列印',
        'bg': 'teal', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 style='font-size:1.8rem;font-weight:800;color:#fff;margin-bottom:20px;text-align:center;'>📋 分組實作：校園調查與合併列印</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div style='background:rgba(255,255,255,0.15);padding:18px;border-radius:12px;'>
    <h3 style='color:#fff;font-size:1rem;margin-bottom:14px;'>📋 實作任務</h3>
    <div style='display:flex;flex-direction:column;gap:10px;'>
      <div style='background:rgba(255,255,255,0.2);padding:12px;border-radius:8px;'>
        <p style='color:#fff;font-weight:700;font-size:.9rem;margin:0 0 4px;'>任務一：設計問卷</p>
        <p style='color:#cffafe;font-size:.8rem;margin:0;'>以「同學的數位生活習慣」為主題，設計一份包含至少 3 種題型的 Google 表單問卷</p>
      </div>
      <div style='background:rgba(255,255,255,0.2);padding:12px;border-radius:8px;'>
        <p style='color:#fff;font-weight:700;font-size:.9rem;margin:0 0 4px;'>任務二：蒐集資料</p>
        <p style='color:#cffafe;font-size:.8rem;margin:0;'>請至少 20 位同學填寫問卷，連結試算表整理資料，製作視覺化圖表</p>
      </div>
      <div style='background:rgba(255,255,255,0.2);padding:12px;border-radius:8px;'>
        <p style='color:#fff;font-weight:700;font-size:.9rem;margin:0 0 4px;'>任務三：合併列印</p>
        <p style='color:#cffafe;font-size:.8rem;margin:0;'>用調查結果製作個人化感謝函，運用合併列印批次產生每位填答者的感謝信</p>
      </div>
    </div>
  </div>
  <div>
    <div style='background:rgba(255,255,255,0.15);padding:15px;border-radius:12px;margin-bottom:12px;'>
      <h3 style='color:#fff;font-size:1rem;margin-bottom:10px;'>📊 成果展示</h3>
      <ul style='color:#cffafe;font-size:.85rem;padding-left:16px;'>
        <li>Google 表單問卷連結</li>
        <li>試算表資料與圖表截圖</li>
        <li>調查結果簡報（Google Slides）</li>
        <li>合併列印完成的感謝函樣本</li>
      </ul>
    </div>
    <div style='background:rgba(255,255,255,0.15);padding:12px;border-radius:8px;'>
      <p style='color:#fff;font-size:.85rem;font-weight:700;margin-bottom:4px;'>🗓️ 繳交方式</p>
      <p style='color:#cffafe;font-size:.82rem;margin:0;'>上傳至 Google Classroom：表單連結 + 簡報檔 + 合併列印PDF</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 24, 'chapter': '分組實作', 'title': '資料的力量',
        'bg': 'navy', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<div style='text-align:center;padding:30px 20px;'>
  <div style='font-size:64px;margin-bottom:20px;'>📊</div>
  <h1 style='font-size:2.2rem;font-weight:900;color:#fff;margin-bottom:12px;'>資料的力量</h1>
  <h2 style='font-size:1.2rem;font-weight:400;color:#93c5fd;margin-bottom:24px;'>從一份問卷，了解整個群體的想法</h2>
  <div style='background:rgba(255,255,255,0.1);padding:18px;border-radius:12px;margin-bottom:24px;max-width:600px;margin-left:auto;margin-right:auto;'>
    <p style='color:#e2e8f0;font-size:1rem;font-style:italic;line-height:1.7;margin:0;'>
      「In God we trust; all others must bring data.」<br>
      <span style='font-size:.85rem;color:#94a3b8;'>— W. Edwards Deming，統計學家</span>
    </p>
  </div>
  <div style='display:flex;justify-content:center;gap:12px;flex-wrap:wrap;'>
    <span style='background:rgba(255,255,255,0.12);color:#e0f2fe;padding:8px 18px;border-radius:20px;font-size:.9rem;'>學會合併列印 ✅</span>
    <span style='background:rgba(255,255,255,0.12);color:#e0f2fe;padding:8px 18px;border-radius:20px;font-size:.9rem;'>設計問卷 ✅</span>
    <span style='background:rgba(255,255,255,0.12);color:#e0f2fe;padding:8px 18px;border-radius:20px;font-size:.9rem;'>下一章見 👋</span>
  </div>
</div>"""
    },
]
