# -*- coding: utf-8 -*-
# Week 10: Power BI 與期末總結

CHAPTERS = [
    {'name': '封面', 'start': 1},
    {'name': '第一章：認識 Power BI', 'start': 2},
    {'name': '第二章：資料匯入與整理', 'start': 8},
    {'name': '第三章：視覺化設計', 'start': 14},
    {'name': '第四章：課程總回顧', 'start': 19},
    {'name': '期末展示', 'start': 23},
]

QUIZZES = {
    'q1': {
        'title': '第一章 隨堂測驗',
        'questions': [
            {
                'q': 'Power BI 與 Excel 圖表最主要的差異是什麼？',
                'options': ['Excel 圖表比 Power BI 能處理更大量的資料', 'Power BI 可製作互動式儀表板並輕鬆分享，Excel 圖表較靜態', 'Power BI 是付費工具，Excel 完全免費', 'Power BI 只能處理 Microsoft 的資料，Excel 可連接任何來源'],
                'answer': 1,
                'explain': 'Power BI 的核心優勢是「互動式儀表板」——使用者可點擊圖表來互相篩選，且可發布至網路讓任何人瀏覽，適合定期更新的報表。'
            },
            {
                'q': 'Power BI Desktop 是什麼？',
                'options': ['付費的雲端訂閱服務', 'Microsoft 365 的一個線上功能', '只能在手機上使用的 APP', '免費的桌面應用程式，用於製作報表和儀表板'],
                'answer': 3,
                'explain': 'Power BI Desktop 是完全免費的 Windows 桌面軟體，可從 Microsoft 官網下載。Power BI Service（雲端發布）才需要付費授權。'
            },
        ]
    },
    'q2': {
        'title': '第二章 隨堂測驗',
        'questions': [
            {
                'q': 'Power BI 的 Power Query 主要用途是什麼？',
                'options': ['設計互動式儀表板的視覺效果', '計算 DAX 量值（如加總、平均）', '匯入並清理/轉換資料，無需手動修改原始檔案', '將完成的報表發布到雲端'],
                'answer': 2,
                'explain': 'Power Query 是 Power BI 的「ETL 工具」（Extract, Transform, Load），可設定資料清理步驟（刪除空白列、合併欄位等），每次重新整理時自動執行。'
            },
            {
                'q': '在 Power BI 中，不同資料表之間建立「關聯性」的目的是什麼？',
                'options': ['讓來自不同資料表的欄位可以一起分析', '加快報表的載入速度', '將兩張表格合併成一張', '自動清理資料中的錯誤'],
                'answer': 0,
                'explain': '就像資料庫的 JOIN：「學生資料表」和「成績資料表」透過「學號」建立關聯，就能在圖表中同時使用兩表的欄位（如用姓名篩選各科成績）。'
            },
        ]
    },
    'q3': {
        'title': '第三章 隨堂測驗',
        'questions': [
            {
                'q': 'Power BI 儀表板中，點擊長條圖的某一長條後，頁面上其他圖表會有什麼反應？',
                'options': ['其他圖表自動篩選顯示對應資料（交叉篩選效果）', '其他圖表被隱藏', '頁面跳轉到另一個報表頁', '長條圖數值自動計算更新'],
                'answer': 0,
                'explain': 'Power BI 的「交叉篩選（Cross-filtering）」是最強大的互動功能：點擊任一圖表的資料點，頁面上所有圖表自動反映篩選結果，讓分析者能快速探索資料。'
            },
            {
                'q': '下列哪種 Power BI 視覺效果最適合展示「台灣各縣市的 YouBike 站點數量分布」？',
                'options': ['折線圖', '矩陣（交叉分析表）', '地圖視覺效果（ArcGIS Maps）', '量測計（Gauge）'],
                'answer': 2,
                'explain': 'Power BI 支援各種地圖視覺效果，可自動辨識地名（台北市、高雄市）並在地圖上標示對應數值，非常適合展示地理分布資料。'
            },
        ]
    },
    'q4': {
        'title': '第四章 隨堂測驗',
        'questions': [
            {
                'q': '十週課程中，「個人資料保護法」主要在哪一週學習？',
                'options': ['第一週：科技演進與硬體', '第六週：網際網路運作原理', '第十週：Power BI 與期末總結', '第三週：個人資料保護與資訊倫理'],
                'answer': 3,
                'explain': '第三週「個人資料保護與資訊倫理」深入探討台灣個資法、Cookie、隱私權、被遺忘權等議題，與 Week 5 表單設計中的個資告知聲明互相呼應。'
            },
            {
                'q': '學習完這十週課程，下列哪個能力「不屬於」你應該具備的資訊素養？',
                'options': ['能辨識資訊安全威脅（如釣魚郵件）', '能自己製造半導體晶片', '能使用 Excel 進行基本資料分析', '能理解 AI 生成內容的著作權問題'],
                'answer': 1,
                'explain': '製造半導體晶片需要高度專業的工程知識，不在本課程範圍。本課程著重「數位公民素養」：安全意識、資料分析、工具應用、法律常識。'
            },
        ]
    },
}

SLIDES = [
    {
        'id': 1,
        'chapter': '封面',
        'title': 'Power BI 與期末總結',
        'bg': 'navy',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<div style='text-align:center;padding:30px 20px;'>
  <div style='font-size:72px;margin-bottom:20px;'>🏆</div>
  <h1 style='font-size:2.8rem;font-weight:900;color:#fff;margin-bottom:12px;'>Power BI 與期末總結</h1>
  <h2 style='font-size:1.5rem;font-weight:400;color:#93c5fd;margin-bottom:30px;'>Power BI &amp; Course Finale</h2>
  <div style='display:flex;justify-content:center;gap:20px;flex-wrap:wrap;margin-bottom:30px;'>
    <span style='background:rgba(255,255,255,0.15);color:#e0f2fe;padding:8px 20px;border-radius:20px;font-size:1rem;'>📊 Power BI</span>
    <span style='background:rgba(255,255,255,0.15);color:#e0f2fe;padding:8px 20px;border-radius:20px;font-size:1rem;'>🎨 儀表板設計</span>
    <span style='background:rgba(255,255,255,0.15);color:#e0f2fe;padding:8px 20px;border-radius:20px;font-size:1rem;'>📚 十週回顧</span>
    <span style='background:rgba(255,255,255,0.15);color:#e0f2fe;padding:8px 20px;border-radius:20px;font-size:1rem;'>🎓 期末展示</span>
  </div>
  <p style='color:#bfdbfe;font-size:1.1rem;'>城市科技 — 第十週（期末）</p>
</div>"""
    },
    {
        'id': 2,
        'chapter': '第一章：認識 Power BI',
        'title': '什麼是 Power BI？',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>什麼是 Power BI？</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;border-left:4px solid #2563eb;padding:15px;border-radius:8px;margin-bottom:15px;'>
      <h3 style='color:#1e40af;font-size:1.1rem;margin-bottom:8px;'>📌 定義</h3>
      <p style='color:#374151;font-size:0.95rem;'>Power BI 是 Microsoft 推出的<strong>商業智慧（Business Intelligence）</strong>工具，可將資料轉化為互動式視覺化報表和儀表板。</p>
    </div>
    <div style='background:#f0fdf4;padding:12px;border-radius:8px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:8px;'>🆓 Power BI Desktop</h3>
      <p style='color:#374151;font-size:0.9rem;margin-bottom:6px;'>完全免費的桌面軟體：</p>
      <ul style='color:#374151;font-size:0.85rem;padding-left:16px;margin:0;'>
        <li>Windows 免費下載</li>
        <li>可連接 100+ 種資料來源</li>
        <li>拖放建立圖表，不需寫程式</li>
        <li>匯出 PDF 或分享給他人</li>
      </ul>
    </div>
  </div>
  <div>
    <div style='background:#fdf4ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#7c3aed;font-size:1rem;margin-bottom:10px;'>📊 Excel vs Power BI</h3>
      <table style='width:100%;border-collapse:collapse;font-size:0.85rem;'>
        <tr style='background:#7c3aed;color:#fff;'>
          <th style='padding:6px;'>功能</th><th style='padding:6px;'>Excel</th><th style='padding:6px;'>Power BI</th>
        </tr>
        <tr><td style='padding:6px;color:#374151;'>資料分析</td><td style='padding:6px;text-align:center;color:#374151;'>✅</td><td style='padding:6px;text-align:center;color:#374151;'>✅✅</td></tr>
        <tr style='background:#f9fafb;'><td style='padding:6px;color:#374151;'>互動儀表板</td><td style='padding:6px;text-align:center;color:#dc2626;'>❌</td><td style='padding:6px;text-align:center;color:#16a34a;font-weight:700;'>✅</td></tr>
        <tr><td style='padding:6px;color:#374151;'>雲端分享</td><td style='padding:6px;text-align:center;color:#374151;'>有限</td><td style='padding:6px;text-align:center;color:#16a34a;font-weight:700;'>✅</td></tr>
        <tr style='background:#f9fafb;'><td style='padding:6px;color:#374151;'>資料量</td><td style='padding:6px;text-align:center;color:#374151;'>有限</td><td style='padding:6px;text-align:center;color:#16a34a;font-weight:700;'>大量</td></tr>
        <tr><td style='padding:6px;color:#374151;'>學習曲線</td><td style='padding:6px;text-align:center;color:#374151;'>較易</td><td style='padding:6px;text-align:center;color:#374151;'>較陡</td></tr>
      </table>
    </div>
  </div>
</div>"""
    },
    {
        'id': 3,
        'chapter': '第一章：認識 Power BI',
        'title': 'Power BI 三大組件',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>Power BI 三大組件</h2>
<div style='display:grid;grid-template-columns:1fr 1fr 1fr;gap:15px;margin-bottom:15px;'>
  <div style='background:#eff6ff;padding:18px;border-radius:12px;text-align:center;border:2px solid #2563eb;'>
    <div style='font-size:2.5rem;margin-bottom:10px;'>💻</div>
    <h3 style='color:#1e40af;font-size:1.1rem;margin-bottom:8px;'>Power BI Desktop</h3>
    <p style='color:#374151;font-size:0.85rem;'>製作報表的工具<br>免費下載<br>Windows 版</p>
    <div style='background:#dbeafe;padding:6px;border-radius:4px;margin-top:8px;'>
      <p style='color:#1e40af;font-size:0.8rem;margin:0;font-weight:700;'>🆓 完全免費</p>
    </div>
  </div>
  <div style='background:#f0fdf4;padding:18px;border-radius:12px;text-align:center;border:2px solid #16a34a;'>
    <div style='font-size:2.5rem;margin-bottom:10px;'>☁️</div>
    <h3 style='color:#15803d;font-size:1.1rem;margin-bottom:8px;'>Power BI Service</h3>
    <p style='color:#374151;font-size:0.85rem;'>雲端發布與分享<br>設定自動重新整理<br>行動版 APP</p>
    <div style='background:#dcfce7;padding:6px;border-radius:4px;margin-top:8px;'>
      <p style='color:#15803d;font-size:0.8rem;margin:0;font-weight:700;'>💰 需要授權</p>
    </div>
  </div>
  <div style='background:#fdf4ff;padding:18px;border-radius:12px;text-align:center;border:2px solid #7c3aed;'>
    <div style='font-size:2.5rem;margin-bottom:10px;'>📱</div>
    <h3 style='color:#7c3aed;font-size:1.1rem;margin-bottom:8px;'>Power BI Mobile</h3>
    <p style='color:#374151;font-size:0.85rem;'>手機/平板瀏覽報表<br>iOS & Android<br>隨時掌握數據</p>
    <div style='background:#e9d5ff;padding:6px;border-radius:4px;margin-top:8px;'>
      <p style='color:#7c3aed;font-size:0.8rem;margin:0;font-weight:700;'>🆓 免費下載</p>
    </div>
  </div>
</div>
<div style='background:#fff7ed;padding:12px;border-radius:8px;border:1px solid #fdba74;'>
  <p style='color:#9a3412;font-size:0.9rem;margin:0;'>🏫 <strong>學生如何免費使用</strong>：使用學校 Microsoft 365 帳號（*.edu.tw）可免費存取 Power BI Service。教育版授權包含 Power BI Pro。</p>
</div>"""
    },
    {
        'id': 4,
        'chapter': '第一章：認識 Power BI',
        'title': 'Power BI 台灣企業應用',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>Power BI 台灣企業應用案例</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div style='display:flex;flex-direction:column;gap:12px;'>
    <div style='background:#eff6ff;padding:14px;border-radius:10px;border-left:4px solid #2563eb;'>
      <h3 style='color:#1e40af;font-size:0.95rem;margin-bottom:6px;'>🏭 台達電子</h3>
      <p style='color:#374151;font-size:0.85rem;margin:0;'>導入 Power BI 建立「即時工廠儀表板」，生產主管在手機上隨時查看各產線良率、產量、設備狀態，大幅加快決策速度。</p>
    </div>
    <div style='background:#f0fdf4;padding:14px;border-radius:10px;border-left:4px solid #16a34a;'>
      <h3 style='color:#15803d;font-size:0.95rem;margin-bottom:6px;'>🏦 富邦金控</h3>
      <p style='color:#374151;font-size:0.85rem;margin:0;'>財務部門用 Power BI 整合各子公司數據，原本需多日人工彙整的財務報表變成即時更新，節省大量人力。</p>
    </div>
  </div>
  <div style='display:flex;flex-direction:column;gap:12px;'>
    <div style='background:#fff7ed;padding:14px;border-radius:10px;border-left:4px solid #ea580c;'>
      <h3 style='color:#ea580c;font-size:0.95rem;margin-bottom:6px;'>🏢 台北市政府</h3>
      <p style='color:#374151;font-size:0.85rem;margin:0;'>「市長室即時儀表板」整合市政指標（垃圾清運率、道路坑洞修復、建管審核時間），市長每天用 Power BI 監控市政績效。</p>
    </div>
    <div style='background:#fdf4ff;padding:14px;border-radius:10px;border-left:4px solid #7c3aed;'>
      <h3 style='color:#7c3aed;font-size:0.95rem;margin-bottom:6px;'>🛒 PChome 網購</h3>
      <p style='color:#374151;font-size:0.85rem;margin:0;'>商品部門用 Power BI 分析銷售趨勢，快速找出滯銷商品、熱門品類，即時調整促銷與備貨策略，改善庫存管理。</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 5,
        'chapter': '第一章：認識 Power BI',
        'title': 'DAX — Power BI 計算語言',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>DAX — Power BI 的計算引擎</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:8px;'>📐 什麼是 DAX？</h3>
      <p style='color:#374151;font-size:0.9rem;margin-bottom:8px;'>DAX（Data Analysis Expressions）是 Power BI 用來建立計算欄位和量值的公式語言，語法類似 Excel 函數。</p>
      <div style='background:#dbeafe;padding:8px;border-radius:6px;'>
        <p style='color:#374151;font-size:0.85rem;margin:0;'>🤔 類比：DAX 是 Power BI 的「Excel 公式」</p>
      </div>
    </div>
    <div style='background:#f0fdf4;padding:12px;border-radius:8px;'>
      <h3 style='color:#15803d;font-size:0.95rem;margin-bottom:8px;'>✨ 常用 DAX 範例</h3>
      <div style='display:flex;flex-direction:column;gap:6px;'>
        <div style='background:#fff;padding:8px;border-radius:6px;font-family:monospace;font-size:0.8rem;'>
          <p style='color:#15803d;margin:0;'>及格人數 = COUNTIF(成績表[成績],">=60")</p>
        </div>
        <div style='background:#fff;padding:8px;border-radius:6px;font-family:monospace;font-size:0.8rem;'>
          <p style='color:#15803d;margin:0;'>平均成績 = AVERAGE(成績表[成績])</p>
        </div>
        <div style='background:#fff;padding:8px;border-radius:6px;font-family:monospace;font-size:0.8rem;'>
          <p style='color:#15803d;margin:0;'>及格率 = DIVIDE([及格人數],[總人數])</p>
        </div>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#fdf4ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#7c3aed;font-size:1rem;margin-bottom:10px;'>🔢 量值 vs 計算欄位</h3>
      <table style='width:100%;border-collapse:collapse;font-size:0.85rem;'>
        <tr style='background:#7c3aed;color:#fff;'>
          <th style='padding:6px;'>類型</th><th style='padding:6px;'>說明</th>
        </tr>
        <tr><td style='padding:6px;color:#374151;font-weight:700;'>計算欄位</td><td style='padding:6px;color:#374151;'>對每一列計算，儲存在資料表中</td></tr>
        <tr style='background:#f9fafb;'><td style='padding:6px;color:#374151;font-weight:700;'>量值（Measure）</td><td style='padding:6px;color:#374151;'>動態計算，根據篩選條件自動調整</td></tr>
      </table>
    </div>
    <div style='background:#fff7ed;padding:10px;border-radius:8px;'>
      <p style='color:#9a3412;font-size:0.85rem;margin:0;'>💡 入門時先用 Power BI 內建功能（加總、平均、計數），DAX 是進階技能，不需要一開始就學。</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 6,
        'chapter': '第一章：認識 Power BI',
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
        <li><strong>顏色一致</strong>：品牌色或主題色</li>
        <li><strong>互動篩選</strong>：讓使用者自行探索</li>
        <li><strong>行動友善</strong>：手機也能看清楚</li>
      </ul>
    </div>
  </div>
  <div>
    <div style='background:#fef9c3;padding:15px;border-radius:10px;margin-bottom:12px;border:1px solid #fde047;'>
      <h3 style='color:#854d0e;font-size:1rem;margin-bottom:10px;'>🎨 版面配置範例</h3>
      <div style='background:#fff;padding:10px;border-radius:8px;'>
        <div style='display:grid;grid-template-columns:1fr 1fr 1fr;gap:4px;margin-bottom:4px;'>
          <div style='background:#dbeafe;padding:8px;border-radius:4px;text-align:center;font-size:0.7rem;color:#1e40af;font-weight:700;'>KPI<br>總銷售額</div>
          <div style='background:#dcfce7;padding:8px;border-radius:4px;text-align:center;font-size:0.7rem;color:#15803d;font-weight:700;'>KPI<br>客戶數</div>
          <div style='background:#fef9c3;padding:8px;border-radius:4px;text-align:center;font-size:0.7rem;color:#854d0e;font-weight:700;'>KPI<br>利潤率</div>
        </div>
        <div style='display:grid;grid-template-columns:2fr 1fr;gap:4px;'>
          <div style='background:#f1f5f9;padding:8px;border-radius:4px;text-align:center;font-size:0.7rem;color:#374151;'>月銷售趨勢（折線圖）</div>
          <div style='background:#f1f5f9;padding:8px;border-radius:4px;text-align:center;font-size:0.7rem;color:#374151;'>地區分布（地圖）</div>
        </div>
      </div>
      <p style='color:#854d0e;font-size:0.8rem;margin-top:8px;'>重要指標在上，詳細圖表在下</p>
    </div>
    <div style='background:#fef2f2;padding:10px;border-radius:8px;'>
      <p style='color:#dc2626;font-size:0.85rem;margin:0;'>❌ <strong>常見錯誤</strong>：使用 12 種以上顏色、一頁放 8 個圖表、圖表沒有標題、字體太小手機看不清楚。</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 7,
        'chapter': '第一章：認識 Power BI',
        'title': '🎯 第一章 隨堂測驗',
        'bg': 'purple',
        'quiz': 'q1',
        'chart': None,
        'video': None,
        'html': """
<div style='text-align:center;padding:20px;'>
  <div style='font-size:56px;margin-bottom:15px;'>🎯</div>
  <h2 style='color:#fff;font-size:2rem;font-weight:800;margin-bottom:10px;'>第一章 隨堂測驗</h2>
  <p style='color:#e9d5ff;font-size:1.1rem;'>認識 Power BI ── 2 道題目，點擊作答！</p>
</div>"""
    },
    {
        'id': 8,
        'chapter': '第二章：資料匯入與整理',
        'title': 'Power Query 資料清理',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>Power Query 資料清理</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>🔧 Power Query 功能</h3>
      <p style='color:#374151;font-size:0.9rem;margin-bottom:8px;'>連接資料來源後，進入 Power Query 編輯器進行清理：</p>
      <div style='display:flex;flex-direction:column;gap:6px;'>
        <div style='background:#fff;padding:8px;border-radius:6px;border-left:3px solid #2563eb;'>
          <p style='color:#374151;font-size:0.85rem;margin:0;'>✅ 移除重複列</p>
        </div>
        <div style='background:#fff;padding:8px;border-radius:6px;border-left:3px solid #2563eb;'>
          <p style='color:#374151;font-size:0.85rem;margin:0;'>✅ 取代/填入缺失值</p>
        </div>
        <div style='background:#fff;padding:8px;border-radius:6px;border-left:3px solid #2563eb;'>
          <p style='color:#374151;font-size:0.85rem;margin:0;'>✅ 分割欄位（姓名+電話→各自欄）</p>
        </div>
        <div style='background:#fff;padding:8px;border-radius:6px;border-left:3px solid #2563eb;'>
          <p style='color:#374151;font-size:0.85rem;margin:0;'>✅ 自訂欄位（計算欄）</p>
        </div>
        <div style='background:#fff;padding:8px;border-radius:6px;border-left:3px solid #2563eb;'>
          <p style='color:#374151;font-size:0.85rem;margin:0;'>✅ 合併多個資料表</p>
        </div>
        <div style='background:#fff;padding:8px;border-radius:6px;border-left:3px solid #2563eb;'>
          <p style='color:#374151;font-size:0.85rem;margin:0;'>✅ 資料類型轉換（文字→數值→日期）</p>
        </div>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:8px;'>⭐ 最大優勢：步驟自動記錄</h3>
      <p style='color:#374151;font-size:0.9rem;margin-bottom:8px;'>Power Query 會自動記錄每個清理步驟，下次匯入新資料時，<strong>自動套用相同步驟</strong>！</p>
      <div style='background:#dcfce7;padding:8px;border-radius:6px;'>
        <p style='color:#15803d;font-size:0.85rem;margin:0;'>例：每月新增銷售資料 → 按「重新整理」→ 所有清理自動完成，圖表自動更新！</p>
      </div>
    </div>
    <div style='background:#fff7ed;padding:10px;border-radius:8px;'>
      <p style='color:#9a3412;font-size:0.85rem;margin:0;'>💡 Power Query 也內建在 Excel 中（資料→從其他來源），不只是 Power BI 專屬功能！</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 9,
        'chapter': '第二章：資料匯入與整理',
        'title': '連接多種資料來源',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': {'url': 'https://www.youtube.com/embed/TmhQCQr_y2A', 'title': 'Power BI 入門教學', 'desc': '10 分鐘學會建立第一個 Power BI 報表'},
        'html': """
<h2 class='slide-title'>連接多種資料來源</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <h3 style='color:#374151;font-size:1rem;margin-bottom:12px;'>🔌 Power BI 支援的資料來源</h3>
    <div style='display:grid;grid-template-columns:1fr 1fr;gap:8px;'>
      <div style='background:#eff6ff;padding:10px;border-radius:8px;text-align:center;'>
        <div>📊</div>
        <p style='color:#1e40af;font-size:0.8rem;font-weight:700;margin:4px 0 0;'>Excel / CSV</p>
      </div>
      <div style='background:#f0fdf4;padding:10px;border-radius:8px;text-align:center;'>
        <div>🗄️</div>
        <p style='color:#15803d;font-size:0.8rem;font-weight:700;margin:4px 0 0;'>SQL 資料庫</p>
      </div>
      <div style='background:#fdf4ff;padding:10px;border-radius:8px;text-align:center;'>
        <div>☁️</div>
        <p style='color:#7c3aed;font-size:0.8rem;font-weight:700;margin:4px 0 0;'>SharePoint</p>
      </div>
      <div style='background:#fff7ed;padding:10px;border-radius:8px;text-align:center;'>
        <div>🌐</div>
        <p style='color:#ea580c;font-size:0.8rem;font-weight:700;margin:4px 0 0;'>Web 網頁</p>
      </div>
      <div style='background:#fef9c3;padding:10px;border-radius:8px;text-align:center;'>
        <div>📡</div>
        <p style='color:#854d0e;font-size:0.8rem;font-weight:700;margin:4px 0 0;'>REST API</p>
      </div>
      <div style='background:#fef2f2;padding:10px;border-radius:8px;text-align:center;'>
        <div>📋</div>
        <p style='color:#dc2626;font-size:0.8rem;font-weight:700;margin:4px 0 0;'>Google Sheets</p>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#f9fafb;padding:15px;border-radius:10px;margin-bottom:12px;border:1px solid #e5e7eb;'>
      <h3 style='color:#374151;font-size:1rem;margin-bottom:10px;'>🔗 資料模型（關聯性）</h3>
      <p style='color:#374151;font-size:0.9rem;margin-bottom:8px;'>多張資料表可以透過共同欄位建立關聯，就像資料庫的外鍵：</p>
      <div style='background:#fff;padding:10px;border-radius:6px;text-align:center;font-size:0.85rem;'>
        <div style='display:flex;justify-content:center;align-items:center;gap:12px;'>
          <div style='background:#dbeafe;padding:8px;border-radius:6px;'>
            <p style='color:#1e40af;font-weight:700;margin:0;'>學生資料表</p>
            <p style='color:#374151;font-size:0.75rem;margin:2px 0 0;'>學號、姓名、班級</p>
          </div>
          <div style='color:#7c3aed;font-size:1.3rem;'>⟷</div>
          <div style='background:#dcfce7;padding:8px;border-radius:6px;'>
            <p style='color:#15803d;font-weight:700;margin:0;'>成績資料表</p>
            <p style='color:#374151;font-size:0.75rem;margin:2px 0 0;'>學號、科目、分數</p>
          </div>
        </div>
        <p style='color:#6b7280;font-size:0.75rem;margin-top:8px;'>透過「學號」連結，可同時使用兩表欄位</p>
      </div>
    </div>
  </div>
</div>"""
    },
    {
        'id': 10,
        'chapter': '第二章：資料匯入與整理',
        'title': '從開放資料到 Power BI',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>從開放資料到 Power BI 儀表板</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>🔄 完整流程</h3>
      <div style='display:flex;flex-direction:column;gap:6px;'>
        <div style='background:#dbeafe;padding:8px;border-radius:6px;display:flex;align-items:center;gap:8px;'>
          <span style='background:#1e40af;color:#fff;padding:2px 8px;border-radius:4px;font-size:0.8rem;'>1</span>
          <span style='color:#374151;font-size:0.85rem;'>data.gov.tw 下載 CSV 資料</span>
        </div>
        <div style='background:#dbeafe;padding:8px;border-radius:6px;display:flex;align-items:center;gap:8px;'>
          <span style='background:#1e40af;color:#fff;padding:2px 8px;border-radius:4px;font-size:0.8rem;'>2</span>
          <span style='color:#374151;font-size:0.85rem;'>Power BI Desktop → 取得資料 → CSV</span>
        </div>
        <div style='background:#dbeafe;padding:8px;border-radius:6px;display:flex;align-items:center;gap:8px;'>
          <span style='background:#1e40af;color:#fff;padding:2px 8px;border-radius:4px;font-size:0.8rem;'>3</span>
          <span style='color:#374151;font-size:0.85rem;'>Power Query 清理資料</span>
        </div>
        <div style='background:#dbeafe;padding:8px;border-radius:6px;display:flex;align-items:center;gap:8px;'>
          <span style='background:#1e40af;color:#fff;padding:2px 8px;border-radius:4px;font-size:0.8rem;'>4</span>
          <span style='color:#374151;font-size:0.85rem;'>拖放建立視覺化圖表</span>
        </div>
        <div style='background:#dcfce7;padding:8px;border-radius:6px;display:flex;align-items:center;gap:8px;'>
          <span style='background:#15803d;color:#fff;padding:2px 8px;border-radius:4px;font-size:0.8rem;'>5</span>
          <span style='color:#374151;font-size:0.85rem;'>發布或匯出 PDF 分享</span>
        </div>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:10px;'>📊 範例：YouBike 分析儀表板</h3>
      <ul style='color:#374151;font-size:0.85rem;padding-left:16px;'>
        <li>資料來源：台北市開放資料 YouBike 站點</li>
        <li>地圖：各站點位置與使用量</li>
        <li>折線圖：各時段租借次數</li>
        <li>長條圖：各行政區站點數比較</li>
        <li>篩選器：可選擇行政區</li>
      </ul>
    </div>
    <div style='background:#fff7ed;padding:10px;border-radius:8px;'>
      <p style='color:#9a3412;font-size:0.85rem;margin:0;'>🎓 期末實作：各組選擇一個 data.gov.tw 資料集，製作至少包含 3 個視覺效果的 Power BI 儀表板。</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 11,
        'chapter': '第二章：資料匯入與整理',
        'title': '資料關聯與模型設計',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>資料模型設計</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>🌟 星型架構（Star Schema）</h3>
      <div style='background:#fff;padding:12px;border-radius:8px;text-align:center;'>
        <div style='background:#fde047;padding:6px 12px;border-radius:6px;display:inline-block;margin-bottom:8px;'>
          <p style='color:#854d0e;font-weight:700;font-size:0.85rem;margin:0;'>中央事實表（銷售記錄）</p>
        </div>
        <div style='display:flex;justify-content:center;gap:8px;flex-wrap:wrap;'>
          <div style='background:#dbeafe;padding:5px 10px;border-radius:4px;font-size:0.75rem;color:#1e40af;'>客戶維度表</div>
          <div style='background:#dcfce7;padding:5px 10px;border-radius:4px;font-size:0.75rem;color:#15803d;'>商品維度表</div>
          <div style='background:#fde047;padding:5px 10px;border-radius:4px;font-size:0.75rem;color:#854d0e;'>時間維度表</div>
          <div style='background:#fdf4ff;padding:5px 10px;border-radius:4px;font-size:0.75rem;color:#7c3aed;'>地區維度表</div>
        </div>
      </div>
      <p style='color:#374151;font-size:0.8rem;margin-top:8px;'>事實表放數值，維度表放描述資訊。這是商業智慧的標準架構。</p>
    </div>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:10px;'>🔗 關聯性類型</h3>
      <table style='width:100%;border-collapse:collapse;font-size:0.85rem;'>
        <tr style='background:#15803d;color:#fff;'>
          <th style='padding:6px;'>類型</th><th style='padding:6px;'>說明</th>
        </tr>
        <tr><td style='padding:6px;color:#374151;font-weight:700;'>一對多</td><td style='padding:6px;color:#374151;'>一個班級對應多個學生（最常見）</td></tr>
        <tr style='background:#f0fdf4;'><td style='padding:6px;color:#374151;font-weight:700;'>一對一</td><td style='padding:6px;color:#374151;'>每個員工對應一張薪資單</td></tr>
        <tr><td style='padding:6px;color:#374151;font-weight:700;'>多對多</td><td style='padding:6px;color:#374151;'>學生選多門課，課有多個學生</td></tr>
      </table>
    </div>
    <div style='background:#eff6ff;padding:10px;border-radius:8px;'>
      <p style='color:#1e40af;font-size:0.85rem;margin:0;'>💡 設計好的資料模型，之後分析時才能靈活組合不同表的資料，不會遇到 DAX 計算錯誤。</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 12,
        'chapter': '第二章：資料匯入與整理',
        'title': '🎯 第二章 隨堂測驗',
        'bg': 'purple',
        'quiz': 'q2',
        'chart': None,
        'video': None,
        'html': """
<div style='text-align:center;padding:20px;'>
  <div style='font-size:56px;margin-bottom:15px;'>🎯</div>
  <h2 style='color:#fff;font-size:2rem;font-weight:800;margin-bottom:10px;'>第二章 隨堂測驗</h2>
  <p style='color:#e9d5ff;font-size:1.1rem;'>資料匯入與整理 ── 2 道題目，點擊作答！</p>
</div>"""
    },
    {
        'id': 13,
        'chapter': '第三章：視覺化設計',
        'title': 'Power BI 視覺效果類型',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>Power BI 視覺效果</h2>
<div style='display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:15px;'>
  <div style='background:#eff6ff;padding:12px;border-radius:8px;text-align:center;'>
    <div style='font-size:1.8rem;'>📊</div>
    <p style='color:#1e40af;font-size:0.8rem;font-weight:700;margin:6px 0 2px;'>群組橫條圖</p>
    <p style='color:#6b7280;font-size:0.7rem;'>比較類別大小</p>
  </div>
  <div style='background:#f0fdf4;padding:12px;border-radius:8px;text-align:center;'>
    <div style='font-size:1.8rem;'>📈</div>
    <p style='color:#15803d;font-size:0.8rem;font-weight:700;margin:6px 0 2px;'>折線圖</p>
    <p style='color:#6b7280;font-size:0.7rem;'>時間趨勢</p>
  </div>
  <div style='background:#fdf4ff;padding:12px;border-radius:8px;text-align:center;'>
    <div style='font-size:1.8rem;'>🗺️</div>
    <p style='color:#7c3aed;font-size:0.8rem;font-weight:700;margin:6px 0 2px;'>地圖</p>
    <p style='color:#6b7280;font-size:0.7rem;'>地理分布</p>
  </div>
  <div style='background:#fff7ed;padding:12px;border-radius:8px;text-align:center;'>
    <div style='font-size:1.8rem;'>🧮</div>
    <p style='color:#ea580c;font-size:0.8rem;font-weight:700;margin:6px 0 2px;'>矩陣</p>
    <p style='color:#6b7280;font-size:0.7rem;'>交叉分析表</p>
  </div>
  <div style='background:#fef2f2;padding:12px;border-radius:8px;text-align:center;'>
    <div style='font-size:1.8rem;'>🎯</div>
    <p style='color:#dc2626;font-size:0.8rem;font-weight:700;margin:6px 0 2px;'>量測計</p>
    <p style='color:#6b7280;font-size:0.7rem;'>目標達成率</p>
  </div>
  <div style='background:#f0f9ff;padding:12px;border-radius:8px;text-align:center;'>
    <div style='font-size:1.8rem;'>🔷</div>
    <p style='color:#0369a1;font-size:0.8rem;font-weight:700;margin:6px 0 2px;'>散佈圖</p>
    <p style='color:#6b7280;font-size:0.7rem;'>相關分析</p>
  </div>
  <div style='background:#f0fdf4;padding:12px;border-radius:8px;text-align:center;'>
    <div style='font-size:1.8rem;'>🃏</div>
    <p style='color:#15803d;font-size:0.8rem;font-weight:700;margin:6px 0 2px;'>卡片</p>
    <p style='color:#6b7280;font-size:0.7rem;'>單一 KPI 值</p>
  </div>
  <div style='background:#fdf4ff;padding:12px;border-radius:8px;text-align:center;'>
    <div style='font-size:1.8rem;'>🌳</div>
    <p style='color:#7c3aed;font-size:0.8rem;font-weight:700;margin:6px 0 2px;'>樹狀圖</p>
    <p style='color:#6b7280;font-size:0.7rem;'>層級比例</p>
  </div>
</div>
<div style='background:#eff6ff;padding:10px;border-radius:8px;'>
  <p style='color:#1e40af;font-size:0.9rem;margin:0;'>💡 Power BI 還有 <strong>AppSource 市集</strong>，提供社群開發的自訂視覺效果（如 Sankey chart、字雲、甘特圖），免費下載使用！</p>
</div>"""
    },
    {
        'id': 14,
        'chapter': '第三章：視覺化設計',
        'title': '交叉篩選與互動效果',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>互動效果 — Power BI 的靈魂</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>🖱️ 互動效果類型</h3>
      <div style='display:flex;flex-direction:column;gap:8px;'>
        <div style='background:#fff;padding:10px;border-radius:6px;border-left:3px solid #2563eb;'>
          <p style='font-weight:700;color:#1e40af;font-size:0.85rem;margin:0;'>交叉篩選（Cross-filter）</p>
          <p style='color:#374151;font-size:0.8rem;margin:4px 0 0;'>點擊長條圖 A 班 → 所有圖表自動篩選顯示 A 班資料</p>
        </div>
        <div style='background:#fff;padding:10px;border-radius:6px;border-left:3px solid #16a34a;'>
          <p style='font-weight:700;color:#15803d;font-size:0.85rem;margin:0;'>交叉反白（Cross-highlight）</p>
          <p style='color:#374151;font-size:0.8rem;margin:4px 0 0;'>其他圖表保持完整但將 A 班資料反白突出</p>
        </div>
        <div style='background:#fff;padding:10px;border-radius:6px;border-left:3px solid #7c3aed;'>
          <p style='font-weight:700;color:#7c3aed;font-size:0.85rem;margin:0;'>向下鑽取（Drill down）</p>
          <p style='color:#374151;font-size:0.8rem;margin:4px 0 0;'>年度圖表 → 點擊 → 自動展開季度 → 月度</p>
        </div>
        <div style='background:#fff;padding:10px;border-radius:6px;border-left:3px solid #ea580c;'>
          <p style='font-weight:700;color:#ea580c;font-size:0.85rem;margin:0;'>切片器（Slicer）</p>
          <p style='color:#374151;font-size:0.8rem;margin:4px 0 0;'>視覺化篩選按鈕，點擊即篩選整頁</p>
        </div>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#fef9c3;padding:15px;border-radius:10px;margin-bottom:12px;border:1px solid #fde047;'>
      <h3 style='color:#854d0e;font-size:1rem;margin-bottom:10px;'>💡 為什麼互動很重要？</h3>
      <p style='color:#374151;font-size:0.9rem;margin-bottom:8px;'>靜態報表：看完就結束</p>
      <p style='color:#374151;font-size:0.9rem;margin-bottom:8px;'>互動儀表板：<strong>使用者主動探索資料</strong></p>
      <div style='background:#fff;padding:10px;border-radius:6px;'>
        <p style='color:#374151;font-size:0.85rem;margin:0;'>📖 場景：校長查看各班成績儀表板，點擊「B班」→ 所有圖表自動聚焦B班，找出哪科需要加強。完全不需要重新做圖表！</p>
      </div>
    </div>
    <div style='background:#eff6ff;padding:10px;border-radius:8px;'>
      <p style='color:#1e40af;font-size:0.85rem;margin:0;'>🔧 設定互動：選取視覺效果 → 格式 → 編輯互動，可自訂每個圖表互相影響的方式。</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 15,
        'chapter': '第三章：視覺化設計',
        'title': '儀表板主題與美化',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>儀表板主題與美化</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>🎨 套用主題</h3>
      <p style='color:#374151;font-size:0.9rem;margin-bottom:8px;'>檢視 → 主題 → 選擇內建主題（20+ 種），或匯入自訂 JSON 主題：</p>
      <div style='display:flex;flex-wrap:wrap;gap:6px;'>
        <span style='background:#1e40af;color:#fff;padding:4px 10px;border-radius:4px;font-size:0.8rem;'>經典</span>
        <span style='background:#dc2626;color:#fff;padding:4px 10px;border-radius:4px;font-size:0.8rem;'>高對比</span>
        <span style='background:#0d9488;color:#fff;padding:4px 10px;border-radius:4px;font-size:0.8rem;'>色盲友善</span>
        <span style='background:#7c3aed;color:#fff;padding:4px 10px;border-radius:4px;font-size:0.8rem;'>深色模式</span>
        <span style='background:#374151;color:#fff;padding:4px 10px;border-radius:4px;font-size:0.8rem;'>自訂</span>
      </div>
    </div>
    <div style='background:#f0fdf4;padding:12px;border-radius:8px;'>
      <h3 style='color:#15803d;font-size:0.95rem;margin-bottom:8px;'>✅ 美化技巧</h3>
      <ul style='color:#374151;font-size:0.85rem;padding-left:16px;margin:0;'>
        <li>加入公司/學校 Logo</li>
        <li>背景使用 PowerPoint 設計</li>
        <li>KPI 卡片數值放大顯著</li>
        <li>工具提示顯示詳細資訊</li>
      </ul>
    </div>
  </div>
  <div>
    <div style='background:#fdf4ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#7c3aed;font-size:1rem;margin-bottom:10px;'>📱 行動版報表</h3>
      <p style='color:#374151;font-size:0.9rem;margin-bottom:8px;'>Power BI Desktop → 檢視 → 手機版面配置：</p>
      <ul style='color:#374151;font-size:0.85rem;padding-left:16px;'>
        <li>專為直向手機設計的版面</li>
        <li>重要 KPI 放最上方</li>
        <li>圖表大小適合手指點擊</li>
      </ul>
    </div>
    <div style='background:#fff7ed;padding:10px;border-radius:8px;'>
      <p style='color:#9a3412;font-size:0.85rem;margin:0;'>🇹🇼 台灣公司實際案例：台達電子主管每天早上在手機上查看當日生產儀表板，<strong>不用打開電腦</strong>，通勤時即完成晨報。</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 16,
        'chapter': '第三章：視覺化設計',
        'title': '發布與分享報表',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>發布與分享報表</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>📤 分享方式</h3>
      <div style='display:flex;flex-direction:column;gap:8px;'>
        <div style='background:#fff;padding:8px;border-radius:6px;border-left:3px solid #2563eb;'>
          <p style='font-weight:700;color:#1e40af;font-size:0.85rem;margin:0;'>匯出 PDF</p>
          <p style='color:#374151;font-size:0.8rem;margin:2px 0 0;'>靜態版本，適合印刷或電子郵件</p>
        </div>
        <div style='background:#fff;padding:8px;border-radius:6px;border-left:3px solid #16a34a;'>
          <p style='font-weight:700;color:#15803d;font-size:0.85rem;margin:0;'>發布到 Power BI Service</p>
          <p style='color:#374151;font-size:0.8rem;margin:2px 0 0;'>雲端互動版，可設定定期自動重整</p>
        </div>
        <div style='background:#fff;padding:8px;border-radius:6px;border-left:3px solid #7c3aed;'>
          <p style='font-weight:700;color:#7c3aed;font-size:0.85rem;margin:0;'>嵌入至網站</p>
          <p style='color:#374151;font-size:0.8rem;margin:2px 0 0;'>用 iframe 嵌入其他網頁或 SharePoint</p>
        </div>
        <div style='background:#fff;padding:8px;border-radius:6px;border-left:3px solid #ea580c;'>
          <p style='font-weight:700;color:#ea580c;font-size:0.85rem;margin:0;'>Teams 整合</p>
          <p style='color:#374151;font-size:0.8rem;margin:2px 0 0;'>直接在 Teams 頻道顯示即時儀表板</p>
        </div>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:8px;'>🔐 權限管理</h3>
      <ul style='color:#374151;font-size:0.9rem;padding-left:16px;'>
        <li>可設定僅特定人員可查看</li>
        <li>「行級安全性（RLS）」：不同用戶看到不同資料（老師看全班，學生只看自己）</li>
        <li>設定資料重新整理排程（每日/每小時）</li>
      </ul>
    </div>
    <div style='background:#fff7ed;padding:10px;border-radius:8px;'>
      <p style='color:#9a3412;font-size:0.85rem;margin:0;'>⚠️ <strong>學生實作</strong>：本課程使用 Power BI Desktop 製作報表後，匯出 PDF 或截圖提交，無需 Power BI Service 帳號。</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 17,
        'chapter': '第三章：視覺化設計',
        'title': '🎯 第三章 隨堂測驗',
        'bg': 'purple',
        'quiz': 'q3',
        'chart': None,
        'video': None,
        'html': """
<div style='text-align:center;padding:20px;'>
  <div style='font-size:56px;margin-bottom:15px;'>🎯</div>
  <h2 style='color:#fff;font-size:2rem;font-weight:800;margin-bottom:10px;'>第三章 隨堂測驗</h2>
  <p style='color:#e9d5ff;font-size:1.1rem;'>視覺化設計 ── 2 道題目，點擊作答！</p>
</div>"""
    },
    {
        'id': 18,
        'chapter': '第四章：課程總回顧',
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
          <p style='font-weight:700;color:#3f6212;font-size:0.85rem;margin:0;'>資料分析實作</p>
          <p style='color:#374151;font-size:0.75rem;margin:0;'>Excel 函數/樞紐/趨勢線</p>
        </div>
      </div>
    </div>
    <div style='background:#1e40af;padding:10px;border-radius:8px;'>
      <div style='display:flex;align-items:center;gap:8px;'>
        <span style='background:#fff;color:#1e40af;padding:2px 10px;border-radius:4px;font-size:0.8rem;font-weight:700;'>W10</span>
        <div>
          <p style='font-weight:700;color:#fff;font-size:0.85rem;margin:0;'>Power BI 與期末總結 🎓</p>
          <p style='color:#bfdbfe;font-size:0.75rem;margin:0;'>儀表板設計/十週回顧/期末展示</p>
        </div>
      </div>
    </div>
  </div>
</div>"""
    },
    {
        'id': 19,
        'chapter': '第四章：課程總回顧',
        'title': '數位公民素養架構',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>數位公民素養架構</h2>
<div style='display:grid;grid-template-columns:1fr 1fr 1fr;gap:15px;margin-bottom:15px;'>
  <div style='background:#eff6ff;padding:15px;border-radius:10px;text-align:center;'>
    <div style='font-size:2.5rem;margin-bottom:8px;'>🛡️</div>
    <h3 style='color:#1e40af;font-size:1rem;margin-bottom:8px;'>數位安全</h3>
    <ul style='color:#374151;font-size:0.8rem;list-style:none;padding:0;text-align:left;'>
      <li>✅ 識別網路詐騙</li>
      <li>✅ 個資保護意識</li>
      <li>✅ 密碼安全管理</li>
      <li>✅ HTTPS 辨識</li>
    </ul>
  </div>
  <div style='background:#f0fdf4;padding:15px;border-radius:10px;text-align:center;'>
    <div style='font-size:2.5rem;margin-bottom:8px;'>⚖️</div>
    <h3 style='color:#15803d;font-size:1rem;margin-bottom:8px;'>數位倫理與法律</h3>
    <ul style='color:#374151;font-size:0.8rem;list-style:none;padding:0;text-align:left;'>
      <li>✅ 著作權基本知識</li>
      <li>✅ AI 生成內容倫理</li>
      <li>✅ 個資法要點</li>
      <li>✅ 數位隱私權</li>
    </ul>
  </div>
  <div style='background:#fdf4ff;padding:15px;border-radius:10px;text-align:center;'>
    <div style='font-size:2.5rem;margin-bottom:8px;'>🛠️</div>
    <h3 style='color:#7c3aed;font-size:1rem;margin-bottom:8px;'>數位工具能力</h3>
    <ul style='color:#374151;font-size:0.8rem;list-style:none;padding:0;text-align:left;'>
      <li>✅ Google Workspace</li>
      <li>✅ Excel 資料分析</li>
      <li>✅ Power BI 儀表板</li>
      <li>✅ AI 工具應用</li>
    </ul>
  </div>
</div>
<div style='background:#fef9c3;padding:12px;border-radius:8px;border:1px solid #fde047;'>
  <p style='color:#854d0e;font-size:0.9rem;margin:0;'>🌏 <strong>未來展望</strong>：數位技能已成為 21 世紀最基本的就業能力。根據麥肯錫報告，到 2030 年，台灣 50% 的工作需要中等以上的數位技能，本課程正是你邁向數位未來的第一步！</p>
</div>"""
    },
    {
        'id': 20,
        'chapter': '第四章：課程總回顧',
        'title': '科技與社會的連結',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>科技與社會的連結</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>🔗 各週主題如何相互連結</h3>
      <div style='display:flex;flex-direction:column;gap:8px;font-size:0.85rem;'>
        <div style='background:#fff;padding:8px;border-radius:6px;'>
          <p style='color:#374151;margin:0;'><strong style='color:#1e40af;'>硬體（W1）</strong> → 運算能力支撐 <strong style='color:#7c3aed;'>AI（W2）</strong></p>
        </div>
        <div style='background:#fff;padding:8px;border-radius:6px;'>
          <p style='color:#374151;margin:0;'><strong style='color:#dc2626;'>個資保護（W3）</strong> → 表單設計注意事項 <strong style='color:#ea580c;'>（W5）</strong></p>
        </div>
        <div style='background:#fff;padding:8px;border-radius:6px;'>
          <p style='color:#374151;margin:0;'><strong style='color:#0369a1;'>網路（W6）</strong> → 基礎讓 <strong style='color:#0d9488;'>IoT（W7）</strong> 得以運作</p>
        </div>
        <div style='background:#fff;padding:8px;border-radius:6px;'>
          <p style='color:#374151;margin:0;'><strong style='color:#ca8a04;'>資料清理（W8）</strong> → Excel 分析 <strong style='color:#65a30d;'>（W9）</strong> → Power BI <strong style='color:#1e40af;'>（W10）</strong></p>
        </div>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:10px;'>💭 學習後的反思問題</h3>
      <ul style='color:#374151;font-size:0.9rem;padding-left:16px;'>
        <li>我如何保護自己的個人資料？</li>
        <li>面對 AI 生成內容，我能辨別真偽嗎？</li>
        <li>我的手機每天蒐集哪些關於我的資料？</li>
        <li>數據分析如何幫助我做更好的決策？</li>
        <li>哪些科技讓台灣社會變得更好？</li>
      </ul>
    </div>
    <div style='background:#fef9c3;padding:10px;border-radius:8px;'>
      <p style='color:#854d0e;font-size:0.85rem;margin:0;'>🎓 <strong>學習不會在今天結束</strong>：科技日新月異，本課程教你的是「如何快速學習新工具」的能力，比任何特定軟體都更有價值。</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 21,
        'chapter': '第四章：課程總回顧',
        'title': 'AI 時代的學習策略',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>AI 時代的學習與就業策略</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>🤖 AI 取代了什麼？</h3>
      <div style='display:flex;flex-direction:column;gap:6px;'>
        <div style='background:#fee2e2;padding:8px;border-radius:6px;'>
          <p style='color:#dc2626;font-size:0.85rem;margin:0;'>❌ 簡單重複性工作（資料輸入、基礎報表）</p>
        </div>
        <div style='background:#fee2e2;padding:8px;border-radius:6px;'>
          <p style='color:#dc2626;font-size:0.85rem;margin:0;'>❌ 標準化文件生成</p>
        </div>
        <div style='background:#fee2e2;padding:8px;border-radius:6px;'>
          <p style='color:#dc2626;font-size:0.85rem;margin:0;'>❌ 基礎客服回覆</p>
        </div>
      </div>
    </div>
    <div style='background:#f0fdf4;padding:12px;border-radius:8px;'>
      <h3 style='color:#15803d;font-size:0.95rem;margin-bottom:8px;'>✅ AI 難以取代的能力</h3>
      <ul style='color:#374151;font-size:0.85rem;padding-left:16px;margin:0;'>
        <li>批判性思考（辨識 AI 錯誤）</li>
        <li>創意與情感連結</li>
        <li>複雜問題解決</li>
        <li>跨領域整合能力</li>
      </ul>
    </div>
  </div>
  <div>
    <div style='background:#fdf4ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#7c3aed;font-size:1rem;margin-bottom:10px;'>🎯 給同學的建議</h3>
      <ul style='color:#374151;font-size:0.9rem;padding-left:16px;'>
        <li><strong>學會與 AI 合作</strong>：善用 ChatGPT、Copilot 提升效率</li>
        <li><strong>培養資料敏感度</strong>：看到數據，習慣問「這合理嗎？」</li>
        <li><strong>T 型技能</strong>：廣泛知識 + 一個深度專業</li>
        <li><strong>持續學習</strong>：科技半衰期越來越短</li>
        <li><strong>解決問題</strong>：工具是手段，問題是目的</li>
      </ul>
    </div>
    <div style='background:#fff7ed;padding:10px;border-radius:8px;'>
      <p style='color:#9a3412;font-size:0.85rem;margin:0;'>🌟 <strong>2030 年最需要的技能（世界經濟論壇）</strong>：分析思維、創意與創新、科技設計與程式、批判思維、解決複雜問題。</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 22,
        'chapter': '第四章：課程總回顧',
        'title': '🎯 第四章 隨堂測驗',
        'bg': 'purple',
        'quiz': 'q4',
        'chart': None,
        'video': None,
        'html': """
<div style='text-align:center;padding:20px;'>
  <div style='font-size:56px;margin-bottom:15px;'>🎯</div>
  <h2 style='color:#fff;font-size:2rem;font-weight:800;margin-bottom:10px;'>第四章 隨堂測驗</h2>
  <p style='color:#e9d5ff;font-size:1.1rem;'>課程總回顧 ── 2 道題目，點擊作答！</p>
</div>"""
    },
    {
        'id': 23,
        'chapter': '期末展示',
        'title': '期末成果展示',
        'bg': 'teal',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 style='font-size:1.8rem;font-weight:800;color:#fff;margin-bottom:20px;text-align:center;'>🎓 期末成果展示</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div style='background:rgba(255,255,255,0.15);padding:18px;border-radius:12px;'>
    <h3 style='color:#fff;font-size:1rem;margin-bottom:14px;'>📋 期末專案要求</h3>
    <div style='display:flex;flex-direction:column;gap:10px;'>
      <div style='background:rgba(255,255,255,0.2);padding:12px;border-radius:8px;'>
        <p style='color:#fff;font-weight:700;font-size:0.9rem;margin:0 0 4px;'>主題：「我的城市數據故事」</p>
        <p style='color:#cffafe;font-size:0.8rem;margin:0;'>用開放資料分析你關心的台灣城市議題</p>
      </div>
      <div style='background:rgba(255,255,255,0.2);padding:12px;border-radius:8px;'>
        <p style='color:#fff;font-weight:700;font-size:0.9rem;margin:0 0 4px;'>必要內容</p>
        <ul style='color:#cffafe;font-size:0.8rem;margin:0;padding-left:16px;'>
          <li>資料來源（政府開放資料）</li>
          <li>資料清理說明（Excel / Google 試算表）</li>
          <li>至少 3 個視覺化圖表（Excel 或 Power BI）</li>
          <li>3 個資料洞見和你的解讀</li>
          <li>與所學課程主題的連結</li>
        </ul>
      </div>
      <div style='background:rgba(255,255,255,0.2);padding:10px;border-radius:8px;'>
        <p style='color:#fff;font-weight:700;font-size:0.9rem;margin:0 0 4px;'>選題建議（選一）</p>
        <ul style='color:#cffafe;font-size:0.8rem;margin:0;padding-left:16px;'>
          <li>各縣市空氣品質 AQI 趨勢</li>
          <li>台北市 YouBike 使用分析</li>
          <li>全台學校數量與學生人數變化</li>
          <li>各縣市人口與房價關係</li>
        </ul>
      </div>
    </div>
  </div>
  <div>
    <div style='background:rgba(255,255,255,0.15);padding:15px;border-radius:12px;margin-bottom:12px;'>
      <h3 style='color:#fff;font-size:1rem;margin-bottom:10px;'>🏆 評分標準（100 分）</h3>
      <table style='width:100%;border-collapse:collapse;font-size:0.85rem;'>
        <tr style='background:rgba(255,255,255,0.2);'>
          <th style='padding:8px;color:#fff;text-align:left;'>項目</th>
          <th style='padding:8px;color:#fff;text-align:center;'>分數</th>
        </tr>
        <tr style='background:rgba(255,255,255,0.1);'>
          <td style='padding:8px;color:#cffafe;'>資料蒐集與清理</td>
          <td style='padding:8px;text-align:center;color:#fff;font-weight:700;'>20</td>
        </tr>
        <tr>
          <td style='padding:8px;color:#cffafe;'>視覺化圖表（3張以上）</td>
          <td style='padding:8px;text-align:center;color:#fff;font-weight:700;'>30</td>
        </tr>
        <tr style='background:rgba(255,255,255,0.1);'>
          <td style='padding:8px;color:#cffafe;'>資料洞見分析</td>
          <td style='padding:8px;text-align:center;color:#fff;font-weight:700;'>30</td>
        </tr>
        <tr>
          <td style='padding:8px;color:#cffafe;'>課程主題連結</td>
          <td style='padding:8px;text-align:center;color:#fff;font-weight:700;'>10</td>
        </tr>
        <tr style='background:rgba(255,255,255,0.1);'>
          <td style='padding:8px;color:#cffafe;'>報告呈現清晰度</td>
          <td style='padding:8px;text-align:center;color:#fff;font-weight:700;'>10</td>
        </tr>
      </table>
    </div>
    <div style='background:rgba(255,255,255,0.15);padding:10px;border-radius:8px;'>
      <p style='color:#fff;font-size:0.85rem;margin:0;'>🗓️ <strong>繳交格式</strong>：Google 試算表連結 + Power BI PDF（或截圖），上傳至班級 Google Classroom</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 24,
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
