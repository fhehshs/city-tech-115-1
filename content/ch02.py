# ────────────────────────────────────────────────────────────
#  AI時代的數位創作者 — 第二週教學內容
#  content.py：所有投影片與測驗資料
# ────────────────────────────────────────────────────────────

# ── 章節對照表（用於 TOC 分組）──────────────────────────────
CHAPTERS = [
    {'name': '封面',              'start': 1},
    {'name': '第一章：數位語言基礎', 'start': 2},
    {'name': '第二章：AI 創作基礎', 'start': 14},
    {'name': '第三章：創作責任',   'start': 25},
    {'name': '總結與作業',         'start': 36},
]

# ── 投影片資料 ────────────────────────────────────────────────
# 欄位說明：
#   id      : 投影片編號（1 開始）
#   chapter : 所屬章節名稱
#   title   : 投影片標題
#   bg      : 背景色 → navy / teal / purple / white
#   quiz    : 觸發哪組測驗（None 或 'q1'~'q5'）
#   chart   : 渲染哪個圖表（None 或字串名稱）
#   video   : 影片設定（None 或 dict）
#   html    : 投影片內容 HTML

SLIDES = [

# ──────────────────────────────────────────
#  封面
# ──────────────────────────────────────────
{
  'id': 1,
  'chapter': '封面',
  'title': 'AI 時代的數位創作者',
  'bg': 'navy',
  'quiz': None, 'chart': None, 'video': None,
  'html': """
<div class='cover-wrap'>
  <div class='cover-badge'>第二週 · 2026 學年度</div>
  <div class='cover-title'>AI 時代的<br>數位創作者</div>
  <div class='cover-sub'>從 0 和 1 到 AI 生成圖，認識數位語言、創作原理與創作責任</div>
  <div class='cover-tags'>
    <span class='tag'>🔢 數位語言</span>
    <span class='tag'>🤖 AI 創作</span>
    <span class='tag'>⚖️ 創作責任</span>
    <span class='tag'>🎨 創用 CC</span>
  </div>
  <div class='cover-meta'>高一城市科技 ｜ 授課老師 ｜ 2026 學年度</div>
</div>"""
},

# ──────────────────────────────────────────
#  第一章：數位語言基礎
# ──────────────────────────────────────────
{
  'id': 2,
  'chapter': '第一章：數位語言基礎',
  'title': '第一章導入：資料如何儲存？',
  'bg': 'navy',
  'quiz': None, 'chart': None, 'video': None,
  'html': """
<div class='slide-inner'>
  <h2 class='slide-title' style='color:#fff'>📦 第一章：數位語言基礎</h2>
  <p class='slide-desc' style='color:rgba(255,255,255,.7)'>引導問題：「資料如何儲存在電腦裡？」</p>
  <div class='fact-box' style='margin-bottom:10px'>
    <p style='color:rgba(255,255,255,.85)'>
      數位世界的一切——文字、圖片、音樂、影片——都以相同的基本單位儲存在電腦中。
      電腦並不像人類一樣理解文字或顏色，它只認識兩種狀態：<strong style='color:#F59E0B'>0</strong> 與 <strong style='color:#5eead4'>1</strong>。
    </p>
  </div>
  <div class='card-grid-3'>
    <div class='info-card'>
      <div class='card-icon'>📡</div>
      <div class='card-label'>類比 vs 數位</div>
      <div class='card-desc'>0 和 1 如何代表自然界的訊號？</div>
    </div>
    <div class='info-card'>
      <div class='card-icon'>🔤</div>
      <div class='card-label'>文字表示法</div>
      <div class='card-desc'>ASCII 與 Unicode 如何儲存文字</div>
    </div>
    <div class='info-card'>
      <div class='card-icon'>🧮</div>
      <div class='card-label'>進位系統</div>
      <div class='card-desc'>二進位、十六進位的應用</div>
    </div>
    <div class='info-card'>
      <div class='card-icon'>🖼️</div>
      <div class='card-label'>像素與色彩</div>
      <div class='card-desc'>解析度、色彩深度怎麼計算？</div>
    </div>
    <div class='info-card'>
      <div class='card-icon'>🎵</div>
      <div class='card-label'>聲音與視訊</div>
      <div class='card-desc'>取樣率、幀率與多媒體格式</div>
    </div>
    <div class='info-card'>
      <div class='card-icon'>📁</div>
      <div class='card-label'>檔案格式</div>
      <div class='card-desc'>JPG / PNG / SVG 怎麼選？</div>
    </div>
  </div>
  <div class='tip-box' style='margin-top:10px'>
    💡 思考：為什麼電腦只用 0 和 1，卻能呈現千萬種顏色和聲音？
  </div>
</div>"""
},


{
  'id': 3,
  'chapter': '第一章：數位語言基礎',
  'title': '類比訊號 vs 數位訊號',
  'bg': 'white',
  'quiz': None, 'chart': None, 'video': None,
  'html': """
<div class='slide-inner'>
  <h2 class='slide-title'>📡 類比訊號 vs 數位訊號</h2>
  <p class='slide-desc'>為什麼電腦只懂 0 和 1？從自然界的連續波到二進位的離散世界</p>
  <div class='card-grid-2' style='margin-bottom:12px'>
    <div style='background:linear-gradient(135deg,#fff7ed,#ffedd5);border:1px solid #fdba74;border-radius:14px;padding:16px'>
      <div style='font-size:1.3rem;margin-bottom:8px'>🌊</div>
      <div style='font-weight:700;color:#9a3412;font-size:.9rem;margin-bottom:8px'>類比訊號（Analog）</div>
      <div style='font-size:.78rem;color:#7c2d12;line-height:1.7'>
        連續不間斷的波形，自然界的聲音、光線都是類比訊號<br>
        ✦ 值域連續，變化平滑<br>
        ✦ 容易受雜訊干擾，傳輸衰減<br>
        例：黑膠唱片、傳統廣播電話
      </div>
    </div>
    <div style='background:linear-gradient(135deg,#eff6ff,#dbeafe);border:1px solid #93c5fd;border-radius:14px;padding:16px'>
      <div style='font-size:1.3rem;margin-bottom:8px'>🔢</div>
      <div style='font-weight:700;color:#1e40af;font-size:.9rem;margin-bottom:8px'>數位訊號（Digital）</div>
      <div style='font-size:.78rem;color:#1e3a8a;line-height:1.7'>
        離散的 0 與 1，電腦處理的基本語言<br>
        ✦ 只有兩種狀態：ON（1）/ OFF（0）<br>
        ✦ 抗雜訊能力強，複製不失真<br>
        例：MP3、數位相片、電腦資料
      </div>
    </div>
  </div>
  <div style='background:#f8fafc;border:1px solid #e2e8f0;border-radius:10px;padding:12px 16px'>
    <div style='font-size:.8rem;font-weight:700;color:#1e293b;margin-bottom:8px'>🔄 類比 → 數位轉換（ADC）流程</div>
    <div style='display:flex;align-items:center;gap:8px;font-size:.75rem;color:#374151;flex-wrap:wrap'>
      <div style='background:#fff7ed;border:1px solid #fed7aa;border-radius:8px;padding:6px 10px'>🌊 類比訊號</div>
      <div style='color:#94a3b8'>→</div>
      <div style='background:#fefce8;border:1px solid #fef08a;border-radius:8px;padding:6px 10px'>⚡ 取樣（Sampling）</div>
      <div style='color:#94a3b8'>→</div>
      <div style='background:#faf5ff;border:1px solid #e9d5ff;border-radius:8px;padding:6px 10px'>📏 量化（Quantization）</div>
      <div style='color:#94a3b8'>→</div>
      <div style='background:#eff6ff;border:1px solid #93c5fd;border-radius:8px;padding:6px 10px'>🔢 數位資料（0 & 1）</div>
      <div style='color:#94a3b8'>→</div>
      <div style='background:#f0fdf4;border:1px solid #86efac;border-radius:8px;padding:6px 10px'>💾 儲存/傳輸</div>
    </div>
  </div>
</div>"""
},


{
  'id': 4,
  'chapter': '第一章：數位語言基礎',
  'title': '文字表示法：ASCII 與 Unicode',
  'bg': 'white',
  'quiz': None, 'chart': None, 'video': None,
  'html': """
<div class='slide-inner'>
  <h2 class='slide-title'>🔤 文字表示法：ASCII 與 Unicode</h2>
  <p class='slide-desc'>電腦如何儲存文字？每個字元都有對應的數字編碼</p>
  <div class='card-grid-2' style='margin-bottom:12px'>
    <div style='background:#f0fdf4;border:1px solid #86efac;border-radius:12px;padding:14px'>
      <div style='font-weight:700;color:#166534;font-size:.88rem;margin-bottom:8px'>📌 ASCII 編碼（1963）</div>
      <div style='font-size:.75rem;color:#14532d;line-height:1.7;margin-bottom:10px'>
        • 美國資訊交換標準碼（7 bits）<br>
        • 共 128 個字元：英文字母、數字、標點<br>
        • 擴展 ASCII（EASCII）= 8 bits，共 256 字元<br>
        • 不含中文、日文等非拉丁字符
      </div>
      <div style='background:#fff;border:1px solid #bbf7d0;border-radius:8px;padding:8px'>
        <div style='font-size:.72rem;color:#374151;font-weight:700;margin-bottom:6px'>ASCII 對照範例：</div>
        <div style='display:grid;grid-template-columns:1fr 1fr 1fr;gap:4px;font-size:.72rem;font-family:monospace'>
          <div style='background:#f0fdf4;padding:4px 6px;border-radius:4px;text-align:center'>A = 65</div>
          <div style='background:#f0fdf4;padding:4px 6px;border-radius:4px;text-align:center'>B = 66</div>
          <div style='background:#f0fdf4;padding:4px 6px;border-radius:4px;text-align:center'>Z = 90</div>
          <div style='background:#f0fdf4;padding:4px 6px;border-radius:4px;text-align:center'>a = 97</div>
          <div style='background:#f0fdf4;padding:4px 6px;border-radius:4px;text-align:center'>0 = 48</div>
          <div style='background:#f0fdf4;padding:4px 6px;border-radius:4px;text-align:center'>空格 = 32</div>
        </div>
      </div>
    </div>
    <div style='background:#eff6ff;border:1px solid #93c5fd;border-radius:12px;padding:14px'>
      <div style='font-weight:700;color:#1e40af;font-size:.88rem;margin-bottom:8px'>🌐 Unicode 與 UTF-8（1991）</div>
      <div style='font-size:.75rem;color:#1e3a8a;line-height:1.7;margin-bottom:10px'>
        • 全球統一字元標準，支援 15 萬以上字元<br>
        • 涵蓋中文、日韓文、阿拉伯文、Emoji<br>
        • UTF-8 最普遍：英文 1 Byte，中文 3 Bytes<br>
        • 現代網頁預設採用 UTF-8 編碼
      </div>
      <div style='background:#fff;border:1px solid #bfdbfe;border-radius:8px;padding:8px'>
        <div style='font-size:.72rem;color:#374151;font-weight:700;margin-bottom:6px'>Unicode 範例：</div>
        <div style='display:grid;grid-template-columns:1fr 1fr;gap:4px;font-size:.72rem'>
          <div style='background:#eff6ff;padding:4px 8px;border-radius:4px'>「好」= U+597D</div>
          <div style='background:#eff6ff;padding:4px 8px;border-radius:4px'>「A」= U+0041</div>
          <div style='background:#eff6ff;padding:4px 8px;border-radius:4px'>😀 = U+1F600</div>
          <div style='background:#eff6ff;padding:4px 8px;border-radius:4px'>「€」= U+20AC</div>
        </div>
      </div>
    </div>
  </div>
  <div class='tip-box'>
    💡 <strong>為何需要 Unicode？</strong> ASCII 只有 128 個字元，無法表示中文、日文等語言。Unicode 統一了全球文字的數字編碼，讓各種語言在同一系統中正確顯示，也讓 Emoji 在全球通用！
  </div>
</div>"""
},


{
  'id': 5,
  'chapter': '第一章：數位語言基礎',
  'title': '系統平台四層架構',
  'bg': 'white',
  'quiz': None, 'chart': None, 'video': None,
  'html': """
<div class='slide-inner'>
  <h2 class='slide-title'>🏗️ 系統平台四層架構</h2>
  <p class='slide-desc'>從硬體到使用者，每一層都有明確的職責</p>
  <div class='layer-stack'>
    <div class='layer layer-user'>
      <div class='layer-num' style='background:#7c3aed;color:#fff'>4</div>
      <div>
        <div class='layer-name'>使用者（User）</div>
        <div class='layer-detail'>操作裝置的人，透過應用程式完成各種數位任務。常見裝置：電腦、智慧型手機、平板、雲端伺服器</div>
      </div>
    </div>
    <div class='layer-arrow'>↑ 互動</div>
    <div class='layer layer-app'>
      <div class='layer-num' style='background:#0d9488;color:#fff'>3</div>
      <div>
        <div class='layer-name'>應用程式（Application）</div>
        <div class='layer-detail'>瀏覽器、LINE、遊戲等軟體，透過作業系統使用硬體功能。</div>
      </div>
    </div>
    <div class='layer-arrow'>↑ 呼叫</div>
    <div class='layer layer-os'>
      <div class='layer-num' style='background:#d97706;color:#fff'>2</div>
      <div>
        <div class='layer-name'>作業系統（OS）</div>
        <div class='layer-detail'>Windows、macOS、Linux、Android，負責管理硬體資源並提供介面。</div>
      </div>
    </div>
    <div class='layer-arrow'>↑ 管理</div>
    <div class='layer layer-hw'>
      <div class='layer-num' style='background:#dc2626;color:#fff'>1</div>
      <div>
        <div class='layer-name'>硬體（Hardware）</div>
        <div class='layer-detail'>CPU、記憶體、硬碟、螢幕等實體元件，是所有運算的基礎。</div>
      </div>
    </div>
  </div>
  <div class='tip-box' style='margin-top:8px'>💡 這四層架構讓同一款 App 可以在不同品牌的硬體上執行！</div>
</div>"""
},

{
  'id': 6,
  'chapter': '第一章：數位語言基礎',
  'title': '儲存單位與進位系統',
  'bg': 'white',
  'quiz': None, 'chart': None,
  'video': {'type': 'search', 'query': '二進位 十六進位 電腦儲存 教學 動畫', 'title': '🔢 進位系統動畫解說', 'desc': '搜尋二進位與進位系統教學影片'},
  'html': """
<div class='slide-inner'>
  <h2 class='slide-title'>📦 儲存單位 × 進位系統</h2>
  <div class='card-grid-2' style='margin-bottom:12px'>
    <div>
      <div style='font-size:.8rem;font-weight:700;color:#1E3A5F;margin-bottom:8px'>📦 儲存單位換算</div>
      <div class='units-grid'>
        <div class='unit-row unit-small'><span class='unit-name'>1 bit（位元）</span><span class='unit-eq'>最小單位，0 或 1</span></div>
        <div class='unit-row unit-small'><span class='unit-name'>1 Byte（位元組）</span><span class='unit-eq'>= 8 bits</span></div>
        <div class='unit-row'><span class='unit-name'>1 KB（千位元組）</span><span class='unit-eq'>= 1,024 Bytes</span></div>
        <div class='unit-row'><span class='unit-name'>1 MB（百萬位元組）</span><span class='unit-eq'>= 1,024 KB</span></div>
        <div class='unit-row'><span class='unit-name'>1 GB（十億位元組）</span><span class='unit-eq'>= 1,024 MB</span></div>
        <div class='unit-row unit-large'><span class='unit-name'>1 TB（兆位元組）</span><span class='unit-eq'>= 1,024 GB</span></div>
      </div>
    </div>
    <div>
      <div style='font-size:.8rem;font-weight:700;color:#1E3A5F;margin-bottom:8px'>🔢 進位系統比較</div>
      <table class='info-table'>
        <thead class='table-header'><tr><th>進位</th><th>使用符號</th><th>用途</th></tr></thead>
        <tbody>
          <tr><td><strong>2 進位</strong></td><td>0, 1</td><td>電腦底層語言</td></tr>
          <tr class='tr-highlight'><td><strong>8 進位</strong></td><td>0–7</td><td>早期程式設計</td></tr>
          <tr><td><strong>10 進位</strong></td><td>0–9</td><td>日常生活</td></tr>
          <tr class='tr-highlight'><td><strong>16 進位</strong></td><td>0–9, A–F</td><td>顏色碼、記憶體位址</td></tr>
        </tbody>
      </table>
      <div style='margin-top:8px;padding:8px 10px;background:#fffbeb;border-radius:8px;font-size:.78rem;color:#92400e'>
        💡 一個英文字母 = 1 Byte<br>
        一首 MP3 歌曲 ≈ 3–5 MB<br>
        一部 4K 電影 ≈ 50–100 GB
      </div>
    </div>
  </div>
  <div id='video-section-6' class='video-section'></div>
</div>"""
},

{
  'id': 7,
  'chapter': '第一章：數位語言基礎',
  'title': '電腦只懂 0 和 1',
  'bg': 'navy',
  'quiz': None, 'chart': None, 'video': None,
  'html': """
<div class='slide-inner'>
  <h2 class='slide-title' style='color:#fff'>💡 數字系統與位元：電腦如何表達全世界？</h2>
  <div style='display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:12px'>
    <div>
      <div class='bit-demo'>
        <div style='display:flex;gap:8px;justify-content:center;margin-bottom:14px'>
          <div class='bit-box bit-off'>OFF = 0</div>
          <div class='bit-box bit-on'>ON = 1</div>
        </div>
        <div style='text-align:center;color:rgba(255,255,255,.7);font-size:.8rem;margin-bottom:8px'>
          1 bit → 8 bits = 1 Byte（256 種組合）
        </div>
        <div style='background:rgba(255,255,255,.08);border-radius:10px;padding:10px 12px;font-size:.78rem'>
          <div style='color:#94a3b8;margin-bottom:6px'>英文字母 A：</div>
          <div style='color:#5eead4;font-family:monospace;letter-spacing:2px;font-size:1rem'>01000001</div>
          <div style='color:#94a3b8;margin-top:6px;margin-bottom:6px'>中文「好」：</div>
          <div style='color:#fcd34d;font-family:monospace;font-size:.72rem'>11100101 10100101 10111101</div>
          <div style='color:#94a3b8;font-size:.72rem;margin-top:4px'>英文 1 Byte，中文（UTF-8）3 Bytes</div>
        </div>
      </div>
    </div>
    <div>
      <div style='font-size:.82rem;font-weight:700;color:var(--gold);margin-bottom:10px'>🎨 顏色的數位表示</div>
      <div style='background:rgba(255,255,255,.08);border-radius:10px;padding:14px;font-size:.8rem'>
        <div style='display:flex;align-items:center;gap:12px;margin-bottom:10px'>
          <div style='width:36px;height:36px;border-radius:8px;background:#E60023;flex-shrink:0'></div>
          <div>
            <div style='color:var(--gold);font-weight:700'>重點紅</div>
            <div style='color:rgba(255,255,255,.6);font-size:.72rem'>#E60023</div>
          </div>
        </div>
        <table style='width:100%;font-size:.75rem;color:rgba(255,255,255,.8)'>
          <tr><td style='color:#94a3b8;padding:3px 0'>Hex（16進位）</td><td><code style='color:#fcd34d'>#E60023</code></td></tr>
          <tr><td style='color:#94a3b8;padding:3px 0'>RGB（10進位）</td><td><code>R:230, G:0, B:35</code></td></tr>
          <tr><td style='color:#94a3b8;padding:3px 0'>Binary（2進位）</td><td style='font-size:.68rem;font-family:monospace'>11100110 00000000 00100011</td></tr>
        </table>
      </div>
      <div class='tip-box' style='margin-top:10px'>
        🖥️ 螢幕上每個像素由 RGB 三色組成，各 0–255，共 24 位元 = 1,677 萬種顏色！
      </div>
    </div>
  </div>
</div>"""
},


{
  'id': 8,
  'chapter': '第一章：數位語言基礎',
  'title': '像素、解析度與色彩深度',
  'bg': 'white',
  'quiz': None, 'chart': None, 'video': None,
  'html': """
<div class='slide-inner'>
  <h2 class='slide-title'>🖼️ 像素、解析度與色彩深度</h2>
  <div style='display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;margin-bottom:12px'>
    <div style='background:#eff6ff;border:1px solid #93c5fd;border-radius:12px;padding:12px'>
      <div style='font-weight:700;color:#1e40af;font-size:.82rem;margin-bottom:6px'>📦 像素（Pixel）</div>
      <div style='font-size:.75rem;color:#1e3a8a;line-height:1.6'>
        數位影像的最小單位<br>
        每個像素儲存一組顏色<br><br>
        <strong>影像大小</strong> = 寬 × 高（像素數）<br>
        Full HD：1920 × 1080<br>
        4K UHD：3840 × 2160
      </div>
    </div>
    <div style='background:#faf5ff;border:1px solid #c4b5fd;border-radius:12px;padding:12px'>
      <div style='font-weight:700;color:#7c3aed;font-size:.82rem;margin-bottom:6px'>📏 解析度（Resolution）</div>
      <div style='font-size:.75rem;color:#581c87;line-height:1.6'>
        單位面積的像素密度<br>
        越高越細緻，品質越好<br><br>
        • 螢幕顯示：72–96 PPI<br>
        • 高品質印刷：300 DPI 以上<br>
        • 高端手機螢幕：400+ PPI
      </div>
    </div>
    <div style='background:#f0fdf4;border:1px solid #86efac;border-radius:12px;padding:12px'>
      <div style='font-weight:700;color:#166534;font-size:.82rem;margin-bottom:6px'>🎨 色彩深度</div>
      <div style='font-size:.75rem;color:#14532d;line-height:1.6'>
        每個像素用幾個 bit 記錄顏色<br>
        bit 數越多，色彩越豐富
      </div>
    </div>
  </div>
  <table class='info-table' style='margin-bottom:12px'>
    <thead class='table-header'><tr><th>色彩深度</th><th>顏色數量</th><th>說明</th><th>常見用途</th></tr></thead>
    <tbody>
      <tr><td><strong>1 bit</strong></td><td>2 色</td><td>黑 / 白（單色）</td><td>傳真機、掃描文件</td></tr>
      <tr class='tr-highlight'><td><strong>8 bit</strong></td><td>256 色</td><td>灰階 / 256 色</td><td>GIF 動圖、早期遊戲</td></tr>
      <tr><td><strong>16 bit</strong></td><td>6.5 萬色</td><td>Hi-Color</td><td>早期手機螢幕</td></tr>
      <tr class='tr-highlight'><td><strong>24 bit</strong></td><td>1,677 萬色</td><td>True Color（RGB 各 8 bit）</td><td>現代螢幕、數位攝影</td></tr>
    </tbody>
  </table>
  <div class='tip-box'>
    💡 <strong>計算未壓縮影像大小</strong>：寬 × 高 × 色彩深度（bit）÷ 8 ÷ 1,048,576 = MB<br>
    例：1920 × 1080 × 24 bit ÷ 8 ÷ 1,048,576 ≈ 5.9 MB（壓縮前 BMP 約這麼大！）
  </div>
</div>"""
},


{
  'id': 9,
  'chapter': '第一章：數位語言基礎',
  'title': '聲音與視訊的數位表示',
  'bg': 'white',
  'quiz': None, 'chart': None, 'video': None,
  'html': """
<div class='slide-inner'>
  <h2 class='slide-title'>🎵 聲音與視訊的數位表示</h2>
  <div class='card-grid-2' style='margin-bottom:12px'>
    <div style='background:linear-gradient(135deg,#fff7ed,#ffedd5);border:1px solid #fdba74;border-radius:12px;padding:14px'>
      <div style='font-weight:700;color:#9a3412;font-size:.88rem;margin-bottom:8px'>🎵 聲音數位化</div>
      <div style='font-size:.78rem;color:#7c2d12;line-height:1.7;margin-bottom:8px'>
        類比聲音 → 數位化需兩步驟：<br>
        ① <strong>取樣率</strong>（Sampling Rate）：每秒取樣次數<br>
        　電話品質：8,000 Hz<br>
        　CD 音質：44,100 Hz<br>
        ② <strong>取樣深度</strong>（Bit Depth）：每次取樣精度<br>
        　CD：16 bit；錄音室：24 bit
      </div>
      <div style='background:#fff8f0;border:1px solid #fde68a;border-radius:8px;padding:8px;font-size:.72rem;color:#92400e'>
        <div style='font-weight:700;margin-bottom:4px'>常見音訊格式：</div>
        <div style='display:grid;grid-template-columns:1fr 1fr;gap:3px;line-height:1.6'>
          <span>🎙️ WAV：無損，檔案最大</span>
          <span>🎵 MP3：有損壓縮，最普遍</span>
          <span>🍎 AAC：Apple 裝置首選</span>
          <span>🎧 FLAC：無損壓縮</span>
        </div>
      </div>
    </div>
    <div style='background:linear-gradient(135deg,#faf5ff,#ede9fe);border:1px solid #c4b5fd;border-radius:12px;padding:14px'>
      <div style='font-weight:700;color:#7c3aed;font-size:.88rem;margin-bottom:8px'>🎬 視訊數位化</div>
      <div style='font-size:.78rem;color:#581c87;line-height:1.7;margin-bottom:8px'>
        影片 = 連續靜態畫面（幀）快速播放<br>
        <strong>幀率</strong>（Frame Rate / fps）：<br>
        　電影：24 fps<br>
        　一般影片/直播：30 fps<br>
        　遊戲/流暢動作：60 fps<br>
        　慢動作拍攝：120–240 fps
      </div>
      <div style='background:#fdf8ff;border:1px solid #e9d5ff;border-radius:8px;padding:8px;font-size:.72rem;color:#581c87'>
        <div style='font-weight:700;margin-bottom:4px'>常見視訊格式：</div>
        <div style='display:grid;grid-template-columns:1fr 1fr;gap:3px;line-height:1.6'>
          <span>📹 MP4：最通用格式</span>
          <span>📱 MOV：Apple 裝置</span>
          <span>🖥️ AVI：Windows 傳統</span>
          <span>🌐 WebM：網頁串流</span>
        </div>
      </div>
    </div>
  </div>
  <div class='tip-box'>
    💡 <strong>為何影片檔案這麼大？</strong> 1 分鐘 1080p 30fps 未壓縮影片 ≈ 6 GB！壓縮技術（H.264/H.265）只記錄畫面間的「變化」，可縮減至原本的 1/50，讓串流成為可能。
  </div>
</div>"""
},


{
  'id': 10,
  'chapter': '第一章：數位語言基礎',
  'title': '進位系統與顏色編碼',
  'bg': 'white',
  'quiz': None, 'chart': None, 'video': None,
  'html': """
<div class='slide-inner'>
  <h2 class='slide-title'>🔢 進位系統與顏色編碼</h2>
  <div style='display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;margin-bottom:12px'>
    <div>
      <div style='font-size:.78rem;font-weight:700;color:#1E3A5F;margin-bottom:8px'>進位系統比較</div>
      <div style='font-size:.78rem;line-height:1.8;background:#f8fafc;padding:10px;border-radius:8px;border:1px solid #e2e8f0'>
        <div><strong>2 進位</strong>：只用 0 和 1，電腦最基本的語言</div>
        <div><strong>8 進位</strong>：用 0–7，早期程式設計常見</div>
        <div><strong>16 進位</strong>：用 0–9 與 A–F，簡潔表示大數值</div>
      </div>
    </div>
    <div>
      <div style='font-size:.78rem;font-weight:700;color:#1E3A5F;margin-bottom:8px'>十進位與轉換</div>
      <div style='font-size:.78rem;line-height:2;background:#f8fafc;padding:10px;border-radius:8px;border:1px solid #e2e8f0'>
        <div>十進位 <strong>10</strong> 的對應：</div>
        <div>二進位：<code style='background:#eff6ff;padding:1px 5px;border-radius:4px'>1010</code></div>
        <div>八進位：<code style='background:#eff6ff;padding:1px 5px;border-radius:4px'>12</code></div>
        <div>十六進位：<code style='background:#eff6ff;padding:1px 5px;border-radius:4px'>A</code></div>
        <div style='font-size:.7rem;color:#64748b;margin-top:4px'>位數越少，表示越簡潔！</div>
      </div>
    </div>
    <div>
      <div style='font-size:.78rem;font-weight:700;color:#1E3A5F;margin-bottom:8px'>顏色編碼實例</div>
      <div style='font-size:.78rem;line-height:1.8;background:#f8fafc;padding:10px;border-radius:8px;border:1px solid #e2e8f0'>
        <div style='display:flex;align-items:center;gap:8px;margin-bottom:6px'>
          <div style='width:20px;height:20px;background:#dc2626;border-radius:4px'></div>
          <span>重點紅 <code>#DC2626</code></span>
        </div>
        <div style='display:flex;align-items:center;gap:8px;margin-bottom:6px'>
          <div style='width:20px;height:20px;background:#0d9488;border-radius:4px'></div>
          <span>科技綠 <code>#0D9488</code></span>
        </div>
        <div style='display:flex;align-items:center;gap:8px'>
          <div style='width:20px;height:20px;background:#6b3fa0;border-radius:4px'></div>
          <span>AI 紫 <code>#6B3FA0</code></span>
        </div>
        <div style='font-size:.7rem;color:#64748b;margin-top:6px'>網頁色彩皆以十六進位表示</div>
      </div>
    </div>
  </div>
  <div class='tip-box'>
    🎯 <strong>重點</strong>：十六進位 #RRGGBB 每兩碼代表一個顏色通道（R/G/B），各自從 00（0）到 FF（255），共 1677 萬種組合。
  </div>
</div>"""
},

{
  'id': 11,
  'chapter': '第一章：數位語言基礎',
  'title': '選對格式，讓創作更有效率',
  'bg': 'white',
  'quiz': None, 'chart': 'formats', 'video': None,
  'html': """
<div class='slide-inner'>
  <h2 class='slide-title'>📁 選對格式，讓創作更有效率！</h2>
  <div class='card-grid-3' style='margin-bottom:12px'>
    <div style='background:#eff6ff;border:1px solid #bfdbfe;border-radius:12px;padding:14px;text-align:center'>
      <div style='font-size:1.5rem;margin-bottom:6px'>🖼️</div>
      <div style='font-weight:700;color:#1e40af;margin-bottom:6px'>JPEG / JPG</div>
      <div style='font-size:.75rem;color:#374151;line-height:1.5'>
        有損壓縮，檔案小<br>
        適合：<strong>照片、寫實圖</strong><br>
        ❌ 不支援透明背景<br>
        ❌ 多次儲存會失真
      </div>
    </div>
    <div style='background:#f0fdf4;border:1px solid #bbf7d0;border-radius:12px;padding:14px;text-align:center'>
      <div style='font-size:1.5rem;margin-bottom:6px'>🏞️</div>
      <div style='font-weight:700;color:#166534;margin-bottom:6px'>PNG</div>
      <div style='font-size:.75rem;color:#374151;line-height:1.5'>
        無損壓縮，品質高<br>
        適合：<strong>圖示、截圖、貼圖</strong><br>
        ✅ 支援透明背景<br>
        ❌ 檔案較大
      </div>
    </div>
    <div style='background:#faf5ff;border:1px solid #e9d5ff;border-radius:12px;padding:14px;text-align:center'>
      <div style='font-size:1.5rem;margin-bottom:6px'>✏️</div>
      <div style='font-weight:700;color:#6b21a8;margin-bottom:6px'>SVG</div>
      <div style='font-size:.75rem;color:#374151;line-height:1.5'>
        向量圖，數學公式<br>
        適合：<strong>Logo、圖示、插圖</strong><br>
        ✅ 無限縮放不失真<br>
        ✅ 檔案超小
      </div>
    </div>
  </div>
  <div style='height:160px'><canvas id='chart-formats'></canvas></div>
</div>"""
},

{
  'id': 12,
  'chapter': '第一章：數位語言基礎',
  'title': '互動提問：你會怎麼選擇？',
  'bg': 'teal',
  'quiz': 'q1', 'chart': None, 'video': None,
  'html': """
<div class='slide-inner'>
  <h2 class='slide-title' style='color:#fff'>💬 互動提問：你會怎麼選擇？</h2>
  <p style='color:rgba(255,255,255,.85);font-size:.88rem;margin-bottom:16px'>
    同一張圖片有三種格式可以選擇：JPG、PNG、SVG。<br>
    你會在什麼情況下選擇哪一種？
  </p>
  <div style='display:flex;flex-direction:column;gap:10px;margin-bottom:16px'>
    <div style='background:rgba(255,255,255,.15);border-radius:12px;padding:12px 16px;font-size:.85rem;color:#fff'>
      📸 <strong>情境 A</strong>：你拍了一張風景照，要放在社群媒體上分享，檔案越小越好。
      <div style='color:#fcd34d;font-size:.8rem;margin-top:4px'>👉 選 <strong>JPEG</strong>——照片有損壓縮，小檔傳輸快</div>
    </div>
    <div style='background:rgba(255,255,255,.15);border-radius:12px;padding:12px 16px;font-size:.85rem;color:#fff'>
      🎨 <strong>情境 B</strong>：你設計了一個 App 圖示，需要透明背景，放在各種顏色的底色上。
      <div style='color:#fcd34d;font-size:.8rem;margin-top:4px'>👉 選 <strong>PNG</strong>——無損壓縮，支援透明</div>
    </div>
    <div style='background:rgba(255,255,255,.15);border-radius:12px;padding:12px 16px;font-size:.85rem;color:#fff'>
      🏢 <strong>情境 C</strong>：你設計了公司 Logo，需要印在名片上，也要放網頁，大小都得清楚。
      <div style='color:#fcd34d;font-size:.8rem;margin-top:4px'>👉 選 <strong>SVG</strong>——向量圖，無限縮放不失真</div>
    </div>
  </div>
  <div style='background:rgba(255,255,255,.2);border-radius:10px;padding:10px 16px;font-size:.82rem;color:#fff;text-align:center'>
    ✋ 準備好了嗎？點「下一頁」進行第一章小測驗！
  </div>
</div>"""
},

{
  'id': 13,
  'chapter': '第一章：數位語言基礎',
  'title': '第一章總結',
  'bg': 'white',
  'quiz': None, 'chart': None, 'video': None,
  'html': """
<div class='slide-inner'>
  <h2 class='slide-title'>✅ 第一章重點整理</h2>
  <div style='display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:12px'>
    <div class='func-card' style='flex-direction:column;align-items:flex-start;gap:6px'>
      <div style='display:flex;align-items:center;gap:8px'><div class='fc-num'>1</div><div class='fc-title'>類比 vs 數位</div></div>
      <div class='fc-desc'>類比訊號連續，數位訊號為 0/1；ADC 取樣量化後儲存</div>
    </div>
    <div class='func-card' style='flex-direction:column;align-items:flex-start;gap:6px'>
      <div style='display:flex;align-items:center;gap:8px'><div class='fc-num'>2</div><div class='fc-title'>文字表示法</div></div>
      <div class='fc-desc'>ASCII 128 字元；Unicode/UTF-8 涵蓋全球語言與 Emoji</div>
    </div>
    <div class='func-card' style='flex-direction:column;align-items:flex-start;gap:6px'>
      <div style='display:flex;align-items:center;gap:8px'><div class='fc-num'>3</div><div class='fc-title'>位元與進位系統</div></div>
      <div class='fc-desc'>1 bit = 0 或 1；8 bits = 1 Byte；16 進位用於顏色碼</div>
    </div>
    <div class='func-card' style='flex-direction:column;align-items:flex-start;gap:6px'>
      <div style='display:flex;align-items:center;gap:8px'><div class='fc-num'>4</div><div class='fc-title'>像素與色彩深度</div></div>
      <div class='fc-desc'>像素是影像最小單位；24 bit True Color = 1,677 萬色</div>
    </div>
    <div class='func-card' style='flex-direction:column;align-items:flex-start;gap:6px'>
      <div style='display:flex;align-items:center;gap:8px'><div class='fc-num'>5</div><div class='fc-title'>聲音與視訊</div></div>
      <div class='fc-desc'>取樣率/深度決定音質；幀率決定影片流暢度</div>
    </div>
    <div class='func-card' style='flex-direction:column;align-items:flex-start;gap:6px'>
      <div style='display:flex;align-items:center;gap:8px'><div class='fc-num'>6</div><div class='fc-title'>檔案格式</div></div>
      <div class='fc-desc'>JPEG（照片）/ PNG（透明）/ SVG（向量）根據用途選擇</div>
    </div>
  </div>
  <div class='tip-box'>
    🔑 <strong>核心概念</strong>：電腦用最簡單的 0 與 1，透過不同的進位系統、編碼與格式，呈現文字、圖像、聲音、影片等豐富數位世界。
  </div>
</div>"""
},

# ──────────────────────────────────────────
#  第二章：AI 創作基礎
# ──────────────────────────────────────────
{
  'id': 14,
  'chapter': '第二章：AI 創作基礎',
  'title': '第二章導入：AI 如何生成圖片？',
  'bg': 'purple',
  'quiz': None, 'chart': None, 'video': None,
  'html': """
<div class='slide-inner'>
  <h2 class='slide-title' style='color:#fff'>🤖 第二章：AI 創作基礎</h2>
  <p class='slide-desc' style='color:rgba(255,255,255,.75)'>核心問題：「AI 如何從雜訊生成圖片？」</p>
  <div class='fact-box' style='margin-bottom:12px'>
    <p style='color:rgba(255,255,255,.85)'>
      在這一章，我們將探索人工智慧如何創作視覺內容——從隨機雜訊出發，逐步「還原」出清晰的圖像。
      這個過程背後，隱藏著數學與模型的魔法。
    </p>
  </div>
  <div class='card-grid-2'>
    <div class='info-card'>
      <div class='card-icon'>🖼️</div>
      <div class='card-label'>點陣圖 vs 向量圖</div>
      <div class='card-desc'>像素 vs 數學公式，放大後的差異</div>
    </div>
    <div class='info-card'>
      <div class='card-icon'>✨</div>
      <div class='card-label'>擴散模型原理</div>
      <div class='card-desc'>從雜訊還原圖像的核心技術</div>
    </div>
    <div class='info-card'>
      <div class='card-icon'>🧩</div>
      <div class='card-label'>三大核心元件</div>
      <div class='card-desc'>文字編碼器→擴散模型→解碼器</div>
    </div>
    <div class='info-card'>
      <div class='card-icon'>🛠️</div>
      <div class='card-label'>主流 AI 工具比較</div>
      <div class='card-desc'>ChatGPT / Canva / Midjourney / Firefly</div>
    </div>
  </div>
</div>"""
},

{
  'id': 15,
  'chapter': '第二章：AI 創作基礎',
  'title': '點陣圖 vs 向量圖',
  'bg': 'white',
  'quiz': None, 'chart': None,
  'video': {'type': 'search', 'query': '點陣圖 向量圖 差異比較 教學', 'title': '🎨 點陣圖 vs 向量圖動畫', 'desc': '搜尋點陣圖與向量圖比較影片'},
  'html': """
<div class='slide-inner'>
  <h2 class='slide-title'>🖼️ 數位影像的兩種基礎：點陣 vs 向量</h2>
  <div class='card-grid-2' style='margin-bottom:12px'>
    <div style='background:linear-gradient(135deg,#eff6ff,#dbeafe);border:1px solid #93c5fd;border-radius:14px;padding:16px'>
      <div style='font-size:1.4rem;margin-bottom:6px'>🔲</div>
      <div style='font-weight:700;color:#1e40af;font-size:.95rem;margin-bottom:8px'>點陣圖 (Bitmap / Raster)</div>
      <div style='font-size:.8rem;color:#1e3a8a;line-height:1.6'>
        由像素（Pixel）方格組成<br>
        照片細節豐富<br>
        ❌ 放大後產生鋸齒失真<br>
        常見格式：<strong>JPEG / PNG</strong>
      </div>
      <div style='margin-top:10px;background:#fff;border-radius:8px;padding:8px;text-align:center;font-size:.72rem;color:#64748b'>
        📸 適合：照片、截圖、數位繪圖
      </div>
    </div>
    <div style='background:linear-gradient(135deg,#faf5ff,#ede9fe);border:1px solid #c4b5fd;border-radius:14px;padding:16px'>
      <div style='font-size:1.4rem;margin-bottom:6px'>✏️</div>
      <div style='font-weight:700;color:#6b21a8;font-size:.95rem;margin-bottom:8px'>向量圖 (Vector)</div>
      <div style='font-size:.8rem;color:#581c87;line-height:1.6'>
        用數學公式記錄點、線、形狀<br>
        ✅ 無限縮放不失真<br>
        適合 Logo 與印刷<br>
        常見格式：<strong>SVG / AI</strong>
      </div>
      <div style='margin-top:10px;background:#fff;border-radius:8px;padding:8px;text-align:center;font-size:.72rem;color:#64748b'>
        🎨 適合：Logo、圖示、插圖
      </div>
    </div>
  </div>
  <div id='video-section-15' class='video-section'></div>
</div>"""
},

{
  'id': 16,
  'chapter': '第二章：AI 創作基礎',
  'title': 'AI 擴散模型原理',
  'bg': 'purple',
  'quiz': None, 'chart': None,
  'video': {'type': 'search', 'query': '擴散模型 Stable Diffusion 原理 教學 中文', 'title': '⚡ 擴散模型是如何運作的？', 'desc': '搜尋 Stable Diffusion 原理解說影片'},
  'html': """
<div class='slide-inner'>
  <h2 class='slide-title' style='color:#fff'>✨ AI 擴散模型原理</h2>
  <div style='display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:12px'>
    <div>
      <div style='font-size:.8rem;font-weight:700;color:rgba(255,255,255,.8);margin-bottom:8px'>📌 什麼是擴散模型？</div>
      <div class='fact-box' style='margin-bottom:0'>
        <p style='color:rgba(255,255,255,.85);font-size:.8rem;line-height:1.6'>
          擴散模型（Diffusion Model）是目前主流 AI 生成圖的核心技術。<br><br>
          訓練時：先將圖片<strong style='color:#fcd34d'>逐步加入雜訊</strong>直到完全模糊<br><br>
          生成時：從純雜訊出發，<strong style='color:#5eead4'>一步步去除雜訊</strong>，還原出圖片
        </p>
      </div>
    </div>
    <div>
      <div style='font-size:.8rem;font-weight:700;color:rgba(255,255,255,.8);margin-bottom:8px'>🔄 生成流程示意</div>
      <div style='display:flex;flex-direction:column;gap:6px'>
        <div style='background:rgba(239,68,68,.2);border:1px solid rgba(239,68,68,.4);border-radius:8px;padding:8px 12px;font-size:.78rem;color:#fca5a5'>
          🌪️ 起點：純隨機雜訊（noise）
        </div>
        <div style='text-align:center;color:rgba(255,255,255,.4);font-size:1rem'>↓ 去雜訊（t 步驟）</div>
        <div style='background:rgba(245,158,11,.15);border:1px solid rgba(245,158,11,.3);border-radius:8px;padding:8px 12px;font-size:.78rem;color:#fcd34d'>
          ⚙️ 中間：模糊但有輪廓的圖形
        </div>
        <div style='text-align:center;color:rgba(255,255,255,.4);font-size:1rem'>↓ 繼續去雜訊</div>
        <div style='background:rgba(13,148,136,.2);border:1px solid rgba(13,148,136,.4);border-radius:8px;padding:8px 12px;font-size:.78rem;color:#5eead4'>
          🖼️ 終點：清晰的生成圖
        </div>
      </div>
    </div>
  </div>
  <div id='video-section-16' class='video-section'></div>
</div>"""
},

{
  'id': 17,
  'chapter': '第二章：AI 創作基礎',
  'title': 'AI 生成圖三元件流程',
  'bg': 'white',
  'quiz': None, 'chart': None, 'video': None,
  'html': """
<div class='slide-inner'>
  <h2 class='slide-title'>🧩 生成圖三元件流程</h2>
  <p class='slide-desc'>三大核心元件：文字 → 圖片的完整流程</p>
  <div style='display:flex;align-items:center;gap:8px;margin-bottom:14px;flex-wrap:wrap'>
    <div style='flex:1;min-width:140px;background:linear-gradient(135deg,#eff6ff,#dbeafe);border:1px solid #93c5fd;border-radius:12px;padding:14px'>
      <div style='font-size:1.2rem;margin-bottom:6px'>① 📝</div>
      <div style='font-weight:700;color:#1e40af;margin-bottom:6px;font-size:.85rem'>文字編碼器</div>
      <div style='font-size:.75rem;color:#1e3a8a;line-height:1.5'>
        將輸入的文字（Prompt）轉換為<strong>數學向量</strong><br>
        讓 AI「理解」文字的語意與概念
      </div>
      <div style='margin-top:8px;font-size:.7rem;color:#3b82f6;background:#e0f2fe;padding:4px 8px;border-radius:6px'>
        例：「一隻在海邊的柴犬」→ [0.3, -0.7, 1.2, ...]
      </div>
    </div>
    <div style='font-size:1.5rem;color:#6B3FA0;font-weight:700'>→</div>
    <div style='flex:1;min-width:140px;background:linear-gradient(135deg,#faf5ff,#ede9fe);border:1px solid #c4b5fd;border-radius:12px;padding:14px'>
      <div style='font-size:1.2rem;margin-bottom:6px'>② ⚡</div>
      <div style='font-weight:700;color:#6b21a8;margin-bottom:6px;font-size:.85rem'>擴散模型</div>
      <div style='font-size:.75rem;color:#581c87;line-height:1.5'>
        接收向量，逐步將雜訊<strong>還原為圖像</strong><br>
        核心運算引擎，決定圖片內容與風格
      </div>
      <div style='margin-top:8px;font-size:.7rem;color:#9333ea;background:#fdf4ff;padding:4px 8px;border-radius:6px'>
        經過數十～數百步去雜訊計算
      </div>
    </div>
    <div style='font-size:1.5rem;color:#6B3FA0;font-weight:700'>→</div>
    <div style='flex:1;min-width:140px;background:linear-gradient(135deg,#f0fdf4,#dcfce7);border:1px solid #86efac;border-radius:12px;padding:14px'>
      <div style='font-size:1.2rem;margin-bottom:6px'>③ 🖼️</div>
      <div style='font-weight:700;color:#166534;margin-bottom:6px;font-size:.85rem'>解碼器</div>
      <div style='font-size:.75rem;color:#14532d;line-height:1.5'>
        將壓縮的潛在空間數據<strong>還原為像素圖片</strong><br>
        輸出最終可視化的高解析度圖像
      </div>
      <div style='margin-top:8px;font-size:.7rem;color:#16a34a;background:#dcfce7;padding:4px 8px;border-radius:6px'>
        輸出：1024×1024 px 圖片
      </div>
    </div>
  </div>
  <div style='background:#f8fafc;border-radius:10px;padding:10px 16px;font-size:.82rem;text-align:center;color:#374151;border:1px solid #e2e8f0'>
    流程：<strong>Prompt 文字</strong> → 編碼 → 去雜訊 → 解碼 → <strong>🖼️ 生成圖片</strong>
  </div>
</div>"""
},

{
  'id': 18,
  'chapter': '第二章：AI 創作基礎',
  'title': 'AI 模型作品比較',
  'bg': 'white',
  'quiz': None, 'chart': None, 'video': None,
  'html': """
<div class='slide-inner'>
  <h2 class='slide-title'>🏆 主流 AI 模型作品比較</h2>
  <div class='card-grid-2' style='margin-bottom:12px'>
    <div style='background:linear-gradient(135deg,#f0fdf4,#dcfce7);border:1px solid #86efac;border-radius:12px;padding:14px'>
      <div style='display:flex;align-items:center;gap:8px;margin-bottom:8px'>
        <span style='font-size:1.2rem'>🟢</span>
        <strong style='color:#166534'>ChatGPT / GPT-4o 圖像生成</strong>
      </div>
      <div style='font-size:.78rem;color:#374151;line-height:1.7'>
        ✦ GPT-4o 整合，文字理解強，圖像高品質<br>
        ✦ 支援對話式修改與多輪生成<br>
        ✦ 免費版可用，Plus 版功能更完整<br>
        △ 商業使用需確認授權條款
      </div>
    </div>
    <div style='background:linear-gradient(135deg,#eff6ff,#dbeafe);border:1px solid #93c5fd;border-radius:12px;padding:14px'>
      <div style='display:flex;align-items:center;gap:8px;margin-bottom:8px'>
        <span style='font-size:1.2rem'>🔵</span>
        <strong style='color:#1e40af'>Canva AI</strong>
      </div>
      <div style='font-size:.78rem;color:#374151;line-height:1.7'>
        ✦ 介面直覺，整合設計工具<br>
        ✦ 適合初學者與簡報製作<br>
        ✦ 一鍵套用設計模板<br>
        △ AI 生成自由度較低
      </div>
    </div>
    <div style='background:linear-gradient(135deg,#fdf4ff,#fae8ff);border:1px solid #e879f9;border-radius:12px;padding:14px'>
      <div style='display:flex;align-items:center;gap:8px;margin-bottom:8px'>
        <span style='font-size:1.2rem'>🟣</span>
        <strong style='color:#86198f'>Midjourney</strong>
      </div>
      <div style='font-size:.78rem;color:#374151;line-height:1.7'>
        ✦ 圖像品質最高，藝術風格多元<br>
        ✦ 適合藝術創作與設計<br>
        ✦ 已推出獨立網頁平台（midjourney.com）<br>
        △ 付費訂閱制，無免費版
      </div>
    </div>
    <div style='background:linear-gradient(135deg,#fff7ed,#ffedd5);border:1px solid #fdba74;border-radius:12px;padding:14px'>
      <div style='display:flex;align-items:center;gap:8px;margin-bottom:8px'>
        <span style='font-size:1.2rem'>🟠</span>
        <strong style='color:#9a3412'>Adobe Firefly</strong>
      </div>
      <div style='font-size:.78rem;color:#374151;line-height:1.7'>
        ✦ 商業授權安全<br>
        ✦ 整合 Photoshop/Illustrator<br>
        ✦ 訓練資料來源合法<br>
        ✦ 適合專業設計用途
      </div>
    </div>
  </div>
  <div class='tip-box'>🔑 <strong>選擇工具三要素</strong>：用途需求 × 授權安全性 × 操作難易度</div>
</div>"""
},

{
  'id': 19,
  'chapter': '第二章：AI 創作基礎',
  'title': 'AI 工具比較表',
  'bg': 'white',
  'quiz': None, 'chart': 'ai_tools', 'video': None,
  'html': """
<div class='slide-inner'>
  <h2 class='slide-title'>📊 AI 工具比較表</h2>
  <div class='platform-table' style='margin-bottom:12px'>
    <div class='pt-header' style='grid-template-columns:1.2fr 1fr 1fr 1fr 1fr'>
      <span>工具</span><span>圖像品質</span><span>操作難易</span><span>授權安全</span><span>費用</span>
    </div>
    <div class='pt-row' style='grid-template-columns:1.2fr 1fr 1fr 1fr 1fr'>
      <span class='pt-name'>ChatGPT GPT-4o</span>
      <span>⭐⭐⭐⭐⭐</span><span>⭐⭐⭐⭐⭐</span><span>⭐⭐⭐</span><span>免費+訂閱</span>
    </div>
    <div class='pt-row' style='grid-template-columns:1.2fr 1fr 1fr 1fr 1fr;background:#f8fafc'>
      <span class='pt-name'>Canva AI</span>
      <span>⭐⭐⭐</span><span>⭐⭐⭐⭐⭐</span><span>⭐⭐⭐⭐</span><span>免費+訂閱</span>
    </div>
    <div class='pt-row' style='grid-template-columns:1.2fr 1fr 1fr 1fr 1fr'>
      <span class='pt-name'>Midjourney</span>
      <span>⭐⭐⭐⭐⭐</span><span>⭐⭐</span><span>⭐⭐⭐</span><span>付費</span>
    </div>
    <div class='pt-row' style='grid-template-columns:1.2fr 1fr 1fr 1fr 1fr;background:#f8fafc'>
      <span class='pt-name'>Adobe Firefly</span>
      <span>⭐⭐⭐⭐</span><span>⭐⭐⭐⭐</span><span>⭐⭐⭐⭐⭐</span><span>訂閱制</span>
    </div>
  </div>
  <div style='height:140px'><canvas id='chart-ai-tools'></canvas></div>
</div>"""
},

{
  'id': 20,
  'chapter': '第二章：AI 創作基礎',
  'title': 'AI 幻覺現象',
  'bg': 'white',
  'quiz': None, 'chart': None, 'video': None,
  'html': """
<div class='slide-inner'>
  <h2 class='slide-title'>⚠️ AI 幻覺（Hallucination）現象</h2>
  <div class='card-grid-3' style='margin-bottom:12px'>
    <div style='background:#fef2f2;border:1px solid #fca5a5;border-radius:12px;padding:12px;text-align:center'>
      <div style='font-size:1.4rem;margin-bottom:6px'>✋</div>
      <div style='font-weight:700;color:#991b1b;font-size:.82rem;margin-bottom:6px'>常見錯誤示例</div>
      <div style='font-size:.75rem;color:#7f1d1d;line-height:1.5'>
        • 六根手指<br>
        • 扭曲五官<br>
        • 文字亂碼<br>
        • 不合邏輯的背景細節
      </div>
    </div>
    <div style='background:#fffbeb;border:1px solid #fcd34d;border-radius:12px;padding:12px;text-align:center'>
      <div style='font-size:1.4rem;margin-bottom:6px'>🔍</div>
      <div style='font-weight:700;color:#92400e;font-size:.82rem;margin-bottom:6px'>如何辨識</div>
      <div style='font-size:.75rem;color:#78350f;line-height:1.5'>
        • 仔細數人物手指數量<br>
        • 檢查五官對稱性<br>
        • 確認文字是否可讀<br>
        • 物體結構是否合理
      </div>
    </div>
    <div style='background:#f0fdf4;border:1px solid #86efac;border-radius:12px;padding:12px;text-align:center'>
      <div style='font-size:1.4rem;margin-bottom:6px'>✅</div>
      <div style='font-weight:700;color:#166534;font-size:.82rem;margin-bottom:6px'>避免誤用原則</div>
      <div style='font-size:.75rem;color:#14532d;line-height:1.5'>
        • 必須標示 AI 生成來源<br>
        • 不可當作真實照片<br>
        • 不能作為事實依據<br>
        • 使用前仔細核查
      </div>
    </div>
  </div>
  <div style='background:#fef2f2;border:1px solid #fca5a5;border-radius:10px;padding:12px 16px;font-size:.82rem;color:#7f1d1d;line-height:1.5'>
    ⚡ <strong>為什麼會幻覺？</strong> AI 是統計模型，它「預測」最可能的下一個像素，而不是真的理解現實世界的物理法則。因此在複雜細節上容易出錯。
  </div>
</div>"""
},

{
  'id': 21,
  'chapter': '第二章：AI 創作基礎',
  'title': 'AI Agent 介紹',
  'bg': 'purple',
  'quiz': None, 'chart': None,
  'video': {'type': 'search', 'query': 'AI Agent 自主 AI 是什麼 教學 中文', 'title': '🤖 AI Agent 是什麼？自主 AI 如何工作？', 'desc': '搜尋 AI Agent 介紹影片'},
  'html': """
<div class='slide-inner'>
  <h2 class='slide-title' style='color:#fff'>🤖 AI Agent 介紹</h2>
  <div style='display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:10px'>
    <div>
      <div style='font-size:.78rem;font-weight:700;color:rgba(255,255,255,.8);margin-bottom:6px'>傳統 AI vs AI Agent</div>
      <div style='background:rgba(255,255,255,.08);border-radius:10px;padding:10px 12px;font-size:.78rem;color:rgba(255,255,255,.8);line-height:1.7'>
        <div style='color:#fca5a5'>❌ 傳統 AI：單一輸入 → 單一輸出，無法自主規劃</div>
        <div style='margin-top:8px;color:#86efac'>✅ AI Agent：能感知環境、制定計畫、使用工具、<strong style='color:#fcd34d'>自主執行任務</strong></div>
      </div>
    </div>
    <div>
      <div style='font-size:.78rem;font-weight:700;color:rgba(255,255,255,.8);margin-bottom:6px'>核心運作流程</div>
      <div style='display:flex;flex-direction:column;gap:4px'>
        <div style='background:rgba(255,255,255,.1);border-radius:7px;padding:6px 10px;font-size:.75rem;color:#fff'>👁️ 感知（Perceive）：觀察環境與任務</div>
        <div style='background:rgba(255,255,255,.1);border-radius:7px;padding:6px 10px;font-size:.75rem;color:#fff'>📋 計畫（Plan）：規劃解決步驟</div>
        <div style='background:rgba(255,255,255,.1);border-radius:7px;padding:6px 10px;font-size:.75rem;color:#fff'>🔧 工具使用（Tool Use）：搜尋、執行程式</div>
        <div style='background:rgba(255,255,255,.1);border-radius:7px;padding:6px 10px;font-size:.75rem;color:#fff'>⚡ 執行（Act）：完成任務</div>
        <div style='background:rgba(255,255,255,.1);border-radius:7px;padding:6px 10px;font-size:.75rem;color:#fff'>📊 回報（Report）：回傳結果</div>
      </div>
    </div>
  </div>
  <div id='video-section-21' class='video-section'></div>
</div>"""
},

{
  'id': 22,
  'chapter': '第二章：AI 創作基礎',
  'title': 'AI 正在改變哪些職業？',
  'bg': 'white',
  'quiz': None, 'chart': None, 'video': None,
  'html': """
<div class='slide-inner'>
  <h2 class='slide-title'>💼 AI 正在改變哪些職業？</h2>
  <div style='display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:12px'>
    <div>
      <div style='font-size:.8rem;font-weight:700;color:#dc2626;margin-bottom:8px;padding-bottom:6px;border-bottom:2px solid #fca5a5'>⚡ 高度受衝擊的工作</div>
      <div style='display:flex;flex-direction:column;gap:6px'>
        <div style='background:#fef2f2;border-radius:8px;padding:8px 10px;font-size:.75rem;color:#7f1d1d'>
          📝 <strong>文字處理</strong>：新聞摘要、基礎翻譯、客服對話
        </div>
        <div style='background:#fef2f2;border-radius:8px;padding:8px 10px;font-size:.75rem;color:#7f1d1d'>
          🎨 <strong>視覺設計</strong>：基礎圖片生成、排版輔助
        </div>
        <div style='background:#fef2f2;border-radius:8px;padding:8px 10px;font-size:.75rem;color:#7f1d1d'>
          💻 <strong>程式開發</strong>：Copilot 等工具協助撰碼，初階工程師需轉型
        </div>
        <div style='background:#fef2f2;border-radius:8px;padding:8px 10px;font-size:.75rem;color:#7f1d1d'>
          🏥 <strong>醫療影像</strong>：AI 輔助 X 光、病理切片診斷
        </div>
      </div>
    </div>
    <div>
      <div style='font-size:.8rem;font-weight:700;color:#0d9488;margin-bottom:8px;padding-bottom:6px;border-bottom:2px solid #5eead4'>🚀 高中生應具備的能力</div>
      <div style='display:flex;flex-direction:column;gap:6px'>
        <div style='background:#f0fdfa;border-radius:8px;padding:8px 10px;font-size:.75rem;color:#134e4a'>
          🎯 <strong>提示工程</strong>：精準指揮 AI 工具產出所需結果
        </div>
        <div style='background:#f0fdfa;border-radius:8px;padding:8px 10px;font-size:.75rem;color:#134e4a'>
          🧠 <strong>批判性思維</strong>：辨識 AI 幻覺與錯誤資訊
        </div>
        <div style='background:#f0fdfa;border-radius:8px;padding:8px 10px;font-size:.75rem;color:#134e4a'>
          🔗 <strong>跨域整合能力</strong>：結合領域知識與 AI 工具
        </div>
        <div style='background:#f0fdfa;border-radius:8px;padding:8px 10px;font-size:.75rem;color:#134e4a'>
          ⚖️ <strong>數位倫理意識</strong>：了解著作權、隱私與 AI 使用的責任邊界
        </div>
      </div>
    </div>
  </div>
  <div style='background:#1e3a5f;border-radius:10px;padding:10px 16px;font-size:.85rem;color:#fff;text-align:center;font-weight:700'>
    未來競爭力 = 專業知識 + AI 協作能力 + 人文素養
  </div>
</div>"""
},

{
  'id': 23,
  'chapter': '第二章：AI 創作基礎',
  'title': 'AI 輔助 vs AI 代工',
  'bg': 'white',
  'quiz': 'q2', 'chart': None, 'video': None,
  'html': """
<div class='slide-inner'>
  <h2 class='slide-title'>🤔 AI 輔助 vs AI 代工</h2>
  <div class='card-grid-2' style='margin-bottom:12px'>
    <div style='background:linear-gradient(135deg,#f0fdf4,#dcfce7);border:1px solid #86efac;border-radius:14px;padding:16px'>
      <div style='display:flex;align-items:center;gap:8px;margin-bottom:10px'>
        <span style='font-size:1.3rem'>✅</span>
        <span style='font-weight:700;color:#166534;font-size:.95rem'>AI 輔助（推薦）</span>
      </div>
      <div style='font-size:.8rem;color:#14532d;line-height:1.7;margin-bottom:10px'>
        作為創作工具，由人主導創作方向與決策。創作者使用 AI 加速流程、激發靈感，但最終作品融入個人思考與判斷。
      </div>
      <div style='background:#f0fdf4;border-radius:8px;padding:8px 10px;font-size:.75rem;color:#15803d'>
        <strong>例：</strong>用 AI 生成草圖後自行修改；用 AI 翻譯後校對潤稿
      </div>
    </div>
    <div style='background:linear-gradient(135deg,#fef2f2,#fee2e2);border:1px solid #fca5a5;border-radius:14px;padding:16px'>
      <div style='display:flex;align-items:center;gap:8px;margin-bottom:10px'>
        <span style='font-size:1.3rem'>⚠️</span>
        <span style='font-weight:700;color:#991b1b;font-size:.95rem'>AI 代工（需謹慎）</span>
      </div>
      <div style='font-size:.8rem;color:#7f1d1d;line-height:1.7;margin-bottom:10px'>
        完全取代人的創作過程，直接繳交 AI 生成內容為自己作品。缺乏個人思考投入，可能違反學術誠信。
      </div>
      <div style='background:#fef2f2;border-radius:8px;padding:8px 10px;font-size:.75rem;color:#b91c1c'>
        <strong>例：</strong>直接將 AI 生成圖或文章原文繳交，未加以修改或標示
      </div>
    </div>
  </div>
  <div class='tip-box'>
    🔑 <strong>核心原則</strong>：AI 是工具，創作者是你。你的想法和判斷才是作品的靈魂。<br>
    ✋ 點「下一頁」進行第二章測驗！
  </div>
</div>"""
},

{
  'id': 24,
  'chapter': '第二章：AI 創作基礎',
  'title': '第二章總結',
  'bg': 'purple',
  'quiz': None, 'chart': None, 'video': None,
  'html': """
<div class='slide-inner'>
  <h2 class='slide-title' style='color:#fff'>✅ 第二章重點整理</h2>
  <div style='display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:12px'>
    <div class='info-card'>
      <div class='card-icon'>🔲</div>
      <div class='card-label'>點陣 vs 向量</div>
      <div class='card-desc'>像素組成（JPEG/PNG）vs 數學公式（SVG），各有適用場景</div>
    </div>
    <div class='info-card'>
      <div class='card-icon'>✨</div>
      <div class='card-label'>擴散模型</div>
      <div class='card-desc'>雜訊→圖像，學習「去雜訊」的過程，是 AI 生成圖的核心</div>
    </div>
    <div class='info-card'>
      <div class='card-icon'>🧩</div>
      <div class='card-label'>三元件流程</div>
      <div class='card-desc'>文字編碼器→擴散模型→解碼器，Prompt→圖片的完整鏈</div>
    </div>
    <div class='info-card'>
      <div class='card-icon'>⚖️</div>
      <div class='card-label'>AI 輔助原則</div>
      <div class='card-desc'>AI 是工具，創作責任在人；輔助 ✅ vs 代工 ⚠️</div>
    </div>
  </div>
  <div class='tip-box' style='background:rgba(255,255,255,.12);border-color:rgba(255,255,255,.25);color:#fff'>
    🚀 <strong>下一章</strong>：我們將探討「創作責任」——使用 AI 和他人作品時，法律與道德的邊界在哪裡？
  </div>
</div>"""
},

# ──────────────────────────────────────────
#  第三章：創作責任
# ──────────────────────────────────────────
{
  'id': 25,
  'chapter': '第三章：創作責任',
  'title': '第三章導入：創作的責任是什麼？',
  'bg': 'navy',
  'quiz': None, 'chart': None, 'video': None,
  'html': """
<div class='slide-inner'>
  <h2 class='slide-title' style='color:#fff'>⚖️ 第三章：創作責任</h2>
  <p class='slide-desc' style='color:rgba(255,255,255,.75)'>💬 「我能用 AI 生成圖交作業嗎？」</p>
  <div class='fact-box' style='margin-bottom:12px'>
    <p style='color:rgba(255,255,255,.85)'>
      當 AI 工具越來越強大，我們每個人都可以輕鬆生成圖片、文字、音樂。但這也帶來了新的問題——<strong style='color:#F59E0B'>創作的責任是什麼？</strong>
    </p>
  </div>
  <div class='card-grid-2'>
    <div class='info-card'>
      <div class='card-icon'>📋</div>
      <div class='card-label'>著作權與創用 CC</div>
      <div class='card-desc'>六種授權組合，從最開放到最嚴格</div>
    </div>
    <div class='info-card'>
      <div class='card-icon'>📌</div>
      <div class='card-label'>合理引用四原則</div>
      <div class='card-desc'>Purpose / Nature / Amount / Market</div>
    </div>
    <div class='info-card'>
      <div class='card-icon'>🏛️</div>
      <div class='card-label'>AI 生成圖法律地位</div>
      <div class='card-desc'>台灣、美國立場與全球爭議</div>
    </div>
    <div class='info-card'>
      <div class='card-icon'>🎓</div>
      <div class='card-label'>學術誠信</div>
      <div class='card-desc'>誠實、透明、尊重的三原則</div>
    </div>
  </div>
  <div class='tip-box' style='margin-top:10px'>
    💡 <strong>能力越強，責任越大</strong>——成為數位創作者，不只是學會工具，更要學會負責任地使用它。
  </div>
</div>"""
},


{
  'id': 26,
  'chapter': '第三章：創作責任',
  'title': '智慧財產權三大分類',
  'bg': 'white',
  'quiz': None, 'chart': None, 'video': None,
  'html': """
<div class='slide-inner'>
  <h2 class='slide-title'>⚖️ 智慧財產權三大分類</h2>
  <p class='slide-desc'>保護人類智慧創作成果的法律制度</p>
  <div class='card-grid-3' style='margin-bottom:12px'>
    <div style='background:linear-gradient(135deg,#eff6ff,#dbeafe);border:1px solid #93c5fd;border-radius:14px;padding:14px;text-align:center'>
      <div style='font-size:1.8rem;margin-bottom:6px'>™</div>
      <div style='font-weight:700;color:#1e40af;font-size:.88rem;margin-bottom:8px'>商標權</div>
      <div style='font-size:.73rem;color:#1e3a8a;line-height:1.7;text-align:left'>
        保護品牌識別符號：<br>文字、圖形、顏色組合<br><br>
        ✦ 需向智財局<strong>申請註冊</strong><br>
        ✦ 保護期 10 年，<strong>可無限展延</strong><br>
        ✦ 例：可口可樂標誌、Nike
      </div>
    </div>
    <div style='background:linear-gradient(135deg,#faf5ff,#ede9fe);border:1px solid #c4b5fd;border-radius:14px;padding:14px;text-align:center'>
      <div style='font-size:1.8rem;margin-bottom:6px'>©</div>
      <div style='font-weight:700;color:#7c3aed;font-size:.88rem;margin-bottom:8px'>著作權</div>
      <div style='font-size:.73rem;color:#581c87;line-height:1.7;text-align:left'>
        保護創作表達：<br>文字、音樂、美術、程式<br><br>
        ✦ <strong>創作完成即自動取得</strong><br>
        ✦ 保護至作者死後 <strong>50 年</strong><br>
        ✦ 例：歌曲、小說、電影
      </div>
    </div>
    <div style='background:linear-gradient(135deg,#fff7ed,#ffedd5);border:1px solid #fdba74;border-radius:14px;padding:14px;text-align:center'>
      <div style='font-size:1.8rem;margin-bottom:6px'>®</div>
      <div style='font-weight:700;color:#9a3412;font-size:.88rem;margin-bottom:8px'>專利權</div>
      <div style='font-size:.73rem;color:#7c2d12;line-height:1.7;text-align:left'>
        保護技術發明與創新方法<br><br>
        ✦ 需向智財局<strong>申請審查</strong><br>
        ✦ 發明專利保護 <strong>20 年</strong><br>
        ✦ 例：iPhone 觸控技術、疫苗製程
      </div>
    </div>
  </div>
  <div class='tip-box'>
    💡 <strong>數位創作者最需注意著作權</strong>：使用他人音樂、圖片、程式碼都需確認授權！商標影響品牌識別，專利影響技術使用。
  </div>
</div>"""
},


{
  'id': 27,
  'chapter': '第三章：創作責任',
  'title': '著作權的兩大分支',
  'bg': 'white',
  'quiz': None, 'chart': None, 'video': None,
  'html': """
<div class='slide-inner'>
  <h2 class='slide-title'>© 著作權的兩大分支</h2>
  <div class='card-grid-2' style='margin-bottom:12px'>
    <div style='background:linear-gradient(135deg,#faf5ff,#ede9fe);border:1px solid #c4b5fd;border-radius:14px;padding:16px'>
      <div style='display:flex;align-items:center;gap:8px;margin-bottom:10px'>
        <div style='width:36px;height:36px;border-radius:50%;background:#7c3aed;color:#fff;display:flex;align-items:center;justify-content:center;font-size:.8rem;font-weight:700;flex-shrink:0'>人格</div>
        <div style='font-weight:700;color:#7c3aed;font-size:.9rem'>著作人格權</div>
      </div>
      <div style='font-size:.75rem;color:#581c87;line-height:1.6;margin-bottom:10px'>
        保護作者與作品的精神連結<br>
        <strong>不可讓與或轉移，永久存在</strong>
      </div>
      <div style='display:flex;flex-direction:column;gap:6px'>
        <div style='background:#faf5ff;border-radius:8px;padding:8px 10px;font-size:.75rem;color:#6b21a8'>
          📢 <strong>公開發表權</strong>：決定是否、何時公開作品
        </div>
        <div style='background:#faf5ff;border-radius:8px;padding:8px 10px;font-size:.75rem;color:#6b21a8'>
          🏷️ <strong>姓名表示權</strong>：決定是否標示真名或筆名
        </div>
        <div style='background:#faf5ff;border-radius:8px;padding:8px 10px;font-size:.75rem;color:#6b21a8'>
          🛡️ <strong>禁止不當改作</strong>：保護作品完整不被扭曲
        </div>
      </div>
    </div>
    <div style='background:linear-gradient(135deg,#eff6ff,#dbeafe);border:1px solid #93c5fd;border-radius:14px;padding:16px'>
      <div style='display:flex;align-items:center;gap:8px;margin-bottom:10px'>
        <div style='width:36px;height:36px;border-radius:50%;background:#1e40af;color:#fff;display:flex;align-items:center;justify-content:center;font-size:.8rem;font-weight:700;flex-shrink:0'>財產</div>
        <div style='font-weight:700;color:#1e40af;font-size:.9rem'>著作財產權</div>
      </div>
      <div style='font-size:.75rem;color:#1e3a8a;line-height:1.6;margin-bottom:10px'>
        保護作品的經濟利益<br>
        <strong>可授權、轉讓、繼承</strong>
      </div>
      <div style='display:flex;flex-direction:column;gap:6px'>
        <div style='background:#eff6ff;border-radius:8px;padding:8px 10px;font-size:.75rem;color:#1e40af'>
          🖨️ <strong>重製權</strong>：複製、印刷
        </div>
        <div style='background:#eff6ff;border-radius:8px;padding:8px 10px;font-size:.75rem;color:#1e40af'>
          📡 <strong>公開傳輸權</strong>：網路分享、串流
        </div>
        <div style='background:#eff6ff;border-radius:8px;padding:8px 10px;font-size:.75rem;color:#1e40af'>
          ✏️ <strong>改作權</strong>：翻譯、改編、二創
        </div>
        <div style='background:#eff6ff;border-radius:8px;padding:8px 10px;font-size:.75rem;color:#1e40af'>
          📦 <strong>散布權</strong>：出版、銷售
        </div>
      </div>
    </div>
  </div>
  <div class='tip-box'>
    ⏱️ <strong>著作財產權期限</strong>：作者終身 + 死後 50 年，期滿進入公眾領域，任何人可自由使用。<br>
    例：貝多芬的音樂、莎士比亞的劇本已可自由改編。
  </div>
</div>"""
},


{
  'id': 28,
  'chapter': '第三章：創作責任',
  'title': '創用 CC 授權介紹（一）',
  'bg': 'white',
  'quiz': None, 'chart': None,
  'video': {'type': 'search', 'query': '創用 CC 授權 詳細 說明 教學 中文', 'title': '📋 創用 CC 授權詳細說明', 'desc': '搜尋 Creative Commons 授權教學影片'},
  'html': """
<div class='slide-inner'>
  <h2 class='slide-title'>📋 創用 CC 授權介紹（一）：四大符號</h2>
  <p class='slide-desc'>Creative Commons 讓創作者可以彈性分享作品，共有四個核心符號：</p>
  <div class='card-grid-2' style='margin-bottom:12px'>
    <div style='background:#eff6ff;border:1px solid #93c5fd;border-radius:12px;padding:14px'>
      <div style='display:flex;align-items:center;gap:10px;margin-bottom:8px'>
        <div style='width:36px;height:36px;border-radius:50%;background:#1e40af;color:#fff;display:flex;align-items:center;justify-content:center;font-size:1rem;font-weight:700;flex-shrink:0'>BY</div>
        <div>
          <div style='font-weight:700;color:#1e40af;font-size:.88rem'>姓名標示（Attribution）</div>
        </div>
      </div>
      <div style='font-size:.78rem;color:#1e3a8a;line-height:1.5'>
        必須標明原作者姓名<br>使用時需保留來源資訊
      </div>
    </div>
    <div style='background:#faf5ff;border:1px solid #c4b5fd;border-radius:12px;padding:14px'>
      <div style='display:flex;align-items:center;gap:10px;margin-bottom:8px'>
        <div style='width:36px;height:36px;border-radius:50%;background:#7c3aed;color:#fff;display:flex;align-items:center;justify-content:center;font-size:.8rem;font-weight:700;flex-shrink:0'>ND</div>
        <div>
          <div style='font-weight:700;color:#7c3aed;font-size:.88rem'>禁止改作（No Derivatives）</div>
        </div>
      </div>
      <div style='font-size:.78rem;color:#581c87;line-height:1.5'>
        不得修改、改編原作品<br>只能原樣轉載使用
      </div>
    </div>
    <div style='background:#fff7ed;border:1px solid #fdba74;border-radius:12px;padding:14px'>
      <div style='display:flex;align-items:center;gap:10px;margin-bottom:8px'>
        <div style='width:36px;height:36px;border-radius:50%;background:#ea580c;color:#fff;display:flex;align-items:center;justify-content:center;font-size:.8rem;font-weight:700;flex-shrink:0'>NC</div>
        <div>
          <div style='font-weight:700;color:#ea580c;font-size:.88rem'>非商業性（Non-Commercial）</div>
        </div>
      </div>
      <div style='font-size:.78rem;color:#9a3412;line-height:1.5'>
        僅限非營利目的使用<br>不可用於商業販售或獲利
      </div>
    </div>
    <div style='background:#f0fdf4;border:1px solid #86efac;border-radius:12px;padding:14px'>
      <div style='display:flex;align-items:center;gap:10px;margin-bottom:8px'>
        <div style='width:36px;height:36px;border-radius:50%;background:#16a34a;color:#fff;display:flex;align-items:center;justify-content:center;font-size:.8rem;font-weight:700;flex-shrink:0'>SA</div>
        <div>
          <div style='font-weight:700;color:#16a34a;font-size:.88rem'>相同方式分享（Share-Alike）</div>
        </div>
      </div>
      <div style='font-size:.78rem;color:#14532d;line-height:1.5'>
        衍生作品須採相同授權<br>保障開放共享精神
      </div>
    </div>
  </div>
  <div id='video-section-28' class='video-section'></div>
</div>"""
},

{
  'id': 29,
  'chapter': '第三章：創作責任',
  'title': '創用 CC 授權介紹（二）',
  'bg': 'white',
  'quiz': None, 'chart': None, 'video': None,
  'html': """
<div class='slide-inner'>
  <h2 class='slide-title'>📋 創用 CC 授權介紹（二）：授權光譜</h2>
  <p class='slide-desc'>從最開放到最嚴格的授權組合</p>
  <div style='display:flex;flex-direction:column;gap:6px;margin-bottom:12px'>
    <div style='background:#f0fdf4;border:1px solid #86efac;border-radius:10px;padding:10px 14px;display:flex;align-items:center;gap:12px'>
      <div style='font-size:.72rem;font-weight:700;color:#166534;min-width:80px'>CC0（公眾領域）</div>
      <div style='flex:1;height:6px;border-radius:3px;background:linear-gradient(90deg,#22c55e,#f3f4f6);position:relative'>
        <div style='position:absolute;left:0%;top:50%;transform:translateY(-50%);width:14px;height:14px;border-radius:50%;background:#22c55e;border:2px solid #fff;box-shadow:0 0 0 2px #22c55e'></div>
      </div>
      <div style='font-size:.75rem;color:#15803d;min-width:120px'>完全放棄著作權，任何人可自由使用</div>
    </div>
    <div style='background:#eff6ff;border:1px solid #93c5fd;border-radius:10px;padding:10px 14px;display:flex;align-items:center;gap:12px'>
      <div style='font-size:.72rem;font-weight:700;color:#1e40af;min-width:80px'>CC BY</div>
      <div style='flex:1;height:6px;border-radius:3px;background:linear-gradient(90deg,#f3f4f6,#3b82f6,#f3f4f6)'></div>
      <div style='font-size:.75rem;color:#1e40af;min-width:120px'>最寬鬆，僅需標示作者</div>
    </div>
    <div style='background:#faf5ff;border:1px solid #c4b5fd;border-radius:10px;padding:10px 14px;display:flex;align-items:center;gap:12px'>
      <div style='font-size:.72rem;font-weight:700;color:#7c3aed;min-width:80px'>CC BY-SA</div>
      <div style='flex:1;height:6px;border-radius:3px;background:#a78bfa'></div>
      <div style='font-size:.75rem;color:#7c3aed;min-width:120px'>需標示，衍生須同授權</div>
    </div>
    <div style='background:#fff7ed;border:1px solid #fdba74;border-radius:10px;padding:10px 14px;display:flex;align-items:center;gap:12px'>
      <div style='font-size:.72rem;font-weight:700;color:#ea580c;min-width:80px'>CC BY-NC</div>
      <div style='flex:1;height:6px;border-radius:3px;background:#fb923c'></div>
      <div style='font-size:.75rem;color:#ea580c;min-width:120px'>需標示，禁止商業用途</div>
    </div>
    <div style='background:#fef2f2;border:1px solid #fca5a5;border-radius:10px;padding:10px 14px;display:flex;align-items:center;gap:12px'>
      <div style='font-size:.72rem;font-weight:700;color:#b91c1c;min-width:80px'>CC BY-ND</div>
      <div style='flex:1;height:6px;border-radius:3px;background:#f87171'></div>
      <div style='font-size:.75rem;color:#b91c1c;min-width:120px'>需標示，禁止改作</div>
    </div>
    <div style='background:#fff1f2;border:2px solid #f43f5e;border-radius:10px;padding:10px 14px;display:flex;align-items:center;gap:12px'>
      <div style='font-size:.72rem;font-weight:700;color:#be123c;min-width:80px'>CC BY-NC-ND</div>
      <div style='flex:1;height:6px;border-radius:3px;background:#f43f5e'></div>
      <div style='font-size:.75rem;color:#be123c;min-width:120px'>⚠️ 限制最多，禁止商用+改作</div>
    </div>
  </div>
  <div class='tip-box'>⚠️ <strong>重點提醒</strong>：授權一旦釋出即<strong>無法撤回</strong>，選擇前請審慎考量創作用途與分享目的。</div>
</div>"""
},


{
  'id': 30,
  'chapter': '第三章：創作責任',
  'title': 'CC0 公眾領域與免費素材資源',
  'bg': 'white',
  'quiz': None, 'chart': None, 'video': None,
  'html': """
<div class='slide-inner'>
  <h2 class='slide-title'>🆓 CC0 公眾領域與免費素材資源</h2>
  <div class='card-grid-2' style='margin-bottom:12px'>
    <div style='background:linear-gradient(135deg,#f0fdf4,#dcfce7);border:1px solid #86efac;border-radius:14px;padding:16px'>
      <div style='font-size:1.2rem;margin-bottom:6px'>0️⃣</div>
      <div style='font-weight:700;color:#166534;font-size:.9rem;margin-bottom:8px'>CC0 ── 公眾領域貢獻宣告</div>
      <div style='font-size:.75rem;color:#14532d;line-height:1.7'>
        作者主動放棄<strong>所有著作權利</strong><br>
        等同於公眾領域（Public Domain）<br><br>
        ✦ 任何人可自由使用、修改、商業應用<br>
        ✦ 無需標示來源（仍建議標示）<br>
        ✦ 比 CC BY 更寬鬆，無任何限制<br>
        ✦ 宣告後<strong>不可撤回</strong>
      </div>
      <div style='margin-top:10px;background:#fff;border:1px solid #bbf7d0;border-radius:8px;padding:8px;font-size:.72rem;color:#14532d'>
        ⚠️ CC0 ≠ CC（創用 CC）<br>
        CC 保留部分權利，CC0 完全放棄！
      </div>
    </div>
    <div style='background:linear-gradient(135deg,#eff6ff,#dbeafe);border:1px solid #93c5fd;border-radius:14px;padding:16px'>
      <div style='font-size:1.2rem;margin-bottom:6px'>🖼️</div>
      <div style='font-weight:700;color:#1e40af;font-size:.9rem;margin-bottom:8px'>推薦免費素材來源</div>
      <div style='display:flex;flex-direction:column;gap:6px'>
        <div style='background:#fff;border:1px solid #bfdbfe;border-radius:8px;padding:8px 10px;font-size:.75rem'>
          <strong style='color:#1e40af'>Unsplash</strong>（unsplash.com）<br>
          <span style='color:#374151'>高品質攝影，CC0 授權，可商用免標示</span>
        </div>
        <div style='background:#fff;border:1px solid #bfdbfe;border-radius:8px;padding:8px 10px;font-size:.75rem'>
          <strong style='color:#1e40af'>Pexels</strong>（pexels.com）<br>
          <span style='color:#374151'>照片與影片，免費商業授權</span>
        </div>
        <div style='background:#fff;border:1px solid #bfdbfe;border-radius:8px;padding:8px 10px;font-size:.75rem'>
          <strong style='color:#1e40af'>故宮 Open Data</strong>（opendata.npm.edu.tw）<br>
          <span style='color:#374151'>台灣故宮藏品高解析圖像，CC0 授權</span>
        </div>
        <div style='background:#fff;border:1px solid #bfdbfe;border-radius:8px;padding:8px 10px;font-size:.75rem'>
          <strong style='color:#1e40af'>Stocksnap.io</strong><br>
          <span style='color:#374151'>大量 CC0 授權高品質照片</span>
        </div>
      </div>
    </div>
  </div>
  <div class='tip-box'>💡 <strong>使用素材前，務必確認授權！</strong> 即使標榜「免費」，也可能需要標示來源或禁止商用。CC0 是最無後顧之憂的選擇。</div>
</div>"""
},


{
  'id': 31,
  'chapter': '第三章：創作責任',
  'title': '開放原始碼 Open Source',
  'bg': 'white',
  'quiz': None, 'chart': None, 'video': None,
  'html': """
<div class='slide-inner'>
  <h2 class='slide-title'>🔓 開放原始碼（Open Source）</h2>
  <div class='card-grid-2' style='margin-bottom:12px'>
    <div>
      <div style='font-size:.8rem;font-weight:700;color:#1E3A5F;margin-bottom:8px'>什麼是開放原始碼？</div>
      <div style='background:#f8fafc;border:1px solid #e2e8f0;border-radius:10px;padding:12px;font-size:.78rem;color:#374151;line-height:1.7;margin-bottom:8px'>
        將程式<strong>原始碼（Source Code）</strong>公開，允許任何人：<br>
        ✦ 免費使用與下載<br>
        ✦ 查看程式運作原理<br>
        ✦ 修改以符合自身需求<br>
        ✦ 將改版分享給他人
      </div>
      <div style='background:#eff6ff;border:1px solid #93c5fd;border-radius:10px;padding:12px;font-size:.78rem;color:#1e3a8a;line-height:1.6'>
        <strong>📱 Android 案例</strong>：Google 將 Android 核心以開源授權釋出，讓三星、小米等廠商能客製化，促成全球最廣泛使用的手機系統。
      </div>
    </div>
    <div>
      <div style='font-size:.8rem;font-weight:700;color:#1E3A5F;margin-bottom:8px'>常見開源授權比較</div>
      <div style='display:flex;flex-direction:column;gap:6px'>
        <div style='background:#f0fdf4;border:1px solid #86efac;border-radius:8px;padding:10px 12px;font-size:.75rem'>
          <strong style='color:#166534'>MIT License</strong><br>
          <span style='color:#374151'>最寬鬆：可商用、改作，僅需保留版權聲明</span>
        </div>
        <div style='background:#eff6ff;border:1px solid #93c5fd;border-radius:8px;padding:10px 12px;font-size:.75rem'>
          <strong style='color:#1e40af'>Apache 2.0</strong><br>
          <span style='color:#374151'>商用友善，需保留原始授權聲明與變更說明</span>
        </div>
        <div style='background:#faf5ff;border:1px solid #c4b5fd;border-radius:8px;padding:10px 12px;font-size:.75rem'>
          <strong style='color:#7c3aed'>GPL（GNU）</strong><br>
          <span style='color:#374151'>最嚴格：改版也必須以 GPL 開源（傳染性條款）</span>
        </div>
        <div style='background:#fff7ed;border:1px solid #fdba74;border-radius:8px;padding:10px 12px;font-size:.75rem'>
          <strong style='color:#9a3412'>著名開源專案</strong><br>
          <span style='color:#374151'>Linux、Python、Firefox、VS Code、Android</span>
        </div>
      </div>
    </div>
  </div>
  <div class='tip-box'>🔑 開源 ≠ 免費商用！使用前務必確認授權條款，GPL 改版需同樣開源，MIT 則相對自由。</div>
</div>"""
},


{
  'id': 32,
  'chapter': '第三章：創作責任',
  'title': '創用 CC 授權介紹（三）',
  'bg': 'white',
  'quiz': None, 'chart': None, 'video': None,
  'html': """
<div class='slide-inner'>
  <h2 class='slide-title'>📋 創用 CC 授權介紹（三）：選擇授權</h2>
  <div style='display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:12px'>
    <div>
      <div style='font-size:.8rem;font-weight:700;color:#1E3A5F;margin-bottom:8px'>不同授權限制比較</div>
      <table class='info-table'>
        <thead class='table-header'>
          <tr><th>授權</th><th>可商用</th><th>可改作</th><th>需同授權</th></tr>
        </thead>
        <tbody>
          <tr><td>CC BY</td><td class='td-center'>✅</td><td class='td-center'>✅</td><td class='td-center'>❌</td></tr>
          <tr class='tr-highlight'><td>CC BY-SA</td><td class='td-center'>✅</td><td class='td-center'>✅</td><td class='td-center'>✅</td></tr>
          <tr><td>CC BY-NC</td><td class='td-center'>❌</td><td class='td-center'>✅</td><td class='td-center'>❌</td></tr>
          <tr class='tr-highlight'><td>CC BY-ND</td><td class='td-center'>✅</td><td class='td-center'>❌</td><td class='td-center'>—</td></tr>
          <tr><td>CC BY-NC-ND</td><td class='td-center'>❌</td><td class='td-center'>❌</td><td class='td-center'>—</td></tr>
        </tbody>
      </table>
    </div>
    <div>
      <div style='font-size:.8rem;font-weight:700;color:#1E3A5F;margin-bottom:8px'>選擇授權的關鍵問題</div>
      <div style='display:flex;flex-direction:column;gap:8px'>
        <div style='background:#eff6ff;border-radius:10px;padding:10px 12px;font-size:.8rem'>
          <div style='font-weight:700;color:#1e40af;margin-bottom:4px'>❓ 你允許他人商業使用嗎？</div>
          <div style='color:#374151'>有 → 不含 NC；否 → 加 NC</div>
        </div>
        <div style='background:#f0fdf4;border-radius:10px;padding:10px 12px;font-size:.8rem'>
          <div style='font-weight:700;color:#166534;margin-bottom:4px'>❓ 你允許他人修改作品嗎？</div>
          <div style='color:#374151'>有 → 不含 ND；否 → 加 ND</div>
        </div>
        <div style='background:#faf5ff;border-radius:10px;padding:10px 12px;font-size:.8rem'>
          <div style='font-weight:700;color:#7c3aed;margin-bottom:4px'>❓ 你要求衍生作品同授權嗎？</div>
          <div style='color:#374151'>有 → 加 SA；否 → 不含 SA</div>
        </div>
      </div>
    </div>
  </div>
  <div class='tip-box'>🌐 查詢/搜尋授權圖片：Google 圖片 → 工具 → 使用權 → 創用 CC 授權</div>
</div>"""
},

{
  'id': 33,
  'chapter': '第三章：創作責任',
  'title': '合理引用四大原則',
  'bg': 'white',
  'quiz': None, 'chart': None, 'video': None,
  'html': """
<div class='slide-inner'>
  <h2 class='slide-title'>📌 合理引用四大原則（Fair Use）</h2>
  <div class='card-grid-2' style='margin-bottom:12px'>
    <div style='background:linear-gradient(135deg,#eff6ff,#dbeafe);border:1px solid #93c5fd;border-radius:14px;padding:16px'>
      <div style='display:flex;align-items:center;gap:8px;margin-bottom:8px'>
        <div style='width:32px;height:32px;border-radius:50%;background:#1e40af;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.9rem'>1</div>
        <div style='font-weight:700;color:#1e40af'>使用目的（Purpose）</div>
      </div>
      <div style='font-size:.8rem;color:#1e3a8a;line-height:1.5'>
        是否用於<strong>教育、評論、非商業</strong>用途？<br>
        教育與評論目的較容易被認定為合理使用。
      </div>
    </div>
    <div style='background:linear-gradient(135deg,#faf5ff,#ede9fe);border:1px solid #c4b5fd;border-radius:14px;padding:16px'>
      <div style='display:flex;align-items:center;gap:8px;margin-bottom:8px'>
        <div style='width:32px;height:32px;border-radius:50%;background:#7c3aed;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.9rem'>2</div>
        <div style='font-weight:700;color:#7c3aed'>著作性質（Nature）</div>
      </div>
      <div style='font-size:.8rem;color:#581c87;line-height:1.5'>
        原著作是否具有<strong>高度創意</strong>或已公開發表？<br>
        事實性資料比創意作品更容易引用。
      </div>
    </div>
    <div style='background:linear-gradient(135deg,#fff7ed,#ffedd5);border:1px solid #fdba74;border-radius:14px;padding:16px'>
      <div style='display:flex;align-items:center;gap:8px;margin-bottom:8px'>
        <div style='width:32px;height:32px;border-radius:50%;background:#ea580c;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.9rem'>3</div>
        <div style='font-weight:700;color:#ea580c'>使用比例（Amount）</div>
      </div>
      <div style='font-size:.8rem;color:#9a3412;line-height:1.5'>
        引用的比例是否合理，<strong>未取代原著作核心</strong>？<br>
        引用越少、越不像核心部分，越安全。
      </div>
    </div>
    <div style='background:linear-gradient(135deg,#fef2f2,#fee2e2);border:1px solid #fca5a5;border-radius:14px;padding:16px'>
      <div style='display:flex;align-items:center;gap:8px;margin-bottom:8px'>
        <div style='width:32px;height:32px;border-radius:50%;background:#dc2626;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.9rem'>4</div>
        <div style='font-weight:700;color:#dc2626'>市場影響（Market）</div>
      </div>
      <div style='font-size:.8rem;color:#991b1b;line-height:1.5'>
        引用是否<strong>損害原著作的市場價值</strong>？<br>
        若引用會讓人不必購買原作，風險較高。
      </div>
    </div>
  </div>
  <div class='tip-box'>⚠️ 即使是免費授權圖片，仍須標示來源，才符合學術誠信與著作權規範。</div>
</div>"""
},

{
  'id': 34,
  'chapter': '第三章：創作責任',
  'title': 'AI 生成圖著作權與法律',
  'bg': 'white',
  'quiz': None, 'chart': None, 'video': None,
  'html': """
<div class='slide-inner'>
  <h2 class='slide-title'>🏛️ AI 生成圖著作權與法律地位</h2>
  <div style='display:flex;flex-direction:column;gap:8px;margin-bottom:12px'>
    <div style='background:#f0fdf4;border:1px solid #86efac;border-radius:10px;padding:10px 14px;font-size:.8rem;color:#14532d;display:flex;gap:10px;align-items:flex-start'>
      <span style='font-size:1.2rem'>🇹🇼</span>
      <div><strong>台灣立場</strong>：AI 生成作品目前<strong>不受著作權保護</strong>，需有人類創作性介入才可主張權利</div>
    </div>
    <div style='background:#eff6ff;border:1px solid #93c5fd;border-radius:10px;padding:10px 14px;font-size:.8rem;color:#1e3a8a;display:flex;gap:10px;align-items:flex-start'>
      <span style='font-size:1.2rem'>🇺🇸</span>
      <div><strong>美國立場</strong>：美國著作權局明確表示，純 AI 生成內容不具著作權；人類選擇與編排可部分主張</div>
    </div>
    <div style='background:#fff7ed;border:1px solid #fdba74;border-radius:10px;padding:10px 14px;font-size:.8rem;color:#9a3412;display:flex;gap:10px;align-items:flex-start'>
      <span style='font-size:1.2rem'>⚠️</span>
      <div><strong>訓練資料爭議</strong>：AI 以版權作品訓練是否侵權，全球仍有法律爭議（如 Getty Images 訴訟案）</div>
    </div>
    <div style='background:#faf5ff;border:1px solid #c4b5fd;border-radius:10px;padding:10px 14px;font-size:.8rem;color:#581c87;display:flex;gap:10px;align-items:flex-start'>
      <span style='font-size:1.2rem'>🎭</span>
      <div><strong>風格模仿與肖像權</strong>：模仿特定藝術家風格或生成真實人物臉孔，可能涉及侵權與肖像權問題</div>
    </div>
    <div style='background:#fef2f2;border:1px solid #fca5a5;border-radius:10px;padding:10px 14px;font-size:.8rem;color:#7f1d1d;display:flex;gap:10px;align-items:flex-start'>
      <span style='font-size:1.2rem'>📋</span>
      <div><strong>台灣法規動向</strong>：《生成式 AI 發展條例》草案推動中，要求 AI 生成內容加註標示，保障資訊透明與創作溯源</div>
    </div>
  </div>
  <div class='tip-box'>💡 <strong>安全原則</strong>：選擇 Adobe Firefly 等使用合法訓練資料的工具，並主動標示 AI 來源。</div>
</div>"""
},

{
  'id': 35,
  'chapter': '第三章：創作責任',
  'title': '作品標示與學術誠信',
  'bg': 'white',
  'quiz': 'q3', 'chart': None, 'video': None,
  'html': """
<div class='slide-inner'>
  <h2 class='slide-title'>📝 作品標示方法 × 學術誠信三原則</h2>
  <div style='display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:12px'>
    <div>
      <div style='font-size:.8rem;font-weight:700;color:#1E3A5F;margin-bottom:8px'>【標示 AI 生成來源的方式】</div>
      <div style='display:flex;flex-direction:column;gap:6px'>
        <div style='background:#f8fafc;border-radius:8px;padding:8px 10px;font-size:.78rem;color:#374151;border:1px solid #e2e8f0'>
          ① 在作品說明中註明：「本圖由 AI 工具（如 ChatGPT）生成」
        </div>
        <div style='background:#f8fafc;border-radius:8px;padding:8px 10px;font-size:.78rem;color:#374151;border:1px solid #e2e8f0'>
          ② 加入 Prompt 說明：記錄使用的提示詞，展現創作思考過程
        </div>
        <div style='background:#f8fafc;border-radius:8px;padding:8px 10px;font-size:.78rem;color:#374151;border:1px solid #e2e8f0'>
          ③ 格式範例：「圖片來源：AI 生成（工具：ChatGPT），Prompt：『...』，生成日期：2026/xx/xx」
        </div>
      </div>
    </div>
    <div>
      <div style='font-size:.8rem;font-weight:700;color:#1E3A5F;margin-bottom:8px'>【學術誠信三原則】</div>
      <div style='display:flex;flex-direction:column;gap:8px'>
        <div style='background:#eff6ff;border:1px solid #93c5fd;border-radius:10px;padding:10px 12px'>
          <div style='font-weight:700;color:#1e40af;font-size:.82rem;margin-bottom:4px'>① 誠實</div>
          <div style='font-size:.75rem;color:#1e3a8a'>作業內容須為自己獨立完成，不以 AI 取代思考與創作</div>
        </div>
        <div style='background:#f0fdf4;border:1px solid #86efac;border-radius:10px;padding:10px 12px'>
          <div style='font-weight:700;color:#166534;font-size:.82rem;margin-bottom:4px'>② 透明</div>
          <div style='font-size:.75rem;color:#14532d'>若使用任何輔助工具，應主動告知老師並說明使用方式</div>
        </div>
        <div style='background:#faf5ff;border:1px solid #c4b5fd;border-radius:10px;padding:10px 12px'>
          <div style='font-weight:700;color:#7c3aed;font-size:.82rem;margin-bottom:4px'>③ 尊重</div>
          <div style='font-size:.75rem;color:#581c87'>遵守課堂規範，理解禁止規定背後的學習目的與意義</div>
        </div>
      </div>
    </div>
  </div>
  <div class='tip-box'>🔑 <strong>核心原則</strong>：AI 是工具，創作者是你。保留創作歷程（截圖、草稿、修改紀錄）是最佳的誠信證明。<br>
  ✋ 點「下一頁」進行第三章測驗！</div>
</div>"""
},

# ──────────────────────────────────────────
#  總結與作業
# ──────────────────────────────────────────
{
  'id': 36,
  'chapter': '總結與作業',
  'title': '個人作業',
  'bg': 'navy',
  'quiz': None, 'chart': None, 'video': None,
  'html': """
<div class='slide-inner'>
  <h2 class='slide-title' style='color:#fff'>📝 個人作業</h2>
  <div class='task-single'>
    <div class='task-title'>👤 個人作業內容（繳交至 Google Classroom）</div>
    <div class='task-item'>① 使用任意一款 AI 工具（ChatGPT、Canva AI 或其他），生成一張符合以下主題的圖片：「芳和 50」</div>
    <div class='task-item'>② 截圖保存你輸入的 Prompt（提示詞），並說明你為什麼這樣寫</div>
    <div class='task-item'>③ 仔細觀察 AI 生成圖，找出至少一個「AI 幻覺」錯誤並指出位置</div>
    <div class='task-item'>④ 為這張圖片選擇一個創用 CC 授權（CC BY、CC BY-NC 等），說明你選擇的理由</div>
    <div class='task-item'>⑤ 寫下你對「AI 生成圖的著作權歸屬」的看法（至少 3 句話）</div>
  </div>
  <div class='submit-box'>
    <div class='submit-icon'>📋</div>
    <div class='submit-info'>
      <div class='submit-title'>繳交方式</div>
      <div class='submit-desc'>完成後至 <strong>Google Classroom</strong> 繳交，填入姓名與班級，<br>
      並將作業說明（圖片截圖、Prompt、授權選擇、心得）一併上傳</div>
    </div>
  </div>
</div>"""
},

{
  'id': 37,
  'chapter': '總結與作業',
  'title': '總結：能力越強，責任越大',
  'bg': 'navy',
  'quiz': 'q4', 'chart': None, 'video': None,
  'html': """
<div class='slide-inner'>
  <h2 class='slide-title' style='color:#fff'>🌟 總結：能力越強，責任越大</h2>
  <div class='fact-box' style='margin-bottom:14px'>
    <p style='color:rgba(255,255,255,.85);line-height:1.7;font-size:.85rem'>
      在 AI 時代，數位創作者擁有前所未有的創作能力，但也肩負更大的責任。
      我們必須尊重著作權、正確標示 AI 生成內容、誠信面對學習與創作。
      <strong style='color:#F59E0B'>技術是工具，品格才是核心。</strong>
    </p>
  </div>
  <div class='card-grid-3' style='margin-bottom:14px'>
    <div class='info-card'>
      <div class='card-icon'>🔢</div>
      <div class='card-label'>數位語言</div>
      <div class='card-desc'>0與1、類比/數位、ASCII、像素、色彩深度、聲音/視訊格式</div>
    </div>
    <div class='info-card'>
      <div class='card-icon'>🤖</div>
      <div class='card-label'>AI 創作</div>
      <div class='card-desc'>擴散模型、三元件流程、幻覺識別、工具比較</div>
    </div>
    <div class='info-card'>
      <div class='card-icon'>⚖️</div>
      <div class='card-label'>創作責任</div>
      <div class='card-desc'>創用 CC、合理引用、AI 著作權、學術誠信</div>
    </div>
  </div>
  <div style='background:linear-gradient(135deg,rgba(13,148,136,.3),rgba(107,63,160,.3));border:1px solid rgba(255,255,255,.2);border-radius:14px;padding:16px;text-align:center'>
    <div style='font-size:1.1rem;font-weight:700;color:#fff;margin-bottom:6px'>
      願每位同學都能成為負責任、有創造力的數位公民
    </div>
    <div style='font-size:.82rem;color:rgba(255,255,255,.7)'>
      用誠信與智慧，在數位世界留下有意義的足跡 🌟
    </div>
    <div style='margin-top:12px;font-size:.8rem;color:rgba(255,255,255,.5)'>
      ✋ 點「下一頁」進行總複習測驗！
    </div>
  </div>
</div>"""
},

]  # end SLIDES


# ── 測驗資料 ──────────────────────────────────────────────────
# 結構：QUIZZES['q1'] = { 'title': '...', 'questions': [...] }
# 每題：{ 'q': '...', 'options': [...], 'answer': int, 'explain': '...' }

QUIZZES = {

  'q1': {
    'title': '🔢 第一章測驗：數位語言基礎',
    'questions': [
      {
        'q': '電腦的最小資料單位是什麼？',
        'options': ['bit（位元）', 'Byte（位元組）', 'KB（千位元組）', 'pixel（像素）'],
        'answer': 0,
        'explain': 'bit（位元）是最小單位，只能是 0 或 1。8 個 bit 才組成 1 個 Byte（位元組）。'
      },
      {
        'q': '十六進位（Hex）最常用於表示什麼？',
        'options': ['時間格式', '顏色碼與記憶體位址', '音量大小', '網路速度'],
        'answer': 1,
        'explain': '十六進位（0–9, A–F）能用更少位數表示大數值，常見於顏色碼（如 #FF0000 代表紅色）和記憶體位址。'
      },
      {
        'q': '1 Byte 等於幾個 bit？',
        'options': ['4 bits', '8 bits', '16 bits', '32 bits'],
        'answer': 1,
        'explain': '1 Byte = 8 bits，是電腦儲存的基本單位。一個英文字母佔 1 Byte，中文字在 UTF-8 編碼下佔 3 Bytes（早期 Big5 編碼為 2 Bytes）。'
      },
      {
        'q': '下列哪種圖片格式支援透明背景？',
        'options': ['JPEG', 'PNG', 'BMP', 'TIFF'],
        'answer': 1,
        'explain': 'PNG 支援 Alpha 通道（透明度），適合需要透明背景的圖示、貼圖、截圖等用途。'
      },
    ]
  },

  'q2': {
    'title': '🤖 第二章測驗：AI 創作基礎',
    'questions': [
      {
        'q': '點陣圖（Bitmap）放大後會出現什麼問題？',
        'options': ['顏色自動變深', '出現鋸齒失真', '檔案變小', '自動轉成向量圖'],
        'answer': 1,
        'explain': '點陣圖由固定數量的像素組成，放大時像素也變大，因此會出現鋸齒狀失真（Pixelation）。'
      },
      {
        'q': 'AI 擴散模型（Diffusion Model）的核心原理是？',
        'options': [
          '從清晰圖片逐步加入雜訊，訓練模型學習反向還原過程',
          '直接複製資料庫中現有的圖片',
          '用數學公式計算每個像素的最終顏色',
          '掃描藝術家的手稿後數位化'
        ],
        'answer': 0,
        'explain': '擴散模型訓練時：將圖片逐步加雜訊至完全模糊。生成時：從純雜訊出發，反向去除雜訊，逐步還原出圖像。'
      },
      {
        'q': 'AI 生成圖的三元件流程順序是？',
        'options': [
          '文字編碼器 → 擴散模型 → 解碼器',
          '解碼器 → 文字編碼器 → 擴散模型',
          '擴散模型 → 文字編碼器 → 解碼器',
          '解碼器 → 擴散模型 → 文字編碼器'
        ],
        'answer': 0,
        'explain': '流程為：① 文字編碼器（Prompt → 數學向量）→ ② 擴散模型（去雜訊生成）→ ③ 解碼器（輸出像素圖片）。'
      },
      {
        'q': '以下哪個 AI 圖像工具的訓練資料授權最安全？',
        'options': ['ChatGPT GPT-4o', 'Midjourney', 'Adobe Firefly', 'Stable Diffusion'],
        'answer': 2,
        'explain': 'Adobe Firefly 使用合法授權的訓練資料（Adobe Stock 等），明確保障商業授權安全，是專業用途首選。'
      },
    ]
  },

  'q3': {
    'title': '⚖️ 第三章測驗：創作責任',
    'questions': [
      {
        'q': 'CC BY-NC 授權代表什麼？',
        'options': [
          '需標示作者、且禁止商業用途',
          '可自由使用，無需標示任何資訊',
          '禁止修改，但可以商業使用',
          '只限個人學習，不可轉發'
        ],
        'answer': 0,
        'explain': 'CC BY-NC = Attribution（姓名標示）+ Non-Commercial（非商業性）。使用時需標示作者，且只能用於非商業目的。'
      },
      {
        'q': '合理引用（Fair Use）的四大原則不包含？',
        'options': ['使用目的（Purpose）', '著作性質（Nature）', '使用比例（Amount）', '作者的國籍'],
        'answer': 3,
        'explain': '合理引用四大原則為：使用目的、著作性質、使用比例、市場影響。作者國籍並不是判斷標準。'
      },
      {
        'q': '台灣目前對「純 AI 生成作品」的著作權立場是？',
        'options': [
          '完全保護，AI 視同創作者',
          '不受著作權保護，需有人類創作性介入才可主張',
          '保護期間為 50 年後進入公眾領域',
          '由 AI 開發公司持有著作權'
        ],
        'answer': 1,
        'explain': '台灣法律立場：純 AI 生成作品不受著作權保護。須有人類的創作性介入（如選擇、編排、修改），才有可能主張著作權。'
      },
      {
        'q': '使用 AI 輔助完成作品，下列哪個做法最符合學術誠信？',
        'options': [
          '直接繳交 AI 生成內容，不加任何說明',
          '只告訴好朋友自己用了 AI',
          '透明說明使用 AI 的部分，並加入個人修改與思考',
          '換個角度，讓 AI 重新生成，讓作品看起來不一樣'
        ],
        'answer': 2,
        'explain': '學術誠信三原則：誠實、透明、尊重。主動說明使用 AI 的方式，並保留個人創作歷程，是最符合誠信的做法。'
      },
    ]
  },

  'q4': {
    'title': '🌟 總複習：AI 時代的數位創作者',
    'questions': [
      {
        'q': 'RGB 顏色模型中，#FF0000 代表什麼顏色？',
        'options': ['純藍色', '純綠色', '純紅色', '純白色'],
        'answer': 2,
        'explain': '#FF0000 = R:255, G:0, B:0，即純紅色。FF 在十六進位等於十進位的 255（最大值），00 等於 0。'
      },
      {
        'q': 'SVG 格式相較於 PNG 最大的優點是什麼？',
        'options': [
          '檔案壓縮率更高',
          '支援動態效果',
          '無限縮放不失真',
          '色彩更豐富'
        ],
        'answer': 2,
        'explain': 'SVG（可縮放向量圖形）用數學公式記錄圖形，因此無論放大多少倍都不會失真，非常適合 Logo 和圖示。'
      },
      {
        'q': 'AI 幻覺現象最常出現在哪個部位？',
        'options': ['天空背景', '人物的手指', '建築物外牆', '地板材質'],
        'answer': 1,
        'explain': 'AI 最容易在人物手指上出現錯誤（六根手指、扭曲指節等），因為手部結構複雜，AI 難以精確還原。'
      },
      {
        'q': '下列哪個情境最適合選擇 CC BY-SA 授權？',
        'options': [
          '我想讓別人商用，但不能修改',
          '我想分享我的教學筆記，允許他人修改，但衍生作品也要開放',
          '我完全放棄著作權，讓任何人自由使用',
          '我只允許個人非商業下載'
        ],
        'answer': 1,
        'explain': 'CC BY-SA（姓名標示－相同方式分享）適合開放教育資源：允許修改，但衍生作品必須採用相同授權，確保持續開放共享。'
      },
    ]
  },

}
