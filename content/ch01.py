# -*- coding: utf-8 -*-
# Ch.1: 科技演進與硬體

CHAPTERS = [
    {'name': '封面', 'start': 1},
    {'name': '第一章：科技的演進', 'start': 2},
    {'name': '第二章：電腦硬體組成', 'start': 8},
    {'name': '第三章：儲存裝置', 'start': 14},
    {'name': '第四章：數位生活中的硬體', 'start': 19},
    {'name': '分組實作', 'start': 23},
]

QUIZZES = {
    'q1': {
        'title': '第一章 隨堂測驗',
        'questions': [
            {
                'q': '下列哪一項科技發明最早出現？',
                'options': ['電腦（1939年）', '電燈（1879年）', '網際網路（1990年）', 'iPhone（2007年）'],
                'answer': 1,
                'explain': '愛迪生於 1879 年發明實用電燈泡。電腦約 1939 年出現，網際網路 1990 年代普及，iPhone 則是 2007 年問世。科技的演進需要幾十年的積累。'
            },
            {
                'q': '「摩爾定律」描述的是什麼現象？',
                'options': ['手機螢幕解析度每年提高一倍', '網路速度每三年增加十倍', '晶片上的電晶體數量每約兩年翻倍，效能提升而成本降低', '硬碟容量每五年增加一百倍'],
                'answer': 2,
                'explain': '英特爾創辦人 Gordon Moore 在 1965 年提出：積體電路上可容納的電晶體數目，每隔約 18-24 個月便會增加一倍。這個規律驅動了半個世紀的科技進步。'
            },
        ]
    },
    'q2': {
        'title': '第二章 隨堂測驗',
        'questions': [
            {
                'q': 'CPU（中央處理器）的主要功能是什麼？',
                'options': ['長期儲存資料，即使關機也不遺失', '顯示畫面，負責圖形輸出', '執行程式指令，是電腦的運算核心', '連接各元件，負責資料傳輸'],
                'answer': 2,
                'explain': 'CPU 是電腦的「大腦」，負責執行所有運算和程式指令。儲存是硬碟的功能，顯示是 GPU 和顯示器的功能，連接傳輸則是主機板和匯流排的工作。'
            },
            {
                'q': '電腦開機後，作業系統和程式會載入到哪裡執行？',
                'options': ['RAM（隨機存取記憶體）', 'SSD 固態硬碟', 'CPU 快取記憶體', 'GPU 顯示記憶體'],
                'answer': 0,
                'explain': 'RAM 是電腦的「工作桌」：速度極快但關機後資料消失（揮發性）。程式從硬碟讀取後載入 RAM 才能執行。RAM 越大，能同時運行的程式越多。'
            },
        ]
    },
    'q3': {
        'title': '第三章 隨堂測驗',
        'questions': [
            {
                'q': 'SSD（固態硬碟）相比 HDD（傳統硬碟）最主要的優點是？',
                'options': ['讀寫速度更快、無機械轉動部件、耐震', '容量更大、價格更便宜', '資料永久保存不會遺失', '溫度更高才能正常運作'],
                'answer': 0,
                'explain': 'SSD 使用快閃記憶體（Flash），沒有旋轉磁盤和讀寫頭，速度比 HDD 快 10-100 倍，且耐摔耐震。HDD 的優點在於相同價格下容量更大。'
            },
            {
                'q': '1 TB（Terabyte）等於多少 GB（Gigabyte）？',
                'options': ['100 GB', '10,000 GB', '512 GB', '1,024 GB'],
                'answer': 3,
                'explain': '儲存單位換算：1 TB = 1,024 GB = 1,024 × 1,024 MB ≈ 100 萬 MB。現在手機通常是 128GB–512GB，筆電硬碟常見 512GB–2TB。'
            },
        ]
    },
    'q4': {
        'title': '第四章 隨堂測驗',
        'questions': [
            {
                'q': '台灣在全球半導體產業中扮演什麼角色？',
                'options': ['全球最大半導體設計公司所在地', '半導體設備製造第一大國', '晶圓代工全球第一，台積電市佔超過 60%', '全球最大 DRAM 記憶體生產國'],
                'answer': 2,
                'explain': '台積電（TSMC）是全球最大晶圓代工廠，生產全球約 60% 以上的先進晶片，包括 Apple、NVIDIA、AMD 的處理器。台灣在半導體供應鏈中地位不可或缺。'
            },
            {
                'q': '下列哪個裝置「不屬於」輸入裝置？',
                'options': ['鍵盤', '印表機', '滑鼠', '麥克風'],
                'answer': 1,
                'explain': '輸入裝置將資訊輸入電腦（鍵盤、滑鼠、麥克風、攝影機、掃描器），輸出裝置將資訊從電腦輸出（印表機、螢幕、喇叭）。印表機是輸出裝置。'
            },
        ]
    },
}

SLIDES = [
    {
        'id': 1, 'chapter': '封面', 'title': '科技演進與硬體',
        'bg': 'navy', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<div style='text-align:center;padding:30px 20px;'>
  <div style='font-size:72px;margin-bottom:20px;'>🖥️</div>
  <h1 style='font-size:2.8rem;font-weight:900;color:#fff;margin-bottom:12px;'>科技演進與硬體</h1>
  <h2 style='font-size:1.5rem;font-weight:400;color:#93c5fd;margin-bottom:30px;'>Technology Evolution &amp; Hardware</h2>
  <div style='display:flex;justify-content:center;gap:20px;flex-wrap:wrap;margin-bottom:30px;'>
    <span style='background:rgba(255,255,255,0.15);color:#e0f2fe;padding:8px 20px;border-radius:20px;font-size:1rem;'>⚡ 科技演進</span>
    <span style='background:rgba(255,255,255,0.15);color:#e0f2fe;padding:8px 20px;border-radius:20px;font-size:1rem;'>💾 硬體組成</span>
    <span style='background:rgba(255,255,255,0.15);color:#e0f2fe;padding:8px 20px;border-radius:20px;font-size:1rem;'>🇹🇼 台灣半導體</span>
  </div>
  <p style='color:#bfdbfe;font-size:1.1rem;'>城市科技 — 第一章</p>
</div>"""
    },
    {
        'id': 2, 'chapter': '第一章：科技的演進', 'title': '時代飛躍的變遷',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>時代飛躍的變遷</h2>
<div style='background:#1e293b;border-radius:12px;padding:20px;margin-bottom:16px;'>
  <div style='display:flex;align-items:center;justify-content:space-between;position:relative;'>
    <div style='position:absolute;left:0;right:0;top:50%;height:4px;background:linear-gradient(90deg,#f59e0b,#ef4444);z-index:0;'></div>
    <div style='display:flex;justify-content:space-between;width:100%;z-index:1;'>
      <div style='text-align:center;'>
        <div style='font-size:1.8rem;margin-bottom:4px;'>💡</div>
        <div style='background:#f59e0b;color:#000;padding:3px 10px;border-radius:10px;font-size:.75rem;font-weight:700;'>1879</div>
        <p style='color:#94a3b8;font-size:.7rem;margin-top:4px;'>電燈</p>
      </div>
      <div style='text-align:center;'>
        <div style='font-size:1.8rem;margin-bottom:4px;'>🖥️</div>
        <div style='background:#f59e0b;color:#000;padding:3px 10px;border-radius:10px;font-size:.75rem;font-weight:700;'>1939</div>
        <p style='color:#94a3b8;font-size:.7rem;margin-top:4px;'>電腦</p>
      </div>
      <div style='text-align:center;'>
        <div style='font-size:1.8rem;margin-bottom:4px;'>🌐</div>
        <div style='background:#f59e0b;color:#000;padding:3px 10px;border-radius:10px;font-size:.75rem;font-weight:700;'>1990</div>
        <p style='color:#94a3b8;font-size:.7rem;margin-top:4px;'>網際網路</p>
      </div>
      <div style='text-align:center;'>
        <div style='font-size:1.8rem;margin-bottom:4px;'>📱</div>
        <div style='background:#f59e0b;color:#000;padding:3px 10px;border-radius:10px;font-size:.75rem;font-weight:700;'>2007</div>
        <p style='color:#94a3b8;font-size:.7rem;margin-top:4px;'>iPhone</p>
      </div>
      <div style='text-align:center;'>
        <div style='font-size:1.8rem;margin-bottom:4px;'>🤖</div>
        <div style='background:#ef4444;color:#fff;padding:3px 10px;border-radius:10px;font-size:.75rem;font-weight:700;'>NOW</div>
        <p style='color:#94a3b8;font-size:.7rem;margin-top:4px;'>AI 時代</p>
      </div>
    </div>
  </div>
</div>
<div style='background:#eff6ff;padding:12px 16px;border-radius:8px;border-left:4px solid #2563eb;'>
  <p style='color:#374151;font-size:.95rem;margin:0;'>💬 <strong>思考一下</strong>：15 年前沒有 iPhone，30 年前沒有網路，80 年前沒有電腦。現在的你，10 年後的科技世界會長什麼樣子？</p>
</div>"""
    },
    {
        'id': 3, 'chapter': '第一章：科技的演進', 'title': '摩爾定律',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>摩爾定律 — 驅動科技進步的引擎</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:8px;'>📐 摩爾定律</h3>
      <p style='color:#374151;font-size:.9rem;margin-bottom:8px;'>積體電路上的電晶體數量，每約 <strong>18–24 個月翻倍</strong>，效能提升但成本不增加。</p>
      <p style='color:#6b7280;font-size:.8rem;'>— Gordon Moore，Intel 共同創辦人，1965年</p>
    </div>
    <div style='background:#f0fdf4;padding:12px;border-radius:8px;'>
      <h3 style='color:#15803d;font-size:.95rem;margin-bottom:8px;'>📊 電晶體數量成長</h3>
      <div style='display:flex;flex-direction:column;gap:6px;font-size:.82rem;'>
        <div style='display:flex;justify-content:space-between;background:#fff;padding:6px 10px;border-radius:6px;'><span style='color:#374151;'>Intel 4004（1971）</span><span style='color:#1e40af;font-weight:700;'>2,300 顆</span></div>
        <div style='display:flex;justify-content:space-between;background:#fff;padding:6px 10px;border-radius:6px;'><span style='color:#374151;'>Pentium（1993）</span><span style='color:#1e40af;font-weight:700;'>310 萬顆</span></div>
        <div style='display:flex;justify-content:space-between;background:#fff;padding:6px 10px;border-radius:6px;'><span style='color:#374151;'>Apple M1（2020）</span><span style='color:#1e40af;font-weight:700;'>160 億顆</span></div>
        <div style='display:flex;justify-content:space-between;background:#dbeafe;padding:6px 10px;border-radius:6px;'><span style='color:#374151;'>Apple M4（2024）</span><span style='color:#1e40af;font-weight:700;'>280 億顆</span></div>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#fdf4ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#7c3aed;font-size:1rem;margin-bottom:8px;'>🇹🇼 台灣的角色</h3>
      <p style='color:#374151;font-size:.9rem;margin-bottom:10px;'>摩爾定律能持續至今，台積電（TSMC）功不可沒：</p>
      <ul style='color:#374151;font-size:.85rem;padding-left:16px;'>
        <li>全球最先進的晶圓代工廠</li>
        <li>3nm / 2nm 製程領先全球</li>
        <li>Apple、NVIDIA、AMD 都找台積電生產</li>
        <li>佔全球先進晶片代工超過 <strong>60%</strong></li>
      </ul>
    </div>
    <div style='background:#fff7ed;padding:10px;border-radius:8px;'>
      <p style='color:#9a3412;font-size:.85rem;margin:0;'>🔍 <strong>近況</strong>：摩爾定律在物理極限下已趨緩，業界改以 3D 堆疊、異質整合等新方式繼續提升效能。</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 4, 'chapter': '第一章：科技的演進', 'title': '科技演進對生活的影響',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>科技演進對生活的影響</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:16px;'>
  <div style='display:flex;flex-direction:column;gap:10px;'>
    <div style='background:#eff6ff;padding:12px;border-radius:10px;border-left:4px solid #2563eb;'>
      <h3 style='color:#1e40af;font-size:.9rem;margin-bottom:6px;'>📸 相機產業</h3>
      <p style='color:#374151;font-size:.82rem;'>底片 → 數位相機 → 手機攝影。柯達（Kodak）曾是世界最大相機公司，2012 年宣告破產。手機取代了一個百年產業。</p>
    </div>
    <div style='background:#f0fdf4;padding:12px;border-radius:10px;border-left:4px solid #16a34a;'>
      <h3 style='color:#15803d;font-size:.9rem;margin-bottom:6px;'>🗺️ 地圖導航</h3>
      <p style='color:#374151;font-size:.82rem;'>紙本地圖 → GPS 導航機 → Google Maps 即時導航。現在我們隨時知道路況，不再迷路。</p>
    </div>
    <div style='background:#fdf4ff;padding:12px;border-radius:10px;border-left:4px solid #7c3aed;'>
      <h3 style='color:#7c3aed;font-size:.9rem;margin-bottom:6px;'>🎵 音樂產業</h3>
      <p style='color:#374151;font-size:.82rem;'>黑膠唱片 → CD → MP3 → 串流（Spotify）。一台手機裝下了數千萬首歌曲。</p>
    </div>
  </div>
  <div style='display:flex;flex-direction:column;gap:10px;'>
    <div style='background:#fff7ed;padding:12px;border-radius:10px;border-left:4px solid #ea580c;'>
      <h3 style='color:#ea580c;font-size:.9rem;margin-bottom:6px;'>📺 影視娛樂</h3>
      <p style='color:#374151;font-size:.82rem;'>電視台排程 → 錄影帶 → DVD → 串流（Netflix）。你選擇看什麼，不再由電視台決定。</p>
    </div>
    <div style='background:#fef9c3;padding:12px;border-radius:10px;border-left:4px solid #ca8a04;'>
      <h3 style='color:#854d0e;font-size:.9rem;margin-bottom:6px;'>🛒 購物方式</h3>
      <p style='color:#374151;font-size:.82rem;'>實體店面 → 電視購物 → 網路購物 → 直播電商。台灣 PChome、蝦皮改變了消費習慣。</p>
    </div>
    <div style='background:#fef2f2;padding:12px;border-radius:10px;border-left:4px solid #dc2626;'>
      <h3 style='color:#dc2626;font-size:.9rem;margin-bottom:6px;'>🤖 AI 的來臨</h3>
      <p style='color:#374151;font-size:.82rem;'>2023 年起，ChatGPT、Copilot、Gemini 讓 AI 進入每個人的生活，再次改寫規則。</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 5, 'chapter': '第一章：科技的演進', 'title': '認識台灣半導體產業',
        'bg': 'white', 'quiz': None, 'chart': None,
        'video': {'url': 'https://www.youtube.com/embed/NSqmBmSMnOE', 'title': '台積電與台灣半導體的故事', 'desc': '了解台灣如何成為全球晶片重鎮'},
        'html': """
<h2 class='slide-title'>台灣半導體：護國神山</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-bottom:12px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>🏭 台積電 TSMC 關鍵數字</h3>
      <div style='display:flex;flex-direction:column;gap:6px;'>
        <div style='background:#fff;padding:8px 12px;border-radius:6px;display:flex;justify-content:space-between;font-size:.85rem;'><span style='color:#374151;'>全球先進晶片代工市佔</span><span style='color:#1e40af;font-weight:700;'>> 60%</span></div>
        <div style='background:#fff;padding:8px 12px;border-radius:6px;display:flex;justify-content:space-between;font-size:.85rem;'><span style='color:#374151;'>市值（2024）</span><span style='color:#1e40af;font-weight:700;'>~ 1 兆美元</span></div>
        <div style='background:#fff;padding:8px 12px;border-radius:6px;display:flex;justify-content:space-between;font-size:.85rem;'><span style='color:#374151;'>員工人數</span><span style='color:#1e40af;font-weight:700;'>~ 7 萬人</span></div>
        <div style='background:#dbeafe;padding:8px 12px;border-radius:6px;display:flex;justify-content:space-between;font-size:.85rem;'><span style='color:#374151;'>最先進製程</span><span style='color:#1e40af;font-weight:700;'>2nm（2025）</span></div>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:8px;'>🌏 為什麼台灣這麼重要？</h3>
      <ul style='color:#374151;font-size:.85rem;padding-left:16px;'>
        <li>iPhone 的 A 系列晶片 → 台積電製造</li>
        <li>NVIDIA 的 AI 晶片（H100）→ 台積電製造</li>
        <li>AMD 處理器 → 台積電製造</li>
        <li>全球 AI 發展高度依賴台灣晶片</li>
      </ul>
    </div>
  </div>
</div>
<div id='video-section-5' class='video-section'></div>"""
    },
    {
        'id': 6, 'chapter': '第一章：科技的演進', 'title': '數位轉型的浪潮',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>數位轉型：每個產業都在改變</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>🏦 金融業</h3>
      <p style='color:#374151;font-size:.85rem;margin-bottom:8px;'>實體銀行 → 網路銀行 → 純網銀（LINE Bank）→ 行動支付</p>
      <div style='background:#dbeafe;padding:8px;border-radius:6px;'><p style='color:#1e40af;font-size:.8rem;margin:0;'>台灣悠遊卡、街口支付每天交易數千萬筆</p></div>
    </div>
    <div style='background:#f0fdf4;padding:12px;border-radius:8px;'>
      <h3 style='color:#15803d;font-size:.95rem;margin-bottom:8px;'>🏥 醫療業</h3>
      <p style='color:#374151;font-size:.82rem;'>紙本病歷 → 電子病歷 → AI 診斷輔助。台灣健保 IC 卡系統是世界先進醫療資訊系統之一。</p>
    </div>
  </div>
  <div>
    <div style='background:#fdf4ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#7c3aed;font-size:1rem;margin-bottom:10px;'>🎓 教育業</h3>
      <p style='color:#374151;font-size:.85rem;margin-bottom:8px;'>黑板粉筆 → 電子白板 → 線上課程（Coursera、YouTube）→ AI 個人化學習</p>
      <div style='background:#e9d5ff;padding:8px;border-radius:6px;'><p style='color:#7c3aed;font-size:.8rem;margin:0;'>你現在使用的這套教學系統，就是數位轉型的一部分！</p></div>
    </div>
    <div style='background:#fff7ed;padding:12px;border-radius:8px;'>
      <h3 style='color:#ea580c;font-size:.95rem;margin-bottom:6px;'>🚗 交通業</h3>
      <p style='color:#374151;font-size:.82rem;'>計程車招手 → Uber 叫車 → 自動駕駛（Tesla）。台灣 YouBike 每天有 30 萬次租借。</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 7, 'chapter': '第一章：科技的演進', 'title': '🎯 第一章 隨堂測驗',
        'bg': 'purple', 'quiz': 'q1', 'chart': None, 'video': None,
        'html': """
<div style='text-align:center;padding:20px;'>
  <div style='font-size:56px;margin-bottom:15px;'>🎯</div>
  <h2 style='color:#fff;font-size:2rem;font-weight:800;margin-bottom:10px;'>第一章 隨堂測驗</h2>
  <p style='color:#e9d5ff;font-size:1.1rem;'>科技演進 ── 2 道題目，點擊作答！</p>
</div>"""
    },
    {
        'id': 8, 'chapter': '第二章：電腦硬體組成', 'title': '電腦硬體架構',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>電腦硬體架構</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <h3 style='color:#374151;font-size:1rem;margin-bottom:12px;'>🔧 五大核心元件</h3>
    <div class='layer-stack'>
      <div class='layer layer-user'>
        <div class='layer-num'>①</div>
        <div><div class='layer-name' style='color:#374151;'>CPU（中央處理器）</div><div class='layer-detail'>電腦大腦，執行所有運算指令</div></div>
      </div>
      <div class='layer layer-app'>
        <div class='layer-num'>②</div>
        <div><div class='layer-name' style='color:#374151;'>RAM（記憶體）</div><div class='layer-detail'>暫存執行中的程式，關機清空</div></div>
      </div>
      <div class='layer layer-os'>
        <div class='layer-num'>③</div>
        <div><div class='layer-name' style='color:#374151;'>儲存裝置（SSD/HDD）</div><div class='layer-detail'>永久儲存資料，關機不遺失</div></div>
      </div>
      <div class='layer layer-hw'>
        <div class='layer-num'>④</div>
        <div><div class='layer-name' style='color:#374151;'>GPU（圖形處理器）</div><div class='layer-detail'>處理畫面渲染與 AI 運算</div></div>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#f9fafb;padding:15px;border-radius:10px;border:1px solid #e5e7eb;margin-bottom:12px;'>
      <h3 style='color:#374151;font-size:1rem;margin-bottom:10px;'>🔁 CPU 工作流程</h3>
      <div style='display:flex;flex-direction:column;gap:6px;font-size:.85rem;'>
        <div style='background:#dbeafe;padding:8px;border-radius:6px;color:#1e40af;'><strong>取指</strong>（Fetch）：從記憶體讀取指令</div>
        <div style='background:#dcfce7;padding:8px;border-radius:6px;color:#15803d;'><strong>解碼</strong>（Decode）：解讀指令意義</div>
        <div style='background:#fde047;padding:8px;border-radius:6px;color:#854d0e;'><strong>執行</strong>（Execute）：進行運算</div>
        <div style='background:#e9d5ff;padding:8px;border-radius:6px;color:#7c3aed;'><strong>回寫</strong>（Write-back）：儲存結果</div>
      </div>
    </div>
  </div>
</div>"""
    },
    {
        'id': 9, 'chapter': '第二章：電腦硬體組成', 'title': 'CPU vs GPU',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>CPU vs GPU — 兩種不同的計算哲學</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div style='background:#eff6ff;padding:18px;border-radius:12px;border:2px solid #2563eb;'>
    <div style='text-align:center;margin-bottom:12px;'>
      <div style='font-size:2rem;'>🧠</div>
      <h3 style='color:#1e40af;font-size:1.1rem;font-weight:800;'>CPU</h3>
      <p style='color:#6b7280;font-size:.8rem;'>Central Processing Unit</p>
    </div>
    <ul style='color:#374151;font-size:.85rem;padding-left:16px;'>
      <li>少數強大核心（4–24核）</li>
      <li>擅長<strong>複雜的序列任務</strong></li>
      <li>作業系統、文書處理、邏輯判斷</li>
      <li>通用型，什麼都能做</li>
    </ul>
    <div style='background:#dbeafe;padding:8px;border-radius:6px;margin-top:10px;'>
      <p style='color:#1e40af;font-size:.8rem;margin:0;'>比喻：一位博學多才的教授</p>
    </div>
  </div>
  <div style='background:#f0fdf4;padding:18px;border-radius:12px;border:2px solid #16a34a;'>
    <div style='text-align:center;margin-bottom:12px;'>
      <div style='font-size:2rem;'>🎮</div>
      <h3 style='color:#15803d;font-size:1.1rem;font-weight:800;'>GPU</h3>
      <p style='color:#6b7280;font-size:.8rem;'>Graphics Processing Unit</p>
    </div>
    <ul style='color:#374151;font-size:.85rem;padding-left:16px;'>
      <li>數千個小核心（NVIDIA H100：14,592核）</li>
      <li>擅長<strong>大量平行運算</strong></li>
      <li>遊戲渲染、AI 訓練、影片剪輯</li>
      <li>NVIDIA 市值 2026 年已突破 4.7 兆美元，成為全球市值最高的公司</li>
    </ul>
    <div style='background:#dcfce7;padding:8px;border-radius:6px;margin-top:10px;'>
      <p style='color:#15803d;font-size:.8rem;margin:0;'>比喻：幾千個同時工作的工人</p>
    </div>
  </div>
</div>
<div style='background:#fef9c3;padding:10px;border-radius:8px;margin-top:12px;'>
  <p style='color:#854d0e;font-size:.85rem;margin:0;'>🤖 <strong>AI 革命的核心</strong>：ChatGPT、Midjourney 等 AI 都靠 NVIDIA GPU 訓練。台積電為 NVIDIA 製造 AI 晶片，讓台灣成為 AI 時代的關鍵地位。</p>
</div>"""
    },
    {
        'id': 10, 'chapter': '第二章：電腦硬體組成', 'title': 'RAM 與記憶體',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>RAM — 電腦的工作桌</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>📋 RAM 特性</h3>
      <div style='display:flex;flex-direction:column;gap:6px;'>
        <div style='background:#fff;padding:8px;border-radius:6px;border-left:3px solid #2563eb;font-size:.85rem;color:#374151;'>⚡ 速度極快（GB/s 等級）</div>
        <div style='background:#fff;padding:8px;border-radius:6px;border-left:3px solid #dc2626;font-size:.85rem;color:#374151;'>💨 揮發性：關機後資料消失</div>
        <div style='background:#fff;padding:8px;border-radius:6px;border-left:3px solid #16a34a;font-size:.85rem;color:#374151;'>🔢 容量：通常 8GB–64GB</div>
        <div style='background:#fff;padding:8px;border-radius:6px;border-left:3px solid #7c3aed;font-size:.85rem;color:#374151;'>💰 價格：比 SSD 貴、比 CPU 快取便宜</div>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#fef9c3;padding:15px;border-radius:10px;border:1px solid #fde047;margin-bottom:12px;'>
      <h3 style='color:#854d0e;font-size:1rem;margin-bottom:10px;'>🏠 記憶體階層</h3>
      <div style='display:flex;flex-direction:column;gap:4px;'>
        <div style='background:#ef4444;color:#fff;padding:8px 12px;border-radius:6px;font-size:.8rem;font-weight:700;'>CPU 快取（L1/L2/L3）：最快、最貴、最小</div>
        <div style='background:#f59e0b;color:#fff;padding:8px 12px;border-radius:6px;font-size:.8rem;font-weight:700;'>RAM：快、適中容量</div>
        <div style='background:#22c55e;color:#fff;padding:8px 12px;border-radius:6px;font-size:.8rem;font-weight:700;'>SSD：慢一些、大容量</div>
        <div style='background:#3b82f6;color:#fff;padding:8px 12px;border-radius:6px;font-size:.8rem;font-weight:700;'>HDD：最慢、最便宜、最大容量</div>
      </div>
    </div>
  </div>
</div>"""
    },
    {
        'id': 11, 'chapter': '第二章：電腦硬體組成', 'title': '主機板與連接介面',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>主機板與連接介面</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>🔌 主機板功能</h3>
      <p style='color:#374151;font-size:.9rem;margin-bottom:8px;'>主機板是電腦的「骨架」，連接所有元件並讓它們互相溝通：</p>
      <ul style='color:#374151;font-size:.85rem;padding-left:16px;'>
        <li>CPU 插槽</li>
        <li>RAM 插槽（通常 2–4 條）</li>
        <li>PCIe 插槽（GPU、SSD）</li>
        <li>USB、HDMI、網路孔</li>
      </ul>
    </div>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:10px;'>🔗 常見連接埠</h3>
      <table style='width:100%;border-collapse:collapse;font-size:.82rem;'>
        <tr style='background:#15803d;color:#fff;'><th style='padding:6px;'>介面</th><th style='padding:6px;'>用途</th></tr>
        <tr><td style='padding:6px;color:#374151;'>USB-A / USB-C</td><td style='padding:6px;color:#374151;'>連接周邊設備</td></tr>
        <tr style='background:#f0fdf4;'><td style='padding:6px;color:#374151;'>HDMI / DisplayPort</td><td style='padding:6px;color:#374151;'>連接螢幕</td></tr>
        <tr><td style='padding:6px;color:#374151;'>RJ-45（網路孔）</td><td style='padding:6px;color:#374151;'>有線網路</td></tr>
        <tr style='background:#f0fdf4;'><td style='padding:6px;color:#374151;'>3.5mm 音訊孔</td><td style='padding:6px;color:#374151;'>耳機 / 麥克風</td></tr>
        <tr><td style='padding:6px;color:#374151;'>Thunderbolt 4</td><td style='padding:6px;color:#374151;'>高速傳輸 / 充電</td></tr>
      </table>
    </div>
  </div>
</div>"""
    },
    {
        'id': 12, 'chapter': '第二章：電腦硬體組成', 'title': '🎯 第二章 隨堂測驗',
        'bg': 'purple', 'quiz': 'q2', 'chart': None, 'video': None,
        'html': """
<div style='text-align:center;padding:20px;'>
  <div style='font-size:56px;margin-bottom:15px;'>🎯</div>
  <h2 style='color:#fff;font-size:2rem;font-weight:800;margin-bottom:10px;'>第二章 隨堂測驗</h2>
  <p style='color:#e9d5ff;font-size:1.1rem;'>電腦硬體 ── 2 道題目，點擊作答！</p>
</div>"""
    },
    {
        'id': 13, 'chapter': '第三章：儲存裝置', 'title': 'HDD vs SSD',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>硬碟大對決：HDD vs SSD</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div style='background:#f9fafb;padding:18px;border-radius:12px;border:2px solid #6b7280;'>
    <div style='text-align:center;margin-bottom:12px;'>
      <div style='font-size:2rem;'>⚙️</div>
      <h3 style='color:#374151;font-size:1.1rem;font-weight:800;'>HDD 傳統硬碟</h3>
    </div>
    <div style='display:flex;flex-direction:column;gap:6px;font-size:.83rem;'>
      <div style='background:#dcfce7;padding:6px 10px;border-radius:6px;color:#15803d;'>✅ 同等價格容量更大</div>
      <div style='background:#dcfce7;padding:6px 10px;border-radius:6px;color:#15803d;'>✅ 適合大量資料備份</div>
      <div style='background:#fee2e2;padding:6px 10px;border-radius:6px;color:#dc2626;'>❌ 速度慢（100 MB/s）</div>
      <div style='background:#fee2e2;padding:6px 10px;border-radius:6px;color:#dc2626;'>❌ 有機械轉動、怕碰撞</div>
      <div style='background:#fee2e2;padding:6px 10px;border-radius:6px;color:#dc2626;'>❌ 較重、較耗電</div>
    </div>
  </div>
  <div style='background:#eff6ff;padding:18px;border-radius:12px;border:2px solid #2563eb;'>
    <div style='text-align:center;margin-bottom:12px;'>
      <div style='font-size:2rem;'>💾</div>
      <h3 style='color:#1e40af;font-size:1.1rem;font-weight:800;'>SSD 固態硬碟</h3>
    </div>
    <div style='display:flex;flex-direction:column;gap:6px;font-size:.83rem;'>
      <div style='background:#dcfce7;padding:6px 10px;border-radius:6px;color:#15803d;'>✅ 速度超快（NVMe 可達 7 GB/s）</div>
      <div style='background:#dcfce7;padding:6px 10px;border-radius:6px;color:#15803d;'>✅ 無機械構造、耐震</div>
      <div style='background:#dcfce7;padding:6px 10px;border-radius:6px;color:#15803d;'>✅ 輕薄省電</div>
      <div style='background:#fee2e2;padding:6px 10px;border-radius:6px;color:#dc2626;'>❌ 同容量價格較高</div>
      <div style='background:#fee2e2;padding:6px 10px;border-radius:6px;color:#dc2626;'>❌ 寫入次數有上限</div>
    </div>
  </div>
</div>
<div style='background:#fef9c3;padding:10px;border-radius:8px;margin-top:12px;'>
  <p style='color:#854d0e;font-size:.85rem;margin:0;'>💡 <strong>現在的選擇</strong>：新購電腦幾乎都配 SSD，因為開機速度和使用體驗差異極大。備份大量資料再考慮 HDD。</p>
</div>"""
    },
    {
        'id': 14, 'chapter': '第三章：儲存裝置', 'title': '儲存單位換算',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>儲存單位換算</h2>
<div class='units-grid'>
  <div class='unit-row unit-small'>
    <span class='unit-name'>1 Bit（位元）</span>
    <span class='unit-eq'>最小單位，只有 0 或 1</span>
  </div>
  <div class='unit-row unit-small'>
    <span class='unit-name'>1 Byte（位元組）</span>
    <span class='unit-eq'>= 8 bits　約存 1 個英文字母</span>
  </div>
  <div class='unit-row'>
    <span class='unit-name'>1 KB（Kilobyte）</span>
    <span class='unit-eq'>= 1,024 Bytes　約 1 頁純文字</span>
  </div>
  <div class='unit-row'>
    <span class='unit-name'>1 MB（Megabyte）</span>
    <span class='unit-eq'>= 1,024 KB　約 1 張照片</span>
  </div>
  <div class='unit-row unit-large'>
    <span class='unit-name'>1 GB（Gigabyte）</span>
    <span class='unit-eq'>= 1,024 MB　約 250 首 MP3 歌曲</span>
  </div>
  <div class='unit-row unit-large'>
    <span class='unit-name'>1 TB（Terabyte）</span>
    <span class='unit-eq'>= 1,024 GB　約 250,000 首歌 / 500 部電影</span>
  </div>
</div>
<div style='background:#eff6ff;padding:12px;border-radius:8px;margin-top:8px;'>
  <p style='color:#374151;font-size:.88rem;margin:0;'>📱 <strong>生活對照</strong>：iPhone 17 Pro Max 最大 2TB、Nintendo Switch 遊戲卡通常 8–32GB、4K 電影約 25–80GB。</p>
</div>"""
    },
    {
        'id': 15, 'chapter': '第三章：儲存裝置', 'title': '雲端儲存 vs 本機儲存',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>雲端儲存 vs 本機儲存</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div style='background:#f0fdf4;padding:16px;border-radius:10px;'>
    <h3 style='color:#15803d;font-size:1rem;margin-bottom:10px;'>☁️ 雲端儲存</h3>
    <p style='color:#374151;font-size:.85rem;margin-bottom:8px;'>資料存在遠端伺服器，透過網路存取。</p>
    <div style='display:flex;flex-direction:column;gap:6px;font-size:.82rem;'>
      <div style='background:#dcfce7;padding:6px;border-radius:5px;color:#15803d;'>✅ 任何裝置都能存取</div>
      <div style='background:#dcfce7;padding:6px;border-radius:5px;color:#15803d;'>✅ 自動備份不怕遺失</div>
      <div style='background:#dcfce7;padding:6px;border-radius:5px;color:#15803d;'>✅ 多人協作共享</div>
      <div style='background:#fee2e2;padding:6px;border-radius:5px;color:#dc2626;'>❌ 需要網路才能存取</div>
      <div style='background:#fee2e2;padding:6px;border-radius:5px;color:#dc2626;'>❌ 隱私疑慮（存在他人伺服器）</div>
    </div>
    <div style='background:#fff;padding:8px;border-radius:6px;margin-top:8px;font-size:.8rem;color:#374151;'>Google Drive、OneDrive、iCloud、Dropbox</div>
  </div>
  <div style='background:#eff6ff;padding:16px;border-radius:10px;'>
    <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>💾 本機儲存</h3>
    <p style='color:#374151;font-size:.85rem;margin-bottom:8px;'>資料存在自己的裝置（電腦、隨身碟）。</p>
    <div style='display:flex;flex-direction:column;gap:6px;font-size:.82rem;'>
      <div style='background:#dcfce7;padding:6px;border-radius:5px;color:#15803d;'>✅ 不需網路、隨時可用</div>
      <div style='background:#dcfce7;padding:6px;border-radius:5px;color:#15803d;'>✅ 資料在自己手中</div>
      <div style='background:#fee2e2;padding:6px;border-radius:5px;color:#dc2626;'>❌ 裝置損壞資料可能遺失</div>
      <div style='background:#fee2e2;padding:6px;border-radius:5px;color:#dc2626;'>❌ 需要手動備份</div>
    </div>
    <div style='background:#fff;padding:8px;border-radius:6px;margin-top:8px;font-size:.8rem;color:#374151;'>電腦硬碟、USB 隨身碟、外接 SSD</div>
  </div>
</div>
<div style='background:#fef9c3;padding:10px;border-radius:8px;margin-top:12px;'>
  <p style='color:#854d0e;font-size:.85rem;margin:0;'>💡 <strong>最佳實踐</strong>：重要資料遵循「3-2-1 原則」：3 份備份、2 種媒介、1 份異地（雲端）。</p>
</div>"""
    },
    {
        'id': 16, 'chapter': '第三章：儲存裝置', 'title': '快閃記憶體與隨身碟',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>快閃記憶體的世界</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>⚡ 快閃記憶體（Flash）</h3>
      <p style='color:#374151;font-size:.88rem;margin-bottom:8px;'>SSD、隨身碟、記憶卡、手機儲存都使用快閃記憶體：</p>
      <ul style='color:#374151;font-size:.83rem;padding-left:16px;'>
        <li>非揮發性：關機後資料保留</li>
        <li>無機械轉動：耐震、靜音、省電</li>
        <li>讀寫次數有上限（P/E cycles）</li>
        <li>台灣旺宏、南亞科生產 NAND Flash</li>
      </ul>
    </div>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:10px;'>📊 USB 速度世代</h3>
      <table style='width:100%;border-collapse:collapse;font-size:.82rem;'>
        <tr style='background:#15803d;color:#fff;'><th style='padding:6px;'>規格</th><th style='padding:6px;'>最高速度</th></tr>
        <tr><td style='padding:6px;color:#374151;'>USB 2.0</td><td style='padding:6px;color:#374151;'>480 Mbps</td></tr>
        <tr style='background:#f0fdf4;'><td style='padding:6px;color:#374151;'>USB 3.0</td><td style='padding:6px;color:#374151;'>5 Gbps</td></tr>
        <tr><td style='padding:6px;color:#374151;'>USB 3.2 Gen 2</td><td style='padding:6px;color:#374151;'>10 Gbps</td></tr>
        <tr style='background:#f0fdf4;'><td style='padding:6px;color:#374151;font-weight:700;'>Thunderbolt 4</td><td style='padding:6px;color:#15803d;font-weight:700;'>40 Gbps</td></tr>
      </table>
    </div>
  </div>
</div>"""
    },
    {
        'id': 17, 'chapter': '第三章：儲存裝置', 'title': '🎯 第三章 隨堂測驗',
        'bg': 'purple', 'quiz': 'q3', 'chart': None, 'video': None,
        'html': """
<div style='text-align:center;padding:20px;'>
  <div style='font-size:56px;margin-bottom:15px;'>🎯</div>
  <h2 style='color:#fff;font-size:2rem;font-weight:800;margin-bottom:10px;'>第三章 隨堂測驗</h2>
  <p style='color:#e9d5ff;font-size:1.1rem;'>儲存裝置 ── 2 道題目，點擊作答！</p>
</div>"""
    },
    {
        'id': 18, 'chapter': '第四章：數位生活中的硬體', 'title': '輸入與輸出裝置',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>輸入與輸出裝置</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>⌨️ 輸入裝置（Input）</h3>
      <p style='color:#374151;font-size:.85rem;margin-bottom:8px;'>將外部資訊輸入電腦：</p>
      <div style='display:grid;grid-template-columns:1fr 1fr;gap:6px;'>
        <div style='background:#fff;padding:8px;border-radius:6px;text-align:center;font-size:.82rem;color:#374151;'>⌨️ 鍵盤</div>
        <div style='background:#fff;padding:8px;border-radius:6px;text-align:center;font-size:.82rem;color:#374151;'>🖱️ 滑鼠</div>
        <div style='background:#fff;padding:8px;border-radius:6px;text-align:center;font-size:.82rem;color:#374151;'>📷 攝影機</div>
        <div style='background:#fff;padding:8px;border-radius:6px;text-align:center;font-size:.82rem;color:#374151;'>🎙️ 麥克風</div>
        <div style='background:#fff;padding:8px;border-radius:6px;text-align:center;font-size:.82rem;color:#374151;'>📱 觸控螢幕</div>
        <div style='background:#fff;padding:8px;border-radius:6px;text-align:center;font-size:.82rem;color:#374151;'>🖊️ 繪圖板</div>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:10px;'>🖥️ 輸出裝置（Output）</h3>
      <p style='color:#374151;font-size:.85rem;margin-bottom:8px;'>將電腦資訊輸出給使用者：</p>
      <div style='display:grid;grid-template-columns:1fr 1fr;gap:6px;'>
        <div style='background:#fff;padding:8px;border-radius:6px;text-align:center;font-size:.82rem;color:#374151;'>🖥️ 螢幕</div>
        <div style='background:#fff;padding:8px;border-radius:6px;text-align:center;font-size:.82rem;color:#374151;'>🖨️ 印表機</div>
        <div style='background:#fff;padding:8px;border-radius:6px;text-align:center;font-size:.82rem;color:#374151;'>🔊 喇叭</div>
        <div style='background:#fff;padding:8px;border-radius:6px;text-align:center;font-size:.82rem;color:#374151;'>📽️ 投影機</div>
      </div>
    </div>
    <div style='background:#fef9c3;padding:10px;border-radius:8px;'>
      <p style='color:#854d0e;font-size:.83rem;margin:0;'>💡 觸控螢幕同時是輸入也是輸出裝置！</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 19, 'chapter': '第四章：數位生活中的硬體', 'title': '手機的硬體',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>你口袋裡的超級電腦</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>📱 iPhone 17 Pro 規格</h3>
      <table style='width:100%;border-collapse:collapse;font-size:.82rem;'>
        <tr style='background:#1e40af;color:#fff;'><th style='padding:6px;'>元件</th><th style='padding:6px;'>規格</th></tr>
        <tr><td style='padding:6px;color:#374151;'>處理器</td><td style='padding:6px;color:#374151;'>Apple A19 Pro（台積電 3nm）</td></tr>
        <tr style='background:#f0f9ff;'><td style='padding:6px;color:#374151;'>RAM</td><td style='padding:6px;color:#374151;'>12 GB LPDDR5X</td></tr>
        <tr><td style='padding:6px;color:#374151;'>儲存</td><td style='padding:6px;color:#374151;'>256GB ~ 2TB NVMe</td></tr>
        <tr style='background:#f0f9ff;'><td style='padding:6px;color:#374151;'>相機</td><td style='padding:6px;color:#374151;'>4800 萬像素主鏡頭</td></tr>
        <tr><td style='padding:6px;color:#374151;'>螢幕</td><td style='padding:6px;color:#374151;'>6.3 吋 120Hz ProMotion</td></tr>
      </table>
    </div>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:8px;'>🚀 手機 vs 1990 年代超級電腦</h3>
      <p style='color:#374151;font-size:.88rem;margin-bottom:10px;'>你手中的 iPhone 效能遠超過 30 年前整棟大樓的超級電腦！</p>
      <ul style='color:#374151;font-size:.83rem;padding-left:16px;'>
        <li>Apollo 11 導航電腦：4KB 記憶體</li>
        <li>你的手機：8,000,000 KB（8GB）</li>
        <li>差距超過 <strong>200 萬倍</strong></li>
      </ul>
    </div>
  </div>
</div>"""
    },
    {
        'id': 20, 'chapter': '第四章：數位生活中的硬體', 'title': '電腦選購指南',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>電腦選購指南</h2>
<div style='display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;margin-bottom:15px;'>
  <div style='background:#eff6ff;padding:14px;border-radius:10px;text-align:center;'>
    <div style='font-size:2rem;margin-bottom:6px;'>📚</div>
    <h3 style='color:#1e40af;font-size:.9rem;margin-bottom:8px;'>一般文書用途</h3>
    <ul style='color:#374151;font-size:.78rem;text-align:left;padding-left:12px;'>
      <li>CPU：Intel i5 / AMD R5</li>
      <li>RAM：8GB~16GB</li>
      <li>SSD：256GB~512GB</li>
      <li>預算：約 2~3 萬</li>
    </ul>
  </div>
  <div style='background:#f0fdf4;padding:14px;border-radius:10px;text-align:center;'>
    <div style='font-size:2rem;margin-bottom:6px;'>🎮</div>
    <h3 style='color:#15803d;font-size:.9rem;margin-bottom:8px;'>遊戲 / 影音剪輯</h3>
    <ul style='color:#374151;font-size:.78rem;text-align:left;padding-left:12px;'>
      <li>CPU：Intel i7 / AMD R7</li>
      <li>RAM：16GB~32GB</li>
      <li>GPU：RTX 5060 以上</li>
      <li>預算：約 4~8 萬</li>
    </ul>
  </div>
  <div style='background:#fdf4ff;padding:14px;border-radius:10px;text-align:center;'>
    <div style='font-size:2rem;margin-bottom:6px;'>🤖</div>
    <h3 style='color:#7c3aed;font-size:.9rem;margin-bottom:8px;'>AI / 深度學習</h3>
    <ul style='color:#374151;font-size:.78rem;text-align:left;padding-left:12px;'>
      <li>CPU：Intel i9 / AMD R9</li>
      <li>RAM：64GB 以上</li>
      <li>GPU：RTX 5090 / H100</li>
      <li>預算：10 萬以上</li>
    </ul>
  </div>
</div>
<div style='background:#fef9c3;padding:10px;border-radius:8px;'>
  <p style='color:#854d0e;font-size:.85rem;margin:0;'>💡 <strong>近期價格飛漲</strong>：由於 AI 應用快速發展，記憶體缺貨導致價格大漲。</p>
</div>"""
    },
    {
        'id': 21, 'chapter': '第四章：數位生活中的硬體', 'title': '硬體辨識實作',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>硬體辨識：認識你的電腦</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>🪟 Windows 查詢方式</h3>
      <div style='display:flex;flex-direction:column;gap:6px;font-size:.83rem;'>
        <div style='background:#fff;padding:8px;border-radius:6px;border-left:3px solid #2563eb;'>
          <p style='color:#1e40af;font-weight:700;margin:0 0 2px;'>系統資訊</p>
          <p style='color:#374151;font-size:.78rem;margin:0;'>開始 → 設定 → 系統 → 關於</p>
        </div>
        <div style='background:#fff;padding:8px;border-radius:6px;border-left:3px solid #2563eb;'>
          <p style='color:#1e40af;font-weight:700;margin:0 0 2px;'>工作管理員</p>
          <p style='color:#374151;font-size:.78rem;margin:0;'>Ctrl+Shift+Esc → 效能標籤</p>
        </div>
        <div style='background:#fff;padding:8px;border-radius:6px;border-left:3px solid #2563eb;'>
          <p style='color:#1e40af;font-weight:700;margin:0 0 2px;'>裝置管理員</p>
          <p style='color:#374151;font-size:.78rem;margin:0;'>Win+X → 裝置管理員</p>
        </div>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:10px;'>🍎 Mac 查詢方式</h3>
      <div style='display:flex;flex-direction:column;gap:6px;font-size:.83rem;'>
        <div style='background:#fff;padding:8px;border-radius:6px;border-left:3px solid #16a34a;'>
          <p style='color:#15803d;font-weight:700;margin:0 0 2px;'>關於這台 Mac</p>
          <p style='color:#374151;font-size:.78rem;margin:0;'>蘋果圖示 → 關於這台 Mac</p>
        </div>
        <div style='background:#fff;padding:8px;border-radius:6px;border-left:3px solid #16a34a;'>
          <p style='color:#15803d;font-weight:700;margin:0 0 2px;'>活動監視器</p>
          <p style='color:#374151;font-size:.78rem;margin:0;'>Spotlight 搜尋「活動監視器」</p>
        </div>
      </div>
    </div>
  </div>
</div>"""
    },
    {
        'id': 22, 'chapter': '第四章：數位生活中的硬體', 'title': '🎯 第四章 隨堂測驗',
        'bg': 'purple', 'quiz': 'q4', 'chart': None, 'video': None,
        'html': """
<div style='text-align:center;padding:20px;'>
  <div style='font-size:56px;margin-bottom:15px;'>🎯</div>
  <h2 style='color:#fff;font-size:2rem;font-weight:800;margin-bottom:10px;'>第四章 隨堂測驗</h2>
  <p style='color:#e9d5ff;font-size:1.1rem;'>數位生活硬體 ── 2 道題目，點擊作答！</p>
</div>"""
    },
    {
        'id': 23, 'chapter': '分組實作', 'title': '分組實作：載具健診報告',
        'bg': 'teal', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 style='font-size:1.8rem;font-weight:800;color:#fff;margin-bottom:20px;text-align:center;'>🔬 分組實作：載具健診報告</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div style='background:rgba(255,255,255,0.15);padding:18px;border-radius:12px;'>
    <h3 style='color:#fff;font-size:1rem;margin-bottom:14px;'>📋 實作任務</h3>
    <div style='display:flex;flex-direction:column;gap:10px;'>
      <div style='background:rgba(255,255,255,0.2);padding:12px;border-radius:8px;'>
        <p style='color:#fff;font-weight:700;font-size:.9rem;margin:0 0 4px;'>任務一：硬體規格調查</p>
        <p style='color:#cffafe;font-size:.8rem;margin:0;'>查詢目前使用的載具(電腦/平板..)：CPU、RAM、儲存空間、作業系統版本</p>
      </div>
      <div style='background:rgba(255,255,255,0.2);padding:12px;border-radius:8px;'>
        <p style='color:#fff;font-weight:700;font-size:.9rem;margin:0 0 4px;'>任務二：效能分析</p>
        <p style='color:#cffafe;font-size:.8rem;margin:0;'>開啟工作管理員，記錄 CPU、RAM 使用率，開多個應用程式觀察變化</p>
      </div>
      <div style='background:rgba(255,255,255,0.2);padding:12px;border-radius:8px;'>
        <p style='color:#fff;font-weight:700;font-size:.9rem;margin:0 0 4px;'>任務三：儲存空間檢查</p>
        <p style='color:#cffafe;font-size:.8rem;margin:0;'>查看磁碟使用狀況，找出占用最多空間的資料夾</p>
      </div>
    </div>
  </div>
  <div>
    <div style='background:rgba(255,255,255,0.15);padding:15px;border-radius:12px;margin-bottom:12px;'>
      <h3 style='color:#fff;font-size:1rem;margin-bottom:10px;'>📊 報告格式(範例建議)</h3>
      <ul style='color:#cffafe;font-size:.85rem;padding-left:16px;'>
        <li>電腦基本規格截圖</li>
        <li>工作管理員效能截圖</li>
        <li>與同組同學的規格比較表</li>
        <li>改善建議（加 RAM？換 SSD？）</li>
      </ul>
    </div>
    <div style='background:rgba(255,255,255,0.15);padding:12px;border-radius:8px;'>
      <p style='color:#fff;font-size:.85rem;font-weight:700;margin-bottom:4px;'>🗓️ 繳交方式</p>
      <p style='color:#cffafe;font-size:.82rem;margin:0;'>Google 文件上傳至 Google Classroom</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 24, 'chapter': '分組實作', 'title': '科技不只是工具',
        'bg': 'navy', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<div style='text-align:center;padding:30px 20px;'>
  <div style='font-size:64px;margin-bottom:20px;'>🌟</div>
  <h1 style='font-size:2.2rem;font-weight:900;color:#fff;margin-bottom:12px;'>科技不只是工具</h1>
  <h2 style='font-size:1.2rem;font-weight:400;color:#93c5fd;margin-bottom:24px;'>它改變了人類思考和生活的方式</h2>
  <div style='background:rgba(255,255,255,0.1);padding:18px;border-radius:12px;margin-bottom:24px;max-width:600px;margin-left:auto;margin-right:auto;'>
    <p style='color:#e2e8f0;font-size:1rem;font-style:italic;line-height:1.7;margin:0;'>
      「Stay Hungry, Stay Foolish.」<br>
      <span style='font-size:.85rem;color:#94a3b8;'>— Steve Jobs，2005 Stanford 畢業演說</span>
    </p>
  </div>
  <div style='display:flex;justify-content:center;gap:12px;flex-wrap:wrap;'>
    <span style='background:rgba(255,255,255,0.12);color:#e0f2fe;padding:8px 18px;border-radius:20px;font-size:.9rem;'>了解了硬體 ✅</span>
    <span style='background:rgba(255,255,255,0.12);color:#e0f2fe;padding:8px 18px;border-radius:20px;font-size:.9rem;'>看見了演進 ✅</span>
    <span style='background:rgba(255,255,255,0.12);color:#e0f2fe;padding:8px 18px;border-radius:20px;font-size:.9rem;'>下一章見 👋</span>
  </div>
</div>"""
    },
]
