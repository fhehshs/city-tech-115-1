# -*- coding: utf-8 -*-
# Week 8: 巨量資料與資料科學

CHAPTERS = [
    {'name': '封面', 'start': 1},
    {'name': '第一章：認識大數據', 'start': 2},
    {'name': '第二章：開放資料 Open Data', 'start': 8},
    {'name': '第三章：資料清理與處理', 'start': 14},
    {'name': '第四章：資料視覺化', 'start': 19},
    {'name': '分組實作', 'start': 23},
]

QUIZZES = {
    'q1': {
        'title': '第一章 隨堂測驗',
        'questions': [
            {
                'q': '大數據（Big Data）的「5V」特性中，哪一個 V 代表資料的可靠性和準確性？',
                'options': ['Velocity（速度）', 'Volume（體量）', 'Value（價值）', 'Veracity（真實性）'],
                'answer': 3,
                'explain': '5V 為：Volume（體量）、Velocity（速度）、Variety（多樣性）、Veracity（真實性）、Value（價值）。Veracity 指資料的準確度和可信度，假新聞、感測誤差都會影響 Veracity。'
            },
            {
                'q': '台灣哪個政府機構負責維運「政府資料開放平台（data.gov.tw）」？',
                'options': ['行政院資安處', '國家發展委員會', '教育部資訊司', '中央研究院'],
                'answer': 1,
                'explain': 'data.gov.tw 由國家發展委員會（國發會）負責維運，是台灣最大的政府開放資料入口，提供超過 50,000 筆資料集。'
            },
        ]
    },
    'q2': {
        'title': '第二章 隨堂測驗',
        'questions': [
            {
                'q': '開放資料（Open Data）最重要的特性是什麼？',
                'options': ['任何人均可免費取得、使用和再散布', '只有學術機構才能使用', '資料永遠不會有錯誤', '只包含政府統計資料'],
                'answer': 0,
                'explain': '開放資料（Open Data）的核心定義：資料可被任何人免費取用、修改、再發布，且沒有著作權或授權的限制，最常見授權方式是 CC BY（創用 CC 姓名標示）。'
            },
            {
                'q': '下列哪項不屬於台灣政府開放資料的常見格式？',
                'options': ['CSV（逗號分隔值）', 'JSON（JavaScript 物件表示法）', '.docx（Word 文件）', 'XML（可延伸標記語言）'],
                'answer': 2,
                'explain': '.docx 是 Microsoft Word 格式，非機器易讀的開放格式。開放資料應使用 CSV、JSON、XML 等機器可讀格式，方便程式直接讀取和分析。'
            },
        ]
    },
    'q3': {
        'title': '第三章 隨堂測驗',
        'questions': [
            {
                'q': '資料清理中，處理「缺失值」最常見的方法是什麼？',
                'options': ['直接刪除整個資料集', '只保留缺失值所在的列', '填入平均值或中位數（插補法）', '將所有缺失值設為 0'],
                'answer': 2,
                'explain': '缺失值處理視情況而定：若缺失不多，可用平均值/中位數插補；若大量缺失，才考慮刪除該行（列）。直接填 0 可能扭曲分析結果。'
            },
            {
                'q': '在 Excel 中，可以用哪個功能快速找出並移除重複資料？',
                'options': ['常用→找到並取代→刪除', '公式→UNIQUE 函數', '插入→樞紐分析表', '資料→移除重複項'],
                'answer': 3,
                'explain': 'Excel「資料」索引標籤下有「移除重複項」功能，可選擇哪些欄位來判斷重複，一鍵刪除重複列。'
            },
        ]
    },
    'q4': {
        'title': '第四章 隨堂測驗',
        'questions': [
            {
                'q': '想比較全班同學各科成績的分布範圍（最高/最低/中位數），最適合使用哪種圖表？',
                'options': ['圓餅圖', '箱形圖（Box Plot）', '折線圖', '泡泡圖'],
                'answer': 1,
                'explain': '箱形圖專門用來顯示資料分布：中位數、四分位距（Q1-Q3）、最大最小值及異常值（離群值），非常適合比較多組資料的分散程度。'
            },
            {
                'q': '想展示台灣各縣市人口密度的差異，最適合哪種視覺化方式？',
                'options': ['地圖熱力圖（Choropleth Map）', '長條圖', '折線圖', '散佈圖'],
                'answer': 0,
                'explain': '地圖熱力圖（Choropleth Map）用顏色深淺表示地理區域的數值大小，非常直覺地展現空間分布差異。展示縣市人口密度、確診率等地理資料的首選。'
            },
        ]
    },
}

SLIDES = [
    {
        'id': 1,
        'chapter': '封面',
        'title': '巨量資料與資料科學',
        'bg': 'navy',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<div style='text-align:center;padding:30px 20px;'>
  <div style='font-size:72px;margin-bottom:20px;'>📊</div>
  <h1 style='font-size:2.8rem;font-weight:900;color:#fff;margin-bottom:12px;'>巨量資料與資料科學</h1>
  <h2 style='font-size:1.5rem;font-weight:400;color:#93c5fd;margin-bottom:30px;'>Big Data &amp; Data Science</h2>
  <div style='display:flex;justify-content:center;gap:20px;flex-wrap:wrap;margin-bottom:30px;'>
    <span style='background:rgba(255,255,255,0.15);color:#e0f2fe;padding:8px 20px;border-radius:20px;font-size:1rem;'>📦 Big Data 5V</span>
    <span style='background:rgba(255,255,255,0.15);color:#e0f2fe;padding:8px 20px;border-radius:20px;font-size:1rem;'>🔓 Open Data</span>
    <span style='background:rgba(255,255,255,0.15);color:#e0f2fe;padding:8px 20px;border-radius:20px;font-size:1rem;'>🧹 資料清理</span>
    <span style='background:rgba(255,255,255,0.15);color:#e0f2fe;padding:8px 20px;border-radius:20px;font-size:1rem;'>📈 資料視覺化</span>
  </div>
  <p style='color:#bfdbfe;font-size:1.1rem;'>城市科技 — 第八週</p>
</div>"""
    },
    {
        'id': 2,
        'chapter': '第一章：認識大數據',
        'title': '什麼是大數據？',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>什麼是大數據？</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;border-left:4px solid #2563eb;padding:15px;border-radius:8px;margin-bottom:15px;'>
      <h3 style='color:#1e40af;font-size:1.1rem;margin-bottom:8px;'>📌 定義</h3>
      <p style='color:#374151;font-size:0.95rem;'>大數據是指<strong>規模龐大、類型多元、產生快速</strong>，以至於傳統工具難以儲存、管理和分析的資料集合。</p>
    </div>
    <div style='background:#fef9c3;padding:12px;border-radius:8px;border:1px solid #fde047;'>
      <h3 style='color:#854d0e;font-size:1rem;margin-bottom:8px;'>📊 每日數據規模</h3>
      <ul style='color:#374151;font-size:0.85rem;padding-left:16px;margin:0;'>
        <li>Google 每天處理 <strong>85 億</strong>次搜尋</li>
        <li>Facebook 每天上傳 <strong>3.5 億</strong>張照片</li>
        <li>WhatsApp 每天傳送 <strong>1,000 億</strong>則訊息</li>
        <li>YouTube 每分鐘上傳 <strong>500 小時</strong>影片</li>
      </ul>
    </div>
  </div>
  <div>
    <div style='background:#f9fafb;padding:15px;border-radius:10px;'>
      <h3 style='color:#374151;font-size:1rem;margin-bottom:12px;'>🌍 人類每日產生資料量</h3>
      <div style='text-align:center;'>
        <div style='font-size:3rem;font-weight:900;color:#1e40af;'>2.5 EB</div>
        <p style='color:#6b7280;font-size:0.85rem;'>（Exabytes = 10¹⁸ bytes）</p>
        <div style='background:#e5e7eb;height:1px;margin:12px 0;'></div>
        <p style='color:#374151;font-size:0.85rem;'>這相當於 <strong>25 億部</strong> 1GB 電影<br>或 <strong>250 億本</strong> 1MB 電子書</p>
      </div>
      <div style='background:#eff6ff;padding:10px;border-radius:6px;margin-top:12px;'>
        <p style='color:#1e40af;font-size:0.85rem;margin:0;'>📈 資料量每 2 年翻倍，預計 2025 全球累積 175 ZB（澤位元組）</p>
      </div>
    </div>
  </div>
</div>"""
    },
    {
        'id': 3,
        'chapter': '第一章：認識大數據',
        'title': '大數據 5V 特性',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>大數據 5V 特性</h2>
<div style='display:grid;grid-template-columns:repeat(5,1fr);gap:12px;'>
  <div style='background:#eff6ff;padding:14px;border-radius:10px;text-align:center;'>
    <div style='font-size:2rem;margin-bottom:8px;'>📦</div>
    <h3 style='color:#1e40af;font-size:1.1rem;margin-bottom:6px;'>Volume</h3>
    <p style='color:#374151;font-size:0.75rem;font-weight:700;'>體量</p>
    <p style='color:#6b7280;font-size:0.75rem;margin-top:6px;'>TB、PB 甚至 ZB 規模，傳統資料庫難以儲存</p>
  </div>
  <div style='background:#f0fdf4;padding:14px;border-radius:10px;text-align:center;'>
    <div style='font-size:2rem;margin-bottom:8px;'>⚡</div>
    <h3 style='color:#15803d;font-size:1.1rem;margin-bottom:6px;'>Velocity</h3>
    <p style='color:#374151;font-size:0.75rem;font-weight:700;'>速度</p>
    <p style='color:#6b7280;font-size:0.75rem;margin-top:6px;'>即時產生、即時分析，如股票價格串流</p>
  </div>
  <div style='background:#fdf4ff;padding:14px;border-radius:10px;text-align:center;'>
    <div style='font-size:2rem;margin-bottom:8px;'>🎭</div>
    <h3 style='color:#7c3aed;font-size:1.1rem;margin-bottom:6px;'>Variety</h3>
    <p style='color:#374151;font-size:0.75rem;font-weight:700;'>多樣性</p>
    <p style='color:#6b7280;font-size:0.75rem;margin-top:6px;'>結構化（表格）、非結構化（影片/文字/圖片）</p>
  </div>
  <div style='background:#fef2f2;padding:14px;border-radius:10px;text-align:center;'>
    <div style='font-size:2rem;margin-bottom:8px;'>✅</div>
    <h3 style='color:#dc2626;font-size:1.1rem;margin-bottom:6px;'>Veracity</h3>
    <p style='color:#374151;font-size:0.75rem;font-weight:700;'>真實性</p>
    <p style='color:#6b7280;font-size:0.75rem;margin-top:6px;'>資料品質和準確度，假新聞影響 Veracity</p>
  </div>
  <div style='background:#fff7ed;padding:14px;border-radius:10px;text-align:center;'>
    <div style='font-size:2rem;margin-bottom:8px;'>💎</div>
    <h3 style='color:#ea580c;font-size:1.1rem;margin-bottom:6px;'>Value</h3>
    <p style='color:#374151;font-size:0.75rem;font-weight:700;'>價值</p>
    <p style='color:#6b7280;font-size:0.75rem;margin-top:6px;'>從海量資料中提取有意義的洞見</p>
  </div>
</div>
<div style='background:#f1f5f9;padding:12px;border-radius:8px;margin-top:15px;'>
  <p style='color:#374151;font-size:0.9rem;margin:0;'>💡 <strong>比喻</strong>：大數據就像大海捕魚——Volume 是大海（海量），Velocity 是海浪速度（即時），Variety 是各種魚種（多元），Veracity 是辨認真魚（品質），Value 是最後端上桌的美食（洞見）。</p>
</div>"""
    },
    {
        'id': 4,
        'chapter': '第一章：認識大數據',
        'title': '大數據技術棧',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>大數據技術棧</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:12px;'>⚙️ 主要技術</h3>
      <div style='display:flex;flex-direction:column;gap:8px;'>
        <div style='background:#fff;padding:10px;border-radius:6px;'>
          <p style='font-weight:700;color:#1e40af;font-size:0.9rem;margin:0;'>Hadoop</p>
          <p style='color:#374151;font-size:0.8rem;margin:4px 0 0;'>分散式儲存（HDFS）+ 平行計算（MapReduce），可橫跨數千台伺服器</p>
        </div>
        <div style='background:#fff;padding:10px;border-radius:6px;'>
          <p style='font-weight:700;color:#ea580c;font-size:0.9rem;margin:0;'>Apache Spark</p>
          <p style='color:#374151;font-size:0.8rem;margin:4px 0 0;'>記憶體計算，比 Hadoop 快 100 倍，支援機器學習</p>
        </div>
        <div style='background:#fff;padding:10px;border-radius:6px;'>
          <p style='font-weight:700;color:#7c3aed;font-size:0.9rem;margin:0;'>Kafka</p>
          <p style='color:#374151;font-size:0.8rem;margin:4px 0 0;'>即時資料串流，每秒處理數百萬筆訊息</p>
        </div>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:10px;'>🇹🇼 台灣大數據應用</h3>
      <ul style='color:#374151;font-size:0.9rem;padding-left:16px;'>
        <li><strong>悠遊卡</strong>：每日數百萬筆交通資料，分析人流模式</li>
        <li><strong>健保署</strong>：2,300 萬人就診紀錄，偵測詐領</li>
        <li><strong>股市分析</strong>：毫秒級交易大數據決策</li>
        <li><strong>Netflix 台灣</strong>：用戶行為預測推薦內容</li>
      </ul>
    </div>
    <div style='background:#fff7ed;padding:10px;border-radius:8px;'>
      <p style='color:#9a3412;font-size:0.85rem;margin:0;'>💡 台灣健保資料庫是全球最完整的醫療大數據之一，已開放給研究機構使用，協助多項世界級醫學研究。</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 5,
        'chapter': '第一章：認識大數據',
        'title': '資料科學工作流程',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>資料科學工作流程</h2>
<div style='display:flex;flex-direction:column;gap:12px;margin-bottom:15px;'>
  <div style='display:grid;grid-template-columns:repeat(6,1fr);gap:8px;'>
    <div style='background:#1e40af;padding:12px;border-radius:8px;text-align:center;'>
      <div style='font-size:1.5rem;'>🎯</div>
      <p style='color:#fff;font-size:0.8rem;font-weight:700;margin:6px 0 0;'>定義問題</p>
    </div>
    <div style='background:#0369a1;padding:12px;border-radius:8px;text-align:center;'>
      <div style='font-size:1.5rem;'>📥</div>
      <p style='color:#fff;font-size:0.8rem;font-weight:700;margin:6px 0 0;'>蒐集資料</p>
    </div>
    <div style='background:#0891b2;padding:12px;border-radius:8px;text-align:center;'>
      <div style='font-size:1.5rem;'>🧹</div>
      <p style='color:#fff;font-size:0.8rem;font-weight:700;margin:6px 0 0;'>清理資料</p>
    </div>
    <div style='background:#0d9488;padding:12px;border-radius:8px;text-align:center;'>
      <div style='font-size:1.5rem;'>🔍</div>
      <p style='color:#fff;font-size:0.8rem;font-weight:700;margin:6px 0 0;'>探索分析</p>
    </div>
    <div style='background:#16a34a;padding:12px;border-radius:8px;text-align:center;'>
      <div style='font-size:1.5rem;'>🤖</div>
      <p style='color:#fff;font-size:0.8rem;font-weight:700;margin:6px 0 0;'>建立模型</p>
    </div>
    <div style='background:#65a30d;padding:12px;border-radius:8px;text-align:center;'>
      <div style='font-size:1.5rem;'>📊</div>
      <p style='color:#fff;font-size:0.8rem;font-weight:700;margin:6px 0 0;'>呈現洞見</p>
    </div>
  </div>
</div>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:15px;'>
  <div style='background:#fef9c3;padding:14px;border-radius:10px;'>
    <h3 style='color:#854d0e;font-size:1rem;margin-bottom:8px;'>⏱️ 時間分配現實</h3>
    <ul style='color:#374151;font-size:0.9rem;padding-left:16px;margin:0;'>
      <li>資料蒐集 + 清理：<strong>70-80%</strong> 時間</li>
      <li>建立模型：<strong>10-15%</strong> 時間</li>
      <li>呈現與溝通：<strong>10-15%</strong> 時間</li>
    </ul>
  </div>
  <div style='background:#eff6ff;padding:14px;border-radius:10px;'>
    <h3 style='color:#1e40af;font-size:1rem;margin-bottom:8px;'>🛠️ 常用工具</h3>
    <ul style='color:#374151;font-size:0.9rem;padding-left:16px;margin:0;'>
      <li><strong>Python</strong>：pandas, numpy, matplotlib</li>
      <li><strong>R</strong>：統計分析首選</li>
      <li><strong>Excel / Google 試算表</strong>：入門首選</li>
      <li><strong>Tableau / Power BI</strong>：視覺化工具</li>
    </ul>
  </div>
</div>"""
    },
    {
        'id': 6,
        'chapter': '第一章：認識大數據',
        'title': '台灣大數據新聞事件',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>台灣大數據應用新聞</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div style='display:flex;flex-direction:column;gap:12px;'>
    <div style='background:#eff6ff;padding:14px;border-radius:10px;border-left:4px solid #2563eb;'>
      <h3 style='color:#1e40af;font-size:0.95rem;margin-bottom:6px;'>📱 COVID-19 大數據防疫（2021-22）</h3>
      <p style='color:#374151;font-size:0.85rem;margin:0;'>陳時中指揮中心每日更新儀表板，結合健保、手機基地台、邊境管制等資料，台灣成全球防疫資料透明度模範。</p>
    </div>
    <div style='background:#f0fdf4;padding:14px;border-radius:10px;border-left:4px solid #16a34a;'>
      <h3 style='color:#15803d;font-size:0.95rem;margin-bottom:6px;'>🚌 MRT 大數據優化班距</h3>
      <p style='color:#374151;font-size:0.85rem;margin:0;'>台北捷運每日 200 多萬人次的刷卡資料，被用來分析各站進出人流、預測尖峰時段，作為調整班距與月台人力配置的依據。</p>
    </div>
  </div>
  <div style='display:flex;flex-direction:column;gap:12px;'>
    <div style='background:#fff7ed;padding:14px;border-radius:10px;border-left:4px solid #ea580c;'>
      <h3 style='color:#ea580c;font-size:0.95rem;margin-bottom:6px;'>🏪 全聯行銷大數據（2023）</h3>
      <p style='color:#374151;font-size:0.85rem;margin:0;'>全聯分析上千萬會員的購物資料，推播個人化促銷與點數活動，會員 APP 已成為台灣大型零售資料平台之一。</p>
    </div>
    <div style='background:#fdf4ff;padding:14px;border-radius:10px;border-left:4px solid #7c3aed;'>
      <h3 style='color:#7c3aed;font-size:0.95rem;margin-bottom:6px;'>🏦 玉山銀行詐欺偵測</h3>
      <p style='color:#374151;font-size:0.85rem;margin:0;'>以 AI 即時分析每筆交易的大量特徵（金額、地點、時間、慣性），在極短時間內判斷風險並攔阻可疑交易，是金融業大數據的代表應用。</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 7,
        'chapter': '第一章：認識大數據',
        'title': '🎯 第一章 隨堂測驗',
        'bg': 'purple',
        'quiz': 'q1',
        'chart': None,
        'video': None,
        'html': """
<div style='text-align:center;padding:20px;'>
  <div style='font-size:56px;margin-bottom:15px;'>🎯</div>
  <h2 style='color:#fff;font-size:2rem;font-weight:800;margin-bottom:10px;'>第一章 隨堂測驗</h2>
  <p style='color:#e9d5ff;font-size:1.1rem;'>認識大數據 ── 2 道題目，點擊作答！</p>
</div>"""
    },
    {
        'id': 8,
        'chapter': '第二章：開放資料 Open Data',
        'title': '什麼是開放資料？',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>什麼是開放資料（Open Data）？</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;border-left:4px solid #2563eb;padding:15px;border-radius:8px;margin-bottom:15px;'>
      <h3 style='color:#1e40af;font-size:1.1rem;margin-bottom:8px;'>🔓 定義</h3>
      <p style='color:#374151;font-size:0.95rem;'>開放資料是指任何人均可<strong>免費取得、使用、修改和再發布</strong>的資料，通常由政府、學術機構或企業主動公開。</p>
    </div>
    <div style='background:#f0fdf4;padding:12px;border-radius:8px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:8px;'>📜 常見授權方式</h3>
      <ul style='color:#374151;font-size:0.9rem;padding-left:16px;margin:0;'>
        <li><strong>CC BY</strong>：姓名標示，可商用</li>
        <li><strong>CC BY-SA</strong>：姓名標示+相同方式分享</li>
        <li><strong>CC0</strong>：公共領域，完全無限制</li>
        <li><strong>政府資料開放授權條款</strong>：台灣政府使用</li>
      </ul>
    </div>
  </div>
  <div>
    <div style='background:#fdf4ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#7c3aed;font-size:1rem;margin-bottom:10px;'>🌐 台灣開放資料平台</h3>
      <div style='display:flex;flex-direction:column;gap:8px;'>
        <div style='background:#fff;padding:8px;border-radius:6px;border-left:3px solid #7c3aed;'>
          <p style='font-weight:700;color:#7c3aed;font-size:0.85rem;margin:0;'>data.gov.tw</p>
          <p style='color:#374151;font-size:0.8rem;margin:2px 0 0;'>政府資料開放平台，50,000+ 資料集</p>
        </div>
        <div style='background:#fff;padding:8px;border-radius:6px;border-left:3px solid #2563eb;'>
          <p style='font-weight:700;color:#2563eb;font-size:0.85rem;margin:0;'>data.taipei.gov.tw</p>
          <p style='color:#374151;font-size:0.8rem;margin:2px 0 0;'>台北市開放資料，涵蓋交通/環境/社福</p>
        </div>
        <div style='background:#fff;padding:8px;border-radius:6px;border-left:3px solid #16a34a;'>
          <p style='font-weight:700;color:#16a34a;font-size:0.85rem;margin:0;'>e-service.cwb.gov.tw</p>
          <p style='color:#374151;font-size:0.8rem;margin:2px 0 0;'>中央氣象局開放氣象資料 API</p>
        </div>
        <div style='background:#fff;padding:8px;border-radius:6px;border-left:3px solid #ea580c;'>
          <p style='font-weight:700;color:#ea580c;font-size:0.85rem;margin:0;'>工業區廠商資料、空汙監測</p>
          <p style='color:#374151;font-size:0.8rem;margin:2px 0 0;'>環境部、教育部、交通部均有開放資料</p>
        </div>
      </div>
    </div>
  </div>
</div>"""
    },
    {
        'id': 9,
        'chapter': '第二章：開放資料 Open Data',
        'title': '開放資料格式',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>開放資料格式</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <h3 style='color:#374151;font-size:1rem;margin-bottom:12px;'>📄 常見開放格式比較</h3>
    <div style='display:flex;flex-direction:column;gap:8px;'>
      <div style='background:#f0fdf4;padding:12px;border-radius:8px;'>
        <h4 style='color:#15803d;font-size:0.9rem;margin-bottom:4px;'>CSV（逗號分隔值）</h4>
        <p style='color:#374151;font-size:0.8rem;margin:0;'>最簡單的表格格式，Excel 可直接開啟。</p>
        <code style='color:#374151;font-size:0.75rem;background:#dcfce7;padding:2px 6px;border-radius:3px;display:block;margin-top:4px;'>姓名,成績,班級<br>小明,85,A班</code>
      </div>
      <div style='background:#eff6ff;padding:12px;border-radius:8px;'>
        <h4 style='color:#1e40af;font-size:0.9rem;margin-bottom:4px;'>JSON</h4>
        <p style='color:#374151;font-size:0.8rem;margin:0;'>網路 API 最常用格式，支援巢狀結構。</p>
        <code style='color:#374151;font-size:0.75rem;background:#dbeafe;padding:2px 6px;border-radius:3px;display:block;margin-top:4px;'>[{"name":"小明","score":85}]</code>
      </div>
      <div style='background:#fdf4ff;padding:12px;border-radius:8px;'>
        <h4 style='color:#7c3aed;font-size:0.9rem;margin-bottom:4px;'>XML</h4>
        <p style='color:#374151;font-size:0.8rem;margin:0;'>標籤結構，台灣電子發票/健保資料常用。</p>
        <code style='color:#374151;font-size:0.75rem;background:#e9d5ff;padding:2px 6px;border-radius:3px;display:block;margin-top:4px;'>&lt;student&gt;&lt;name&gt;小明&lt;/name&gt;&lt;/student&gt;</code>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#fff7ed;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#ea580c;font-size:1rem;margin-bottom:10px;'>⭐ 開放資料評級（Tim Berners-Lee）</h3>
      <table style='width:100%;border-collapse:collapse;font-size:0.85rem;'>
        <tr style='background:#ea580c;color:#fff;'>
          <th style='padding:6px;'>星數</th><th style='padding:6px;'>標準</th>
        </tr>
        <tr><td style='padding:6px;text-align:center;'>⭐</td><td style='padding:6px;color:#374151;'>任何格式（包括 PDF、圖片）</td></tr>
        <tr style='background:#fff7ed;'><td style='padding:6px;text-align:center;'>⭐⭐</td><td style='padding:6px;color:#374151;'>機器可讀（如 Excel）</td></tr>
        <tr><td style='padding:6px;text-align:center;'>⭐⭐⭐</td><td style='padding:6px;color:#374151;'>開放格式（CSV, JSON）</td></tr>
        <tr style='background:#fff7ed;'><td style='padding:6px;text-align:center;'>⭐⭐⭐⭐</td><td style='padding:6px;color:#374151;'>使用 URI 識別資源</td></tr>
        <tr><td style='padding:6px;text-align:center;'>⭐⭐⭐⭐⭐</td><td style='padding:6px;color:#374151;'>連結到其他資料（關聯資料）</td></tr>
      </table>
    </div>
  </div>
</div>"""
    },
    {
        'id': 10,
        'chapter': '第二章：開放資料 Open Data',
        'title': '開放資料實際應用',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': {'url': 'https://www.youtube.com/embed/3YR4CseY9pk', 'title': '開放資料的力量', 'desc': '了解開放資料如何改變政府與市民的關係'},
        'html': """
<h2 class='slide-title'>開放資料改變生活</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div style='display:flex;flex-direction:column;gap:12px;'>
    <div style='background:#eff6ff;padding:14px;border-radius:10px;border-left:4px solid #2563eb;'>
      <h3 style='color:#1e40af;font-size:0.95rem;margin-bottom:6px;'>🚌 PTX 公共運輸開放資料</h3>
      <p style='color:#374151;font-size:0.85rem;margin:0;'>交通部 PTX 平台開放公車、捷運、火車即時班次，催生了超過 500 個第三方 APP（如台北等公車、時刻表 APP）。</p>
    </div>
    <div style='background:#f0fdf4;padding:14px;border-radius:10px;border-left:4px solid #16a34a;'>
      <h3 style='color:#15803d;font-size:0.95rem;margin-bottom:6px;'>🌡️ 空汙 AQI 開放資料</h3>
      <p style='color:#374151;font-size:0.85rem;margin:0;'>環境部開放 PM2.5、AQI 即時數據，AirVisual、紫爆等 APP 基於此資料，讓市民即時知道是否戴口罩。</p>
    </div>
  </div>
  <div style='display:flex;flex-direction:column;gap:12px;'>
    <div style='background:#fff7ed;padding:14px;border-radius:10px;border-left:4px solid #ea580c;'>
      <h3 style='color:#ea580c;font-size:0.95rem;margin-bottom:6px;'>💊 口罩地圖（2020）</h3>
      <p style='color:#374151;font-size:0.85rem;margin:0;'>疫情初期，政府 48 小時內開放藥局口罩庫存 API，全台工程師 2 天開發出口罩地圖，獲國際媒體大幅報導。</p>
    </div>
    <div style='background:#fdf4ff;padding:14px;border-radius:10px;border-left:4px solid #7c3aed;'>
      <h3 style='color:#7c3aed;font-size:0.95rem;margin-bottom:6px;'>🏠 實價登錄開放資料</h3>
      <p style='color:#374151;font-size:0.85rem;margin:0;'>不動產實際成交資料開放後，催生信義房屋、樂屋等平台的房價分析功能，讓買房更透明公平。</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 11,
        'chapter': '第二章：開放資料 Open Data',
        'title': '動手查開放資料',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>動手查開放資料</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>🔍 步驟：從 data.gov.tw 下載資料</h3>
      <ol style='color:#374151;font-size:0.9rem;padding-left:18px;'>
        <li>前往 <strong>data.gov.tw</strong></li>
        <li>搜尋關鍵字（如「YouBike」）</li>
        <li>選擇資料集，確認授權條款</li>
        <li>下載 CSV 格式</li>
        <li>用 Excel/Google 試算表開啟</li>
      </ol>
    </div>
    <div style='background:#fef9c3;padding:10px;border-radius:8px;border:1px solid #fde047;'>
      <p style='color:#854d0e;font-size:0.85rem;margin:0;'>💡 CSV 下載後若出現亂碼，請用 Excel 匯入功能並選擇 UTF-8 編碼。</p>
    </div>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:10px;'>📊 有趣的資料集推薦</h3>
      <ul style='color:#374151;font-size:0.85rem;padding-left:16px;'>
        <li>🚲 YouBike 即時站點資訊</li>
        <li>🌧️ 各縣市年降雨量統計</li>
        <li>🏫 全台學校基本資料</li>
        <li>🏥 台灣醫院評鑑資料</li>
        <li>🗳️ 歷年選舉得票數</li>
        <li>🌡️ 各站空氣品質 AQI</li>
        <li>🏘️ 不動產實價登錄</li>
      </ul>
    </div>
  </div>
</div>"""
    },
    {
        'id': 12,
        'chapter': '第二章：開放資料 Open Data',
        'title': '🎯 第二章 隨堂測驗',
        'bg': 'purple',
        'quiz': 'q2',
        'chart': None,
        'video': None,
        'html': """
<div style='text-align:center;padding:20px;'>
  <div style='font-size:56px;margin-bottom:15px;'>🎯</div>
  <h2 style='color:#fff;font-size:2rem;font-weight:800;margin-bottom:10px;'>第二章 隨堂測驗</h2>
  <p style='color:#e9d5ff;font-size:1.1rem;'>開放資料 Open Data ── 2 道題目，點擊作答！</p>
</div>"""
    },
    {
        'id': 13,
        'chapter': '第三章：資料清理與處理',
        'title': '資料清理的重要性',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>資料清理的重要性</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#fef2f2;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#dc2626;font-size:1rem;margin-bottom:10px;'>🗑️ 常見髒資料問題</h3>
      <div style='display:flex;flex-direction:column;gap:6px;'>
        <div style='background:#fee2e2;padding:8px;border-radius:6px;'>
          <p style='color:#991b1b;font-size:0.85rem;margin:0;'><strong>缺失值</strong>：欄位空白或 NULL</p>
        </div>
        <div style='background:#fee2e2;padding:8px;border-radius:6px;'>
          <p style='color:#991b1b;font-size:0.85rem;margin:0;'><strong>重複資料</strong>：同一筆記錄出現兩次</p>
        </div>
        <div style='background:#fee2e2;padding:8px;border-radius:6px;'>
          <p style='color:#991b1b;font-size:0.85rem;margin:0;'><strong>格式不一致</strong>：日期「2024/1/1」vs「01-01-2024」</p>
        </div>
        <div style='background:#fee2e2;padding:8px;border-radius:6px;'>
          <p style='color:#991b1b;font-size:0.85rem;margin:0;'><strong>異常值</strong>：年齡填 -5 或 999</p>
        </div>
        <div style='background:#fee2e2;padding:8px;border-radius:6px;'>
          <p style='color:#991b1b;font-size:0.85rem;margin:0;'><strong>錯誤分類</strong>：性別欄填了「男生」和「male」</p>
        </div>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:10px;'>🧹 處理方法</h3>
      <table style='width:100%;border-collapse:collapse;font-size:0.85rem;'>
        <tr style='background:#15803d;color:#fff;'>
          <th style='padding:7px;'>問題</th><th style='padding:7px;'>處理方式</th>
        </tr>
        <tr><td style='padding:7px;color:#374151;'>缺失值少</td><td style='padding:7px;color:#374151;'>填入平均/中位數</td></tr>
        <tr style='background:#f0fdf4;'><td style='padding:7px;color:#374151;'>缺失值多</td><td style='padding:7px;color:#374151;'>刪除該列/欄</td></tr>
        <tr><td style='padding:7px;color:#374151;'>重複資料</td><td style='padding:7px;color:#374151;'>移除重複項</td></tr>
        <tr style='background:#f0fdf4;'><td style='padding:7px;color:#374151;'>格式不一</td><td style='padding:7px;color:#374151;'>標準化（統一格式）</td></tr>
        <tr><td style='padding:7px;color:#374151;'>異常值</td><td style='padding:7px;color:#374151;'>確認後刪除或修正</td></tr>
      </table>
    </div>
    <div style='background:#fff7ed;padding:10px;border-radius:8px;'>
      <p style='color:#9a3412;font-size:0.85rem;margin:0;'>💡 <strong>GIGO</strong>（Garbage In, Garbage Out）：輸入髒資料，輸出的分析結果一定是垃圾。資料品質決定分析品質！</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 14,
        'chapter': '第三章：資料清理與處理',
        'title': 'Excel 資料清理技巧',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>Excel 資料清理技巧</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <h3 style='color:#374151;font-size:1rem;margin-bottom:12px;'>🛠️ 常用 Excel 清理工具</h3>
    <div style='display:flex;flex-direction:column;gap:8px;'>
      <div style='background:#eff6ff;padding:10px;border-radius:8px;border-left:3px solid #2563eb;'>
        <p style='font-weight:700;color:#1e40af;font-size:0.9rem;margin:0;'>資料 → 移除重複項</p>
        <p style='color:#374151;font-size:0.8rem;margin:4px 0 0;'>選定欄位，一鍵刪除重複列</p>
      </div>
      <div style='background:#f0fdf4;padding:10px;border-radius:8px;border-left:3px solid #16a34a;'>
        <p style='font-weight:700;color:#15803d;font-size:0.9rem;margin:0;'>TRIM() 函數</p>
        <p style='color:#374151;font-size:0.8rem;margin:4px 0 0;'>移除文字前後多餘空格：=TRIM(A1)</p>
      </div>
      <div style='background:#fff7ed;padding:10px;border-radius:8px;border-left:3px solid #ea580c;'>
        <p style='font-weight:700;color:#ea580c;font-size:0.9rem;margin:0;'>UPPER() / LOWER() / PROPER()</p>
        <p style='color:#374151;font-size:0.8rem;margin:4px 0 0;'>統一大小寫：PROPER("john doe") → "John Doe"</p>
      </div>
      <div style='background:#fdf4ff;padding:10px;border-radius:8px;border-left:3px solid #7c3aed;'>
        <p style='font-weight:700;color:#7c3aed;font-size:0.9rem;margin:0;'>資料 → 文字到欄</p>
        <p style='color:#374151;font-size:0.8rem;margin:4px 0 0;'>將「姓名,電話」一欄拆成兩欄</p>
      </div>
      <div style='background:#fef9c3;padding:10px;border-radius:8px;border-left:3px solid #ca8a04;'>
        <p style='font-weight:700;color:#854d0e;font-size:0.9rem;margin:0;'>條件式格式設定 → 突出顯示規則</p>
        <p style='color:#374151;font-size:0.8rem;margin:4px 0 0;'>快速標記異常值（如成績 &gt; 100）</p>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#f9fafb;padding:15px;border-radius:10px;border:1px solid #e5e7eb;margin-bottom:12px;'>
      <h3 style='color:#374151;font-size:1rem;margin-bottom:10px;'>📋 清理前後對比</h3>
      <p style='color:#dc2626;font-size:0.85rem;font-weight:700;margin-bottom:5px;'>清理前（髒資料）</p>
      <table style='width:100%;border-collapse:collapse;font-size:0.8rem;margin-bottom:10px;'>
        <tr style='background:#fee2e2;'>
          <td style='padding:5px;color:#374151;'>  小明 </td><td style='padding:5px;color:#374151;'>male</td><td style='padding:5px;color:#374151;'>85</td>
        </tr>
        <tr style='background:#fee2e2;'>
          <td style='padding:5px;color:#374151;'>小明</td><td style='padding:5px;color:#374151;'>男</td><td style='padding:5px;color:#374151;'></td>
        </tr>
        <tr style='background:#fee2e2;'>
          <td style='padding:5px;color:#374151;'>小華</td><td style='padding:5px;color:#374151;'>Male</td><td style='padding:5px;color:#374151;'>999</td>
        </tr>
      </table>
      <p style='color:#15803d;font-size:0.85rem;font-weight:700;margin-bottom:5px;'>清理後</p>
      <table style='width:100%;border-collapse:collapse;font-size:0.8rem;'>
        <tr style='background:#dcfce7;'>
          <td style='padding:5px;color:#374151;'>小明</td><td style='padding:5px;color:#374151;'>男</td><td style='padding:5px;color:#374151;'>85</td>
        </tr>
        <tr style='background:#dcfce7;'>
          <td style='padding:5px;color:#374151;'>小華</td><td style='padding:5px;color:#374151;'>男</td><td style='padding:5px;color:#dc2626;font-style:italic;'>（刪除）</td>
        </tr>
      </table>
    </div>
  </div>
</div>"""
    },
    {
        'id': 15,
        'chapter': '第三章：資料清理與處理',
        'title': '資料篩選與排序',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>資料篩選與排序</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>🔽 自動篩選</h3>
      <p style='color:#374151;font-size:0.9rem;margin-bottom:8px;'>資料 → 自動篩選，在欄位標題出現下拉選單：</p>
      <ul style='color:#374151;font-size:0.85rem;padding-left:16px;'>
        <li>依數值範圍篩選（成績 &gt; 80）</li>
        <li>依文字條件（班級 = "A班"）</li>
        <li>依顏色篩選（條件式格式設定後）</li>
        <li>多欄位組合篩選</li>
      </ul>
    </div>
    <div style='background:#f0fdf4;padding:12px;border-radius:8px;'>
      <h3 style='color:#15803d;font-size:0.95rem;margin-bottom:8px;'>🔼 排序技巧</h3>
      <ul style='color:#374151;font-size:0.85rem;padding-left:16px;margin:0;'>
        <li>單欄排序：點欄標題旁的箭頭</li>
        <li>多層排序：資料→排序→加入層次</li>
        <li>自訂清單排序（如職稱順序）</li>
      </ul>
    </div>
  </div>
  <div>
    <div style='background:#fdf4ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#7c3aed;font-size:1rem;margin-bottom:10px;'>🔍 進階篩選</h3>
      <p style='color:#374151;font-size:0.9rem;margin-bottom:8px;'>資料 → 進階篩選，支援複雜條件：</p>
      <div style='background:#fff;padding:10px;border-radius:6px;font-size:0.85rem;'>
        <p style='color:#7c3aed;font-weight:700;margin:0 0 4px;'>條件區域範例：</p>
        <table style='border-collapse:collapse;font-size:0.8rem;'>
          <tr style='background:#e9d5ff;'>
            <td style='padding:4px 8px;color:#374151;'>成績</td><td style='padding:4px 8px;color:#374151;'>班級</td>
          </tr>
          <tr><td style='padding:4px 8px;color:#7c3aed;font-weight:700;'>&gt;=80</td><td style='padding:4px 8px;color:#7c3aed;font-weight:700;'>A班</td></tr>
        </table>
        <p style='color:#374151;font-size:0.8rem;margin-top:6px;'>→ 篩選 A 班成績 ≥ 80 的學生</p>
      </div>
    </div>
    <div style='background:#fff7ed;padding:10px;border-radius:8px;'>
      <p style='color:#9a3412;font-size:0.85rem;margin:0;'>💡 Google 試算表也有相同的篩選/排序功能，且可即時多人協作！</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 16,
        'chapter': '第三章：資料清理與處理',
        'title': '統計函數應用',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>統計函數應用</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <h3 style='color:#374151;font-size:1rem;margin-bottom:10px;'>📐 基本描述統計</h3>
    <table style='width:100%;border-collapse:collapse;font-size:0.85rem;'>
      <tr style='background:#1e40af;color:#fff;'>
        <th style='padding:7px;text-align:left;'>函數</th>
        <th style='padding:7px;text-align:left;'>用途</th>
        <th style='padding:7px;text-align:left;'>範例</th>
      </tr>
      <tr><td style='padding:7px;color:#1e40af;font-weight:700;'>AVERAGE</td><td style='padding:7px;color:#374151;'>平均值</td><td style='padding:7px;color:#374151;font-family:monospace;'>=AVERAGE(B2:B50)</td></tr>
      <tr style='background:#f8fafc;'><td style='padding:7px;color:#1e40af;font-weight:700;'>MEDIAN</td><td style='padding:7px;color:#374151;'>中位數</td><td style='padding:7px;color:#374151;font-family:monospace;'>=MEDIAN(B2:B50)</td></tr>
      <tr><td style='padding:7px;color:#1e40af;font-weight:700;'>MODE</td><td style='padding:7px;color:#374151;'>眾數</td><td style='padding:7px;color:#374151;font-family:monospace;'>=MODE(B2:B50)</td></tr>
      <tr style='background:#f8fafc;'><td style='padding:7px;color:#1e40af;font-weight:700;'>STDEV</td><td style='padding:7px;color:#374151;'>標準差</td><td style='padding:7px;color:#374151;font-family:monospace;'>=STDEV(B2:B50)</td></tr>
      <tr><td style='padding:7px;color:#1e40af;font-weight:700;'>MAX/MIN</td><td style='padding:7px;color:#374151;'>最大/小值</td><td style='padding:7px;color:#374151;font-family:monospace;'>=MAX(B2:B50)</td></tr>
      <tr style='background:#f8fafc;'><td style='padding:7px;color:#1e40af;font-weight:700;'>COUNTIF</td><td style='padding:7px;color:#374151;'>條件計數</td><td style='padding:7px;color:#374151;font-family:monospace;'>=COUNTIF(B2:B50,">=80")</td></tr>
    </table>
  </div>
  <div>
    <div style='background:#fef9c3;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#854d0e;font-size:1rem;margin-bottom:8px;'>📊 平均 vs 中位數</h3>
      <p style='color:#374151;font-size:0.9rem;margin-bottom:8px;'>月薪資料：3萬×9人 + 100萬×1人</p>
      <p style='color:#374151;font-size:0.85rem;'>平均月薪 = <strong style='color:#dc2626;'>12.7萬</strong>（被高薪拉高，不代表多數人）</p>
      <p style='color:#374151;font-size:0.85rem;'>中位數月薪 = <strong style='color:#15803d;'>3萬</strong>（更能反映一般水準）</p>
      <div style='background:#fef3c7;padding:8px;border-radius:6px;margin-top:8px;'>
        <p style='color:#854d0e;font-size:0.8rem;margin:0;'>💡 有極端值時，用中位數比平均數更能代表「典型值」</p>
      </div>
    </div>
    <div style='background:#eff6ff;padding:10px;border-radius:8px;'>
      <p style='color:#1e40af;font-size:0.85rem;margin:0;'>🇹🇼 <strong>台灣薪資數據</strong>：2024 年台灣平均月薪 58,013 元，但中位數僅 43,636 元，差距顯示高薪者拉高了平均值。</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 17,
        'chapter': '第三章：資料清理與處理',
        'title': '🎯 第三章 隨堂測驗',
        'bg': 'purple',
        'quiz': 'q3',
        'chart': None,
        'video': None,
        'html': """
<div style='text-align:center;padding:20px;'>
  <div style='font-size:56px;margin-bottom:15px;'>🎯</div>
  <h2 style='color:#fff;font-size:2rem;font-weight:800;margin-bottom:10px;'>第三章 隨堂測驗</h2>
  <p style='color:#e9d5ff;font-size:1.1rem;'>資料清理與處理 ── 2 道題目，點擊作答！</p>
</div>"""
    },
    {
        'id': 18,
        'chapter': '第四章：資料視覺化',
        'title': '資料視覺化原則',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>資料視覺化原則</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>📊 選對圖表類型</h3>
      <table style='width:100%;border-collapse:collapse;font-size:0.85rem;'>
        <tr style='background:#1e40af;color:#fff;'>
          <th style='padding:6px;'>目的</th><th style='padding:6px;'>圖表</th>
        </tr>
        <tr><td style='padding:6px;color:#374151;'>比較大小</td><td style='padding:6px;color:#374151;'>長條圖 / 橫條圖</td></tr>
        <tr style='background:#f0f9ff;'><td style='padding:6px;color:#374151;'>趨勢變化</td><td style='padding:6px;color:#374151;'>折線圖</td></tr>
        <tr><td style='padding:6px;color:#374151;'>比例組成</td><td style='padding:6px;color:#374151;'>圓餅圖 / 環形圖</td></tr>
        <tr style='background:#f0f9ff;'><td style='padding:6px;color:#374151;'>相關性</td><td style='padding:6px;color:#374151;'>散佈圖</td></tr>
        <tr><td style='padding:6px;color:#374151;'>分布範圍</td><td style='padding:6px;color:#374151;'>箱形圖 / 直方圖</td></tr>
        <tr style='background:#f0f9ff;'><td style='padding:6px;color:#374151;'>地理分布</td><td style='padding:6px;color:#374151;'>地圖熱力圖</td></tr>
      </table>
    </div>
  </div>
  <div>
    <div style='background:#fdf4ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#7c3aed;font-size:1rem;margin-bottom:10px;'>✅ 好視覺化的原則</h3>
      <ul style='color:#374151;font-size:0.9rem;padding-left:16px;'>
        <li><strong>一圖一訊息</strong>：主題明確，避免雜亂</li>
        <li><strong>軸線有標題</strong>：X/Y 軸說明清楚</li>
        <li><strong>顏色有意義</strong>：不超過 5-6 種顏色</li>
        <li><strong>資料來源</strong>：標明出處增加可信度</li>
        <li><strong>不截斷 Y 軸</strong>：避免視覺誤導</li>
      </ul>
    </div>
    <div style='background:#fef2f2;padding:10px;border-radius:8px;'>
      <p style='color:#dc2626;font-size:0.85rem;margin:0;'>⚠️ <strong>謊言圖表</strong>：截斷 Y 軸從非零開始，讓小差距看起來很大。媒體常用此技巧製造誇大效果！</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 19,
        'chapter': '第四章：資料視覺化',
        'title': 'Google 試算表圖表製作',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': {'url': 'https://www.youtube.com/embed/LvmjGGXFaXA', 'title': 'Google 試算表圖表教學', 'desc': '學習如何在 Google 試算表製作各種圖表'},
        'html': """
<h2 class='slide-title'>Google 試算表圖表製作</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>📈 製作步驟</h3>
      <ol style='color:#374151;font-size:0.9rem;padding-left:18px;'>
        <li>選取要製作圖表的資料範圍</li>
        <li>點「插入」→「圖表」</li>
        <li>在右側「圖表編輯器」選擇類型</li>
        <li>設定標題、軸標題、顏色</li>
        <li>「自訂」標籤可進階調整</li>
        <li>可下載為 PNG / SVG 或嵌入 Docs</li>
      </ol>
    </div>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:10px;'>🎨 圖表美化技巧</h3>
      <ul style='color:#374151;font-size:0.85rem;padding-left:16px;'>
        <li>主題：選擇統一配色方案</li>
        <li>資料標籤：在長條上顯示數值</li>
        <li>趨勢線：折線圖加入預測趨勢</li>
        <li>誤差線：顯示資料不確定性</li>
        <li>雙軸：比較不同單位的兩組資料</li>
      </ul>
    </div>
    <div style='background:#fff7ed;padding:10px;border-radius:8px;'>
      <p style='color:#9a3412;font-size:0.85rem;margin:0;'>💡 Google Looker Studio（原 Data Studio）是免費的互動式儀表板工具，連結 Google 試算表即可自動更新圖表！</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 20,
        'chapter': '第四章：資料視覺化',
        'title': '台灣資料新聞',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>台灣資料新聞（Data Journalism）</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div style='display:flex;flex-direction:column;gap:12px;'>
    <div style='background:#eff6ff;padding:14px;border-radius:10px;border-left:4px solid #2563eb;'>
      <h3 style='color:#1e40af;font-size:0.95rem;margin-bottom:6px;'>📰 天下雜誌資料分析</h3>
      <p style='color:#374151;font-size:0.85rem;margin:0;'>「縣市競爭力排名」每年利用 70 個指標的開放資料，製作全台縣市綜合評比互動地圖，讀者可點擊比較不同縣市。</p>
    </div>
    <div style='background:#f0fdf4;padding:14px;border-radius:10px;border-left:4px solid #16a34a;'>
      <h3 style='color:#15803d;font-size:0.95rem;margin-bottom:6px;'>📊 關鍵評論網 + g0v</h3>
      <p style='color:#374151;font-size:0.85rem;margin:0;'>g0v（零時政府）黑客松，公民工程師取用政府開放資料，製作「各縣市議員問政紀錄」視覺化，提升政治透明度。</p>
    </div>
  </div>
  <div style='display:flex;flex-direction:column;gap:12px;'>
    <div style='background:#fff7ed;padding:14px;border-radius:10px;border-left:4px solid #ea580c;'>
      <h3 style='color:#ea580c;font-size:0.95rem;margin-bottom:6px;'>🗳️ 選舉資料視覺化</h3>
      <p style='color:#374151;font-size:0.85rem;margin:0;'>每次選舉，公視、TVBS 等媒體製作即時開票地圖，顏色深淺代表得票率，讓觀眾秒懂各地投票結果。</p>
    </div>
    <div style='background:#fdf4ff;padding:14px;border-radius:10px;border-left:4px solid #7c3aed;'>
      <h3 style='color:#7c3aed;font-size:0.95rem;margin-bottom:6px;'>🌡️ 空汙視覺化</h3>
      <p style='color:#374151;font-size:0.85rem;margin:0;'>彩色「紫爆」地圖讓一般民眾一目了然哪個地區空氣品質不好，有效推動民眾戴口罩習慣及政府改善政策。</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 21,
        'chapter': '第四章：資料視覺化',
        'title': '資料說謊的方式',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>資料視覺化如何說謊？</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div style='display:flex;flex-direction:column;gap:12px;'>
    <div style='background:#fef2f2;padding:14px;border-radius:10px;border-left:4px solid #dc2626;'>
      <h3 style='color:#dc2626;font-size:0.95rem;margin-bottom:6px;'>❌ 截斷 Y 軸</h3>
      <p style='color:#374151;font-size:0.85rem;margin:0;'>Y 軸從 98 開始而非 0，讓 98→100 的微小差異看起來是 0→100 的巨大差距。廣告常用此手法。</p>
    </div>
    <div style='background:#fef2f2;padding:14px;border-radius:10px;border-left:4px solid #dc2626;'>
      <h3 style='color:#dc2626;font-size:0.95rem;margin-bottom:6px;'>❌ 混淆百分比基數</h3>
      <p style='color:#374151;font-size:0.85rem;margin:0;'>「成長了 200%！」但基數是 1 人，現在 3 人而已。百分比增長要注意基數大小。</p>
    </div>
    <div style='background:#fef2f2;padding:14px;border-radius:10px;border-left:4px solid #dc2626;'>
      <h3 style='color:#dc2626;font-size:0.95rem;margin-bottom:6px;'>❌ 圓餅圖超過 100%</h3>
      <p style='color:#374151;font-size:0.85sm;margin:0;'>各切片加總超過 100% 或數量 > 7 個，讓圓餅圖失去意義。</p>
    </div>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:10px;'>✅ 判斷圖表真偽的方法</h3>
      <ul style='color:#374151;font-size:0.9rem;padding-left:16px;'>
        <li>確認 Y 軸從 0 開始</li>
        <li>查看資料來源與日期</li>
        <li>確認樣本數是否足夠</li>
        <li>注意圖表標題是否引導讀者</li>
        <li>相關不代表因果關係</li>
      </ul>
    </div>
    <div style='background:#fff7ed;padding:10px;border-radius:8px;'>
      <p style='color:#9a3412;font-size:0.85rem;margin:0;'>💡 <strong>相關 ≠ 因果</strong>：「吃冰淇淋的人溺水率較高」——因為夏天兩者都多，不代表吃冰淇淋導致溺水！</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 22,
        'chapter': '第四章：資料視覺化',
        'title': '🎯 第四章 隨堂測驗',
        'bg': 'purple',
        'quiz': 'q4',
        'chart': None,
        'video': None,
        'html': """
<div style='text-align:center;padding:20px;'>
  <div style='font-size:56px;margin-bottom:15px;'>🎯</div>
  <h2 style='color:#fff;font-size:2rem;font-weight:800;margin-bottom:10px;'>第四章 隨堂測驗</h2>
  <p style='color:#e9d5ff;font-size:1.1rem;'>資料視覺化 ── 2 道題目，點擊作答！</p>
</div>"""
    },
    {
        'id': 23,
        'chapter': '分組實作',
        'title': '分組實作：Google 試算表圖表分析',
        'bg': 'teal',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 style='font-size:1.8rem;font-weight:800;color:#fff;margin-bottom:20px;text-align:center;'>📊 分組實作：開放資料視覺化</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div style='background:rgba(255,255,255,0.15);padding:18px;border-radius:12px;'>
    <h3 style='color:#fff;font-size:1rem;margin-bottom:14px;'>📋 任務流程</h3>
    <div style='display:flex;flex-direction:column;gap:10px;'>
      <div style='background:rgba(255,255,255,0.2);padding:10px;border-radius:8px;'>
        <p style='color:#fff;font-weight:700;font-size:0.9rem;margin:0 0 4px;'>① 下載開放資料</p>
        <p style='color:#cffafe;font-size:0.8rem;margin:0;'>從 data.gov.tw 下載「YouBike 各站點使用量統計」或「各縣市人口統計」CSV</p>
      </div>
      <div style='background:rgba(255,255,255,0.2);padding:10px;border-radius:8px;'>
        <p style='color:#fff;font-weight:700;font-size:0.9rem;margin:0 0 4px;'>② 匯入 Google 試算表</p>
        <p style='color:#cffafe;font-size:0.8rem;margin:0;'>「檔案→匯入」，選 UTF-8 編碼避免亂碼</p>
      </div>
      <div style='background:rgba(255,255,255,0.2);padding:10px;border-radius:8px;'>
        <p style='color:#fff;font-weight:700;font-size:0.9rem;margin:0 0 4px;'>③ 資料清理</p>
        <p style='color:#cffafe;font-size:0.8rem;margin:0;'>找出並處理缺失值、格式問題（至少 2 種清理操作）</p>
      </div>
      <div style='background:rgba(255,255,255,0.2);padding:10px;border-radius:8px;'>
        <p style='color:#fff;font-weight:700;font-size:0.9rem;margin:0 0 4px;'>④ 製作 3 種圖表</p>
        <p style='color:#cffafe;font-size:0.8rem;margin:0;'>長條圖＋折線圖＋一種自選，每張圖需有標題和軸標示</p>
      </div>
      <div style='background:rgba(255,255,255,0.2);padding:10px;border-radius:8px;'>
        <p style='color:#fff;font-weight:700;font-size:0.9rem;margin:0 0 4px;'>⑤ 寫下 3 個洞見</p>
        <p style='color:#cffafe;font-size:0.8rem;margin:0;'>從圖表中發現什麼有趣的現象？</p>
      </div>
    </div>
  </div>
  <div>
    <div style='background:rgba(255,255,255,0.15);padding:15px;border-radius:12px;margin-bottom:12px;'>
      <h3 style='color:#fff;font-size:1rem;margin-bottom:10px;'>💡 洞見範例</h3>
      <div style='display:flex;flex-direction:column;gap:8px;'>
        <div style='background:rgba(255,255,255,0.2);padding:8px;border-radius:6px;'>
          <p style='color:#cffafe;font-size:0.85rem;margin:0;'>「YouBike 尖峰時段集中在上午 8-9 點和下午 5-6 點，符合通勤行為」</p>
        </div>
        <div style='background:rgba(255,255,255,0.2);padding:8px;border-radius:6px;'>
          <p style='color:#cffafe;font-size:0.85rem;margin:0;'>「台北市人口正在下滑，新北市持續增長，顯示人口往郊區移動趨勢」</p>
        </div>
      </div>
    </div>
    <div style='background:rgba(255,255,255,0.15);padding:12px;border-radius:10px;'>
      <h3 style='color:#fff;font-size:0.9rem;margin-bottom:8px;'>🏆 評分標準（100 分）</h3>
      <ul style='color:#cffafe;font-size:0.85rem;padding-left:16px;margin:0;'>
        <li>下載並成功匯入資料 <strong style='color:#fff;'>15 分</strong></li>
        <li>完成資料清理（說明操作）<strong style='color:#fff;'>25 分</strong></li>
        <li>製作 3 種圖表（格式完整）<strong style='color:#fff;'>40 分</strong></li>
        <li>洞見分析（言之有據）<strong style='color:#fff;'>20 分</strong></li>
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
<h2 style='font-size:1.8rem;font-weight:800;color:#fff;margin-bottom:20px;text-align:center;'>📖 Week 8 重點回顧</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:15px;'>
  <div style='background:rgba(255,255,255,0.12);padding:14px;border-radius:10px;'>
    <h3 style='color:#93c5fd;font-size:1rem;margin-bottom:8px;'>第一章 認識大數據</h3>
    <ul style='color:#e2e8f0;font-size:0.85rem;padding-left:16px;margin:0;'>
      <li>5V：Volume/Velocity/Variety/Veracity/Value</li>
      <li>資料科學流程：定義→蒐集→清理→分析→呈現</li>
      <li>台灣健保/悠遊卡/捷運大數據應用</li>
    </ul>
  </div>
  <div style='background:rgba(255,255,255,0.12);padding:14px;border-radius:10px;'>
    <h3 style='color:#93c5fd;font-size:1rem;margin-bottom:8px;'>第二章 Open Data</h3>
    <ul style='color:#e2e8f0;font-size:0.85rem;padding-left:16px;margin:0;'>
      <li>data.gov.tw 政府開放平台</li>
      <li>CSV/JSON/XML 機器可讀格式</li>
      <li>口罩地圖、空汙 AQI、公車 APP 案例</li>
    </ul>
  </div>
  <div style='background:rgba(255,255,255,0.12);padding:14px;border-radius:10px;'>
    <h3 style='color:#93c5fd;font-size:1rem;margin-bottom:8px;'>第三章 資料清理</h3>
    <ul style='color:#e2e8f0;font-size:0.85rem;padding-left:16px;margin:0;'>
      <li>GIGO：髒資料進，錯誤結論出</li>
      <li>缺失值/重複/格式不一/異常值處理</li>
      <li>平均 vs 中位數：極端值影響</li>
    </ul>
  </div>
  <div style='background:rgba(255,255,255,0.12);padding:14px;border-radius:10px;'>
    <h3 style='color:#93c5fd;font-size:1rem;margin-bottom:8px;'>第四章 資料視覺化</h3>
    <ul style='color:#e2e8f0;font-size:0.85rem;padding-left:16px;margin:0;'>
      <li>選對圖表：趨勢→折線、比例→圓餅</li>
      <li>謊言圖表：截斷 Y 軸、混淆基數</li>
      <li>相關 ≠ 因果，需進一步驗證</li>
    </ul>
  </div>
</div>
<div style='background:rgba(255,255,255,0.1);padding:12px;border-radius:8px;margin-top:15px;text-align:center;'>
  <p style='color:#bfdbfe;font-size:0.95rem;margin:0;'>下週預告：<strong style='color:#fff;'>資料分析實作</strong> ── Excel 函數、樞紐分析表、趨勢線與預測</p>
</div>"""
    }
]
