# -*- coding: utf-8 -*-
# Week 10: Google 試算表儀表板與期末總結

CHAPTERS = [
    {'name': '封面', 'start': 1},
    {'name': '第一章：認識資料儀表板', 'start': 2},
    {'name': '第二章：準備儀表板的資料', 'start': 8},
    {'name': '第三章：製作互動儀表板', 'start': 14},
    {'name': '第四章：城市科技與人類社會', 'start': 19},
    {'name': '期末展示', 'start': 24},
]

QUIZZES = {
    'q1': {
        'title': '第一章 隨堂測驗',
        'questions': [
            {
                'q': '「儀表板」和「一張圖表」最大的差別是什麼？',
                'options': ['儀表板一定要用付費軟體才能做', '儀表板把重要數字和多張圖表放在同一頁，讓人一眼掌握整體狀況', '儀表板只能放文字，不能放圖表', '儀表板的資料不能更新'],
                'answer': 1,
                'explain': '儀表板（Dashboard）像汽車的儀表板：把最重要的指標（KPI）和幾張相關圖表集中在一頁，看一眼就知道現況。一張圖表只回答一個問題，儀表板則讓你同時看到多個面向。'
            },
            {
                'q': '想在儀表板最上方顯示「全市可借車輛數」這個大數字，Google 試算表最適合用哪一種圖表？',
                'options': ['圓餅圖', '散佈圖', '計分卡圖表', '折線圖'],
                'answer': 2,
                'explain': '計分卡圖表（Scorecard）專門用來顯示一個關鍵數字，還可以和基準值比較（例如比昨天同一時間多或少多少），最適合放在儀表板最上方當 KPI。'
            },
        ]
    },
    'q2': {
        'title': '第二章 隨堂測驗',
        'questions': [
            {
                'q': '要做成儀表板的原始資料，下列哪一種整理方式最正確？',
                'options': ['每一列是一筆資料、第一列是欄位名稱，中間沒有合併儲存格或空白列', '為了好看，把相同的縣市合併成一格', '在資料中間插入小計列', '每個月的資料放在不同檔案'],
                'answer': 0,
                'explain': '圖表、樞紐分析表和篩選器都需要「乾淨的表格」：一列一筆、一欄一種資料、第一列是標題。合併儲存格、空白列、中間的小計列都會讓統計結果出錯。'
            },
            {
                'q': '=QUERY(A1:D100, "select B, sum(D) group by B") 這個公式在做什麼？',
                'options': ['把 B 欄和 D 欄相乘', '刪除 B 欄重複的資料', '依 B 欄分組，計算每一組 D 欄的總和', '把 A1:D100 排序'],
                'answer': 2,
                'explain': 'QUERY 函數可以用類似資料庫的語法整理資料：select 選欄位、sum 加總、group by 分組。這一行的效果和「列＝B 欄、值＝D 欄加總」的樞紐分析表一樣。'
            },
        ]
    },
    'q3': {
        'title': '第三章 隨堂測驗',
        'questions': [
            {
                'q': 'Google 試算表的「交叉分析篩選器」有什麼功能？',
                'options': ['自動幫資料畫出地圖', '點選一個條件，使用同一份資料的圖表和樞紐分析表會一起篩選', '把試算表轉成 PDF', '檢查公式有沒有錯誤'],
                'answer': 1,
                'explain': '交叉分析篩選器（Slicer）是讓儀表板「可以互動」的關鍵：選擇「大安區」，所有使用同一份資料範圍的圖表與樞紐分析表都只顯示大安區的資料，不用一張一張改。'
            },
            {
                'q': '要比較「台北市 12 個行政區的 YouBike 借車次數」，最適合哪一種圖表？',
                'options': ['長條圖', '圓餅圖', '計分卡圖表', '折線圖'],
                'answer': 0,
                'explain': '比較多個類別的數量大小用長條圖最清楚。圓餅圖適合看「占整體的比例」，而且類別太多會很難讀；折線圖適合看隨時間的變化。'
            },
        ]
    },
    'q4': {
        'title': '第四章 隨堂測驗',
        'questions': [
            {
                'q': '「工業 4.0」主要整合了哪些技術，讓工廠變成「智慧工廠」？',
                'options': ['蒸汽機與鐵路', '人工智慧、物聯網、巨量資料、雲端運算', '電話與傳真機', '只靠增加工人'],
                'answer': 1,
                'explain': '工業 4.0 整合 AI、IoT、巨量資料與雲端：設備、物料和人員高度互聯，製造過程即時數據化，還能自我學習與改善。'
            },
            {
                'q': 'ATM 出現後，銀行櫃員的總人數反而沒有減少，主要原因是？',
                'options': ['ATM 常常故障', 'ATM 取代重複的工作，銀行開了更多分行，櫃員轉做客戶關係與服務', '政府禁止裁員', '大家不會用 ATM'],
                'answer': 1,
                'explain': '科技常常取代的是「工作中重複的部分」，而不是整個職業。人力會轉向更需要溝通與判斷的工作——AI 時代也是一樣。'
            },
            {
                'q': '在網路上看到驚人的消息，下列哪一種做法最能避免被假消息騙？',
                'options': ['馬上轉傳給家人提醒', '看按讚數多不多', '找政府（.gov）、教育（.edu）等可靠來源，並用事實查核網站多方查證', '只要有圖片就是真的'],
                'answer': 2,
                'explain': '假消息傳得快又廣、造假技術越來越真、還會精準投遞給容易相信的人。要從可靠來源、多個管道確認，也可以查事實查核網站。'
            },
            {
                'q': '民眾自發用開放資料做網站、監督政府預算（例如 g0v 零時政府），這屬於？',
                'options': ['公民參與', '數位落差', '網路爬蟲', '工業 4.0'],
                'answer': 0,
                'explain': '公民參與是讓大家參與公共事務的決策。開放資料讓一般人也能分析政府資料、提出建議，這也是你期末報告用開放資料的意義。'
            },
        ]
    },
}

SLIDES = [
    {
        'id': 1,
        'chapter': '封面',
        'title': 'Google 試算表儀表板與期末總結',
        'bg': 'navy',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<div style='text-align:center;padding:30px 20px;'>
  <div style='font-size:72px;margin-bottom:20px;'>🏆</div>
  <h1 style='font-size:2.6rem;font-weight:900;color:#fff;margin-bottom:12px;'>Google 試算表儀表板與期末總結</h1>
  <h2 style='font-size:1.4rem;font-weight:400;color:#93c5fd;margin-bottom:30px;'>Data Dashboard &amp; Course Finale</h2>
  <div style='display:flex;justify-content:center;gap:20px;flex-wrap:wrap;margin-bottom:30px;'>
    <span style='background:rgba(255,255,255,0.15);color:#e0f2fe;padding:8px 20px;border-radius:20px;font-size:1rem;'>📊 資料儀表板</span>
    <span style='background:rgba(255,255,255,0.15);color:#e0f2fe;padding:8px 20px;border-radius:20px;font-size:1rem;'>🎛️ 交叉分析篩選器</span>
    <span style='background:rgba(255,255,255,0.15);color:#e0f2fe;padding:8px 20px;border-radius:20px;font-size:1rem;'>📚 十週回顧</span>
    <span style='background:rgba(255,255,255,0.15);color:#e0f2fe;padding:8px 20px;border-radius:20px;font-size:1rem;'>🎓 期末報告</span>
  </div>
  <p style='color:#bfdbfe;font-size:1.1rem;'>城市科技 — 第十章（期末）</p>
</div>"""
    },
    {
        'id': 2,
        'chapter': '第一章：認識資料儀表板',
        'title': '什麼是資料儀表板？',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>什麼是資料儀表板？</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;border-left:4px solid #2563eb;padding:15px;border-radius:8px;margin-bottom:15px;'>
      <h3 style='color:#1e40af;font-size:1.1rem;margin-bottom:8px;'>📌 定義</h3>
      <p style='color:#374151;font-size:0.95rem;margin:0;'>資料儀表板（Dashboard）把<strong>最重要的數字</strong>和<strong>幾張相關圖表</strong>放在同一頁，就像汽車的儀表板，看一眼就知道現在的狀況。</p>
    </div>
    <div style='background:#f0fdf4;padding:12px;border-radius:8px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:8px;'>🧰 這週用的工具：Google 試算表</h3>
      <ul style='color:#374151;font-size:0.88rem;padding-left:16px;margin:0;line-height:1.7;'>
        <li>用學校 Google 帳號就能用，不用安裝軟體</li>
        <li>Ch08、Ch09 學過的清理、函數、樞紐分析都用得到</li>
        <li>圖表＋計分卡＋交叉分析篩選器 → 組成互動儀表板</li>
        <li>可以共用連結，或下載成 PDF</li>
      </ul>
    </div>
  </div>
  <div>
    <div style='background:#fdf4ff;padding:15px;border-radius:10px;'>
      <h3 style='color:#7c3aed;font-size:1rem;margin-bottom:10px;'>📊 一張圖表 vs 儀表板</h3>
      <table style='width:100%;border-collapse:collapse;font-size:0.85rem;'>
        <tr style='background:#7c3aed;color:#fff;'>
          <th style='padding:6px;'>比較</th><th style='padding:6px;'>一張圖表</th><th style='padding:6px;'>儀表板</th>
        </tr>
        <tr><td style='padding:6px;color:#374151;'>回答的問題</td><td style='padding:6px;text-align:center;color:#374151;'>1 個</td><td style='padding:6px;text-align:center;color:#16a34a;font-weight:700;'>多個面向</td></tr>
        <tr style='background:#f9fafb;'><td style='padding:6px;color:#374151;'>重要數字（KPI）</td><td style='padding:6px;text-align:center;color:#dc2626;'>沒有</td><td style='padding:6px;text-align:center;color:#16a34a;font-weight:700;'>放在最上方</td></tr>
        <tr><td style='padding:6px;color:#374151;'>互動篩選</td><td style='padding:6px;text-align:center;color:#dc2626;'>沒有</td><td style='padding:6px;text-align:center;color:#16a34a;font-weight:700;'>點選就篩選</td></tr>
        <tr style='background:#f9fafb;'><td style='padding:6px;color:#374151;'>資料更新</td><td style='padding:6px;text-align:center;color:#374151;'>要重畫</td><td style='padding:6px;text-align:center;color:#16a34a;font-weight:700;'>改資料就自動更新</td></tr>
      </table>
    </div>
  </div>
</div>"""
    },
    {
        'id': 3,
        'chapter': '第一章：認識資料儀表板',
        'title': '儀表板的四個組成',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>儀表板的四個組成（Google 試算表對應功能）</h2>
<div style='display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:15px;'>
  <div style='background:#eff6ff;padding:14px;border-radius:12px;text-align:center;border:2px solid #2563eb;'>
    <div style='font-size:2.2rem;margin-bottom:6px;'>🔢</div>
    <h3 style='color:#1e40af;font-size:1rem;margin-bottom:6px;'>KPI 數字</h3>
    <p style='color:#374151;font-size:0.82rem;margin:0;'>總數、平均、最高<br>→ <strong>計分卡圖表</strong></p>
  </div>
  <div style='background:#f0fdf4;padding:14px;border-radius:12px;text-align:center;border:2px solid #16a34a;'>
    <div style='font-size:2.2rem;margin-bottom:6px;'>📊</div>
    <h3 style='color:#15803d;font-size:1rem;margin-bottom:6px;'>圖表</h3>
    <p style='color:#374151;font-size:0.82rem;margin:0;'>比較、趨勢、比例<br>→ <strong>插入 → 圖表</strong></p>
  </div>
  <div style='background:#fff7ed;padding:14px;border-radius:12px;text-align:center;border:2px solid #ea580c;'>
    <div style='font-size:2.2rem;margin-bottom:6px;'>🎛️</div>
    <h3 style='color:#c2410c;font-size:1rem;margin-bottom:6px;'>篩選器</h3>
    <p style='color:#374151;font-size:0.82rem;margin:0;'>點選條件一起篩選<br>→ <strong>交叉分析篩選器</strong></p>
  </div>
  <div style='background:#fdf4ff;padding:14px;border-radius:12px;text-align:center;border:2px solid #7c3aed;'>
    <div style='font-size:2.2rem;margin-bottom:6px;'>🗂️</div>
    <h3 style='color:#7c3aed;font-size:1rem;margin-bottom:6px;'>彙總表</h3>
    <p style='color:#374151;font-size:0.82rem;margin:0;'>分組加總、平均<br>→ <strong>樞紐分析表</strong></p>
  </div>
</div>
<div style='background:#fff7ed;padding:12px;border-radius:8px;border:1px solid #fdba74;'>
  <p style='color:#9a3412;font-size:0.9rem;margin:0;'>💡 這四樣東西 Ch08、Ch09 幾乎都學過了，這週的重點是把它們<strong>組合在同一頁</strong>，並讓它們<strong>一起連動</strong>。</p>
</div>"""
    },
    {
        'id': 4,
        'chapter': '第一章：認識資料儀表板',
        'title': '生活中的儀表板',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>生活中的儀表板</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div style='display:flex;flex-direction:column;gap:12px;'>
    <div style='background:#eff6ff;padding:14px;border-radius:10px;border-left:4px solid #2563eb;'>
      <h3 style='color:#1e40af;font-size:0.95rem;margin-bottom:6px;'>⚡ 台電「今日電力資訊」</h3>
      <p style='color:#374151;font-size:0.85rem;margin:0;'>用燈號和數字顯示今天的用電量、備轉容量率，一眼就知道供電是否吃緊，是很典型的 KPI 儀表板。</p>
    </div>
    <div style='background:#f0fdf4;padding:14px;border-radius:10px;border-left:4px solid #16a34a;'>
      <h3 style='color:#15803d;font-size:0.95rem;margin-bottom:6px;'>🌫️ 空氣品質監測網</h3>
      <p style='color:#374151;font-size:0.85rem;margin:0;'>環境部把全台測站的 AQI 用顏色畫在地圖上，再搭配各測站的數值與趨勢，選測站就能看細節。</p>
    </div>
  </div>
  <div style='display:flex;flex-direction:column;gap:12px;'>
    <div style='background:#fff7ed;padding:14px;border-radius:10px;border-left:4px solid #ea580c;'>
      <h3 style='color:#ea580c;font-size:0.95rem;margin-bottom:6px;'>⌚ 手機的健康 App</h3>
      <p style='color:#374151;font-size:0.85rem;margin:0;'>今天走了幾步、睡了多久，用大數字顯示，下面再用長條圖比較一週的變化——你每天都在看儀表板。</p>
    </div>
    <div style='background:#fdf4ff;padding:14px;border-radius:10px;border-left:4px solid #7c3aed;'>
      <h3 style='color:#7c3aed;font-size:0.95rem;margin-bottom:6px;'>🚲 這週的範例：YouBike 即時儀表板</h3>
      <p style='color:#374151;font-size:0.85rem;margin:0;'>用臺北市資料大平臺的 YouBike 2.0 即時資料做成一頁：最上方是站點數、可借車輛，下面是各區長條圖，再加上「行政區」篩選器。</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 5,
        'chapter': '第一章：認識資料儀表板',
        'title': '用公式算出 KPI',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>用公式算出 KPI</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:8px;'>📐 什麼是 KPI？</h3>
      <p style='color:#374151;font-size:0.9rem;margin:0;'>KPI（關鍵績效指標）是最能代表現況的幾個數字。先在一個「計算」分頁用公式算好，再拿去做計分卡。</p>
    </div>
    <div style='background:#f0fdf4;padding:12px;border-radius:8px;'>
      <h3 style='color:#15803d;font-size:0.95rem;margin-bottom:8px;'>✨ 常用 KPI 公式（Ch09 學過）</h3>
      <div style='display:flex;flex-direction:column;gap:6px;font-family:monospace;font-size:0.8rem;'>
        <div style='background:#fff;padding:8px;border-radius:6px;color:#15803d;'>總借車次數 =SUM(資料!E2:E200)</div>
        <div style='background:#fff;padding:8px;border-radius:6px;color:#15803d;'>平均每站 =AVERAGE(資料!E2:E200)</div>
        <div style='background:#fff;padding:8px;border-radius:6px;color:#15803d;'>大站數量 =COUNTIF(資料!E2:E200,"&gt;=4000")</div>
        <div style='background:#fff;padding:8px;border-radius:6px;color:#15803d;'>及格率 =COUNTIF(B2:B31,"&gt;=60")/COUNT(B2:B31)</div>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#fdf4ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#7c3aed;font-size:1rem;margin-bottom:10px;'>🔢 好的 KPI 要符合</h3>
      <ul style='color:#374151;font-size:0.88rem;padding-left:16px;margin:0;line-height:1.7;'>
        <li><strong>少</strong>：一個儀表板 3–4 個就好</li>
        <li><strong>有意義</strong>：跟你想回答的問題有關</li>
        <li><strong>可比較</strong>：最好有基準（上個月、全市平均）</li>
        <li><strong>標清楚單位</strong>：次、人、%、元</li>
      </ul>
    </div>
    <div style='background:#fff7ed;padding:10px;border-radius:8px;'>
      <p style='color:#9a3412;font-size:0.85rem;margin:0;'>💡 公式引用原始資料，原始資料一更新，KPI 和計分卡就會自動跟著更新。</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 6,
        'chapter': '第一章：認識資料儀表板',
        'title': '儀表板設計原則',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>儀表板設計原則</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>✅ 好儀表板的特徵</h3>
      <ul style='color:#374151;font-size:0.9rem;padding-left:16px;'>
        <li><strong>5 秒原則</strong>：5 秒內看懂核心訊息</li>
        <li><strong>F 型閱讀</strong>：重要 KPI 放左上角</li>
        <li><strong>一頁一主題</strong>：不要塞太多圖表</li>
        <li><strong>顏色一致</strong>：同一種資料用同一個顏色</li>
        <li><strong>互動篩選</strong>：讓使用者自行探索</li>
        <li><strong>標題清楚</strong>：每張圖都有標題和單位</li>
      </ul>
    </div>
  </div>
  <div>
    <div style='background:#fef9c3;padding:15px;border-radius:10px;margin-bottom:12px;border:1px solid #fde047;'>
      <h3 style='color:#854d0e;font-size:1rem;margin-bottom:10px;'>🎨 版面配置範例（YouBike 儀表板）</h3>
      <div style='background:#fff;padding:10px;border-radius:8px;'>
        <div style='display:grid;grid-template-columns:1fr 1fr 1fr;gap:4px;margin-bottom:4px;'>
          <div style='background:#dbeafe;padding:8px;border-radius:4px;text-align:center;font-size:0.7rem;color:#1e40af;font-weight:700;'>KPI<br>總借車次數</div>
          <div style='background:#dcfce7;padding:8px;border-radius:4px;text-align:center;font-size:0.7rem;color:#15803d;font-weight:700;'>KPI<br>站點數</div>
          <div style='background:#fef9c3;padding:8px;border-radius:4px;text-align:center;font-size:0.7rem;color:#854d0e;font-weight:700;'>KPI<br>平均每站</div>
        </div>
        <div style='display:grid;grid-template-columns:2fr 1fr;gap:4px;'>
          <div style='background:#f1f5f9;padding:8px;border-radius:4px;text-align:center;font-size:0.7rem;color:#374151;'>各區借車次數（長條圖）</div>
          <div style='background:#f1f5f9;padding:8px;border-radius:4px;text-align:center;font-size:0.7rem;color:#374151;'>行政區篩選器</div>
        </div>
      </div>
      <p style='color:#854d0e;font-size:0.8rem;margin-top:8px;'>重要指標在上，詳細圖表在下</p>
    </div>
    <div style='background:#fef2f2;padding:10px;border-radius:8px;'>
      <p style='color:#dc2626;font-size:0.85rem;margin:0;'>❌ <strong>常見錯誤</strong>：顏色太多、一頁放 8 個圖表、圖表沒有標題、字太小看不清楚。</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 7,
        'chapter': '第一章：認識資料儀表板',
        'title': '🎯 第一章 隨堂測驗',
        'bg': 'purple',
        'quiz': 'q1',
        'chart': None,
        'video': None,
        'html': """
<div style='text-align:center;padding:20px;'>
  <div style='font-size:56px;margin-bottom:15px;'>🎯</div>
  <h2 style='color:#fff;font-size:2rem;font-weight:800;margin-bottom:10px;'>第一章 隨堂測驗</h2>
  <p style='color:#e9d5ff;font-size:1.1rem;'>認識資料儀表板 ── 2 道題目，點擊作答！</p>
</div>"""
    },
    {
        'id': 8,
        'chapter': '第二章：準備儀表板的資料',
        'title': '儀表板的資料要先整理好',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>儀表板的資料要先整理好</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div style='background:#f0fdf4;padding:15px;border-radius:10px;border-top:4px solid #16a34a;'>
    <h3 style='color:#15803d;font-size:1rem;margin-bottom:10px;'>✅ 乾淨表格的規則</h3>
    <ul style='color:#374151;font-size:0.9rem;padding-left:16px;margin:0;line-height:1.8;'>
      <li>第一列是欄位名稱，而且不重複</li>
      <li>每一列是一筆資料（一個站點、一位學生）</li>
      <li>每一欄只放一種資料（數字欄不要混文字）</li>
      <li>不要合併儲存格、不要空白列、不要在中間插小計</li>
      <li>Ch08 的清理步驟先做完：TRIM、去重複、補缺值</li>
    </ul>
  </div>
  <div>
    <div style='background:#fef2f2;padding:12px;border-radius:8px;margin-bottom:10px;'>
      <p style='color:#991b1b;font-weight:700;font-size:0.9rem;margin:0 0 6px;'>❌ 不適合做儀表板</p>
      <table style='width:100%;border-collapse:collapse;font-size:0.78rem;color:#374151;'>
        <tr style='background:#fee2e2;'><td style='padding:4px;'>大安區（合併）</td><td style='padding:4px;'>公館站 3,200</td></tr>
        <tr><td style='padding:4px;'></td><td style='padding:4px;'>大安站 2,950</td></tr>
        <tr style='background:#fee2e2;'><td style='padding:4px;'>小計</td><td style='padding:4px;'>6,150</td></tr>
      </table>
    </div>
    <div style='background:#ecfdf5;padding:12px;border-radius:8px;'>
      <p style='color:#065f46;font-weight:700;font-size:0.9rem;margin:0 0 6px;'>✅ 適合做儀表板</p>
      <table style='width:100%;border-collapse:collapse;font-size:0.78rem;color:#374151;'>
        <tr style='background:#d1fae5;font-weight:700;'><td style='padding:4px;'>行政區</td><td style='padding:4px;'>站點</td><td style='padding:4px;'>借車次數</td></tr>
        <tr><td style='padding:4px;'>大安區</td><td style='padding:4px;'>公館站</td><td style='padding:4px;'>3200</td></tr>
        <tr><td style='padding:4px;'>大安區</td><td style='padding:4px;'>大安站</td><td style='padding:4px;'>2950</td></tr>
      </table>
    </div>
  </div>
</div>"""
    },
    {
        'id': 9,
        'chapter': '第二章：準備儀表板的資料',
        'title': '把開放資料匯入 Google 試算表',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>把開放資料匯入 Google 試算表</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div style='background:#eff6ff;padding:15px;border-radius:10px;'>
    <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>📥 方法一：下載 CSV 再匯入</h3>
    <ol style='color:#374151;font-size:0.88rem;padding-left:18px;margin:0;line-height:1.8;'>
      <li>到 data.gov.tw 或臺北市資料大平臺下載 CSV</li>
      <li>Google 試算表 → 檔案 → 匯入 → 上傳</li>
      <li>選「插入新工作表」，分隔符號選「自動偵測」</li>
      <li>工作表改名為「資料」，不要直接在這裡改原始數字</li>
    </ol>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:8px;'>🔗 方法二：用公式直接讀網址</h3>
      <div style='background:#fff;padding:8px;border-radius:6px;font-family:monospace;font-size:0.8rem;color:#15803d;margin-bottom:6px;'>=IMPORTDATA("CSV 檔的網址")</div>
      <p style='color:#374151;font-size:0.85rem;margin:0;'>資料平臺提供 CSV 下載網址時，可以用 IMPORTDATA 直接讀進來，網址上的資料更新，試算表也會跟著更新。</p>
    </div>
    <div style='background:#fff7ed;padding:10px;border-radius:8px;'>
      <p style='color:#9a3412;font-size:0.85rem;margin:0;'>⚠️ 中文出現亂碼時，改用「檔案 → 匯入」上傳，或確認 CSV 是 UTF-8 編碼。記得寫下資料名稱、提供機關與下載日期，期末報告要用。</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 10,
        'chapter': '第二章：準備儀表板的資料',
        'title': '用樞紐分析表彙總',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>用樞紐分析表彙總資料</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div style='background:#eff6ff;padding:15px;border-radius:10px;'>
    <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>🗂️ 步驟（Ch09 學過）</h3>
    <ol style='color:#374151;font-size:0.88rem;padding-left:18px;margin:0;line-height:1.8;'>
      <li>選取整份資料（含第一列標題）</li>
      <li>插入 → 樞紐分析表 → 新工作表</li>
      <li>列：行政區　值：借車次數（SUM）</li>
      <li>再新增一個值：站點（COUNTA）→ 每區有幾站</li>
      <li>依借車次數「遞減」排序</li>
    </ol>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:12px;border-radius:8px;margin-bottom:10px;'>
      <p style='color:#15803d;font-weight:700;font-size:0.9rem;margin:0 0 6px;'>📊 樞紐分析結果</p>
      <table style='width:100%;border-collapse:collapse;font-size:0.8rem;color:#374151;'>
        <tr style='background:#dcfce7;font-weight:700;'><td style='padding:4px;'>行政區</td><td style='padding:4px;'>借車次數</td><td style='padding:4px;'>站點數</td></tr>
        <tr><td style='padding:4px;'>大安區</td><td style='padding:4px;'>28,567</td><td style='padding:4px;'>5</td></tr>
        <tr><td style='padding:4px;'>中正區</td><td style='padding:4px;'>21,757</td><td style='padding:4px;'>4</td></tr>
        <tr><td style='padding:4px;'>…</td><td style='padding:4px;'>…</td><td style='padding:4px;'>…</td></tr>
      </table>
      <p style='color:#64748b;font-size:0.72rem;margin:4px 0 0;'>（教學模擬資料）</p>
    </div>
    <div style='background:#fff7ed;padding:10px;border-radius:8px;'>
      <p style='color:#9a3412;font-size:0.85rem;margin:0;'>💡 樞紐分析表本身就可以拿來畫圖表；交叉分析篩選器也能同時篩選樞紐分析表。</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 11,
        'chapter': '第二章：準備儀表板的資料',
        'title': 'QUERY、FILTER、SORT 函數',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>用函數整理資料：QUERY、FILTER、SORT</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div style='display:flex;flex-direction:column;gap:10px;'>
    <div style='background:#eff6ff;padding:12px;border-radius:8px;'>
      <p style='color:#1e40af;font-weight:700;font-size:0.9rem;margin:0 0 6px;'>QUERY：分組加總（像樞紐分析表）</p>
      <div style='background:#fff;padding:8px;border-radius:6px;font-family:monospace;font-size:0.78rem;color:#1e40af;'>=QUERY(資料!A1:F200, "select C, sum(E) group by C order by sum(E) desc", 1)</div>
      <p style='color:#374151;font-size:0.8rem;margin:6px 0 0;'>依 C 欄（行政區）分組，加總 E 欄（借車次數），由大到小排列。</p>
    </div>
    <div style='background:#f0fdf4;padding:12px;border-radius:8px;'>
      <p style='color:#15803d;font-weight:700;font-size:0.9rem;margin:0 0 6px;'>FILTER：只留下符合條件的資料</p>
      <div style='background:#fff;padding:8px;border-radius:6px;font-family:monospace;font-size:0.78rem;color:#15803d;'>=FILTER(資料!A2:F200, 資料!C2:C200="大安區")</div>
    </div>
  </div>
  <div style='display:flex;flex-direction:column;gap:10px;'>
    <div style='background:#fdf4ff;padding:12px;border-radius:8px;'>
      <p style='color:#7c3aed;font-weight:700;font-size:0.9rem;margin:0 0 6px;'>SORT：排序（找前幾名）</p>
      <div style='background:#fff;padding:8px;border-radius:6px;font-family:monospace;font-size:0.78rem;color:#7c3aed;'>=SORT(資料!B2:E200, 4, FALSE)</div>
      <p style='color:#374151;font-size:0.8rem;margin:6px 0 0;'>依範圍內第 4 欄由大到小排序；搭配 ARRAY_CONSTRAIN 可只取前 5 名。</p>
    </div>
    <div style='background:#fff7ed;padding:12px;border-radius:8px;'>
      <p style='color:#9a3412;font-size:0.85rem;margin:0;'>💡 這些函數的結果會<strong>跟著原始資料自動更新</strong>，很適合當儀表板圖表的資料來源。不熟也沒關係，用樞紐分析表一樣做得到。</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 12,
        'chapter': '第二章：準備儀表板的資料',
        'title': '規劃三個工作表',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>規劃三個工作表：資料 → 計算 → 儀表板</h2>
<div style='display:grid;grid-template-columns:1fr auto 1fr auto 1fr;gap:10px;align-items:center;margin-bottom:15px;'>
  <div style='background:#eff6ff;padding:15px;border-radius:12px;text-align:center;border:2px solid #2563eb;'>
    <div style='font-size:2rem;'>📄</div>
    <h3 style='color:#1e40af;font-size:1rem;margin:6px 0;'>資料</h3>
    <p style='color:#374151;font-size:0.8rem;margin:0;'>匯入的原始資料<br>清理後就不要再動</p>
  </div>
  <div style='font-size:1.6rem;color:#64748b;'>→</div>
  <div style='background:#f0fdf4;padding:15px;border-radius:12px;text-align:center;border:2px solid #16a34a;'>
    <div style='font-size:2rem;'>🧮</div>
    <h3 style='color:#15803d;font-size:1rem;margin:6px 0;'>計算</h3>
    <p style='color:#374151;font-size:0.8rem;margin:0;'>KPI 公式、樞紐分析表<br>QUERY 的結果</p>
  </div>
  <div style='font-size:1.6rem;color:#64748b;'>→</div>
  <div style='background:#fdf4ff;padding:15px;border-radius:12px;text-align:center;border:2px solid #7c3aed;'>
    <div style='font-size:2rem;'>📊</div>
    <h3 style='color:#7c3aed;font-size:1rem;margin:6px 0;'>儀表板</h3>
    <p style='color:#374151;font-size:0.8rem;margin:0;'>只放計分卡、圖表<br>和篩選器</p>
  </div>
</div>
<div style='background:#fff7ed;padding:12px;border-radius:8px;border:1px solid #fdba74;'>
  <p style='color:#9a3412;font-size:0.9rem;margin:0;'>💡 分開放的好處：原始資料不會被誤改、公式好檢查，儀表板頁面也比較乾淨。儀表板頁可以「檢視 → 隱藏格線」，看起來更像一頁報表。</p>
</div>"""
    },
    {
        'id': 13,
        'chapter': '第二章：準備儀表板的資料',
        'title': '🎯 第二章 隨堂測驗',
        'bg': 'purple',
        'quiz': 'q2',
        'chart': None,
        'video': None,
        'html': """
<div style='text-align:center;padding:20px;'>
  <div style='font-size:56px;margin-bottom:15px;'>🎯</div>
  <h2 style='color:#fff;font-size:2rem;font-weight:800;margin-bottom:10px;'>第二章 隨堂測驗</h2>
  <p style='color:#e9d5ff;font-size:1.1rem;'>準備儀表板的資料 ── 2 道題目，點擊作答！</p>
</div>"""
    },
    {
        'id': 14,
        'chapter': '第三章：製作互動儀表板',
        'title': '選對圖表類型',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>選對圖表類型</h2>
<table class='info-table' style='font-size:0.85rem;margin-bottom:12px;'>
  <thead class='table-header'><tr><th style='width:22%;'>想表達</th><th style='width:24%;'>Google 試算表圖表</th><th>例子</th></tr></thead>
  <tbody>
    <tr><td>一個關鍵數字</td><td><strong>計分卡圖表</strong></td><td>全市總借車次數、全班平均</td></tr>
    <tr class='tr-highlight'><td>比較大小</td><td><strong>長條圖／柱狀圖</strong></td><td>各行政區借車次數</td></tr>
    <tr><td>隨時間變化</td><td><strong>折線圖</strong></td><td>每小時借車次數、每月 AQI</td></tr>
    <tr class='tr-highlight'><td>占整體比例</td><td><strong>圓餅圖</strong>（類別 5 個以內）</td><td>各等第人數比例</td></tr>
    <tr><td>兩個變數的關係</td><td><strong>散佈圖</strong></td><td>車柱數 vs 借車次數</td></tr>
    <tr class='tr-highlight'><td>詳細數字</td><td><strong>表格圖表</strong></td><td>前 10 名站點清單</td></tr>
  </tbody>
</table>
<div style='background:#fef2f2;padding:10px;border-radius:8px;'>
  <p style='color:#dc2626;font-size:0.85rem;margin:0;'>⚠️ Ch08 學過的「資料說謊」：Y 軸不要從中間開始、不要用 3D 圖表、圓餅圖不要放太多類別。</p>
</div>"""
    },
    {
        'id': 15,
        'chapter': '第三章：製作互動儀表板',
        'title': '插入圖表與計分卡',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>插入圖表與計分卡</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div style='background:#eff6ff;padding:15px;border-radius:10px;'>
    <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>🔢 計分卡圖表（KPI）</h3>
    <ol style='color:#374151;font-size:0.88rem;padding-left:18px;margin:0;line-height:1.8;'>
      <li>選取要加總的數字欄</li>
      <li>插入 → 圖表 → 圖表類型選「計分卡圖表」</li>
      <li>「主要值」選欄位，彙總方式選加總或平均</li>
      <li>可設定「基準值」，顯示比基準高或低多少</li>
      <li>自訂 → 改字體大小與顏色</li>
    </ol>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:8px;'>📊 一般圖表</h3>
      <ul style='color:#374151;font-size:0.88rem;padding-left:16px;margin:0;line-height:1.7;'>
        <li>選取樞紐分析表或 QUERY 結果 → 插入 → 圖表</li>
        <li>圖表編輯器「設定」選類型、「自訂」改標題與軸標</li>
        <li>剪下圖表，貼到「儀表板」工作表排版</li>
      </ul>
    </div>
    <div style='background:#fff7ed;padding:10px;border-radius:8px;'>
      <p style='color:#9a3412;font-size:0.85rem;margin:0;'>💡 每張圖都要有<strong>標題、軸標與單位</strong>；同一個儀表板的圖表大小盡量一致、對齊排好。</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 16,
        'chapter': '第三章：製作互動儀表板',
        'title': '交叉分析篩選器：讓儀表板動起來',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>交叉分析篩選器：讓儀表板動起來</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div style='background:#eff6ff;padding:15px;border-radius:10px;'>
    <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>🎛️ 新增篩選器</h3>
    <ol style='color:#374151;font-size:0.88rem;padding-left:18px;margin:0;line-height:1.8;'>
      <li>點選資料範圍內任一格</li>
      <li>資料 → 新增交叉分析篩選器</li>
      <li>在右側選要篩選的欄位（例如「行政區」）</li>
      <li>把篩選器拖到儀表板最上方</li>
      <li>點篩選器，勾選「大安區」試試看</li>
    </ol>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:8px;'>✨ 會發生什麼事？</h3>
      <p style='color:#374151;font-size:0.88rem;margin:0;'>使用<strong>同一個資料範圍</strong>的圖表和樞紐分析表，會一起只顯示「大安區」的資料。這就是儀表板的「互動」。</p>
    </div>
    <div style='background:#fff7ed;padding:10px;border-radius:8px;margin-bottom:10px;'>
      <p style='color:#9a3412;font-size:0.85rem;margin:0;'>⚠️ 用公式（QUERY、SUM）算出來的 KPI 不會被篩選器影響；想讓 KPI 也連動，可以改用計分卡圖表直接讀原始資料範圍。</p>
    </div>
    <div style='background:#fdf4ff;padding:10px;border-radius:8px;'>
      <p style='color:#7c3aed;font-size:0.85rem;margin:0;'>💡 可以放兩個篩選器（例如「行政區」＋「月份」），交叉找出想看的資料。</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 17,
        'chapter': '第三章：製作互動儀表板',
        'title': '美化、分享與下載',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>美化、分享與下載</h2>
<div style='display:grid;grid-template-columns:repeat(3,1fr);gap:14px;'>
  <div style='background:#eff6ff;padding:14px;border-radius:10px;'>
    <h3 style='color:#1e40af;font-size:0.95rem;margin-bottom:8px;'>🎨 美化</h3>
    <ul style='color:#374151;font-size:0.85rem;padding-left:16px;margin:0;line-height:1.7;'>
      <li>格式 → 主題，統一字型與配色</li>
      <li>檢視 → 隱藏格線</li>
      <li>最上方加大標題、資料來源與更新日期</li>
      <li>圖表大小一致、上下左右對齊</li>
    </ul>
  </div>
  <div style='background:#f0fdf4;padding:14px;border-radius:10px;'>
    <h3 style='color:#15803d;font-size:0.95rem;margin-bottom:8px;'>🔗 分享</h3>
    <ul style='color:#374151;font-size:0.85rem;padding-left:16px;margin:0;line-height:1.7;'>
      <li>共用 → 一般存取權設為「檢視者」</li>
      <li>別人只能看、能操作篩選器，不會改到資料</li>
      <li>不要把含個資的資料公開分享</li>
    </ul>
  </div>
  <div style='background:#fdf4ff;padding:14px;border-radius:10px;'>
    <h3 style='color:#7c3aed;font-size:0.95rem;margin-bottom:8px;'>📄 下載與放進報告</h3>
    <ul style='color:#374151;font-size:0.85rem;padding-left:16px;margin:0;line-height:1.7;'>
      <li>檔案 → 下載 → PDF，選「儀表板」工作表</li>
      <li>單張圖表：點圖表右上角 ⋮ → 下載 PNG</li>
      <li>期末報告的圖表就可以從這裡來</li>
    </ul>
  </div>
</div>
<div style='background:#fff7ed;padding:12px;border-radius:8px;margin-top:14px;border:1px solid #fdba74;'>
  <p style='color:#9a3412;font-size:0.9rem;margin:0;'>🚀 想挑戰更進階的儀表板工具，可以自己試試 Google 的 Looker Studio，它可以直接連接你的 Google 試算表。</p>
</div>"""
    },
    {
        'id': 18,
        'chapter': '第三章：製作互動儀表板',
        'title': '🎯 第三章 隨堂測驗',
        'bg': 'purple',
        'quiz': 'q3',
        'chart': None,
        'video': None,
        'html': """
<div style='text-align:center;padding:20px;'>
  <div style='font-size:56px;margin-bottom:15px;'>🎯</div>
  <h2 style='color:#fff;font-size:2rem;font-weight:800;margin-bottom:10px;'>第三章 隨堂測驗</h2>
  <p style='color:#e9d5ff;font-size:1.1rem;'>製作互動儀表板 ── 2 道題目，點擊作答！</p>
</div>"""
    },
    {
        'id': 19,
        'chapter': '第四章：城市科技與人類社會',
        'title': '十週學習地圖',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>十週學習地圖</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:15px;'>
  <div style='display:flex;flex-direction:column;gap:8px;'>
    <div style='background:#eff6ff;padding:10px;border-radius:8px;border-left:3px solid #2563eb;'>
      <div style='display:flex;align-items:center;gap:8px;'>
        <span style='background:#2563eb;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.8rem;font-weight:700;'>W1</span>
        <div>
          <p style='font-weight:700;color:#1e40af;font-size:0.85rem;margin:0;'>科技演進與硬體</p>
          <p style='color:#374151;font-size:0.75rem;margin:0;'>CPU/記憶體/硬體辨識</p>
        </div>
      </div>
    </div>
    <div style='background:#f0fdf4;padding:10px;border-radius:8px;border-left:3px solid #16a34a;'>
      <div style='display:flex;align-items:center;gap:8px;'>
        <span style='background:#16a34a;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.8rem;font-weight:700;'>W2</span>
        <div>
          <p style='font-weight:700;color:#15803d;font-size:0.85rem;margin:0;'>AI 時代的數位創作者</p>
          <p style='color:#374151;font-size:0.75rem;margin:0;'>位元/進位/著作權/AI 生成</p>
        </div>
      </div>
    </div>
    <div style='background:#fef2f2;padding:10px;border-radius:8px;border-left:3px solid #dc2626;'>
      <div style='display:flex;align-items:center;gap:8px;'>
        <span style='background:#dc2626;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.8rem;font-weight:700;'>W3</span>
        <div>
          <p style='font-weight:700;color:#dc2626;font-size:0.85rem;margin:0;'>個人資料保護與資訊倫理</p>
          <p style='color:#374151;font-size:0.75rem;margin:0;'>個資法/Cookie/隱私/資安</p>
        </div>
      </div>
    </div>
    <div style='background:#fdf4ff;padding:10px;border-radius:8px;border-left:3px solid #7c3aed;'>
      <div style='display:flex;align-items:center;gap:8px;'>
        <span style='background:#7c3aed;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.8rem;font-weight:700;'>W4</span>
        <div>
          <p style='font-weight:700;color:#7c3aed;font-size:0.85rem;margin:0;'>Google Workspace 文書應用</p>
          <p style='color:#374151;font-size:0.75rem;margin:0;'>樣式/目錄/共同編輯</p>
        </div>
      </div>
    </div>
    <div style='background:#fff7ed;padding:10px;border-radius:8px;border-left:3px solid #ea580c;'>
      <div style='display:flex;align-items:center;gap:8px;'>
        <span style='background:#ea580c;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.8rem;font-weight:700;'>W5</span>
        <div>
          <p style='font-weight:700;color:#ea580c;font-size:0.85rem;margin:0;'>合併列印與表單應用</p>
          <p style='color:#374151;font-size:0.75rem;margin:0;'>邀請函/信封/Google 表單</p>
        </div>
      </div>
    </div>
  </div>
  <div style='display:flex;flex-direction:column;gap:8px;'>
    <div style='background:#eff6ff;padding:10px;border-radius:8px;border-left:3px solid #0369a1;'>
      <div style='display:flex;align-items:center;gap:8px;'>
        <span style='background:#0369a1;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.8rem;font-weight:700;'>W6</span>
        <div>
          <p style='font-weight:700;color:#0369a1;font-size:0.85rem;margin:0;'>網際網路運作原理</p>
          <p style='color:#374151;font-size:0.75rem;margin:0;'>TCP/IP/DNS/HTTPS/5G</p>
        </div>
      </div>
    </div>
    <div style='background:#f0fdf4;padding:10px;border-radius:8px;border-left:3px solid #0d9488;'>
      <div style='display:flex;align-items:center;gap:8px;'>
        <span style='background:#0d9488;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.8rem;font-weight:700;'>W7</span>
        <div>
          <p style='font-weight:700;color:#0d9488;font-size:0.85rem;margin:0;'>新興科技應用</p>
          <p style='color:#374151;font-size:0.75rem;margin:0;'>IoT/AIoT/雲端/量子/智慧城市</p>
        </div>
      </div>
    </div>
    <div style='background:#fef9c3;padding:10px;border-radius:8px;border-left:3px solid #ca8a04;'>
      <div style='display:flex;align-items:center;gap:8px;'>
        <span style='background:#ca8a04;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.8rem;font-weight:700;'>W8</span>
        <div>
          <p style='font-weight:700;color:#854d0e;font-size:0.85rem;margin:0;'>巨量資料與資料科學</p>
          <p style='color:#374151;font-size:0.75rem;margin:0;'>Big Data/Open Data/視覺化</p>
        </div>
      </div>
    </div>
    <div style='background:#f0fdf4;padding:10px;border-radius:8px;border-left:3px solid #65a30d;'>
      <div style='display:flex;align-items:center;gap:8px;'>
        <span style='background:#65a30d;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.8rem;font-weight:700;'>W9</span>
        <div>
          <p style='font-weight:700;color:#3f6212;font-size:0.85rem;margin:0;'>用試算表分析開放資料</p>
          <p style='color:#374151;font-size:0.75rem;margin:0;'>試算表函數/樞紐/趨勢線</p>
        </div>
      </div>
    </div>
    <div style='background:#1e40af;padding:10px;border-radius:8px;'>
      <div style='display:flex;align-items:center;gap:8px;'>
        <span style='background:#fff;color:#1e40af;padding:2px 10px;border-radius:4px;font-size:0.8rem;font-weight:700;'>W10</span>
        <div>
          <p style='font-weight:700;color:#fff;font-size:0.85rem;margin:0;'>試算表儀表板與期末總結 🎓</p>
          <p style='color:#bfdbfe;font-size:0.75rem;margin:0;'>儀表板設計/十週回顧/期末展示</p>
        </div>
      </div>
    </div>
  </div>
</div>"""
    },
    {
        'id': 20,
        'chapter': '第四章：城市科技與人類社會',
        'title': '科技如何改變產業與工作',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>科技如何改變產業與工作</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:16px;'><div><div style='background:#eff6ff;padding:12px 14px;border-radius:10px;border-left:4px solid #2563eb;margin-bottom:10px;'><h3 style='color:#1e40af;font-size:0.95rem;margin:0 0 6px;'>🏭 工業 4.0：智慧工廠</h3><div style='color:#374151;font-size:0.84rem;line-height:1.6;'>整合<strong>人工智慧、物聯網、巨量資料、雲端運算</strong>，三個特徵：<ol style='padding-left:18px;margin:6px 0 0;'><li>設備、物料、成品和人員<strong>高度互聯</strong></li><li>製造過程<strong>即時數據化</strong></li><li>可以<strong>自我學習與改善</strong></li></ol></div></div><div style='background:#f0fdf4;padding:12px 14px;border-radius:10px;border-left:4px solid #16a34a;margin-bottom:10px;'><h3 style='color:#15803d;font-size:0.95rem;margin:0 0 6px;'>📱 活絡的數位平台</h3><div style='color:#374151;font-size:0.84rem;line-height:1.6;'>平台型企業直接<strong>媒合供需雙方</strong>：Facebook、YouTube、Coursera、Google Play、Uber、foodpanda。<br>想一想：外送平台讓誰更方便？又讓誰的工作變得不穩定？</div></div></div><div><div style='background:#fff7ed;padding:12px 14px;border-radius:10px;border-left:4px solid #ea580c;margin-bottom:10px;'><h3 style='color:#c2410c;font-size:0.95rem;margin:0 0 6px;'>🏧 工作型態的改變：ATM 的故事</h3><div style='color:#374151;font-size:0.84rem;line-height:1.6;'>ATM 出現後，每家分行的櫃員變少，但銀行<strong>開了更多分行</strong>，櫃員總數反而沒有減少。<br>ATM 取代了重複無聊的工作，櫃員轉做<strong>經營客戶關係、提供更好的服務</strong>。</div></div><div style='background:#fdf4ff;padding:12px 14px;border-radius:10px;border-left:4px solid #7c3aed;margin-bottom:10px;'><h3 style='color:#7c3aed;font-size:0.95rem;margin:0 0 6px;'>💳 金融科技（FinTech）</h3><div style='color:#374151;font-size:0.84rem;line-height:1.6;'>行動支付、數位貨幣、用 AI 和大數據做理財建議的「機器人理財」，正在改變銀行與投資業。</div></div></div></div>"""
    },
    {
        'id': 21,
        'chapter': '第四章：城市科技與人類社會',
        'title': '科技帶來的挑戰：假消息與數位落差',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>科技帶來的挑戰：假消息與數位落差</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:16px;'><div><div style='background:#fef2f2;padding:12px 14px;border-radius:10px;border-left:4px solid #dc2626;margin-bottom:10px;'><h3 style='color:#dc2626;font-size:0.95rem;margin:0 0 6px;'>📰 假消息為什麼這麼多？</h3><div style='color:#374151;font-size:0.84rem;line-height:1.6;'><ul style='padding-left:18px;margin:0;'><li>傳播<strong>快又廣</strong></li><li><strong>造假技術</strong>進步（AI 生成圖、深偽影片）</li><li>演算法<strong>精準投遞</strong>給容易相信的人</li></ul></div></div><div style='background:#f0fdf4;padding:12px 14px;border-radius:10px;border-left:4px solid #16a34a;margin-bottom:10px;'><h3 style='color:#15803d;font-size:0.95rem;margin:0 0 6px;'>✅ 三招查證</h3><div style='color:#374151;font-size:0.84rem;line-height:1.6;'><ol style='padding-left:18px;margin:0;'><li>找<strong>官方或可靠網站</strong>：.gov 政府、.edu 教育、.org 法人組織</li><li><strong>多個管道</strong>交叉確認</li><li>查<strong>事實查核網站</strong>，如台灣事實查核中心</li></ol></div></div></div><div><div style='background:#eff6ff;padding:12px 14px;border-radius:10px;border-left:4px solid #2563eb;margin-bottom:10px;'><h3 style='color:#1e40af;font-size:0.95rem;margin:0 0 6px;'>🌉 數位落差</h3><div style='color:#374151;font-size:0.84rem;line-height:1.6;'>不同年齡、居住地、經濟背景的人，<strong>使用資訊科技的機會與能力</strong>不一樣。<br>例：長輩不會用行動支付、偏鄉網路慢、家裡沒有電腦可以寫作業。</div></div><div style='background:#fefce8;padding:12px 14px;border-radius:10px;border-left:4px solid #ca8a04;margin-bottom:10px;'><h3 style='color:#a16207;font-size:0.95rem;margin:0 0 6px;'>🤝 怎麼縮小落差？</h3><div style='color:#374151;font-size:0.84rem;line-height:1.6;'><ul style='padding-left:18px;margin:0;'><li>臺北市為<strong>銀髮族、新住民</strong>開設數位課程，並提供經濟弱勢借用平板</li><li>教育部推動<strong>偏鄉數位應用</strong>計畫</li><li>你也可以：教家人用手機、設計長輩看得懂的介面</li></ul></div></div></div></div>"""
    },
    {
        'id': 22,
        'chapter': '第四章：城市科技與人類社會',
        'title': '開放資料：讓市民一起參與城市',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>開放資料：讓市民一起參與城市</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:16px;'><div><div style='background:#eff6ff;padding:12px 14px;border-radius:10px;border-left:4px solid #2563eb;margin-bottom:10px;'><h3 style='color:#1e40af;font-size:0.95rem;margin:0 0 6px;'>🔓 開放資料的好處</h3><div style='color:#374151;font-size:0.84rem;line-height:1.6;'>資料開放給社會大眾，<strong>任何人都可以自由、重複使用</strong>：政府更透明、企業能開發新服務（如公車 App）、學生能做研究——你這學期就用它做報告。</div></div><div style='background:#f0fdf4;padding:12px 14px;border-radius:10px;border-left:4px solid #16a34a;margin-bottom:10px;'><h3 style='color:#15803d;font-size:0.95rem;margin:0 0 6px;'>🗳️ 公民參與</h3><div style='color:#374151;font-size:0.84rem;line-height:1.6;'>讓大家參與公共事務的決策。例如 <strong>g0v 零時政府</strong>：一群志工用開放資料把政府預算做成看得懂的網站，讓市民一起監督。</div></div></div><div><div style='background:#fff7ed;padding:12px 14px;border-radius:10px;border-left:4px solid #ea580c;margin-bottom:10px;'><h3 style='color:#c2410c;font-size:0.95rem;margin:0 0 6px;'>🔬 公民科學</h3><div style='color:#374151;font-size:0.84rem;line-height:1.6;'>一般民眾參與科學研究：提出問題、蒐集資料、分析資料。例如用手機回報看到的鳥類、路殺動物或空氣品質，<strong>人多力量大</strong>，資料量是研究團隊自己做不到的。</div></div><div style='background:#fdf4ff;padding:12px 14px;border-radius:10px;border-left:4px solid #7c3aed;margin-bottom:10px;'><h3 style='color:#7c3aed;font-size:0.95rem;margin:0 0 6px;'>🔭 對未來的展望</h3><div style='color:#374151;font-size:0.84rem;line-height:1.6;'><ul style='padding-left:18px;margin:0;'><li><strong>更快的運算</strong>：雲端、超級電腦、量子電腦</li><li><strong>更巨大的資料革命</strong>：IoT 讓城市每秒產生資料</li><li><strong>更精準的解決方法</strong>：用資料找出問題真正的原因</li></ul></div></div></div></div><div style='background:#fef3c7;border-left:4px solid #f59e0b;padding:10px 14px;border-radius:8px;font-size:.85rem;color:#78350f;margin-top:4px;'>💡 這三頁的每個主題，都可以是你的<strong>期末報告題目</strong>：例如「行動支付對長輩的影響」用數位落差調查資料、「YouBike 如何改變通勤」用 YouBike 開放資料。</div>"""
    },
    {
        'id': 23,
        'chapter': '第四章：城市科技與人類社會',
        'title': '🎯 第四章 隨堂測驗',
        'bg': 'purple',
        'quiz': 'q4',
        'chart': None,
        'video': None,
        'html': """
<div style='text-align:center;padding:20px;'>
  <div style='font-size:56px;margin-bottom:15px;'>🎯</div>
  <h2 style='color:#fff;font-size:2rem;font-weight:800;margin-bottom:10px;'>第四章 隨堂測驗</h2>
  <p style='color:#e9d5ff;font-size:1.1rem;'>城市科技與人類社會 ── 4 道題目，點擊作答！</p>
</div>"""
    },
    {
        'id': 24,
        'chapter': '期末展示',
        'title': '期末個人報告：城市科技與人類社會的關係',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<div class='slide-inner'>
  <h2 class='slide-title'>🎓 期末個人報告：城市科技與人類社會的關係</h2>
  <p class='slide-desc'>用 Ch08–Ch10 學的<strong>開放資料分析與視覺化</strong>，寫一份有資料、有圖表、有自己看法的書面報告</p>

  <div class='card-grid-2' style='margin-bottom:10px;'>
    <div style='background:#eff6ff;border-radius:10px;padding:12px 14px;border-top:4px solid #3b82f6;'>
      <p style='font-weight:700;color:#1e40af;margin:0 0 6px;font-size:.9rem;'>📌 題目自訂，選一個你關心的面向</p>
      <div style='display:grid;grid-template-columns:1fr 1fr;gap:4px 10px;font-size:.78rem;color:#374151;line-height:1.55;'>
        <div>🏭 工業 4.0 與智慧製造</div>
        <div>🛵 數位平台（外送、叫車、YouTube）</div>
        <div>📰 假訊息與媒體識讀</div>
        <div>👵 數位落差（長輩、偏鄉、新住民）</div>
        <div>💼 工作型態與金融科技</div>
        <div>🚲 開放資料與智慧城市</div>
        <div>🗳️ 公民參與（零時政府、提點子）</div>
        <div>🔬 公民科學與環境監測</div>
      </div>
    </div>
    <div style='background:#f0fdf4;border-radius:10px;padding:12px 14px;border-top:4px solid #22c55e;'>
      <p style='font-weight:700;color:#166534;margin:0 0 6px;font-size:.9rem;'>✅ 必要條件</p>
      <ul style='font-size:.8rem;color:#374151;margin:0;padding-left:18px;line-height:1.7;'>
        <li><strong>個人</strong>完成，一人一份</li>
        <li>資料分析請用<strong>政府開放資料</strong>（data.gov.tw、臺北市資料大平臺…）</li>
        <li>至少 <strong>2 張圖表</strong>（用 Google 試算表製作，做法同 Ch09）</li>
        <li>依<strong>前言、正文、結論、參考資料</strong>四段撰寫，A4 約 <strong>3–6 頁</strong></li>
        <li>參考資料要寫清楚，不引用論壇、問答或聊天網站</li>
        <li>有使用 AI 請附 <strong>AI 使用聲明</strong>（工具＋Prompt＋日期）</li>
      </ul>
    </div>
  </div>

  <div style='background:#fef3c7;border-left:4px solid #f59e0b;padding:10px 14px;border-radius:8px;font-size:.82rem;color:#78350f;line-height:1.6;'>
    💡 <strong>好題目的公式</strong>：「<strong>某項城市科技</strong>」對「<strong>某一群人／某個城市問題</strong>」的影響。<br>
    例：〈YouBike 2.0 站點分布與各行政區的通勤需要〉、〈臺北市長者使用行動支付的數位落差〉
  </div>
</div>"""
    },
    {
        'id': 25,
        'chapter': '期末展示',
        'title': '報告四段架構：每一段要寫什麼',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<div class='slide-inner'>
  <h2 class='slide-title'>🏗️ 報告四段架構：每一段要寫什麼</h2>
  <p class='slide-desc'>每一段標題用「標題 1」，排版整齊又能自動產生目錄</p>

  <table class='info-table' style='font-size:.82rem;margin-bottom:10px;'>
    <thead class='table-header'>
      <tr><th style='width:20%;'>段落</th><th>要寫什麼</th><th style='width:12%;text-align:center;'>配分</th></tr>
    </thead>
    <tbody>
      <tr><td><strong>壹、前言</strong></td><td>研究動機（為什麼想研究這個）、研究目的（想知道什麼）、研究方法（用了哪份開放資料、用什麼工具分析）</td><td style='text-align:center;'>30%</td></tr>
      <tr class='tr-highlight'><td><strong>貳、正文</strong></td><td>問題探討、資料分析結果、資料視覺化（圖表＋文字解讀），並引用、彙整相關資料</td><td style='text-align:center;'>40%</td></tr>
      <tr><td><strong>參、結論</strong></td><td>提出你對研究結果的看法，結論要和研究目的、正文互相呼應；說明未來值得進一步研究的方向</td><td style='text-align:center;'>15%</td></tr>
      <tr class='tr-highlight'><td><strong>肆、參考資料</strong></td><td>列出引用的資料與開放資料集；最好引用可信度較高的來源（.gov／.edu／新聞媒體）</td><td style='text-align:center;'>5%</td></tr>
    </tbody>
  </table>

  <div class='card-grid-2'>
    <div style='background:#eff6ff;border-radius:8px;padding:8px 12px;font-size:.78rem;color:#1e3a8a;'>
      📊 <strong>圖表小提醒</strong>：每張圖都要有標題和資料來源，文字要說明「這張圖告訴我們什麼」
    </div>
    <div style='background:#faf5ff;border-radius:8px;padding:8px 12px;font-size:.78rem;color:#581c87;'>
      🚀 <strong>下學期預告</strong>：第二學期的程式專題，會再挑戰完整的小論文格式
    </div>
  </div>
</div>"""
    },
    {
        'id': 26,
        'chapter': '期末展示',
        'title': '期末報告：時程與評分',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<div class='slide-inner'>
  <h2 class='slide-title'>🗓️ 期末報告：時程與評分</h2>

  <div class='card-grid-2' style='margin-bottom:10px;'>
    <div>
      <div style='display:flex;flex-direction:column;gap:6px;'>
        <div style='background:#eff6ff;border-left:4px solid #3b82f6;border-radius:6px;padding:8px 12px;font-size:.8rem;'>
          <strong style='color:#1e40af;'>① 秋假前最後一節</strong><br>題目與要用的開放資料定案，給老師看過
        </div>
        <div style='background:#f0fdf4;border-left:4px solid #22c55e;border-radius:6px;padding:8px 12px;font-size:.8rem;'>
          <strong style='color:#166534;'>② 秋假期間</strong><br>下載資料、做圖表、完成四段報告
        </div>
        <div style='background:#fef2f2;border-left:4px solid #ef4444;border-radius:6px;padding:8px 12px;font-size:.8rem;'>
          <strong style='color:#991b1b;'>③ 秋假最後一天 23:59 前</strong><br>匯出 PDF，檔名「班級座號姓名_題目.pdf」，上傳 Google Classroom
        </div>
        <div style='background:#faf5ff;border-left:4px solid #8b5cf6;border-radius:6px;padding:8px 12px;font-size:.8rem;'>
          <strong style='color:#6b21a8;'>④ 秋假後第 1–2 週</strong><br>每人上台 <strong>3 分鐘</strong>；全班填同學互評表
        </div>
      </div>
    </div>
    <div>
      <table class='info-table' style='font-size:.82rem;'>
        <thead class='table-header'><tr><th>評分項目</th><th style='width:20%;text-align:center;'>分數</th></tr></thead>
        <tbody>
          <tr><td colspan='2' style='background:#dbeafe;font-weight:700;color:#1e40af;'>📄 書面報告 90 分</td></tr>
          <tr><td>前言（動機、目的、方法）</td><td style='text-align:center;'>30</td></tr>
          <tr class='tr-highlight'><td>正文（問題探討、資料分析、視覺化、引用彙整）</td><td style='text-align:center;'>40</td></tr>
          <tr><td>結論（看法、未來研究方向）</td><td style='text-align:center;'>15</td></tr>
          <tr class='tr-highlight'><td>參考資料</td><td style='text-align:center;'>5</td></tr>
          <tr><td colspan='2' style='background:#ede9fe;font-weight:700;color:#6b21a8;'>🎤 口頭發表 10 分</td></tr>
          <tr><td>上台 3 分鐘（老師評分，參考同學互評）</td><td style='text-align:center;'>10</td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <div style='background:#fef3c7;border-left:4px solid #f59e0b;padding:8px 12px;border-radius:8px;font-size:.8rem;color:#78350f;'>
    🎤 <strong>3 分鐘怎麼講</strong>：我研究什麼（30 秒）→ 用了什麼資料（30 秒）→ 最重要的圖表告訴我們什麼（1 分半）→ 我的結論（30 秒）。
  </div>
</div>"""
    },
    {
        'id': 27,
        'chapter': '期末展示',
        'title': '感謝與祝福',
        'bg': 'navy',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<div style='text-align:center;padding:20px;'>
  <div style='font-size:72px;margin-bottom:20px;'>🎓</div>
  <h1 style='font-size:2.5rem;font-weight:900;color:#fff;margin-bottom:12px;'>恭喜完成十週課程！</h1>
  <h2 style='font-size:1.3rem;font-weight:400;color:#93c5fd;margin-bottom:30px;'>城市科技 — 數位公民素養</h2>
  <div style='display:grid;grid-template-columns:1fr 1fr 1fr;gap:15px;margin-bottom:25px;max-width:600px;margin-left:auto;margin-right:auto;'>
    <div style='background:rgba(255,255,255,0.12);padding:14px;border-radius:10px;'>
      <div style='font-size:2rem;margin-bottom:6px;'>🔒</div>
      <p style='color:#93c5fd;font-size:0.85rem;font-weight:700;margin:0;'>你能保護自己的數位安全</p>
    </div>
    <div style='background:rgba(255,255,255,0.12);padding:14px;border-radius:10px;'>
      <div style='font-size:2rem;margin-bottom:6px;'>📊</div>
      <p style='color:#93c5fd;font-size:0.85rem;font-weight:700;margin:0;'>你能用資料說故事</p>
    </div>
    <div style='background:rgba(255,255,255,0.12);padding:14px;border-radius:10px;'>
      <div style='font-size:2rem;margin-bottom:6px;'>🤖</div>
      <p style='color:#93c5fd;font-size:0.85rem;font-weight:700;margin:0;'>你能善用 AI 工具</p>
    </div>
  </div>
  <div style='background:rgba(255,255,255,0.1);padding:18px;border-radius:12px;margin-bottom:20px;'>
    <p style='color:#e2e8f0;font-size:1.1rem;font-style:italic;margin:0;'>"科技是工具，人才是目的。<br>願你用數位力量，為自己和社會創造更好的未來。"</p>
  </div>
  <div style='display:flex;justify-content:center;gap:12px;flex-wrap:wrap;'>
    <span style='background:rgba(255,255,255,0.15);color:#e0f2fe;padding:6px 18px;border-radius:20px;font-size:0.9rem;'>感謝大家的努力 🙏</span>
    <span style='background:rgba(255,255,255,0.15);color:#e0f2fe;padding:6px 18px;border-radius:20px;font-size:0.9rem;'>下學期見 👋</span>
  </div>
</div>"""
    }
]
