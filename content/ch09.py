# -*- coding: utf-8 -*-
# Week 9: 資料分析實作

CHAPTERS = [
    {'name': '封面', 'start': 1},
    {'name': '第一章：Excel 核心函數', 'start': 2},
    {'name': '第二章：條件判斷與查詢', 'start': 8},
    {'name': '第三章：樞紐分析表', 'start': 14},
    {'name': '第四章：圖表與預測', 'start': 19},
    {'name': '分組實作', 'start': 23},
]

QUIZZES = {
    'q1': {
        'title': '第一章 隨堂測驗',
        'questions': [
            {
                'q': '在 Excel 中，要計算 A1 到 A50 範圍內，成績大於等於 60 的學生人數，應使用哪個公式？',
                'options': ['=COUNTIF(A1:A50,">=60")', '=COUNT(A1:A50,>=60)', '=SUM(A1:A50,">=60")', '=IF(A1:A50>=60,1,0)'],
                'answer': 0,
                'explain': 'COUNTIF 函數語法：=COUNTIF(範圍, 條件)。條件要用引號包住，例如 ">=60"。COUNT 只計算數字個數，不能加條件。'
            },
            {
                'q': 'AVERAGE 函數會如何處理空白儲存格？',
                'options': ['將空白視為 0 計算', '回傳錯誤訊息', '忽略空白，只平均有數值的儲存格', '自動填入 0 後計算'],
                'answer': 2,
                'explain': 'AVERAGE 自動忽略空白儲存格（和文字），只計算有數值的儲存格的平均。若要把空白視為 0，要先用 IF 轉換再計算。'
            },
        ]
    },
    'q2': {
        'title': '第二章 隨堂測驗',
        'questions': [
            {
                'q': 'VLOOKUP 的第三個參數（col_index_num）代表什麼？',
                'options': ['要搜尋的欄位編號', '要比對的精確度（0 or 1）', '查詢結果的格式', '要回傳的欄位編號（從查詢範圍最左欄算起）'],
                'answer': 3,
                'explain': 'VLOOKUP(查詢值, 資料範圍, 欄號, 完全比對)：第3個參數是「回傳範圍第幾欄的值」，從查詢範圍的最左欄（第1欄）算起。'
            },
            {
                'q': 'IF(A1>=60,"及格","不及格") 這個公式，當 A1=59 時會顯示什麼？',
                'options': ['及格', '不及格', '#VALUE!', '59'],
                'answer': 1,
                'explain': 'A1=59，條件 A1>=60 為 FALSE，所以回傳第三個參數「不及格」。IF 函數：=IF(條件, 條件為真時的值, 條件為假時的值)。'
            },
        ]
    },
    'q3': {
        'title': '第三章 隨堂測驗',
        'questions': [
            {
                'q': '樞紐分析表的「值」區域通常放什麼類型的欄位？',
                'options': ['文字欄位（如姓名、部門）', '數值欄位（如金額、分數、數量）', '日期欄位', '任意欄位都可以'],
                'answer': 1,
                'explain': '「值」區域放數值欄位，用來做加總、平均、計數等計算。「列」和「欄」放分類欄位（文字），「篩選」放要過濾的欄位。'
            },
            {
                'q': '建立樞紐分析表後，原始資料新增了幾列，樞紐分析表如何更新？',
                'options': ['右鍵→重新整理（或點「重新整理」按鈕）', '關掉再重開 Excel', '刪除舊的再重新建立', '樞紐分析表會自動即時更新'],
                'answer': 0,
                'explain': '樞紐分析表不會自動偵測原始資料的新增，需要手動「重新整理」。也可設定開啟檔案時自動重新整理。'
            },
        ]
    },
    'q4': {
        'title': '第四章 隨堂測驗',
        'questions': [
            {
                'q': '折線圖的趨勢線選擇「線性」，其代表的含意是什麼？',
                'options': ['資料呈現加速增長的曲線趨勢', '資料呈現週期性變化', '資料呈現固定速率的增長或減少趨勢', '資料完全隨機無規律'],
                'answer': 2,
                'explain': '線性趨勢線（y = mx + b）假設資料以固定速率增減，R² 值越接近 1 代表擬合度越好。若資料呈指數增長應選「指數」趨勢線。'
            },
            {
                'q': '想預測一個月後的銷售量，最適合使用 Excel 的哪個功能？',
                'options': ['VLOOKUP 查詢歷史資料', 'SUMIF 加總條件範圍', 'COUNTIF 計算符合條件數量', 'FORECAST.ETS 或趨勢線外插'],
                'answer': 3,
                'explain': 'FORECAST.ETS 使用指數平滑法（ETS 演算法）預測時間序列，Excel 365 的「預測工作表」功能可一鍵建立預測圖表，比手動外插更準確。'
            },
        ]
    },
}

SLIDES = [
    {
        'id': 1,
        'chapter': '封面',
        'title': '資料分析實作',
        'bg': 'navy',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<div style='text-align:center;padding:30px 20px;'>
  <div style='font-size:72px;margin-bottom:20px;'>📈</div>
  <h1 style='font-size:2.8rem;font-weight:900;color:#fff;margin-bottom:12px;'>資料分析實作</h1>
  <h2 style='font-size:1.5rem;font-weight:400;color:#93c5fd;margin-bottom:30px;'>Data Analysis in Practice</h2>
  <div style='display:flex;justify-content:center;gap:20px;flex-wrap:wrap;margin-bottom:30px;'>
    <span style='background:rgba(255,255,255,0.15);color:#e0f2fe;padding:8px 20px;border-radius:20px;font-size:1rem;'>📐 Excel 函數</span>
    <span style='background:rgba(255,255,255,0.15);color:#e0f2fe;padding:8px 20px;border-radius:20px;font-size:1rem;'>🔍 條件查詢</span>
    <span style='background:rgba(255,255,255,0.15);color:#e0f2fe;padding:8px 20px;border-radius:20px;font-size:1rem;'>🗂️ 樞紐分析表</span>
    <span style='background:rgba(255,255,255,0.15);color:#e0f2fe;padding:8px 20px;border-radius:20px;font-size:1rem;'>📉 趨勢預測</span>
  </div>
  <p style='color:#bfdbfe;font-size:1.1rem;'>城市科技 — 第九週</p>
</div>"""
    },
    {
        'id': 2,
        'chapter': '第一章：Excel 核心函數',
        'title': 'Excel 函數基礎',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>Excel 函數基礎</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;border-left:4px solid #2563eb;padding:15px;border-radius:8px;margin-bottom:15px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:8px;'>📌 函數基本語法</h3>
      <div style='background:#fff;padding:12px;border-radius:6px;font-family:monospace;text-align:center;'>
        <p style='font-size:1.1rem;color:#1e40af;font-weight:700;margin:0;'>=函數名稱(引數1, 引數2, ...)</p>
      </div>
      <ul style='color:#374151;font-size:0.9rem;padding-left:16px;margin-top:10px;'>
        <li>必須以 <strong>=</strong> 開頭</li>
        <li>引數用逗號分隔</li>
        <li>範圍用冒號：A1:A50</li>
        <li>文字引數用雙引號：&quot;及格&quot;</li>
      </ul>
    </div>
  </div>
  <div>
    <h3 style='color:#374151;font-size:1rem;margin-bottom:10px;'>⭐ 最常用 10 大函數</h3>
    <table style='width:100%;border-collapse:collapse;font-size:0.85rem;'>
      <tr style='background:#1e40af;color:#fff;'>
        <th style='padding:6px;text-align:left;'>函數</th>
        <th style='padding:6px;text-align:left;'>功能</th>
      </tr>
      <tr><td style='padding:6px;color:#1e40af;font-weight:700;font-family:monospace;'>SUM</td><td style='padding:6px;color:#374151;'>加總</td></tr>
      <tr style='background:#f8fafc;'><td style='padding:6px;color:#1e40af;font-weight:700;font-family:monospace;'>AVERAGE</td><td style='padding:6px;color:#374151;'>平均值</td></tr>
      <tr><td style='padding:6px;color:#1e40af;font-weight:700;font-family:monospace;'>COUNT/COUNTA</td><td style='padding:6px;color:#374151;'>計算數字/非空格數量</td></tr>
      <tr style='background:#f8fafc;'><td style='padding:6px;color:#1e40af;font-weight:700;font-family:monospace;'>MAX/MIN</td><td style='padding:6px;color:#374151;'>最大/最小值</td></tr>
      <tr><td style='padding:6px;color:#1e40af;font-weight:700;font-family:monospace;'>IF</td><td style='padding:6px;color:#374151;'>條件判斷</td></tr>
      <tr style='background:#f8fafc;'><td style='padding:6px;color:#1e40af;font-weight:700;font-family:monospace;'>COUNTIF/SUMIF</td><td style='padding:6px;color:#374151;'>條件計數/加總</td></tr>
      <tr><td style='padding:6px;color:#1e40af;font-weight:700;font-family:monospace;'>VLOOKUP</td><td style='padding:6px;color:#374151;'>垂直查詢</td></tr>
      <tr style='background:#f8fafc;'><td style='padding:6px;color:#1e40af;font-weight:700;font-family:monospace;'>TEXT</td><td style='padding:6px;color:#374151;'>格式化數字/日期</td></tr>
      <tr><td style='padding:6px;color:#1e40af;font-weight:700;font-family:monospace;'>RANK</td><td style='padding:6px;color:#374151;'>排名</td></tr>
      <tr style='background:#f8fafc;'><td style='padding:6px;color:#1e40af;font-weight:700;font-family:monospace;'>TRIM/UPPER/LOWER</td><td style='padding:6px;color:#374151;'>文字清理</td></tr>
    </table>
  </div>
</div>"""
    },
    {
        'id': 3,
        'chapter': '第一章：Excel 核心函數',
        'title': 'SUM、AVERAGE、COUNT 實例',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>SUM、AVERAGE、COUNT 實作</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <h3 style='color:#374151;font-size:1rem;margin-bottom:10px;'>📋 範例資料（全班成績）</h3>
    <table style='width:100%;border-collapse:collapse;font-size:0.85rem;'>
      <tr style='background:#1e40af;color:#fff;'>
        <th style='padding:7px;'>A：姓名</th><th style='padding:7px;'>B：數學</th><th style='padding:7px;'>C：國語</th><th style='padding:7px;'>D：英文</th>
      </tr>
      <tr><td style='padding:7px;color:#374151;'>小明</td><td style='padding:7px;text-align:center;color:#374151;'>85</td><td style='padding:7px;text-align:center;color:#374151;'>92</td><td style='padding:7px;text-align:center;color:#374151;'>78</td></tr>
      <tr style='background:#f8fafc;'><td style='padding:7px;color:#374151;'>小華</td><td style='padding:7px;text-align:center;color:#374151;'>72</td><td style='padding:7px;text-align:center;color:#374151;'>88</td><td style='padding:7px;text-align:center;color:#374151;'>95</td></tr>
      <tr><td style='padding:7px;color:#374151;'>小美</td><td style='padding:7px;text-align:center;color:#374151;'>90</td><td style='padding:7px;text-align:center;color:#374151;'>76</td><td style='padding:7px;text-align:center;color:#374151;'>82</td></tr>
      <tr style='background:#f8fafc;'><td style='padding:7px;color:#374151;'>⋮（到 B40）</td><td style='padding:7px;text-align:center;color:#6b7280;'>…</td><td style='padding:7px;text-align:center;color:#6b7280;'>…</td><td style='padding:7px;text-align:center;color:#6b7280;'>…</td></tr>
    </table>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:10px;'>✏️ 常用公式範例</h3>
      <div style='display:flex;flex-direction:column;gap:8px;'>
        <div style='background:#fff;padding:8px;border-radius:6px;'>
          <p style='color:#15803d;font-weight:700;font-size:0.85rem;margin:0;'>E2 = 小明總分</p>
          <code style='color:#374151;font-size:0.8rem;'>= SUM(B2:D2)</code>
          <p style='color:#6b7280;font-size:0.75rem;margin:2px 0 0;'>→ 85+92+78 = 255</p>
        </div>
        <div style='background:#fff;padding:8px;border-radius:6px;'>
          <p style='color:#15803d;font-weight:700;font-size:0.85rem;margin:0;'>F2 = 小明平均</p>
          <code style='color:#374151;font-size:0.8rem;'>= AVERAGE(B2:D2)</code>
          <p style='color:#6b7280;font-size:0.75rem;margin:2px 0 0;'>→ 85 分</p>
        </div>
        <div style='background:#fff;padding:8px;border-radius:6px;'>
          <p style='color:#15803d;font-weight:700;font-size:0.85rem;margin:0;'>B42 = 全班數學平均</p>
          <code style='color:#374151;font-size:0.8rem;'>= AVERAGE(B2:B41)</code>
        </div>
        <div style='background:#fff;padding:8px;border-radius:6px;'>
          <p style='color:#15803d;font-weight:700;font-size:0.85rem;margin:0;'>全班人數</p>
          <code style='color:#374151;font-size:0.8rem;'>= COUNTA(A2:A41)</code>
          <p style='color:#6b7280;font-size:0.75rem;margin:2px 0 0;'>→ 計算非空格（含文字）</p>
        </div>
      </div>
    </div>
  </div>
</div>"""
    },
    {
        'id': 4,
        'chapter': '第一章：Excel 核心函數',
        'title': 'COUNTIF 與 SUMIF',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>COUNTIF 與 SUMIF — 條件統計</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>🔢 COUNTIF — 條件計數</h3>
      <div style='background:#fff;padding:10px;border-radius:6px;margin-bottom:8px;font-family:monospace;'>
        <p style='color:#1e40af;font-size:0.85rem;margin:0;'>=COUNTIF(範圍, 條件)</p>
      </div>
      <div style='display:flex;flex-direction:column;gap:6px;'>
        <div style='background:#dbeafe;padding:8px;border-radius:6px;'>
          <p style='color:#374151;font-size:0.85rem;margin:0;'>及格人數（≥60）：<code>=COUNTIF(B2:B41,">=60")</code></p>
        </div>
        <div style='background:#dbeafe;padding:8px;border-radius:6px;'>
          <p style='color:#374151;font-size:0.85rem;margin:0;'>A 班人數：<code>=COUNTIF(C2:C41,"A班")</code></p>
        </div>
        <div style='background:#dbeafe;padding:8px;border-radius:6px;'>
          <p style='color:#374151;font-size:0.85rem;margin:0;'>不及格人數：<code>=COUNTIF(B2:B41,"&lt;60")</code></p>
        </div>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:10px;'>➕ SUMIF — 條件加總</h3>
      <div style='background:#fff;padding:10px;border-radius:6px;margin-bottom:8px;font-family:monospace;'>
        <p style='color:#15803d;font-size:0.85rem;margin:0;'>=SUMIF(條件範圍, 條件, 加總範圍)</p>
      </div>
      <div style='display:flex;flex-direction:column;gap:6px;'>
        <div style='background:#dcfce7;padding:8px;border-radius:6px;'>
          <p style='color:#374151;font-size:0.85rem;margin:0;'>A 班總分：<code>=SUMIF(C2:C41,"A班",B2:B41)</code></p>
        </div>
        <div style='background:#dcfce7;padding:8px;border-radius:6px;'>
          <p style='color:#374151;font-size:0.85rem;margin:0;'>80 分以上的成績總和：<code>=SUMIF(B2:B41,">=80",B2:B41)</code></p>
        </div>
      </div>
    </div>
    <div style='background:#fff7ed;padding:10px;border-radius:8px;'>
      <p style='color:#9a3412;font-size:0.85rem;margin:0;'>💡 <strong>COUNTIFS / SUMIFS</strong>（加 S）可設定多個條件，例如「A 班且成績≥80」：<br><code style='font-size:0.8rem;'>=COUNTIFS(班級範圍,"A班",成績範圍,">=80")</code></p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 5,
        'chapter': '第一章：Excel 核心函數',
        'title': 'RANK 與 PERCENTRANK',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>RANK 排名函數</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>🏆 RANK 函數</h3>
      <div style='background:#fff;padding:10px;border-radius:6px;margin-bottom:10px;font-family:monospace;'>
        <p style='color:#1e40af;font-size:0.85rem;margin:0;'>=RANK(數值, 參考範圍, 0 or 1)</p>
      </div>
      <ul style='color:#374151;font-size:0.9rem;padding-left:16px;'>
        <li>第 3 個引數 <strong>0</strong> = 由大到小排名（高分第 1）</li>
        <li>第 3 個引數 <strong>1</strong> = 由小到大排名（低分第 1）</li>
        <li>範圍加 <strong>$</strong> 鎖定（絕對參照），才能往下複製</li>
      </ul>
      <div style='background:#dbeafe;padding:8px;border-radius:6px;margin-top:8px;'>
        <p style='color:#374151;font-size:0.85rem;margin:0;'>E2 = 小明成績排名：<br><code>=RANK(B2, $B$2:$B$41, 0)</code></p>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:10px;'>📊 絕對參照 vs 相對參照</h3>
      <table style='width:100%;border-collapse:collapse;font-size:0.85rem;'>
        <tr style='background:#15803d;color:#fff;'>
          <th style='padding:6px;'>符號</th><th style='padding:6px;'>說明</th>
        </tr>
        <tr><td style='padding:6px;font-weight:700;color:#374151;'>A1</td><td style='padding:6px;color:#374151;'>相對參照，複製時隨位置變動</td></tr>
        <tr style='background:#f0fdf4;'><td style='padding:6px;font-weight:700;color:#374151;'>$A$1</td><td style='padding:6px;color:#374151;'>絕對參照，複製時固定不變</td></tr>
        <tr><td style='padding:6px;font-weight:700;color:#374151;'>$A1</td><td style='padding:6px;color:#374151;'>鎖欄不鎖列</td></tr>
        <tr style='background:#f0fdf4;'><td style='padding:6px;font-weight:700;color:#374151;'>A$1</td><td style='padding:6px;color:#374151;'>鎖列不鎖欄</td></tr>
      </table>
      <div style='background:#dcfce7;padding:8px;border-radius:6px;margin-top:8px;'>
        <p style='color:#15803d;font-size:0.85rem;margin:0;'>💡 按 <strong>F4</strong> 鍵可快速切換四種參照模式！</p>
      </div>
    </div>
  </div>
</div>"""
    },
    {
        'id': 6,
        'chapter': '第一章：Excel 核心函數',
        'title': '成績等第換算',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>成績等第換算</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>🔤 IFS 多條件判斷（Excel 2019+）</h3>
      <div style='background:#fff;padding:10px;border-radius:6px;font-family:monospace;font-size:0.8rem;'>
        <p style='color:#1e40af;margin:0;'>=IFS(</p>
        <p style='color:#374151;margin:2px 0;'>  B2>=90, "A",</p>
        <p style='color:#374151;margin:2px 0;'>  B2>=80, "B",</p>
        <p style='color:#374151;margin:2px 0;'>  B2>=70, "C",</p>
        <p style='color:#374151;margin:2px 0;'>  B2>=60, "D",</p>
        <p style='color:#374151;margin:2px 0;'>  TRUE, "F"</p>
        <p style='color:#1e40af;margin:0;'>)</p>
      </div>
    </div>
    <div style='background:#f0fdf4;padding:12px;border-radius:8px;'>
      <h3 style='color:#15803d;font-size:0.95rem;margin-bottom:6px;'>🔢 VLOOKUP 等第表查詢</h3>
      <p style='color:#374151;font-size:0.85rem;'>建立等第對應表，VLOOKUP 自動比對（最後一個引數填 1 = 近似比對）</p>
    </div>
  </div>
  <div>
    <div style='background:#fdf4ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#7c3aed;font-size:1rem;margin-bottom:10px;'>📋 等第換算表</h3>
      <table style='width:100%;border-collapse:collapse;font-size:0.85rem;'>
        <tr style='background:#7c3aed;color:#fff;'>
          <th style='padding:7px;'>分數範圍</th><th style='padding:7px;'>等第</th><th style='padding:7px;'>說明</th>
        </tr>
        <tr><td style='padding:7px;text-align:center;color:#374151;'>90-100</td><td style='padding:7px;text-align:center;'><span style='background:#dcfce7;color:#15803d;padding:2px 8px;border-radius:4px;font-weight:700;'>A</span></td><td style='padding:7px;color:#374151;'>優秀</td></tr>
        <tr style='background:#f9fafb;'><td style='padding:7px;text-align:center;color:#374151;'>80-89</td><td style='padding:7px;text-align:center;'><span style='background:#dbeafe;color:#1e40af;padding:2px 8px;border-radius:4px;font-weight:700;'>B</span></td><td style='padding:7px;color:#374151;'>良好</td></tr>
        <tr><td style='padding:7px;text-align:center;color:#374151;'>70-79</td><td style='padding:7px;text-align:center;'><span style='background:#fef9c3;color:#854d0e;padding:2px 8px;border-radius:4px;font-weight:700;'>C</span></td><td style='padding:7px;color:#374151;'>普通</td></tr>
        <tr style='background:#f9fafb;'><td style='padding:7px;text-align:center;color:#374151;'>60-69</td><td style='padding:7px;text-align:center;'><span style='background:#fff7ed;color:#ea580c;padding:2px 8px;border-radius:4px;font-weight:700;'>D</span></td><td style='padding:7px;color:#374151;'>及格</td></tr>
        <tr><td style='padding:7px;text-align:center;color:#374151;'>0-59</td><td style='padding:7px;text-align:center;'><span style='background:#fee2e2;color:#dc2626;padding:2px 8px;border-radius:4px;font-weight:700;'>F</span></td><td style='padding:7px;color:#374151;'>不及格</td></tr>
      </table>
    </div>
  </div>
</div>"""
    },
    {
        'id': 7,
        'chapter': '第一章：Excel 核心函數',
        'title': '🎯 第一章 隨堂測驗',
        'bg': 'purple',
        'quiz': 'q1',
        'chart': None,
        'video': None,
        'html': """
<div style='text-align:center;padding:20px;'>
  <div style='font-size:56px;margin-bottom:15px;'>🎯</div>
  <h2 style='color:#fff;font-size:2rem;font-weight:800;margin-bottom:10px;'>第一章 隨堂測驗</h2>
  <p style='color:#e9d5ff;font-size:1.1rem;'>Excel 核心函數 ── 2 道題目，點擊作答！</p>
</div>"""
    },
    {
        'id': 8,
        'chapter': '第二章：條件判斷與查詢',
        'title': 'IF 函數',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>IF 函數 — 條件判斷</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>🔀 IF 基本語法</h3>
      <div style='background:#fff;padding:10px;border-radius:6px;margin-bottom:10px;text-align:center;'>
        <p style='font-family:monospace;font-size:0.9rem;color:#1e40af;margin:0;'>=IF(條件, 為真回傳值, 為假回傳值)</p>
      </div>
      <div style='background:#dbeafe;padding:8px;border-radius:6px;margin-bottom:6px;'>
        <p style='color:#374151;font-size:0.85rem;margin:0;'>及格判斷：<code>=IF(B2>=60,"及格","不及格")</code></p>
      </div>
      <div style='background:#dbeafe;padding:8px;border-radius:6px;'>
        <p style='color:#374151;font-size:0.85rem;margin:0;'>出席獎勵：<code>=IF(C2>=27,"優良","一般")</code></p>
      </div>
    </div>
    <div style='background:#f0fdf4;padding:12px;border-radius:8px;'>
      <h3 style='color:#15803d;font-size:0.95rem;margin-bottom:8px;'>🔗 巢狀 IF（多層條件）</h3>
      <div style='background:#fff;padding:8px;border-radius:6px;font-family:monospace;font-size:0.8rem;'>
        <p style='color:#374151;margin:0;'>=IF(B2>=80,"優",</p>
        <p style='color:#374151;margin:2px 0 2px 16px;'>IF(B2>=60,"及格","不及格"))</p>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#fff7ed;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#ea580c;font-size:1rem;margin-bottom:10px;'>⚡ AND / OR 結合 IF</h3>
      <div style='display:flex;flex-direction:column;gap:8px;'>
        <div style='background:#fff;padding:8px;border-radius:6px;'>
          <p style='font-weight:700;color:#ea580c;font-size:0.85rem;margin:0;'>AND（且）— 全部條件都成立</p>
          <code style='color:#374151;font-size:0.8rem;'>= IF(AND(B2>=60, C2>=60), "雙科及格", "待補考")</code>
        </div>
        <div style='background:#fff;padding:8px;border-radius:6px;'>
          <p style='font-weight:700;color:#ea580c;font-size:0.85rem;margin:0;'>OR（或）— 任一條件成立</p>
          <code style='color:#374151;font-size:0.8rem;'>= IF(OR(B2>=90, C2>=90), "至少一科優秀", "普通")</code>
        </div>
      </div>
    </div>
    <div style='background:#fdf4ff;padding:10px;border-radius:8px;'>
      <p style='color:#7c3aed;font-size:0.85rem;margin:0;'>💡 <strong>生活應用</strong>：大學申請入學「國文 AND 英文都達門檻，OR 總分超過 X 分，才資格審核通過」的判斷。</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 9,
        'chapter': '第二章：條件判斷與查詢',
        'title': 'VLOOKUP 查詢函數',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': {'url': 'https://www.youtube.com/embed/d3BYVQ6xIE4', 'title': 'VLOOKUP 教學', 'desc': '學會 VLOOKUP 讓你的 Excel 技能大幅提升'},
        'html': """
<h2 class='slide-title'>VLOOKUP 查詢函數</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>🔍 VLOOKUP 語法</h3>
      <div style='background:#fff;padding:10px;border-radius:6px;margin-bottom:8px;text-align:center;'>
        <p style='font-family:monospace;font-size:0.85rem;color:#1e40af;margin:0;'>=VLOOKUP(查詢值, 資料範圍, 欄號, 0)</p>
      </div>
      <ul style='color:#374151;font-size:0.85rem;padding-left:16px;'>
        <li><strong>查詢值</strong>：要找什麼（如學號 A2）</li>
        <li><strong>資料範圍</strong>：在哪裡找（如 $F$2:$H$100）</li>
        <li><strong>欄號</strong>：回傳第幾欄（從範圍最左欄算）</li>
        <li><strong>0</strong>：完全比對（FALSE）</li>
      </ul>
    </div>
    <div style='background:#dcfce7;padding:10px;border-radius:6px;'>
      <p style='color:#15803d;font-size:0.85rem;margin:0;'>範例：<code>=VLOOKUP(A2,$F$2:$H$100,2,0)</code><br>→ 在 F~H 欄查學號，回傳第 2 欄（姓名）</p>
    </div>
  </div>
  <div>
    <div style='background:#fef9c3;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#854d0e;font-size:1rem;margin-bottom:10px;'>💡 VLOOKUP 使用情境</h3>
      <div style='display:flex;flex-direction:column;gap:8px;'>
        <div style='background:#fff;padding:8px;border-radius:6px;'>
          <p style='font-size:0.85rem;color:#374151;margin:0;'>🏫 用學號查詢班級或姓名</p>
        </div>
        <div style='background:#fff;padding:8px;border-radius:6px;'>
          <p style='font-size:0.85rem;color:#374151;margin:0;'>🏪 用商品代碼查詢商品名稱和價格</p>
        </div>
        <div style='background:#fff;padding:8px;border-radius:6px;'>
          <p style='font-size:0.85rem;color:#374151;margin:0;'>💰 用員工 ID 查詢部門和薪資</p>
        </div>
      </div>
    </div>
    <div style='background:#fef2f2;padding:10px;border-radius:8px;'>
      <p style='color:#dc2626;font-size:0.85rem;margin:0;'>⚠️ <strong>常見錯誤</strong>：範圍沒加 $ 鎖定，往下複製時範圍跑掉；查詢值不在資料範圍最左欄，會回傳 #N/A 錯誤。</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 10,
        'chapter': '第二章：條件判斷與查詢',
        'title': 'TEXT 與日期函數',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>文字與日期函數</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>📝 文字函數</h3>
      <div style='display:flex;flex-direction:column;gap:6px;'>
        <div style='background:#fff;padding:8px;border-radius:6px;'>
          <code style='color:#1e40af;font-size:0.85rem;'>LEFT(A1, 3)</code>
          <p style='color:#374151;font-size:0.8rem;margin:2px 0 0;'>取左邊 3 個字元</p>
        </div>
        <div style='background:#fff;padding:8px;border-radius:6px;'>
          <code style='color:#1e40af;font-size:0.85rem;'>RIGHT(A1, 4)</code>
          <p style='color:#374151;font-size:0.8rem;margin:2px 0 0;'>取右邊 4 個字元</p>
        </div>
        <div style='background:#fff;padding:8px;border-radius:6px;'>
          <code style='color:#1e40af;font-size:0.85rem;'>LEN(A1)</code>
          <p style='color:#374151;font-size:0.8rem;margin:2px 0 0;'>計算字元長度</p>
        </div>
        <div style='background:#fff;padding:8px;border-radius:6px;'>
          <code style='color:#1e40af;font-size:0.85rem;'>&amp; 運算符</code>
          <p style='color:#374151;font-size:0.8rem;margin:2px 0 0;'>串接文字：=A1&amp;"同學"</p>
        </div>
        <div style='background:#fff;padding:8px;border-radius:6px;'>
          <code style='color:#1e40af;font-size:0.85rem;'>TEXT(A1,"0.00%")</code>
          <p style='color:#374151;font-size:0.8rem;margin:2px 0 0;'>格式化：0.856 → 85.60%</p>
        </div>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:10px;'>📅 日期函數</h3>
      <div style='display:flex;flex-direction:column;gap:6px;'>
        <div style='background:#fff;padding:8px;border-radius:6px;'>
          <code style='color:#15803d;font-size:0.85rem;'>TODAY()</code>
          <p style='color:#374151;font-size:0.8rem;margin:2px 0 0;'>今天日期（每天自動更新）</p>
        </div>
        <div style='background:#fff;padding:8px;border-radius:6px;'>
          <code style='color:#15803d;font-size:0.85rem;'>YEAR(A1) / MONTH() / DAY()</code>
          <p style='color:#374151;font-size:0.8rem;margin:2px 0 0;'>取出年/月/日</p>
        </div>
        <div style='background:#fff;padding:8px;border-radius:6px;'>
          <code style='color:#15803d;font-size:0.85rem;'>DATEDIF(A1,B1,"D")</code>
          <p style='color:#374151;font-size:0.8rem;margin:2px 0 0;'>計算兩日期相差天數</p>
        </div>
        <div style='background:#dcfce7;padding:8px;border-radius:6px;'>
          <p style='color:#374151;font-size:0.85rem;margin:0;'>🎂 計算年齡：<code>=DATEDIF(生日,TODAY(),"Y")</code></p>
        </div>
      </div>
    </div>
  </div>
</div>"""
    },
    {
        'id': 11,
        'chapter': '第二章：條件判斷與查詢',
        'title': '條件式格式設定',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>條件式格式設定</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>🎨 條件式格式設定（Conditional Formatting）</h3>
      <p style='color:#374151;font-size:0.9rem;margin-bottom:8px;'>根據儲存格數值自動套用顏色或圖示，快速識別重要資訊。</p>
      <ol style='color:#374151;font-size:0.85rem;padding-left:18px;'>
        <li>選取要格式化的範圍</li>
        <li>常用 → 條件式格式設定</li>
        <li>選擇規則類型</li>
        <li>設定條件和顏色</li>
      </ol>
    </div>
  </div>
  <div>
    <div style='background:#f9fafb;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#374151;font-size:1rem;margin-bottom:10px;'>✨ 視覺效果展示</h3>
      <p style='color:#374151;font-size:0.85rem;margin-bottom:8px;'>成績表條件式格式設定範例：</p>
      <div style='display:flex;flex-direction:column;gap:5px;'>
        <div style='display:flex;gap:8px;align-items:center;'>
          <span style='background:#dcfce7;color:#15803d;padding:4px 12px;border-radius:4px;font-weight:700;font-size:0.85rem;'>95</span>
          <span style='color:#374151;font-size:0.85rem;'>≥90：綠色</span>
        </div>
        <div style='display:flex;gap:8px;align-items:center;'>
          <span style='background:#dbeafe;color:#1e40af;padding:4px 12px;border-radius:4px;font-weight:700;font-size:0.85rem;'>82</span>
          <span style='color:#374151;font-size:0.85rem;'>80-89：藍色</span>
        </div>
        <div style='display:flex;gap:8px;align-items:center;'>
          <span style='background:#fef9c3;color:#854d0e;padding:4px 12px;border-radius:4px;font-weight:700;font-size:0.85rem;'>65</span>
          <span style='color:#374151;font-size:0.85rem;'>60-79：黃色</span>
        </div>
        <div style='display:flex;gap:8px;align-items:center;'>
          <span style='background:#fee2e2;color:#dc2626;padding:4px 12px;border-radius:4px;font-weight:700;font-size:0.85rem;'>45</span>
          <span style='color:#374151;font-size:0.85rem;'>&lt;60：紅色（不及格）</span>
        </div>
      </div>
      <div style='background:#eff6ff;padding:8px;border-radius:6px;margin-top:10px;'>
        <p style='color:#1e40af;font-size:0.8rem;margin:0;'>💡 「資料橫條」和「色階」可讓數值大小一目了然！</p>
      </div>
    </div>
  </div>
</div>"""
    },
    {
        'id': 12,
        'chapter': '第二章：條件判斷與查詢',
        'title': '🎯 第二章 隨堂測驗',
        'bg': 'purple',
        'quiz': 'q2',
        'chart': None,
        'video': None,
        'html': """
<div style='text-align:center;padding:20px;'>
  <div style='font-size:56px;margin-bottom:15px;'>🎯</div>
  <h2 style='color:#fff;font-size:2rem;font-weight:800;margin-bottom:10px;'>第二章 隨堂測驗</h2>
  <p style='color:#e9d5ff;font-size:1.1rem;'>條件判斷與查詢 ── 2 道題目，點擊作答！</p>
</div>"""
    },
    {
        'id': 13,
        'chapter': '第三章：樞紐分析表',
        'title': '樞紐分析表簡介',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>樞紐分析表（Pivot Table）</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;border-left:4px solid #2563eb;padding:15px;border-radius:8px;margin-bottom:15px;'>
      <h3 style='color:#1e40af;font-size:1.1rem;margin-bottom:8px;'>🗂️ 什麼是樞紐分析表？</h3>
      <p style='color:#374151;font-size:0.95rem;'>可以<strong>快速彙總、分組和計算</strong>大量資料，用拖放方式改變資料的呈現角度，不需要寫公式。</p>
    </div>
    <div style='background:#f0fdf4;padding:12px;border-radius:8px;'>
      <h3 style='color:#15803d;font-size:0.95rem;margin-bottom:8px;'>📍 建立方式</h3>
      <ol style='color:#374151;font-size:0.85rem;padding-left:18px;margin:0;'>
        <li>選取資料範圍（含標題）</li>
        <li>插入 → 樞紐分析表</li>
        <li>選擇放置位置（新工作表）</li>
        <li>在右側面板拖曳欄位</li>
      </ol>
    </div>
  </div>
  <div>
    <div style='background:#fdf4ff;padding:15px;border-radius:10px;'>
      <h3 style='color:#7c3aed;font-size:1rem;margin-bottom:12px;'>🎯 四個區域的作用</h3>
      <div style='display:grid;grid-template-columns:1fr 1fr;gap:8px;'>
        <div style='background:#fff;padding:10px;border-radius:8px;border:2px solid #7c3aed;text-align:center;'>
          <p style='font-weight:700;color:#7c3aed;font-size:0.85rem;margin:0;'>🔽 篩選</p>
          <p style='color:#374151;font-size:0.75rem;margin:4px 0 0;'>整個報表的篩選條件（如：學年度）</p>
        </div>
        <div style='background:#fff;padding:10px;border-radius:8px;border:2px solid #2563eb;text-align:center;'>
          <p style='font-weight:700;color:#2563eb;font-size:0.85rem;margin:0;'>➡️ 欄</p>
          <p style='color:#374151;font-size:0.75rem;margin:4px 0 0;'>橫向分組（如：學期）</p>
        </div>
        <div style='background:#fff;padding:10px;border-radius:8px;border:2px solid #16a34a;text-align:center;'>
          <p style='font-weight:700;color:#16a34a;font-size:0.85rem;margin:0;'>⬇️ 列</p>
          <p style='color:#374151;font-size:0.75rem;margin:4px 0 0;'>縱向分組（如：班級）</p>
        </div>
        <div style='background:#fff;padding:10px;border-radius:8px;border:2px solid #ea580c;text-align:center;'>
          <p style='font-weight:700;color:#ea580c;font-size:0.85rem;margin:0;'>🔢 值</p>
          <p style='color:#374151;font-size:0.75rem;margin:4px 0 0;'>計算結果（加總/平均/計數）</p>
        </div>
      </div>
    </div>
  </div>
</div>"""
    },
    {
        'id': 14,
        'chapter': '第三章：樞紐分析表',
        'title': '樞紐分析表實作',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>樞紐分析表實作範例</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <h3 style='color:#374151;font-size:1rem;margin-bottom:10px;'>📋 原始資料（成績表）</h3>
    <table style='width:100%;border-collapse:collapse;font-size:0.8rem;'>
      <tr style='background:#374151;color:#fff;'>
        <th style='padding:6px;'>姓名</th><th style='padding:6px;'>班級</th><th style='padding:6px;'>科目</th><th style='padding:6px;'>成績</th>
      </tr>
      <tr><td style='padding:6px;color:#374151;'>小明</td><td style='padding:6px;color:#374151;'>A班</td><td style='padding:6px;color:#374151;'>數學</td><td style='padding:6px;text-align:right;color:#374151;'>85</td></tr>
      <tr style='background:#f9fafb;'><td style='padding:6px;color:#374151;'>小明</td><td style='padding:6px;color:#374151;'>A班</td><td style='padding:6px;color:#374151;'>國語</td><td style='padding:6px;text-align:right;color:#374151;'>92</td></tr>
      <tr><td style='padding:6px;color:#374151;'>小華</td><td style='padding:6px;color:#374151;'>B班</td><td style='padding:6px;color:#374151;'>數學</td><td style='padding:6px;text-align:right;color:#374151;'>78</td></tr>
      <tr style='background:#f9fafb;'><td style='padding:6px;color:#374151;'>小美</td><td style='padding:6px;color:#374151;'>A班</td><td style='padding:6px;color:#374151;'>數學</td><td style='padding:6px;text-align:right;color:#374151;'>90</td></tr>
      <tr><td style='padding:6px;color:#6b7280;'>⋮ 更多資料 ⋮</td><td style='padding:6px;'></td><td style='padding:6px;'></td><td style='padding:6px;'></td></tr>
    </table>
  </div>
  <div>
    <h3 style='color:#374151;font-size:1rem;margin-bottom:10px;'>📊 樞紐分析表結果</h3>
    <p style='color:#6b7280;font-size:0.8rem;margin-bottom:8px;'>設定：列=班級，欄=科目，值=平均成績</p>
    <table style='width:100%;border-collapse:collapse;font-size:0.85rem;'>
      <tr style='background:#1e40af;color:#fff;'>
        <th style='padding:7px;'>班級</th><th style='padding:7px;text-align:center;'>數學</th><th style='padding:7px;text-align:center;'>國語</th><th style='padding:7px;text-align:center;'>英文</th>
      </tr>
      <tr><td style='padding:7px;font-weight:700;color:#374151;'>A班</td><td style='padding:7px;text-align:center;color:#374151;'>85.2</td><td style='padding:7px;text-align:center;color:#374151;'>88.4</td><td style='padding:7px;text-align:center;color:#374151;'>82.1</td></tr>
      <tr style='background:#f8fafc;'><td style='padding:7px;font-weight:700;color:#374151;'>B班</td><td style='padding:7px;text-align:center;color:#374151;'>79.8</td><td style='padding:7px;text-align:center;color:#374151;'>82.6</td><td style='padding:7px;text-align:center;color:#374151;'>86.3</td></tr>
      <tr><td style='padding:7px;font-weight:700;color:#374151;'>C班</td><td style='padding:7px;text-align:center;color:#374151;'>83.1</td><td style='padding:7px;text-align:center;color:#374151;'>79.2</td><td style='padding:7px;text-align:center;color:#374151;'>88.7</td></tr>
      <tr style='background:#eff6ff;'><td style='padding:7px;font-weight:700;color:#1e40af;'>總計</td><td style='padding:7px;text-align:center;color:#1e40af;font-weight:700;'>82.7</td><td style='padding:7px;text-align:center;color:#1e40af;font-weight:700;'>83.4</td><td style='padding:7px;text-align:center;color:#1e40af;font-weight:700;'>85.7</td></tr>
    </table>
    <div style='background:#f0fdf4;padding:8px;border-radius:6px;margin-top:10px;'>
      <p style='color:#15803d;font-size:0.8rem;margin:0;'>✅ 不用寫任何公式，拖曳幾個欄位就得到完整的班級科目平均分析！</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 15,
        'chapter': '第三章：樞紐分析表',
        'title': '樞紐分析表進階功能',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>樞紐分析表進階功能</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>🔢 值計算方式</h3>
      <table style='width:100%;border-collapse:collapse;font-size:0.85rem;'>
        <tr style='background:#1e40af;color:#fff;'>
          <th style='padding:6px;'>選項</th><th style='padding:6px;'>說明</th>
        </tr>
        <tr><td style='padding:6px;color:#374151;'>加總</td><td style='padding:6px;color:#374151;'>SUM，預設選項</td></tr>
        <tr style='background:#f8fafc;'><td style='padding:6px;color:#374151;'>計數</td><td style='padding:6px;color:#374151;'>COUNT，統計筆數</td></tr>
        <tr><td style='padding:6px;color:#374151;'>平均值</td><td style='padding:6px;color:#374151;'>AVERAGE</td></tr>
        <tr style='background:#f8fafc;'><td style='padding:6px;color:#374151;'>最大值/最小值</td><td style='padding:6px;color:#374151;'>MAX / MIN</td></tr>
        <tr><td style='padding:6px;color:#374151;'>總計百分比</td><td style='padding:6px;color:#374151;'>各項佔總計 %</td></tr>
      </table>
    </div>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:10px;'>⚙️ 實用技巧</h3>
      <ul style='color:#374151;font-size:0.9rem;padding-left:16px;'>
        <li><strong>交叉分析篩選器</strong>：視覺化篩選按鈕，點選即篩</li>
        <li><strong>群組</strong>：日期自動群組成月/季/年</li>
        <li><strong>計算欄位</strong>：加入自訂公式（如利潤率 = 利潤/收入）</li>
        <li><strong>樞紐分析圖</strong>：直接從樞紐表生成圖表</li>
        <li><strong>格式</strong>：右鍵→值的顯示方式→百分比</li>
      </ul>
    </div>
    <div style='background:#fff7ed;padding:10px;border-radius:8px;'>
      <p style='color:#9a3412;font-size:0.85rem;margin:0;'>🇹🇼 <strong>職場實用</strong>：打開 104 人力銀行，行銷、業務、企劃類職缺大量要求「熟悉 Excel 樞紐分析表」，這是職場最實用的資料技能之一。</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 16,
        'chapter': '第三章：樞紐分析表',
        'title': 'Google 試算表樞紐分析',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>Google 試算表樞紐分析</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>📌 Google 試算表操作</h3>
      <ol style='color:#374151;font-size:0.9rem;padding-left:18px;'>
        <li>選取資料範圍</li>
        <li>插入 → 樞紐分析表</li>
        <li>在右側「樞紐分析表編輯器」設定</li>
        <li>新增「列」、「欄」、「值」欄位</li>
        <li>AI 功能：點「建議」自動產生分析</li>
      </ol>
    </div>
    <div style='background:#f0fdf4;padding:10px;border-radius:8px;'>
      <p style='color:#15803d;font-size:0.85rem;margin:0;'>✅ Google 試算表的樞紐分析與 Excel 功能幾乎相同，且可多人即時協作！</p>
    </div>
  </div>
  <div>
    <div style='background:#fdf4ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#7c3aed;font-size:1rem;margin-bottom:10px;'>🤖 Gemini AI 輔助分析</h3>
      <p style='color:#374151;font-size:0.9rem;margin-bottom:8px;'>2024 年 Google 試算表整合 Gemini AI，可以直接用文字指令分析資料：</p>
      <div style='background:#fff;padding:10px;border-radius:6px;font-style:italic;border-left:3px solid #7c3aed;'>
        <p style='color:#374151;font-size:0.85rem;margin:0;'>「請計算各班的數學平均成績，並找出最高分的班級」</p>
      </div>
      <div style='background:#e9d5ff;padding:8px;border-radius:6px;margin-top:8px;'>
        <p style='color:#374151;font-size:0.8rem;margin:0;'>→ Gemini 自動建立樞紐表並回答問題！</p>
      </div>
    </div>
    <div style='background:#fff7ed;padding:10px;border-radius:8px;'>
      <p style='color:#9a3412;font-size:0.85rem;margin:0;'>💡 AI 輔助並非取代分析能力，理解資料結構仍然很重要，才能判斷 AI 給的答案是否正確！</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 17,
        'chapter': '第三章：樞紐分析表',
        'title': '🎯 第三章 隨堂測驗',
        'bg': 'purple',
        'quiz': 'q3',
        'chart': None,
        'video': None,
        'html': """
<div style='text-align:center;padding:20px;'>
  <div style='font-size:56px;margin-bottom:15px;'>🎯</div>
  <h2 style='color:#fff;font-size:2rem;font-weight:800;margin-bottom:10px;'>第三章 隨堂測驗</h2>
  <p style='color:#e9d5ff;font-size:1.1rem;'>樞紐分析表 ── 2 道題目，點擊作答！</p>
</div>"""
    },
    {
        'id': 18,
        'chapter': '第四章：圖表與預測',
        'title': '圖表類型選擇',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>從資料到圖表 — 選對類型</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#f9fafb;padding:15px;border-radius:10px;margin-bottom:12px;border:1px solid #e5e7eb;'>
      <h3 style='color:#374151;font-size:1rem;margin-bottom:10px;'>📊 成績分析適用圖表</h3>
      <div style='display:flex;flex-direction:column;gap:8px;'>
        <div style='background:#eff6ff;padding:10px;border-radius:6px;'>
          <p style='font-weight:700;color:#1e40af;font-size:0.85rem;margin:0;'>📊 長條圖</p>
          <p style='color:#374151;font-size:0.8rem;margin:2px 0 0;'>比較各班/各科平均成績</p>
        </div>
        <div style='background:#f0fdf4;padding:10px;border-radius:6px;'>
          <p style='font-weight:700;color:#15803d;font-size:0.85rem;margin:0;'>📈 折線圖</p>
          <p style='color:#374151;font-size:0.8rem;margin:2px 0 0;'>觀察學生各次考試成績趨勢</p>
        </div>
        <div style='background:#fdf4ff;padding:10px;border-radius:6px;'>
          <p style='font-weight:700;color:#7c3aed;font-size:0.85rem;margin:0;'>🔵 散佈圖</p>
          <p style='color:#374151;font-size:0.8rem;margin:2px 0 0;'>出席率 vs 成績的相關性</p>
        </div>
        <div style='background:#fef9c3;padding:10px;border-radius:6px;'>
          <p style='font-weight:700;color:#854d0e;font-size:0.85rem;margin:0;'>📦 直方圖</p>
          <p style='color:#374151;font-size:0.8rem;margin:2px 0 0;'>全班成績分布（幾個人落在各分數段）</p>
        </div>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#fef2f2;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#dc2626;font-size:1rem;margin-bottom:8px;'>❌ 不適合的圖表</h3>
      <ul style='color:#374151;font-size:0.9rem;padding-left:16px;'>
        <li>成績比較 ❌ 圓餅圖（圓餅不適合比較大小，適合比例）</li>
        <li>多人成績 ❌ 雷達圖（類別超過 5 個就很難讀）</li>
        <li>3D 效果 ❌（扭曲視覺比例，讓判讀更困難）</li>
      </ul>
    </div>
    <div style='background:#f0fdf4;padding:10px;border-radius:8px;'>
      <p style='color:#15803d;font-size:0.85rem;margin:0;'>✅ <strong>決策原則</strong>：圖表的目的是「幫助理解」，不是「看起來很炫」。最清楚的圖表往往是最簡單的。</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 19,
        'chapter': '第四章：圖表與預測',
        'title': '趨勢線與預測',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>趨勢線與預測</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>📉 加入趨勢線步驟</h3>
      <ol style='color:#374151;font-size:0.9rem;padding-left:18px;'>
        <li>選取折線圖或散佈圖</li>
        <li>右鍵圖表 → 加入趨勢線</li>
        <li>選擇類型（線性、指數、多項式）</li>
        <li>勾選「顯示公式」、「顯示 R²」</li>
        <li>設定「往後預測幾期」</li>
      </ol>
      <div style='background:#dbeafe;padding:8px;border-radius:6px;margin-top:8px;'>
        <p style='color:#1e40af;font-size:0.85rem;margin:0;'><strong>R² 值</strong>：越接近 1 表示趨勢線擬合越好（0.8 以上算不錯）</p>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:10px;'>📐 趨勢線類型</h3>
      <table style='width:100%;border-collapse:collapse;font-size:0.85rem;'>
        <tr style='background:#15803d;color:#fff;'>
          <th style='padding:6px;'>類型</th><th style='padding:6px;'>適用情況</th>
        </tr>
        <tr><td style='padding:6px;color:#374151;font-weight:700;'>線性</td><td style='padding:6px;color:#374151;'>固定速率增減（大多數情況）</td></tr>
        <tr style='background:#f0fdf4;'><td style='padding:6px;color:#374151;font-weight:700;'>指數</td><td style='padding:6px;color:#374151;'>加速增長（病毒擴散、複利）</td></tr>
        <tr><td style='padding:6px;color:#374151;font-weight:700;'>多項式</td><td style='padding:6px;color:#374151;'>先升後降的曲線（氣溫）</td></tr>
        <tr style='background:#f0fdf4;'><td style='padding:6px;color:#374151;font-weight:700;'>移動平均</td><td style='padding:6px;color:#374151;'>平滑雜亂的時間序列資料</td></tr>
      </table>
    </div>
    <div style='background:#fff7ed;padding:10px;border-radius:8px;'>
      <p style='color:#9a3412;font-size:0.85rem;margin:0;'>⚠️ <strong>預測的局限性</strong>：趨勢線只能外推歷史趨勢，無法預測突發事件（如 COVID-19 對銷售的衝擊）。</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 20,
        'chapter': '第四章：圖表與預測',
        'title': 'FORECAST 預測函數',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>FORECAST 預測函數</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>🔮 FORECAST.LINEAR</h3>
      <div style='background:#fff;padding:10px;border-radius:6px;margin-bottom:8px;font-family:monospace;'>
        <p style='color:#1e40af;font-size:0.85rem;margin:0;'>=FORECAST.LINEAR(x, 已知y值, 已知x值)</p>
      </div>
      <div style='background:#dbeafe;padding:8px;border-radius:6px;'>
        <p style='color:#374151;font-size:0.85rem;margin:0;'>預測第 13 個月銷售量：<br><code>=FORECAST.LINEAR(13, B2:B13, A2:A13)</code></p>
      </div>
    </div>
    <div style='background:#f0fdf4;padding:12px;border-radius:8px;'>
      <h3 style='color:#15803d;font-size:0.95rem;margin-bottom:8px;'>📅 FORECAST.ETS（季節性預測）</h3>
      <p style='color:#374151;font-size:0.85rem;'>可以考慮季節性波動（如每年過年前業績高峰），比 LINEAR 更適合有週期性的資料。</p>
    </div>
  </div>
  <div>
    <div style='background:#fef9c3;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#854d0e;font-size:1rem;margin-bottom:10px;'>📊 一鍵「預測工作表」</h3>
      <p style='color:#374151;font-size:0.9rem;margin-bottom:8px;'>Excel 365 內建「預測工作表」，一鍵完成：</p>
      <ol style='color:#374151;font-size:0.85rem;padding-left:18px;'>
        <li>選取時間序列資料</li>
        <li>資料 → 預測工作表</li>
        <li>設定預測結束日期</li>
        <li>自動產生預測圖表 + 信賴區間</li>
      </ol>
      <div style='background:#fef3c7;padding:8px;border-radius:6px;margin-top:8px;'>
        <p style='color:#854d0e;font-size:0.8rem;margin:0;'>藍色線 = 歷史資料；橘色線 = 預測；灰色區域 = 不確定性範圍</p>
      </div>
    </div>
    <div style='background:#eff6ff;padding:10px;border-radius:8px;'>
      <p style='color:#1e40af;font-size:0.85rem;margin:0;'>🇹🇼 <strong>生活應用</strong>：台電每年用電量預測、全聯存貨補貨預測、各學校招生人數預測，都用到類似的時間序列預測方法。</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 21,
        'chapter': '第四章：圖表與預測',
        'title': '散佈圖與相關分析',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>散佈圖與相關係數</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>🔵 散佈圖分析兩變數關係</h3>
      <div style='background:#fff;padding:12px;border-radius:6px;text-align:center;'>
        <div style='display:flex;justify-content:space-around;'>
          <div>
            <p style='color:#15803d;font-size:0.8rem;font-weight:700;'>正相關</p>
            <div style='width:60px;height:60px;background:#dcfce7;border-radius:6px;display:flex;align-items:center;justify-content:center;font-size:1.5rem;'>↗️</div>
            <p style='color:#6b7280;font-size:0.7rem;'>r ≈ +1</p>
          </div>
          <div>
            <p style='color:#6b7280;font-size:0.8rem;font-weight:700;'>無相關</p>
            <div style='width:60px;height:60px;background:#f1f5f9;border-radius:6px;display:flex;align-items:center;justify-content:center;font-size:1.5rem;'>↔️</div>
            <p style='color:#6b7280;font-size:0.7rem;'>r ≈ 0</p>
          </div>
          <div>
            <p style='color:#dc2626;font-size:0.8rem;font-weight:700;'>負相關</p>
            <div style='width:60px;height:60px;background:#fee2e2;border-radius:6px;display:flex;align-items:center;justify-content:center;font-size:1.5rem;'>↘️</div>
            <p style='color:#6b7280;font-size:0.7rem;'>r ≈ -1</p>
          </div>
        </div>
      </div>
    </div>
    <div style='background:#f0fdf4;padding:10px;border-radius:8px;'>
      <p style='color:#374151;font-size:0.85rem;margin:0;'>Excel 相關係數：<code>=CORREL(A2:A41, B2:B41)</code></p>
    </div>
  </div>
  <div>
    <div style='background:#fff7ed;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#ea580c;font-size:1rem;margin-bottom:10px;'>🏫 學校資料相關分析範例</h3>
      <table style='width:100%;border-collapse:collapse;font-size:0.85rem;'>
        <tr style='background:#ea580c;color:#fff;'>
          <th style='padding:6px;'>X 變數</th><th style='padding:6px;'>Y 變數</th><th style='padding:6px;'>r 值</th>
        </tr>
        <tr><td style='padding:6px;color:#374151;'>出席率</td><td style='padding:6px;color:#374151;'>期末成績</td><td style='padding:6px;'><span style='color:#15803d;font-weight:700;'>+0.72</span></td></tr>
        <tr style='background:#fff7ed;'><td style='padding:6px;color:#374151;'>每日睡眠時數</td><td style='padding:6px;color:#374151;'>考試成績</td><td style='padding:6px;'><span style='color:#15803d;font-weight:700;'>+0.55</span></td></tr>
        <tr><td style='padding:6px;color:#374151;'>打遊戲時數</td><td style='padding:6px;color:#374151;'>成績</td><td style='padding:6px;'><span style='color:#dc2626;font-weight:700;'>-0.41</span></td></tr>
        <tr style='background:#fff7ed;'><td style='padding:6px;color:#374151;'>身高</td><td style='padding:6px;color:#374151;'>成績</td><td style='padding:6px;'><span style='color:#6b7280;font-weight:700;'>+0.03</span></td></tr>
      </table>
    </div>
    <div style='background:#fef2f2;padding:8px;border-radius:6px;'>
      <p style='color:#dc2626;font-size:0.8rem;margin:0;'>⚠️ 相關 ≠ 因果！打遊戲與成績的負相關，不代表打遊戲「導致」成績下降，可能兩者都受其他因素影響。</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 22,
        'chapter': '第四章：圖表與預測',
        'title': '🎯 第四章 隨堂測驗',
        'bg': 'purple',
        'quiz': 'q4',
        'chart': None,
        'video': None,
        'html': """
<div style='text-align:center;padding:20px;'>
  <div style='font-size:56px;margin-bottom:15px;'>🎯</div>
  <h2 style='color:#fff;font-size:2rem;font-weight:800;margin-bottom:10px;'>第四章 隨堂測驗</h2>
  <p style='color:#e9d5ff;font-size:1.1rem;'>圖表與預測 ── 2 道題目，點擊作答！</p>
</div>"""
    },
    {
        'id': 23,
        'chapter': '分組實作',
        'title': '分組實作：班級成績分析',
        'bg': 'teal',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 style='font-size:1.8rem;font-weight:800;color:#fff;margin-bottom:20px;text-align:center;'>📊 分組實作：班級成績分析系統</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div style='background:rgba(255,255,255,0.15);padding:18px;border-radius:12px;'>
    <h3 style='color:#fff;font-size:1rem;margin-bottom:14px;'>📋 實作任務（Google 試算表）</h3>
    <div style='display:flex;flex-direction:column;gap:9px;'>
      <div style='background:rgba(255,255,255,0.2);padding:10px;border-radius:8px;'>
        <p style='color:#fff;font-weight:700;font-size:0.9rem;margin:0 0 4px;'>① 建立成績資料表</p>
        <p style='color:#cffafe;font-size:0.8rem;margin:0;'>30 位同學、3 科成績（自行輸入或使用老師提供資料）</p>
      </div>
      <div style='background:rgba(255,255,255,0.2);padding:10px;border-radius:8px;'>
        <p style='color:#fff;font-weight:700;font-size:0.9rem;margin:0 0 4px;'>② 計算欄位</p>
        <p style='color:#cffafe;font-size:0.8rem;margin:0;'>總分(SUM) / 平均(AVERAGE) / 等第(IFS) / 名次(RANK)</p>
      </div>
      <div style='background:rgba(255,255,255,0.2);padding:10px;border-radius:8px;'>
        <p style='color:#fff;font-weight:700;font-size:0.9rem;margin:0 0 4px;'>③ 統計摘要</p>
        <p style='color:#cffafe;font-size:0.8rem;margin:0;'>全班各科平均/最高/最低 + 各等第人數(COUNTIF)</p>
      </div>
      <div style='background:rgba(255,255,255,0.2);padding:10px;border-radius:8px;'>
        <p style='color:#fff;font-weight:700;font-size:0.9rem;margin:0 0 4px;'>④ 樞紐分析</p>
        <p style='color:#cffafe;font-size:0.8rem;margin:0;'>分析各等第人數分布 + 各科成績比較</p>
      </div>
      <div style='background:rgba(255,255,255,0.2);padding:10px;border-radius:8px;'>
        <p style='color:#fff;font-weight:700;font-size:0.9rem;margin:0 0 4px;'>⑤ 圖表製作</p>
        <p style='color:#cffafe;font-size:0.8rem;margin:0;'>各科成績長條圖 + 成績分布直方圖</p>
      </div>
    </div>
  </div>
  <div>
    <div style='background:rgba(255,255,255,0.15);padding:15px;border-radius:12px;margin-bottom:12px;'>
      <h3 style='color:#fff;font-size:1rem;margin-bottom:10px;'>🎨 加分挑戰</h3>
      <ul style='color:#cffafe;font-size:0.85rem;padding-left:16px;margin:0;'>
        <li>條件式格式：紅色標記不及格</li>
        <li>用 VLOOKUP 建立等第對應表</li>
        <li>預測下次考試全班平均（趨勢線）</li>
        <li>散佈圖：出席率 vs 成績相關性</li>
      </ul>
    </div>
    <div style='background:rgba(255,255,255,0.15);padding:12px;border-radius:10px;'>
      <h3 style='color:#fff;font-size:0.9rem;margin-bottom:8px;'>🏆 評分標準（100 分）</h3>
      <ul style='color:#cffafe;font-size:0.85rem;padding-left:16px;margin:0;'>
        <li>基本函數運算正確 <strong style='color:#fff;'>40 分</strong></li>
        <li>樞紐分析表完成 <strong style='color:#fff;'>25 分</strong></li>
        <li>圖表製作（格式完整）<strong style='color:#fff;'>25 分</strong></li>
        <li>加分挑戰 <strong style='color:#fff;'>10 分（每項 2.5 分）</strong></li>
      </ul>
    </div>
  </div>
</div>"""
    },
    {
        'id': 24,
        'chapter': '分組實作',
        'title': '本週重點回顧',
        'bg': 'navy',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 style='font-size:1.8rem;font-weight:800;color:#fff;margin-bottom:20px;text-align:center;'>📖 Week 9 重點回顧</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:15px;'>
  <div style='background:rgba(255,255,255,0.12);padding:14px;border-radius:10px;'>
    <h3 style='color:#93c5fd;font-size:1rem;margin-bottom:8px;'>第一章 核心函數</h3>
    <ul style='color:#e2e8f0;font-size:0.85rem;padding-left:16px;margin:0;'>
      <li>SUM/AVERAGE/COUNT/RANK 基礎統計</li>
      <li>COUNTIF/SUMIF 條件計算</li>
      <li>$符號鎖定：絕對 vs 相對參照</li>
    </ul>
  </div>
  <div style='background:rgba(255,255,255,0.12);padding:14px;border-radius:10px;'>
    <h3 style='color:#93c5fd;font-size:1rem;margin-bottom:8px;'>第二章 條件與查詢</h3>
    <ul style='color:#e2e8f0;font-size:0.85rem;padding-left:16px;margin:0;'>
      <li>IF/IFS 多條件等第判斷</li>
      <li>VLOOKUP 從對應表查詢資料</li>
      <li>條件式格式：視覺化突出重點</li>
    </ul>
  </div>
  <div style='background:rgba(255,255,255,0.12);padding:14px;border-radius:10px;'>
    <h3 style='color:#93c5fd;font-size:1rem;margin-bottom:8px;'>第三章 樞紐分析表</h3>
    <ul style='color:#e2e8f0;font-size:0.85rem;padding-left:16px;margin:0;'>
      <li>列/欄/值/篩選四個區域</li>
      <li>多維度交叉分析，不需公式</li>
      <li>Google 試算表同樣支援，可協作</li>
    </ul>
  </div>
  <div style='background:rgba(255,255,255,0.12);padding:14px;border-radius:10px;'>
    <h3 style='color:#93c5fd;font-size:1rem;margin-bottom:8px;'>第四章 圖表與預測</h3>
    <ul style='color:#e2e8f0;font-size:0.85rem;padding-left:16px;margin:0;'>
      <li>R² 值衡量趨勢線擬合好壞</li>
      <li>FORECAST.ETS 時間序列預測</li>
      <li>相關係數 r：-1 到 +1</li>
    </ul>
  </div>
</div>
<div style='background:rgba(255,255,255,0.1);padding:12px;border-radius:8px;margin-top:15px;text-align:center;'>
  <p style='color:#bfdbfe;font-size:0.95rem;margin:0;'>最後一週：<strong style='color:#fff;'>Power BI 與期末總結</strong> ── 儀表板設計、十週課程回顧</p>
</div>"""
    }
]
