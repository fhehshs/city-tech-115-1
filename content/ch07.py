# -*- coding: utf-8 -*-
# Week 7: 新興科技應用

CHAPTERS = [
    {'name': '封面', 'start': 1},
    {'name': '第一章：物聯網 IoT', 'start': 2},
    {'name': '第二章：AIoT 智慧應用', 'start': 8},
    {'name': '第三章：雲端運算', 'start': 14},
    {'name': '第四章：量子電腦與智慧城市', 'start': 19},
    {'name': '分組實作', 'start': 23},
]

QUIZZES = {
    'q1': {
        'title': '第一章 隨堂測驗',
        'questions': [
            {
                'q': '下列哪個裝置「不屬於」物聯網（IoT）設備？',
                'options': ['智慧型電錶（可遠端讀取用電量）', '可監測睡眠的智慧手環', '未連接網路的電風扇', '連網冰箱（可顯示食材保存期限）'],
                'answer': 2,
                'explain': 'IoT 的定義是「能連上網路、蒐集和交換資料的物理設備」。傳統電風扇沒有感測器也沒有網路連接，因此不屬於 IoT。'
            },
            {
                'q': 'IoT 設備的感測器主要負責什麼工作？',
                'options': ['蒐集環境中的物理資料（溫度、位置等）', '將資料加密傳輸到雲端', '分析大量數據並做出決策', '提供用戶介面供操作'],
                'answer': 0,
                'explain': '感測器（Sensor）是 IoT 的「眼睛和耳朵」，負責感知物理世界的資訊，如溫度、溼度、光線、動作等。'
            },
        ]
    },
    'q2': {
        'title': '第二章 隨堂測驗',
        'questions': [
            {
                'q': 'AIoT 是什麼的結合？',
                'options': ['自動化（Automation）+ 光學（Optics）', '人工智慧（AI）+ 物聯網（IoT）', '增強實境（AR）+ 物聯網（IoT）', '人工智慧（AI）+ 天文學（Astronomy）'],
                'answer': 1,
                'explain': 'AIoT = AI + IoT。IoT 負責收集資料，AI 負責分析決策，兩者結合讓設備從「能感知」進化到「能思考」。'
            },
            {
                'q': '以下哪個是 AIoT 在台灣農業的應用案例？',
                'options': ['機器人代替農民在田間行走', '超市用 AI 辨識顧客並推薦商品', 'GPS 追蹤農產品運送路線', '農業感測器偵測土壤溼度，AI 自動調節灌溉量'],
                'answer': 3,
                'explain': '台灣農委會推動「智慧農業 4.0」，結合土壤感測器、AI 模型，實現精準灌溉，用水量減少約 30%，產量提升 15%。'
            },
        ]
    },
    'q3': {
        'title': '第三章 隨堂測驗',
        'questions': [
            {
                'q': '下列哪種雲端服務模式，用戶管理的範圍最廣（需要自行管理應用、資料、OS）？',
                'options': ['IaaS（基礎設施即服務）', 'PaaS（平台即服務）', 'SaaS（軟體即服務）', 'FaaS（功能即服務）'],
                'answer': 0,
                'explain': 'IaaS 提供虛擬機器等基礎硬體，用戶需自行安裝 OS、中介軟體、應用程式。PaaS 再幫你管好 OS，SaaS 連應用都幫你處理好。'
            },
            {
                'q': 'Gmail、Google 文件這類「打開瀏覽器就能直接使用的軟體」，屬於哪一種雲端服務模式？',
                'options': ['IaaS（基礎設施即服務）', 'PaaS（平台即服務）', 'SaaS（軟體即服務）', '私有雲'],
                'answer': 2,
                'explain': 'SaaS（Software as a Service）是直接使用完整軟體，不需安裝與維護，例如 Gmail、Google Docs、LINE。IaaS 提供虛擬機等硬體資源，PaaS 提供開發平台。'
            },
        ]
    },
    'q4': {
        'title': '第四章 隨堂測驗',
        'questions': [
            {
                'q': '量子電腦相較於傳統電腦的核心優勢是什麼？',
                'options': ['晶片面積比傳統電腦小 1000 倍', '完全不消耗電力，靠量子能量運作', '只需要用光就能計算，不需電力', '可同時處理大量可能性（量子疊加態）'],
                'answer': 3,
                'explain': '量子位元（Qubit）利用疊加態可同時是 0 和 1，讓量子電腦在特定問題（加密破解、藥物模擬）上比傳統電腦快指數級。'
            },
            {
                'q': '台北市智慧城市最廣為人知的應用是？',
                'options': ['全市自動駕駛公車', 'YouBike 智慧單車共享系統', 'AI 機器人取代所有市政員工', '空中計程車（Flying Taxi）'],
                'answer': 1,
                'explain': 'YouBike 是台北市智慧城市的標竿案例，即時顯示各站點車輛數量，2023 年 YouBike 2.0 已擴展至全台 22 縣市，日均使用次數超過 30 萬次。'
            },
        ]
    },
}

SLIDES = [
    {
        'id': 1,
        'chapter': '封面',
        'title': '新興科技應用',
        'bg': 'navy',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<div style='text-align:center;padding:30px 20px;'>
  <div style='font-size:72px;margin-bottom:20px;'>🤖</div>
  <h1 style='font-size:2.8rem;font-weight:900;color:#fff;margin-bottom:12px;'>新興科技應用</h1>
  <h2 style='font-size:1.5rem;font-weight:400;color:#93c5fd;margin-bottom:30px;'>Emerging Technologies</h2>
  <div style='display:flex;justify-content:center;gap:20px;flex-wrap:wrap;margin-bottom:30px;'>
    <span style='background:rgba(255,255,255,0.15);color:#e0f2fe;padding:8px 20px;border-radius:20px;font-size:1rem;'>🌐 物聯網 IoT</span>
    <span style='background:rgba(255,255,255,0.15);color:#e0f2fe;padding:8px 20px;border-radius:20px;font-size:1rem;'>🧠 AIoT</span>
    <span style='background:rgba(255,255,255,0.15);color:#e0f2fe;padding:8px 20px;border-radius:20px;font-size:1rem;'>☁️ 雲端運算</span>
    <span style='background:rgba(255,255,255,0.15);color:#e0f2fe;padding:8px 20px;border-radius:20px;font-size:1rem;'>⚛️ 量子電腦</span>
    <span style='background:rgba(255,255,255,0.15);color:#e0f2fe;padding:8px 20px;border-radius:20px;font-size:1rem;'>🏙️ 智慧城市</span>
  </div>
  <p style='color:#bfdbfe;font-size:1.1rem;'>城市科技 — 第七週</p>
</div>"""
    },
    {
        'id': 2,
        'chapter': '第一章：物聯網 IoT',
        'title': '什麼是物聯網？',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>什麼是物聯網（IoT）？</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;border-left:4px solid #2563eb;padding:15px;border-radius:8px;margin-bottom:15px;'>
      <h3 style='color:#1e40af;font-size:1.1rem;margin-bottom:8px;'>📌 定義</h3>
      <p style='color:#374151;font-size:0.95rem;'>IoT（Internet of Things）是指將各種「物品」賦予感測、計算和聯網能力，使其能夠自動蒐集、傳送和接收資料的技術生態系統。</p>
    </div>
    <div style='background:#f0fdf4;border-left:4px solid #16a34a;padding:15px;border-radius:8px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:8px;'>🔢 IoT 規模</h3>
      <ul style='color:#374151;font-size:0.9rem;padding-left:16px;margin:0;'>
        <li>2024 全球 IoT 設備：<strong>175 億台</strong></li>
        <li>2030 預估：<strong>290 億台</strong></li>
        <li>台灣 IoT 產值：<strong>5,000 億台幣</strong>（2024）</li>
      </ul>
    </div>
  </div>
  <div>
    <div style='background:#fdf4ff;padding:15px;border-radius:10px;'>
      <h3 style='color:#7c3aed;font-size:1rem;margin-bottom:12px;'>🔗 IoT 四大組成</h3>
      <div style='display:flex;flex-direction:column;gap:8px;'>
        <div style='background:#fff;padding:10px;border-radius:6px;display:flex;align-items:center;gap:10px;'>
          <span style='font-size:1.4rem;'>📡</span>
          <div><p style='font-weight:700;color:#7c3aed;font-size:0.9rem;margin:0;'>感測器</p><p style='color:#374151;font-size:0.8rem;margin:0;'>感知溫度、位置、影像等物理資料</p></div>
        </div>
        <div style='background:#fff;padding:10px;border-radius:6px;display:flex;align-items:center;gap:10px;'>
          <span style='font-size:1.4rem;'>🔌</span>
          <div><p style='font-weight:700;color:#7c3aed;font-size:0.9rem;margin:0;'>連網模組</p><p style='color:#374151;font-size:0.8rem;margin:0;'>Wi-Fi、藍牙、NB-IoT、5G 等</p></div>
        </div>
        <div style='background:#fff;padding:10px;border-radius:6px;display:flex;align-items:center;gap:10px;'>
          <span style='font-size:1.4rem;'>☁️</span>
          <div><p style='font-weight:700;color:#7c3aed;font-size:0.9rem;margin:0;'>雲端平台</p><p style='color:#374151;font-size:0.8rem;margin:0;'>儲存、分析大量感測資料</p></div>
        </div>
        <div style='background:#fff;padding:10px;border-radius:6px;display:flex;align-items:center;gap:10px;'>
          <span style='font-size:1.4rem;'>📱</span>
          <div><p style='font-weight:700;color:#7c3aed;font-size:0.9rem;margin:0;'>應用介面</p><p style='color:#374151;font-size:0.8rem;margin:0;'>APP、網頁儀表板供用戶操控</p></div>
        </div>
      </div>
    </div>
  </div>
</div>"""
    },
    {
        'id': 3,
        'chapter': '第一章：物聯網 IoT',
        'title': 'IoT 生活應用',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>IoT 生活應用</h2>
<div style='display:grid;grid-template-columns:repeat(3,1fr);gap:15px;'>
  <div style='background:#eff6ff;padding:15px;border-radius:10px;text-align:center;'>
    <div style='font-size:2.5rem;margin-bottom:8px;'>🏠</div>
    <h3 style='color:#1e40af;font-size:1rem;margin-bottom:8px;'>智慧家庭</h3>
    <ul style='color:#374151;font-size:0.85rem;list-style:none;padding:0;text-align:left;'>
      <li>☑️ 智慧音箱（Alexa/小愛）</li>
      <li>☑️ 智慧門鎖/門鈴攝影機</li>
      <li>☑️ 掃地機器人</li>
      <li>☑️ 智慧空調自動調溫</li>
    </ul>
  </div>
  <div style='background:#f0fdf4;padding:15px;border-radius:10px;text-align:center;'>
    <div style='font-size:2.5rem;margin-bottom:8px;'>🏭</div>
    <h3 style='color:#15803d;font-size:1rem;margin-bottom:8px;'>工業物聯網</h3>
    <ul style='color:#374151;font-size:0.85rem;list-style:none;padding:0;text-align:left;'>
      <li>☑️ 機台預測維護</li>
      <li>☑️ 供應鏈即時追蹤</li>
      <li>☑️ 品質自動檢測</li>
      <li>☑️ 能源消耗優化</li>
    </ul>
  </div>
  <div style='background:#fdf4ff;padding:15px;border-radius:10px;text-align:center;'>
    <div style='font-size:2.5rem;margin-bottom:8px;'>🏥</div>
    <h3 style='color:#7c3aed;font-size:1rem;margin-bottom:8px;'>智慧醫療</h3>
    <ul style='color:#374151;font-size:0.85rem;list-style:none;padding:0;text-align:left;'>
      <li>☑️ 智慧手環監測心跳</li>
      <li>☑️ 遠距血糖偵測</li>
      <li>☑️ 醫院床位即時追蹤</li>
      <li>☑️ 藥品冷鏈溫控</li>
    </ul>
  </div>
</div>
<div style='background:#fef9c3;padding:12px;border-radius:8px;margin-top:15px;border:1px solid #fde047;'>
  <p style='color:#854d0e;font-size:0.9rem;margin:0;'>🇹🇼 <strong>台灣案例</strong>：高雄港導入 IoT 貨櫃追蹤系統，即時掌握 200 萬個貨櫃位置，裝卸效率提升 25%。亞洲第一個實現全港 IoT 化的智慧港口。</p>
</div>"""
    },
    {
        'id': 4,
        'chapter': '第一章：物聯網 IoT',
        'title': 'IoT 通訊協定',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>IoT 通訊協定</h2>
<table style='width:100%;border-collapse:collapse;font-size:0.9rem;'>
  <tr style='background:#1e40af;color:#fff;'>
    <th style='padding:10px;text-align:left;'>協定</th>
    <th style='padding:10px;text-align:left;'>距離</th>
    <th style='padding:10px;text-align:left;'>功耗</th>
    <th style='padding:10px;text-align:left;'>速度</th>
    <th style='padding:10px;text-align:left;'>典型應用</th>
  </tr>
  <tr style='background:#eff6ff;'>
    <td style='padding:8px;font-weight:700;color:#1e40af;'>Wi-Fi 6</td>
    <td style='padding:8px;color:#374151;'>室內100m</td>
    <td style='padding:8px;color:#dc2626;'>高</td>
    <td style='padding:8px;color:#374151;'>9.6 Gbps</td>
    <td style='padding:8px;color:#374151;'>智慧家庭、監視器</td>
  </tr>
  <tr>
    <td style='padding:8px;font-weight:700;color:#1e40af;'>藍牙 BLE</td>
    <td style='padding:8px;color:#374151;'>10-100m</td>
    <td style='padding:8px;color:#15803d;'>極低</td>
    <td style='padding:8px;color:#374151;'>2 Mbps</td>
    <td style='padding:8px;color:#374151;'>智慧手環、AirTag</td>
  </tr>
  <tr style='background:#eff6ff;'>
    <td style='padding:8px;font-weight:700;color:#1e40af;'>Zigbee</td>
    <td style='padding:8px;color:#374151;'>10-100m</td>
    <td style='padding:8px;color:#15803d;'>極低</td>
    <td style='padding:8px;color:#374151;'>250 Kbps</td>
    <td style='padding:8px;color:#374151;'>智慧燈泡、門窗感測</td>
  </tr>
  <tr>
    <td style='padding:8px;font-weight:700;color:#1e40af;'>LoRa</td>
    <td style='padding:8px;color:#374151;'>15 km</td>
    <td style='padding:8px;color:#15803d;'>極低</td>
    <td style='padding:8px;color:#374151;'>50 Kbps</td>
    <td style='padding:8px;color:#374151;'>農業感測、水表抄表</td>
  </tr>
  <tr style='background:#eff6ff;'>
    <td style='padding:8px;font-weight:700;color:#1e40af;'>NB-IoT</td>
    <td style='padding:8px;color:#374151;'>城市廣域</td>
    <td style='padding:8px;color:#15803d;'>極低</td>
    <td style='padding:8px;color:#374151;'>250 Kbps</td>
    <td style='padding:8px;color:#374151;'>智慧電錶、停車場</td>
  </tr>
  <tr>
    <td style='padding:8px;font-weight:700;color:#1e40af;'>5G</td>
    <td style='padding:8px;color:#374151;'>城市廣域</td>
    <td style='padding:8px;color:#dc2626;'>中-高</td>
    <td style='padding:8px;color:#374151;'>20 Gbps</td>
    <td style='padding:8px;color:#374151;'>自駕車、遠距手術</td>
  </tr>
</table>
<div style='background:#f0fdf4;padding:10px;border-radius:8px;margin-top:12px;'>
  <p style='color:#15803d;font-size:0.85rem;margin:0;'>💡 選擇協定要考量：距離遠近、是否需要電池（功耗）、傳輸量大小、建置成本。</p>
</div>"""
    },
    {
        'id': 5,
        'chapter': '第一章：物聯網 IoT',
        'title': 'IoT 資安風險',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>IoT 資安風險</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#fef2f2;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#dc2626;font-size:1rem;margin-bottom:10px;'>⚠️ IoT 安全三大弱點</h3>
      <div style='display:flex;flex-direction:column;gap:8px;'>
        <div style='background:#fee2e2;padding:8px;border-radius:6px;'>
          <p style='font-weight:700;color:#dc2626;font-size:0.9rem;margin:0;'>1. 預設密碼不更改</p>
          <p style='color:#374151;font-size:0.8rem;margin:4px 0 0;'>90% 的 IoT 入侵源自「admin/admin」等預設帳密</p>
        </div>
        <div style='background:#fee2e2;padding:8px;border-radius:6px;'>
          <p style='font-weight:700;color:#dc2626;font-size:0.9rem;margin:0;'>2. 韌體不更新</p>
          <p style='color:#374151;font-size:0.8rem;margin:4px 0 0;'>設備出廠後廠商不再更新，舊漏洞長期存在</p>
        </div>
        <div style='background:#fee2e2;padding:8px;border-radius:6px;'>
          <p style='font-weight:700;color:#dc2626;font-size:0.9rem;margin:0;'>3. 通訊未加密</p>
          <p style='color:#374151;font-size:0.8rem;margin:4px 0 0;'>便宜 IoT 設備省去加密，資料明文傳輸</p>
        </div>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#fff7ed;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#ea580c;font-size:1rem;margin-bottom:8px;'>📰 真實案例</h3>
      <p style='color:#374151;font-size:0.9rem;'><strong>2016 Mirai 殭屍網路</strong>：駭客入侵全球數十萬台 IoT 設備（監視器、路由器），發動 DDoS 攻擊，造成 Twitter、Netflix 服務中斷達數小時。</p>
      <p style='color:#9a3412;font-size:0.85rem;margin-top:8px;'>起因：所有設備使用相同預設密碼 admin/admin。</p>
    </div>
    <div style='background:#f0fdf4;padding:12px;border-radius:8px;'>
      <h3 style='color:#15803d;font-size:0.95rem;margin-bottom:6px;'>🛡️ 防護建議</h3>
      <ul style='color:#374151;font-size:0.85rem;padding-left:16px;margin:0;'>
        <li>立即更改預設密碼</li>
        <li>定期更新韌體</li>
        <li>IoT 設備放獨立子網路</li>
        <li>購買有安全認證的品牌</li>
      </ul>
    </div>
  </div>
</div>"""
    },
    {
        'id': 6,
        'chapter': '第一章：物聯網 IoT',
        'title': '邊緣運算 Edge Computing',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': {'url': 'https://www.youtube.com/embed/cEOUeItHDdo', 'title': '邊緣運算介紹', 'desc': '了解 IoT 邊緣運算如何讓設備更聰明'},
        'html': """
<h2 class='slide-title'>邊緣運算 Edge Computing</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>📌 什麼是邊緣運算？</h3>
      <p style='color:#374151;font-size:0.9rem;'>在<strong>靠近資料來源的地方</strong>（設備端、基地台）進行運算，而不是把資料全送到遠端雲端處理。</p>
      <div style='background:#fff;padding:10px;border-radius:6px;margin-top:10px;text-align:center;'>
        <p style='color:#374151;font-size:0.85rem;margin:0;'>感測器 → <span style='color:#dc2626;text-decoration:line-through;'>雲端</span> → <span style='color:#16a34a;font-weight:700;'>邊緣伺服器</span> → 即時決策</p>
      </div>
    </div>
    <div style='background:#f0fdf4;padding:12px;border-radius:8px;'>
      <h3 style='color:#15803d;font-size:0.95rem;margin-bottom:8px;'>✅ 優點</h3>
      <ul style='color:#374151;font-size:0.85rem;padding-left:16px;margin:0;'>
        <li>超低延遲（&lt;5ms）</li>
        <li>減少頻寬使用</li>
        <li>離線仍可運作</li>
        <li>資料不離開本地，更安全</li>
      </ul>
    </div>
  </div>
  <div>
    <div style='background:#fdf4ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#7c3aed;font-size:1rem;margin-bottom:10px;'>🏭 應用場景</h3>
      <div style='display:flex;flex-direction:column;gap:8px;'>
        <div style='background:#fff;padding:8px;border-radius:6px;'>
          <span style='color:#7c3aed;font-weight:700;font-size:0.85rem;'>🚗 自駕車</span>
          <p style='color:#374151;font-size:0.8rem;margin:2px 0 0;'>不能等雲端回應，車上 AI 即時判斷（&lt;50ms）</p>
        </div>
        <div style='background:#fff;padding:8px;border-radius:6px;'>
          <span style='color:#7c3aed;font-weight:700;font-size:0.85rem;'>🏭 工廠品管</span>
          <p style='color:#374151;font-size:0.8rem;margin:2px 0 0;'>高速生產線即時辨識瑕疵品，無法等傳到雲端</p>
        </div>
        <div style='background:#fff;padding:8px;border-radius:6px;'>
          <span style='color:#7c3aed;font-weight:700;font-size:0.85rem;'>🔒 門禁系統</span>
          <p style='color:#374151;font-size:0.8rem;margin:2px 0 0;'>臉部辨識在本地運算，人臉特徵不上傳雲端</p>
        </div>
      </div>
    </div>
    <div style='background:#fff7ed;padding:10px;border-radius:8px;'>
      <p style='color:#9a3412;font-size:0.85rem;margin:0;'>💡 台灣 NVIDIA 合作：工研院推動邊緣 AI 晶片，讓台灣工廠的 AIoT 設備在產線上即時運算，不依賴雲端。</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 7,
        'chapter': '第一章：物聯網 IoT',
        'title': '🎯 第一章 隨堂測驗',
        'bg': 'purple',
        'quiz': 'q1',
        'chart': None,
        'video': None,
        'html': """
<div style='text-align:center;padding:20px;'>
  <div style='font-size:56px;margin-bottom:15px;'>🎯</div>
  <h2 style='color:#fff;font-size:2rem;font-weight:800;margin-bottom:10px;'>第一章 隨堂測驗</h2>
  <p style='color:#e9d5ff;font-size:1.1rem;'>物聯網 IoT ── 2 道題目，點擊作答！</p>
</div>"""
    },
    {
        'id': 8,
        'chapter': '第二章：AIoT 智慧應用',
        'title': 'AI + IoT = AIoT',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>AI + IoT = AIoT</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#fef9c3;padding:15px;border-radius:10px;margin-bottom:15px;border:1px solid #fde047;'>
      <h3 style='color:#854d0e;font-size:1rem;margin-bottom:10px;'>🤔 IoT 的限制</h3>
      <p style='color:#374151;font-size:0.9rem;'>傳統 IoT 只能<strong>感知資料</strong>，但無法自行<strong>判斷決策</strong>：</p>
      <ul style='color:#374151;font-size:0.85rem;padding-left:16px;margin-top:8px;'>
        <li>感測器回傳溫度 38°C</li>
        <li>但不知道這是否「異常」</li>
        <li>需要人工設規則：>37°C 就警報</li>
        <li>固定規則難以應付複雜情況</li>
      </ul>
    </div>
    <div style='background:#dcfce7;padding:12px;border-radius:8px;border:1px solid #86efac;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:8px;'>✨ AIoT 的突破</h3>
      <p style='color:#374151;font-size:0.85rem;margin:0;'>AI 學習歷史資料，自動找出「正常」與「異常」的模式，不需要人工設規則，且隨時間越來越聰明。</p>
    </div>
  </div>
  <div style='background:#f0f9ff;padding:15px;border-radius:10px;'>
    <h3 style='color:#0369a1;font-size:1rem;margin-bottom:12px;'>🔄 AIoT 運作流程</h3>
    <div style='display:flex;flex-direction:column;gap:8px;'>
      <div style='background:#fff;padding:10px;border-radius:8px;display:flex;align-items:center;gap:10px;'>
        <div style='background:#0369a1;color:#fff;width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:0.9rem;flex-shrink:0;'>1</div>
        <div>
          <p style='font-weight:700;color:#0369a1;font-size:0.9rem;margin:0;'>感知</p>
          <p style='color:#374151;font-size:0.8rem;margin:0;'>IoT 感測器蒐集環境資料</p>
        </div>
      </div>
      <div style='background:#fff;padding:10px;border-radius:8px;display:flex;align-items:center;gap:10px;'>
        <div style='background:#0369a1;color:#fff;width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:0.9rem;flex-shrink:0;'>2</div>
        <div>
          <p style='font-weight:700;color:#0369a1;font-size:0.9rem;margin:0;'>傳輸</p>
          <p style='color:#374151;font-size:0.8rem;margin:0;'>透過網路傳送至邊緣或雲端</p>
        </div>
      </div>
      <div style='background:#fff;padding:10px;border-radius:8px;display:flex;align-items:center;gap:10px;'>
        <div style='background:#0369a1;color:#fff;width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:0.9rem;flex-shrink:0;'>3</div>
        <div>
          <p style='font-weight:700;color:#0369a1;font-size:0.9rem;margin:0;'>分析</p>
          <p style='color:#374151;font-size:0.8rem;margin:0;'>AI 模型判斷情況、預測趨勢</p>
        </div>
      </div>
      <div style='background:#dcfce7;padding:10px;border-radius:8px;display:flex;align-items:center;gap:10px;'>
        <div style='background:#15803d;color:#fff;width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:0.9rem;flex-shrink:0;'>4</div>
        <div>
          <p style='font-weight:700;color:#15803d;font-size:0.9rem;margin:0;'>行動</p>
          <p style='color:#374151;font-size:0.8rem;margin:0;'>自動執行決策或通知管理者</p>
        </div>
      </div>
    </div>
  </div>
</div>"""
    },
    {
        'id': 9,
        'chapter': '第二章：AIoT 智慧應用',
        'title': 'AIoT 台灣案例：智慧農業',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>AIoT 台灣案例：智慧農業</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:10px;'>🌾 台南白河菱角 AIoT 示範場</h3>
      <ul style='color:#374151;font-size:0.9rem;padding-left:16px;'>
        <li>土壤感測器：偵測含水量、氮磷鉀</li>
        <li>氣象站：溫濕度、日照量、降雨</li>
        <li>AI 模型：預測病蟲害風險</li>
        <li>自動灌溉：依感測值調節水量</li>
        <li>無人機：噴藥、巡田拍照</li>
      </ul>
      <div style='background:#dcfce7;padding:8px;border-radius:6px;margin-top:10px;'>
        <p style='color:#15803d;font-size:0.85rem;margin:0;'>結果：<strong>用水量 -30%、農藥 -25%、產量 +18%</strong></p>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>🐟 台灣漁業 AIoT</h3>
      <p style='color:#374151;font-size:0.9rem;margin-bottom:8px;'>屏東水產試驗所「智慧養殖」：</p>
      <ul style='color:#374151;font-size:0.85rem;padding-left:16px;'>
        <li>水中 DO（溶氧量）感測器</li>
        <li>AI 預測魚群健康狀態</li>
        <li>自動打氧機依溶氧量啟動</li>
        <li>死亡率從 15% 降至 3%</li>
      </ul>
    </div>
    <div style='background:#fff7ed;padding:12px;border-radius:8px;'>
      <p style='color:#9a3412;font-size:0.85rem;margin:0;'>🌍 <strong>全球視角</strong>：聯合國糧農組織（FAO）估計 2050 年全球糧食需求將大幅成長，智慧農業被視為在有限土地與水資源下增產的關鍵技術。</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 10,
        'chapter': '第二章：AIoT 智慧應用',
        'title': 'AIoT 台灣案例：智慧製造',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>AIoT 台灣案例：智慧製造</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#fdf4ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#7c3aed;font-size:1rem;margin-bottom:10px;'>🏭 智慧製造：燈塔工廠</h3>
      <p style='color:#374151;font-size:0.9rem;margin-bottom:8px;'>世界經濟論壇（WEF）認證的「燈塔工廠」代表全球最先進的智慧製造，台灣的台達電子等企業已入選；台積電等大廠同樣深度導入 AIoT：</p>
      <ul style='color:#374151;font-size:0.85rem;padding-left:16px;'>
        <li>數千個感測器監測設備狀態</li>
        <li>AI 預測機台故障（提前 48 小時）</li>
        <li>自動搬運機器人（AGV）</li>
        <li>以 AI 即時監控維持極高良率</li>
        <li>大幅縮短換線與停機時間</li>
      </ul>
    </div>
  </div>
  <div>
    <div style='background:#fff7ed;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#ea580c;font-size:1rem;margin-bottom:10px;'>⚙️ 預測維護 vs 傳統維護</h3>
      <table style='width:100%;border-collapse:collapse;font-size:0.85rem;'>
        <tr style='background:#ea580c;color:#fff;'>
          <th style='padding:6px;'>項目</th><th style='padding:6px;'>傳統</th><th style='padding:6px;'>AIoT 預測</th>
        </tr>
        <tr><td style='padding:6px;color:#374151;'>維護時機</td><td style='padding:6px;color:#374151;'>故障後</td><td style='padding:6px;color:#16a34a;font-weight:700;'>故障前</td></tr>
        <tr style='background:#fff7ed;'><td style='padding:6px;color:#374151;'>停機時間</td><td style='padding:6px;color:#374151;'>數天</td><td style='padding:6px;color:#16a34a;font-weight:700;'>計劃停機</td></tr>
        <tr><td style='padding:6px;color:#374151;'>維修成本</td><td style='padding:6px;color:#374151;'>高（緊急）</td><td style='padding:6px;color:#16a34a;font-weight:700;'>低 (-40%)</td></tr>
      </table>
    </div>
    <div style='background:#eff6ff;padding:10px;border-radius:8px;'>
      <p style='color:#1e40af;font-size:0.85rem;margin:0;'>🇹🇼 台灣正加速推動製造業導入 AIoT，「智慧機械」是政府重點產業政策之一。</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 11,
        'chapter': '第二章：AIoT 智慧應用',
        'title': '穿戴裝置與健康科技',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>穿戴裝置與健康科技</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#fef2f2;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#dc2626;font-size:1rem;margin-bottom:10px;'>❤️ Apple Watch 醫療功能</h3>
      <ul style='color:#374151;font-size:0.9rem;padding-left:16px;'>
        <li><strong>ECG 心電圖</strong>：偵測心房顫動</li>
        <li><strong>血氧偵測</strong>：SpO₂ 監測</li>
        <li><strong>跌倒偵測</strong>：自動呼叫救援</li>
        <li><strong>睡眠分析</strong>：深淺睡眠週期</li>
        <li><strong>體溫偵測</strong>（Series 8+）</li>
      </ul>
    </div>
    <div style='background:#eff6ff;padding:10px;border-radius:8px;'>
      <p style='color:#1e40af;font-size:0.85rem;margin:0;'>📰 <strong>台灣案例</strong>：國內多家醫學中心已試辦以智慧手錶遠距監測心律不整、慢性病患者，及早發現異常、減少不必要的回診。</p>
    </div>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:10px;'>🏃 健身科技生態</h3>
      <table style='width:100%;border-collapse:collapse;font-size:0.85rem;'>
        <tr style='background:#15803d;color:#fff;'>
          <th style='padding:6px;'>裝置</th><th style='padding:6px;'>監測項目</th>
        </tr>
        <tr><td style='padding:6px;color:#374151;'>Apple Watch</td><td style='padding:6px;color:#374151;'>心率/ECG/血氧</td></tr>
        <tr style='background:#f0fdf4;'><td style='padding:6px;color:#374151;'>Garmin</td><td style='padding:6px;color:#374151;'>GPS/跑步動態</td></tr>
        <tr><td style='padding:6px;color:#374151;'>Fitbit</td><td style='padding:6px;color:#374151;'>睡眠/步數</td></tr>
        <tr style='background:#f0fdf4;'><td style='padding:6px;color:#374151;'>Oura Ring</td><td style='padding:6px;color:#374151;'>恢復狀態指數</td></tr>
      </table>
    </div>
    <div style='background:#fef9c3;padding:10px;border-radius:8px;'>
      <p style='color:#854d0e;font-size:0.85rem;margin:0;'>⚠️ <strong>隱私思考</strong>：穿戴裝置蒐集你最私密的健康資料，這些資料被儲存在美國/中國的伺服器，你同意嗎？</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 12,
        'chapter': '第二章：AIoT 智慧應用',
        'title': '🎯 第二章 隨堂測驗',
        'bg': 'purple',
        'quiz': 'q2',
        'chart': None,
        'video': None,
        'html': """
<div style='text-align:center;padding:20px;'>
  <div style='font-size:56px;margin-bottom:15px;'>🎯</div>
  <h2 style='color:#fff;font-size:2rem;font-weight:800;margin-bottom:10px;'>第二章 隨堂測驗</h2>
  <p style='color:#e9d5ff;font-size:1.1rem;'>AIoT 智慧應用 ── 2 道題目，點擊作答！</p>
</div>"""
    },
    {
        'id': 13,
        'chapter': '第三章：雲端運算',
        'title': '雲端運算基礎',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>雲端運算基礎</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:8px;'>☁️ 什麼是雲端？</h3>
      <p style='color:#374151;font-size:0.9rem;'>透過網際網路，隨需取用<strong>運算、儲存、資料庫、軟體</strong>等 IT 資源，按使用量付費，不需要自建機房。</p>
    </div>
    <h3 style='color:#374151;font-size:1rem;margin-bottom:10px;'>📊 三種服務模式</h3>
    <div style='display:flex;flex-direction:column;gap:8px;'>
      <div style='background:#fef2f2;padding:10px;border-radius:8px;border-left:3px solid #dc2626;'>
        <p style='font-weight:700;color:#dc2626;font-size:0.9rem;margin:0;'>IaaS — 基礎設施即服務</p>
        <p style='color:#374151;font-size:0.8rem;margin:4px 0 0;'>提供虛擬機、儲存、網路。用戶自管 OS 以上。<br>例：AWS EC2, GCP Compute Engine</p>
      </div>
      <div style='background:#fff7ed;padding:10px;border-radius:8px;border-left:3px solid #ea580c;'>
        <p style='font-weight:700;color:#ea580c;font-size:0.9rem;margin:0;'>PaaS — 平台即服務</p>
        <p style='color:#374151;font-size:0.8rem;margin:4px 0 0;'>提供開發環境，用戶只管應用程式。<br>例：Google App Engine, Heroku</p>
      </div>
      <div style='background:#f0fdf4;padding:10px;border-radius:8px;border-left:3px solid #16a34a;'>
        <p style='font-weight:700;color:#16a34a;font-size:0.9rem;margin:0;'>SaaS — 軟體即服務</p>
        <p style='color:#374151;font-size:0.8rem;margin:4px 0 0;'>直接使用完整軟體，無需安裝。<br>例：Gmail, Google Docs, LINE</p>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#f9fafb;padding:15px;border-radius:10px;margin-bottom:12px;border:1px solid #e5e7eb;'>
      <h3 style='color:#374151;font-size:1rem;margin-bottom:10px;'>🍕 比喻：披薩即服務</h3>
      <table style='width:100%;border-collapse:collapse;font-size:0.85rem;'>
        <tr style='background:#374151;color:#fff;'>
          <th style='padding:6px;'>模式</th><th style='padding:6px;'>你負責</th>
        </tr>
        <tr><td style='padding:6px;color:#374151;'>在家自做</td><td style='padding:6px;color:#374151;'>一切（食材+烤箱+桌椅）</td></tr>
        <tr style='background:#f1f5f9;'><td style='padding:6px;color:#1e40af;font-weight:700;'>IaaS</td><td style='padding:6px;color:#374151;'>食材和烹飪（用店家烤箱）</td></tr>
        <tr><td style='padding:6px;color:#ea580c;font-weight:700;'>PaaS</td><td style='padding:6px;color:#374151;'>只做披薩（烤箱+廚具齊備）</td></tr>
        <tr style='background:#f1f5f9;'><td style='padding:6px;color:#16a34a;font-weight:700;'>SaaS</td><td style='padding:6px;color:#374151;'>直接到店吃（什麼都不管）</td></tr>
      </table>
    </div>
    <div style='background:#eff6ff;padding:10px;border-radius:8px;'>
      <p style='color:#1e40af;font-size:0.85rem;margin:0;'>🌍 全球雲端市場 2024：AWS 31%, Azure 24%, GCP 11%，三大巨頭合計超過 65%。</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 14,
        'chapter': '第三章：雲端運算',
        'title': '公有雲、私有雲、混合雲',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>公有雲、私有雲、混合雲</h2>
<div style='display:grid;grid-template-columns:1fr 1fr 1fr;gap:15px;margin-bottom:15px;'>
  <div style='background:#eff6ff;padding:14px;border-radius:10px;text-align:center;'>
    <div style='font-size:2rem;margin-bottom:6px;'>🌍</div>
    <h3 style='color:#1e40af;font-size:1rem;margin-bottom:8px;'>公有雲</h3>
    <p style='color:#374151;font-size:0.85rem;'>AWS、Azure、GCP 等，由廠商管理，多用戶共用資源</p>
    <div style='background:#dbeafe;padding:6px;border-radius:4px;margin-top:8px;'>
      <p style='color:#1e40af;font-size:0.8rem;margin:0;'>✅ 低成本、快速擴充<br>⚠️ 資料在他人伺服器</p>
    </div>
  </div>
  <div style='background:#f0fdf4;padding:14px;border-radius:10px;text-align:center;'>
    <div style='font-size:2rem;margin-bottom:6px;'>🏠</div>
    <h3 style='color:#15803d;font-size:1rem;margin-bottom:8px;'>私有雲</h3>
    <p style='color:#374151;font-size:0.85rem;'>企業自建機房，完全控制，資料不離開組織</p>
    <div style='background:#dcfce7;padding:6px;border-radius:4px;margin-top:8px;'>
      <p style='color:#15803d;font-size:0.8rem;margin:0;'>✅ 高安全性、客製化<br>⚠️ 建置成本高</p>
    </div>
  </div>
  <div style='background:#fdf4ff;padding:14px;border-radius:10px;text-align:center;'>
    <div style='font-size:2rem;margin-bottom:6px;'>🔄</div>
    <h3 style='color:#7c3aed;font-size:1rem;margin-bottom:8px;'>混合雲</h3>
    <p style='color:#374151;font-size:0.85rem;'>敏感資料放私有雲，一般業務用公有雲</p>
    <div style='background:#e9d5ff;padding:6px;border-radius:4px;margin-top:8px;'>
      <p style='color:#7c3aed;font-size:0.8rem;margin:0;'>✅ 靈活、最佳化成本<br>⚠️ 管理複雜度高</p>
    </div>
  </div>
</div>
<div style='background:#fff7ed;padding:12px;border-radius:8px;border:1px solid #fdba74;'>
  <p style='color:#9a3412;font-size:0.9rem;margin:0;'>🇹🇼 <strong>台灣政府雲</strong>：行政院「G-Cloud」政府私有雲，存放各機關資料；2023 年起開放部分業務遷移至 AWS GovCloud，採混合雲架構。金融業（銀行）受 FSC 規定，核心資料必須留在私有雲。</p>
</div>"""
    },
    {
        'id': 15,
        'chapter': '第三章：雲端運算',
        'title': '雲端儲存與協作',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': {'url': 'https://www.youtube.com/embed/M988_fsOSWo', 'title': '雲端運算介紹', 'desc': '了解雲端運算如何改變現代工作方式'},
        'html': """
<h2 class='slide-title'>雲端儲存與協作工具</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <h3 style='color:#374151;font-size:1rem;margin-bottom:12px;'>💾 主流雲端儲存比較</h3>
    <table style='width:100%;border-collapse:collapse;font-size:0.85rem;'>
      <tr style='background:#374151;color:#fff;'>
        <th style='padding:7px;text-align:left;'>服務</th>
        <th style='padding:7px;text-align:center;'>免費空間</th>
        <th style='padding:7px;text-align:center;'>適合</th>
      </tr>
      <tr><td style='padding:7px;color:#374151;'>Google Drive</td><td style='padding:7px;text-align:center;color:#374151;'>15 GB</td><td style='padding:7px;color:#374151;'>協作文件</td></tr>
      <tr style='background:#f8fafc;'><td style='padding:7px;color:#374151;'>OneDrive</td><td style='padding:7px;text-align:center;color:#374151;'>5 GB</td><td style='padding:7px;color:#374151;'>Office 整合</td></tr>
      <tr><td style='padding:7px;color:#374151;'>Dropbox</td><td style='padding:7px;text-align:center;color:#374151;'>2 GB</td><td style='padding:7px;color:#374151;'>團隊分享</td></tr>
      <tr style='background:#f8fafc;'><td style='padding:7px;color:#374151;'>iCloud Drive</td><td style='padding:7px;text-align:center;color:#374151;'>5 GB</td><td style='padding:7px;color:#374151;'>Apple 生態</td></tr>
      <tr><td style='padding:7px;color:#374151;'>華為雲</td><td style='padding:7px;text-align:center;color:#374151;'>50 GB</td><td style='padding:7px;color:#374151;'>華為設備</td></tr>
    </table>
  </div>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:8px;'>🔒 資料主權問題</h3>
      <p style='color:#374151;font-size:0.9rem;margin-bottom:8px;'>使用美國雲端服務，資料受美國《CLOUD Act》管轄，美國政府可要求取得資料。</p>
      <ul style='color:#374151;font-size:0.85rem;padding-left:16px;margin:0;'>
        <li>歐盟：GDPR 要求資料留在歐洲</li>
        <li>中國：資料必須儲存在境內</li>
        <li>台灣：目前無強制規定，但政府研議中</li>
      </ul>
    </div>
    <div style='background:#fef9c3;padding:10px;border-radius:8px;'>
      <p style='color:#854d0e;font-size:0.85rem;margin:0;'>💡 <strong>3-2-1 備份原則</strong>：3 份備份，2 種媒體，1 份放異地（包含雲端）</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 16,
        'chapter': '第三章：雲端運算',
        'title': '無伺服器運算與 AI 雲端服務',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>雲端 AI 服務的興起</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#fdf4ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#7c3aed;font-size:1rem;margin-bottom:10px;'>🤖 主流雲端 AI 服務</h3>
      <div style='display:flex;flex-direction:column;gap:6px;'>
        <div style='background:#fff;padding:8px;border-radius:6px;border-left:3px solid #7c3aed;'>
          <p style='font-weight:700;color:#7c3aed;font-size:0.85rem;margin:0;'>OpenAI API</p>
          <p style='color:#374151;font-size:0.8rem;margin:2px 0 0;'>GPT-4o、DALL-E 生圖、Whisper 語音辨識</p>
        </div>
        <div style='background:#fff;padding:8px;border-radius:6px;border-left:3px solid #2563eb;'>
          <p style='font-weight:700;color:#2563eb;font-size:0.85rem;margin:0;'>Google Cloud AI</p>
          <p style='color:#374151;font-size:0.8rem;margin:2px 0 0;'>Gemini、Vision API、Speech-to-Text</p>
        </div>
        <div style='background:#fff;padding:8px;border-radius:6px;border-left:3px solid #0369a1;'>
          <p style='font-weight:700;color:#0369a1;font-size:0.85rem;margin:0;'>Azure AI</p>
          <p style='color:#374151;font-size:0.8rem;margin:2px 0 0;'>GPT 企業版、臉部辨識、翻譯服務</p>
        </div>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:10px;'>💡 無伺服器運算（Serverless）</h3>
      <p style='color:#374151;font-size:0.9rem;margin-bottom:8px;'>不需要管理伺服器，只寫「函數」，有請求時才執行，按執行次數付費：</p>
      <ul style='color:#374151;font-size:0.85rem;padding-left:16px;'>
        <li>AWS Lambda</li>
        <li>Google Cloud Functions</li>
        <li>Azure Functions</li>
      </ul>
      <div style='background:#dcfce7;padding:8px;border-radius:6px;margin-top:8px;'>
        <p style='color:#15803d;font-size:0.8rem;margin:0;'>適合：事件驅動型工作（如收到訂單自動寄確認信）</p>
      </div>
    </div>
    <div style='background:#fff7ed;padding:10px;border-radius:8px;'>
      <p style='color:#9a3412;font-size:0.85rem;margin:0;'>🇹🇼 台灣 LINE Bank、玉山銀行、富邦金控均已導入 AI 雲端服務，用於客服機器人、詐騙偵測、信用評分。</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 17,
        'chapter': '第三章：雲端運算',
        'title': '🎯 第三章 隨堂測驗',
        'bg': 'purple',
        'quiz': 'q3',
        'chart': None,
        'video': None,
        'html': """
<div style='text-align:center;padding:20px;'>
  <div style='font-size:56px;margin-bottom:15px;'>🎯</div>
  <h2 style='color:#fff;font-size:2rem;font-weight:800;margin-bottom:10px;'>第三章 隨堂測驗</h2>
  <p style='color:#e9d5ff;font-size:1.1rem;'>雲端運算 ── 2 道題目，點擊作答！</p>
</div>"""
    },
    {
        'id': 18,
        'chapter': '第四章：量子電腦與智慧城市',
        'title': '量子電腦',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>量子電腦</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:8px;'>⚛️ 基本原理</h3>
      <table style='width:100%;border-collapse:collapse;font-size:0.85rem;'>
        <tr style='background:#1e40af;color:#fff;'>
          <th style='padding:6px;'>比較</th><th style='padding:6px;'>傳統電腦</th><th style='padding:6px;'>量子電腦</th>
        </tr>
        <tr><td style='padding:6px;color:#374151;'>基本單位</td><td style='padding:6px;color:#374151;'>位元 (0/1)</td><td style='padding:6px;color:#374151;'>量子位元 (Qubit)</td></tr>
        <tr style='background:#f8fafc;'><td style='padding:6px;color:#374151;'>狀態</td><td style='padding:6px;color:#374151;'>非0即1</td><td style='padding:6px;color:#374151;'>疊加態（0和1同時）</td></tr>
        <tr><td style='padding:6px;color:#374151;'>工作溫度</td><td style='padding:6px;color:#374151;'>室溫</td><td style='padding:6px;color:#374151;'>-273°C（接近絕對零度）</td></tr>
        <tr style='background:#f8fafc;'><td style='padding:6px;color:#374151;'>強項</td><td style='padding:6px;color:#374151;'>通用計算</td><td style='padding:6px;color:#374151;'>特定優化問題</td></tr>
      </table>
    </div>
  </div>
  <div>
    <div style='background:#fdf4ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#7c3aed;font-size:1rem;margin-bottom:10px;'>🎯 量子電腦的強項</h3>
      <ul style='color:#374151;font-size:0.9rem;padding-left:16px;'>
        <li><strong>密碼學</strong>：破解 RSA 加密（目前最大威脅）</li>
        <li><strong>藥物研發</strong>：模擬分子鍵結，加速新藥發現</li>
        <li><strong>最佳化問題</strong>：物流路線規劃、交通號誌優化</li>
        <li><strong>材料科學</strong>：設計新型超導材料</li>
        <li><strong>氣候模擬</strong>：更精準的氣候預測</li>
      </ul>
    </div>
    <div style='background:#fef2f2;padding:10px;border-radius:8px;'>
      <p style='color:#dc2626;font-size:0.85rem;margin:0;'>⚠️ <strong>Harvest Now, Decrypt Later</strong>：駭客正在大量收集加密資料，等量子電腦成熟後再解密，各國政府緊急制定後量子密碼學標準。</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 19,
        'chapter': '第四章：量子電腦與智慧城市',
        'title': '智慧城市',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>智慧城市</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>🏙️ 智慧城市六大面向</h3>
      <div style='display:grid;grid-template-columns:1fr 1fr;gap:8px;'>
        <div style='background:#fff;padding:8px;border-radius:6px;text-align:center;'>
          <div>🚌</div><p style='color:#1e40af;font-size:0.8rem;font-weight:700;margin:4px 0 0;'>智慧交通</p>
        </div>
        <div style='background:#fff;padding:8px;border-radius:6px;text-align:center;'>
          <div>⚡</div><p style='color:#1e40af;font-size:0.8rem;font-weight:700;margin:4px 0 0;'>智慧能源</p>
        </div>
        <div style='background:#fff;padding:8px;border-radius:6px;text-align:center;'>
          <div>🏥</div><p style='color:#1e40af;font-size:0.8rem;font-weight:700;margin:4px 0 0;'>智慧醫療</p>
        </div>
        <div style='background:#fff;padding:8px;border-radius:6px;text-align:center;'>
          <div>🎓</div><p style='color:#1e40af;font-size:0.8rem;font-weight:700;margin:4px 0 0;'>智慧教育</p>
        </div>
        <div style='background:#fff;padding:8px;border-radius:6px;text-align:center;'>
          <div>🌿</div><p style='color:#1e40af;font-size:0.8rem;font-weight:700;margin:4px 0 0;'>智慧環境</p>
        </div>
        <div style='background:#fff;padding:8px;border-radius:6px;text-align:center;'>
          <div>🏛️</div><p style='color:#1e40af;font-size:0.8rem;font-weight:700;margin:4px 0 0;'>智慧治理</p>
        </div>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:10px;'>🇹🇼 台北智慧城市成果</h3>
      <ul style='color:#374151;font-size:0.85rem;padding-left:16px;'>
        <li><strong>YouBike 2.0</strong>：AI 預測補車、即時空位顯示</li>
        <li><strong>智慧路燈</strong>：感測車流自動調光，省電 50%</li>
        <li><strong>垃圾車 IoT</strong>：即時追蹤位置，提前 10 分鐘通知</li>
        <li><strong>智慧停車格</strong>：感測器偵測是否有車，APP 導引</li>
        <li><strong>台北通</strong>：整合 62 種市民服務的 APP</li>
      </ul>
    </div>
    <div style='background:#fef9c3;padding:10px;border-radius:8px;'>
      <p style='color:#854d0e;font-size:0.85rem;margin:0;'>🌍 <strong>全球排名</strong>：台北多次名列 IMD 智慧城市指數全球前段班（新加坡、蘇黎世長年位居前列）。</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 20,
        'chapter': '第四章：量子電腦與智慧城市',
        'title': '智慧城市的隱私爭議',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>智慧城市的隱私爭議</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#fef2f2;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#dc2626;font-size:1rem;margin-bottom:10px;'>👁️ 監控社會的風險</h3>
      <ul style='color:#374151;font-size:0.9rem;padding-left:16px;'>
        <li>人臉辨識攝影機遍布街頭</li>
        <li>智慧電錶洩露生活作息</li>
        <li>手機 GPS 完整移動紀錄</li>
        <li>車牌辨識全面追蹤</li>
      </ul>
      <div style='background:#fee2e2;padding:8px;border-radius:6px;margin-top:8px;'>
        <p style='color:#991b1b;font-size:0.85rem;margin:0;'>中國「社會信用系統」：蒐集公民行為評分，影響出行、就業、貸款資格。</p>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:10px;'>⚖️ 如何平衡？</h3>
      <ul style='color:#374151;font-size:0.9rem;padding-left:16px;'>
        <li>明確的<strong>資料使用目的限制</strong></li>
        <li>市民<strong>知情同意</strong>機制</li>
        <li>資料保存<strong>期限限制</strong></li>
        <li>獨立的<strong>監察委員會</strong></li>
        <li>資料收集<strong>最小化原則</strong></li>
      </ul>
    </div>
    <div style='background:#eff6ff;padding:12px;border-radius:8px;'>
      <p style='color:#1e40af;font-size:0.85rem;margin:0;'>🗣️ <strong>討論題</strong>：台北市要在每個路口安裝 AI 攝影機以改善交通安全，你支持還是反對？請用「利」與「弊」各舉一個理由。</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 21,
        'chapter': '第四章：量子電腦與智慧城市',
        'title': '元宇宙與數位孿生',
        'bg': 'white',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 class='slide-title'>元宇宙與數位孿生</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#fdf4ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#7c3aed;font-size:1rem;margin-bottom:10px;'>🌐 元宇宙（Metaverse）</h3>
      <p style='color:#374151;font-size:0.9rem;margin-bottom:8px;'>結合 VR/AR/MR 的<strong>持續性虛擬世界</strong>，可在其中工作、社交、購物、娛樂。</p>
      <ul style='color:#374151;font-size:0.85rem;padding-left:16px;'>
        <li>Meta Quest VR 頭盔</li>
        <li>Fortnite、Roblox 遊戲元宇宙</li>
        <li>虛擬演唱會（Travis Scott 1,200 萬人）</li>
        <li>虛擬辦公室 Horizon Workrooms</li>
      </ul>
    </div>
  </div>
  <div>
    <div style='background:#fff7ed;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#ea580c;font-size:1rem;margin-bottom:10px;'>🏭 數位孿生（Digital Twin）</h3>
      <p style='color:#374151;font-size:0.9rem;margin-bottom:8px;'>在虛擬世界建立真實物體的<strong>精確數位副本</strong>，即時同步現實資料。</p>
      <ul style='color:#374151;font-size:0.85rem;padding-left:16px;'>
        <li>台積電廠房數位孿生：VR 監控產線</li>
        <li>台北港口數位孿生：模擬裝卸流程</li>
        <li>新加坡整個城市數位孿生</li>
        <li>波音飛機數位孿生：預測維修</li>
      </ul>
    </div>
    <div style='background:#eff6ff;padding:10px;border-radius:8px;'>
      <p style='color:#1e40af;font-size:0.85rem;margin:0;'>💡 數位孿生 + AIoT + 5G = 未來智慧城市的核心技術組合</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 22,
        'chapter': '第四章：量子電腦與智慧城市',
        'title': '🎯 第四章 隨堂測驗',
        'bg': 'purple',
        'quiz': 'q4',
        'chart': None,
        'video': None,
        'html': """
<div style='text-align:center;padding:20px;'>
  <div style='font-size:56px;margin-bottom:15px;'>🎯</div>
  <h2 style='color:#fff;font-size:2rem;font-weight:800;margin-bottom:10px;'>第四章 隨堂測驗</h2>
  <p style='color:#e9d5ff;font-size:1.1rem;'>量子電腦與智慧城市 ── 2 道題目，點擊作答！</p>
</div>"""
    },
    {
        'id': 23,
        'chapter': '分組實作',
        'title': '分組實作：AIoT 案例探討',
        'bg': 'teal',
        'quiz': None,
        'chart': None,
        'video': None,
        'html': """
<h2 style='font-size:1.8rem;font-weight:800;color:#fff;margin-bottom:20px;text-align:center;'>🔬 分組實作：AIoT 案例探討</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div style='background:rgba(255,255,255,0.15);padding:18px;border-radius:12px;'>
    <h3 style='color:#fff;font-size:1rem;margin-bottom:14px;'>📋 探討流程</h3>
    <div style='display:flex;flex-direction:column;gap:10px;'>
      <div style='background:rgba(255,255,255,0.2);padding:10px;border-radius:8px;'>
        <p style='color:#fff;font-weight:700;font-size:0.9rem;margin:0 0 4px;'>步驟一：選擇案例（從以下選一）</p>
        <ul style='color:#cffafe;font-size:0.8rem;margin:0;padding-left:16px;'>
          <li>台北 YouBike 智慧調度系統</li>
          <li>台積電智慧製造 AIoT</li>
          <li>台南白河農業 AIoT</li>
          <li>高雄港智慧物流</li>
          <li>醫院穿戴裝置遠距監測</li>
        </ul>
      </div>
      <div style='background:rgba(255,255,255,0.2);padding:10px;border-radius:8px;'>
        <p style='color:#fff;font-weight:700;font-size:0.9rem;margin:0 0 4px;'>步驟二：分析（填入報告表）</p>
        <ul style='color:#cffafe;font-size:0.8rem;margin:0;padding-left:16px;'>
          <li>使用了哪些感測器？</li>
          <li>資料如何傳輸和儲存？</li>
          <li>AI 如何分析並決策？</li>
          <li>帶來了什麼效益？</li>
        </ul>
      </div>
      <div style='background:rgba(255,255,255,0.2);padding:10px;border-radius:8px;'>
        <p style='color:#fff;font-weight:700;font-size:0.9rem;margin:0 0 4px;'>步驟三：延伸創意</p>
        <p style='color:#cffafe;font-size:0.8rem;margin:0;'>提出一個「芳和實中 AIoT 應用」的想法，說明要解決什麼問題。</p>
      </div>
    </div>
  </div>
  <div>
    <div style='background:rgba(255,255,255,0.15);padding:15px;border-radius:12px;margin-bottom:12px;'>
      <h3 style='color:#fff;font-size:1rem;margin-bottom:10px;'>📝 報告格式（Google 簡報 3 頁）</h3>
      <ol style='color:#cffafe;font-size:0.85rem;padding-left:16px;margin:0;'>
        <li>案例背景：問題是什麼？</li>
        <li>AIoT 解決方案：技術架構圖</li>
        <li>成效數據 + 你的創意延伸</li>
      </ol>
    </div>
    <div style='background:rgba(255,255,255,0.15);padding:12px;border-radius:10px;'>
      <h3 style='color:#fff;font-size:0.9rem;margin-bottom:8px;'>🏆 評分標準（100 分）</h3>
      <ul style='color:#cffafe;font-size:0.85rem;padding-left:16px;margin:0;'>
        <li>案例理解正確完整 <strong style='color:#fff;'>30 分</strong></li>
        <li>技術架構說明清晰 <strong style='color:#fff;'>30 分</strong></li>
        <li>效益數據引用正確 <strong style='color:#fff;'>20 分</strong></li>
        <li>創意延伸可行性 <strong style='color:#fff;'>20 分</strong></li>
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
<h2 style='font-size:1.8rem;font-weight:800;color:#fff;margin-bottom:20px;text-align:center;'>📖 Week 7 重點回顧</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:15px;'>
  <div style='background:rgba(255,255,255,0.12);padding:14px;border-radius:10px;'>
    <h3 style='color:#93c5fd;font-size:1rem;margin-bottom:8px;'>第一章 物聯網 IoT</h3>
    <ul style='color:#e2e8f0;font-size:0.85rem;padding-left:16px;margin:0;'>
      <li>感測器→連網→雲端→應用四要素</li>
      <li>IoT 安全三弱點：預設密碼/不更新/未加密</li>
      <li>邊緣運算解決低延遲需求</li>
    </ul>
  </div>
  <div style='background:rgba(255,255,255,0.12);padding:14px;border-radius:10px;'>
    <h3 style='color:#93c5fd;font-size:1rem;margin-bottom:8px;'>第二章 AIoT</h3>
    <ul style='color:#e2e8f0;font-size:0.85rem;padding-left:16px;margin:0;'>
      <li>IoT 感知 + AI 決策 = AIoT</li>
      <li>台灣農業/製造/醫療案例豐富</li>
      <li>預測維護大幅降低停機損失</li>
    </ul>
  </div>
  <div style='background:rgba(255,255,255,0.12);padding:14px;border-radius:10px;'>
    <h3 style='color:#93c5fd;font-size:1rem;margin-bottom:8px;'>第三章 雲端運算</h3>
    <ul style='color:#e2e8f0;font-size:0.85rem;padding-left:16px;margin:0;'>
      <li>IaaS/PaaS/SaaS 三層服務模式</li>
      <li>公有雲成本低，私有雲安全高</li>
      <li>資料主權是全球重要議題</li>
    </ul>
  </div>
  <div style='background:rgba(255,255,255,0.12);padding:14px;border-radius:10px;'>
    <h3 style='color:#93c5fd;font-size:1rem;margin-bottom:8px;'>第四章 量子與智慧城市</h3>
    <ul style='color:#e2e8f0;font-size:0.85rem;padding-left:16px;margin:0;'>
      <li>量子位元利用疊加態並行計算</li>
      <li>台北智慧城市名列全球前段班</li>
      <li>監控與隱私須審慎平衡</li>
    </ul>
  </div>
</div>
<div style='background:rgba(255,255,255,0.1);padding:12px;border-radius:8px;margin-top:15px;text-align:center;'>
  <p style='color:#bfdbfe;font-size:0.95rem;margin:0;'>下週預告：<strong style='color:#fff;'>巨量資料與資料科學</strong> ── Big Data、Open Data、資料清理、視覺化</p>
</div>"""
    }
]
