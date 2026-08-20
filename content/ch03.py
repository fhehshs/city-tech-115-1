# -*- coding: utf-8 -*-
# Ch.3: 個人資料保護與資訊倫理

CHAPTERS = [
    {'name': '封面', 'start': 1},
    {'name': '第一章：個人資料與隱私', 'start': 2},
    {'name': '第二章：個資法與法律保護', 'start': 8},
    {'name': '第三章：資安威脅與攻擊', 'start': 14},
    {'name': '第四章：資訊倫理', 'start': 19},
    {'name': '分組實作', 'start': 23},
]

QUIZZES = {
    'q1': {
        'title': '第一章 隨堂測驗',
        'questions': [
            {
                'q': '下列哪一項「不屬於」個人資料保護法所定義的個人資料？',
                'options': ['姓名', '身分證字號', '某本書的 ISBN 書號', '電話號碼'],
                'answer': 2,
                'explain': '個資法定義的個人資料是指「足以識別自然人身份」的資訊，包括姓名、身分證字號、電話、地址、照片、指紋等。ISBN 書號是識別書籍的編號，並非個人資料。'
            },
            {
                'q': 'Cookie 的主要功能是什麼？',
                'options': ['加密傳輸資料，保護安全', '記錄使用者在網站的行為與偏好，讓網站「記住」你', '阻擋惡意廣告', '加快網頁載入速度'],
                'answer': 1,
                'explain': 'Cookie 是網站儲存在你瀏覽器中的小型文字檔，用來記住登入狀態、購物車內容、語言偏好等。但也可能被用於追蹤你的瀏覽行為，因此 GDPR 規定網站需要取得你的同意。'
            },
        ]
    },
    'q2': {
        'title': '第二章 隨堂測驗',
        'questions': [
            {
                'q': '台灣個人資料保護法中，個資蒐集需具備的條件是？',
                'options': ['需有特定目的，且當事人已同意或有法定事由', '只要是商業用途即可蒐集', '政府機關可以不需同意直接蒐集', '在網路上公開的資料可以任意使用'],
                'answer': 0,
                'explain': '台灣個資法規定，蒐集、處理個人資料需有「特定目的」，且原則上需取得當事人同意，或符合法定特定情形（如公務機關執行職務）。在網路公開的資料也受到保護，不能任意用於其他目的。'
            },
            {
                'q': '歐盟 GDPR 賦予使用者哪項重要權利？',
                'options': ['瀏覽任何網站的權利', '免費使用所有數位服務的權利', '要求公司分享競爭對手資訊的權利', '被遺忘權：要求刪除個人資料'],
                'answer': 3,
                'explain': 'GDPR（歐盟一般資料保護規則）賦予使用者「被遺忘權」（Right to be forgotten）：可以要求企業刪除自己的個人資料。違反 GDPR 的企業可被處以高額罰款，對台灣企業做歐洲市場也適用。'
            },
        ]
    },
    'q3': {
        'title': '第三章 隨堂測驗',
        'questions': [
            {
                'q': '「釣魚攻擊（Phishing）」是指什麼？',
                'options': ['使用高效能電腦暴力破解密碼', '假冒合法機構發送郵件或建立假網站，誘騙使用者輸入帳號密碼', '在公共 WiFi 上監聽他人網路流量', '植入病毒鎖住電腦勒索金錢'],
                'answer': 1,
                'explain': '釣魚攻擊是最常見的社交工程攻擊：駭客假冒銀行、政府、LINE 等機構，發送看似真實的郵件或訊息，誘使你點擊假連結並輸入個人資訊。識別方法：仔細檢查寄件人網域、不隨意點擊連結。'
            },
            {
                'q': '勒索軟體（Ransomware）的攻擊方式是？',
                'options': ['加密受害者電腦中的檔案，要求支付贖金才解鎖', '竊取信用卡資料後立即消費', '讓電腦過熱損壞硬體', '在社群媒體發布假新聞'],
                'answer': 0,
                'explain': '勒索軟體會加密你電腦的所有檔案，使你無法開啟，然後要求支付比特幣換取解密金鑰。2017 年 WannaCry 攻擊影響全球 150 國。預防方式：定期備份、不開可疑附件、維持系統更新。'
            },
        ]
    },
    'q4': {
        'title': '第四章 隨堂測驗',
        'questions': [
            {
                'q': '使用 AI 工具生成的圖片，著作權歸屬是？',
                'options': ['永遠歸屬於 AI 工具的開發公司', '永遠歸屬於輸入提示詞的使用者', 'AI 生成的作品無法使用，使用即違法', '目前法律尚未明確，各國見解不一，通常認為純 AI 生成不受著作權保護'],
                'answer': 3,
                'explain': '這是當前著作權法的灰色地帶。美國著作權局認為純 AI 生成（無人工創作成分）不受保護；台灣法律尚未明文規定。使用 AI 工具時需注意：了解平台授權條款、標示 AI 生成，以及避免讓 AI 模仿特定藝術家風格。'
            },
            {
                'q': '以下哪個行為符合資訊倫理？',
                'options': ['下載付費軟體的破解版自用', '未經同意將朋友照片上傳至公開社群', '引用網路文章時標明原作者與來源', '用 AI 寫作業但不告知老師'],
                'answer': 2,
                'explain': '資訊倫理的核心包括：尊重著作權（引用須標明來源）、尊重隱私（不擅自分享他人照片）、誠信原則（學術誠信）、不侵犯智慧財產（不使用破解軟體）。符合倫理的行為是引用時標明來源。'
            },
        ]
    },
}

SLIDES = [
    {
        'id': 1, 'chapter': '封面', 'title': '個人資料保護與資訊倫理',
        'bg': 'navy', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<div style='text-align:center;padding:30px 20px;'>
  <div style='font-size:72px;margin-bottom:20px;'>🔒</div>
  <h1 style='font-size:2.8rem;font-weight:900;color:#fff;margin-bottom:12px;'>個人資料保護與資訊倫理</h1>
  <h2 style='font-size:1.5rem;font-weight:400;color:#93c5fd;margin-bottom:30px;'>Personal Data Protection &amp; Information Ethics</h2>
  <div style='display:flex;justify-content:center;gap:20px;flex-wrap:wrap;margin-bottom:30px;'>
    <span style='background:rgba(255,255,255,0.15);color:#e0f2fe;padding:8px 20px;border-radius:20px;font-size:1rem;'>🛡️ 個資法</span>
    <span style='background:rgba(255,255,255,0.15);color:#e0f2fe;padding:8px 20px;border-radius:20px;font-size:1rem;'>🎣 釣魚攻擊</span>
    <span style='background:rgba(255,255,255,0.15);color:#e0f2fe;padding:8px 20px;border-radius:20px;font-size:1rem;'>⚖️ 資訊倫理</span>
  </div>
  <p style='color:#bfdbfe;font-size:1.1rem;'>城市科技 — 第三章</p>
</div>"""
    },
    {
        'id': 2, 'chapter': '第一章：個人資料與隱私', 'title': '什麼是個人資料？',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>什麼是個人資料？</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>📋 個資法定義</h3>
      <p style='color:#374151;font-size:.9rem;margin-bottom:10px;'>「足以識別自然人身份的任何資訊」</p>
      <div style='display:grid;grid-template-columns:1fr 1fr;gap:6px;'>
        <div style='background:#dbeafe;padding:6px;border-radius:6px;font-size:.8rem;color:#1e40af;text-align:center;'>👤 姓名</div>
        <div style='background:#dbeafe;padding:6px;border-radius:6px;font-size:.8rem;color:#1e40af;text-align:center;'>🪪 身分證字號</div>
        <div style='background:#dbeafe;padding:6px;border-radius:6px;font-size:.8rem;color:#1e40af;text-align:center;'>📱 手機號碼</div>
        <div style='background:#dbeafe;padding:6px;border-radius:6px;font-size:.8rem;color:#1e40af;text-align:center;'>📍 住址</div>
        <div style='background:#dbeafe;padding:6px;border-radius:6px;font-size:.8rem;color:#1e40af;text-align:center;'>📷 照片</div>
        <div style='background:#dbeafe;padding:6px;border-radius:6px;font-size:.8rem;color:#1e40af;text-align:center;'>🩺 健康資料</div>
        <div style='background:#fde047;padding:6px;border-radius:6px;font-size:.8rem;color:#854d0e;text-align:center;font-weight:700;'>🌐 IP 位址</div>
        <div style='background:#fde047;padding:6px;border-radius:6px;font-size:.8rem;color:#854d0e;text-align:center;font-weight:700;'>📧 電子郵件</div>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#fef2f2;padding:15px;border-radius:10px;border:1px solid #fecaca;'>
      <h3 style='color:#dc2626;font-size:1rem;margin-bottom:10px;'>⚠️ 特種個資（更嚴格保護）</h3>
      <ul style='color:#374151;font-size:.88rem;padding-left:16px;'>
        <li>病歷、醫療資訊、基因</li>
        <li>性生活與性取向</li>
        <li>健康檢查結果</li>
        <li>犯罪前科</li>
        <li>政治意見、宗教信仰</li>
        <li>工會會員身分</li>
      </ul>
      <div style='background:#fee2e2;padding:8px;border-radius:6px;margin-top:8px;'>
        <p style='color:#dc2626;font-size:.8rem;margin:0;'>蒐集特種個資需更嚴格的法定事由</p>
      </div>
    </div>
  </div>
</div>"""
    },
    {
        'id': 3, 'chapter': '第一章：個人資料與隱私', 'title': 'Cookie 是什麼？',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>Cookie：網站記住你的方式</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#fff7ed;padding:15px;border-radius:10px;border:1px solid #fed7aa;margin-bottom:12px;'>
      <h3 style='color:#ea580c;font-size:1rem;margin-bottom:10px;'>🍪 Cookie 是什麼？</h3>
      <p style='color:#374151;font-size:.88rem;margin-bottom:8px;'>網站在你瀏覽器存放的小型文字檔，記錄：</p>
      <ul style='color:#374151;font-size:.83rem;padding-left:16px;'>
        <li>你的登入狀態（讓你不用每次重新登入）</li>
        <li>購物車內容</li>
        <li>語言與地區偏好</li>
        <li>你的瀏覽行為與喜好（廣告追蹤）</li>
      </ul>
    </div>
    <div style='background:#fef9c3;padding:10px;border-radius:8px;'>
      <p style='color:#854d0e;font-size:.85rem;margin:0;'>💡 為什麼網站要你同意 Cookie？歐盟 GDPR 規定，追蹤性 Cookie 需取得明確同意。</p>
    </div>
  </div>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>🔍 Cookie 的種類</h3>
      <div style='display:flex;flex-direction:column;gap:8px;font-size:.83rem;'>
        <div style='background:#dcfce7;padding:8px;border-radius:6px;'><strong style='color:#15803d;'>必要性 Cookie</strong><br><span style='color:#374151;'>維持網站基本功能（登入狀態），不需同意</span></div>
        <div style='background:#fde047;padding:8px;border-radius:6px;'><strong style='color:#854d0e;'>功能性 Cookie</strong><br><span style='color:#374151;'>記住你的偏好（語言、字體大小）</span></div>
        <div style='background:#fee2e2;padding:8px;border-radius:6px;'><strong style='color:#dc2626;'>追蹤性 Cookie</strong><br><span style='color:#374151;'>跨網站追蹤行為，用於精準廣告</span></div>
      </div>
    </div>
  </div>
</div>"""
    },
    {
        'id': 4, 'chapter': '第一章：個人資料與隱私', 'title': '數位足跡',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>你的數位足跡</h2>
<div style='background:#1e293b;padding:20px;border-radius:12px;margin-bottom:16px;'>
  <h3 style='color:#94a3b8;font-size:.85rem;text-align:center;margin-bottom:16px;letter-spacing:.05em;'>一個普通的一天，你留下了多少數位足跡？</h3>
  <div style='display:grid;grid-template-columns:repeat(4,1fr);gap:10px;'>
    <div style='background:#0f172a;padding:12px;border-radius:8px;text-align:center;border-left:3px solid #3b82f6;'>
      <div style='font-size:1.6rem;'>📱</div>
      <p style='color:#93c5fd;font-size:.72rem;margin-top:4px;'>手機開機<br>IMEI 被記錄</p>
    </div>
    <div style='background:#0f172a;padding:12px;border-radius:8px;text-align:center;border-left:3px solid #22c55e;'>
      <div style='font-size:1.6rem;'>🏷️</div>
      <p style='color:#86efac;font-size:.72rem;margin-top:4px;'>悠遊卡刷卡<br>時間地點被記錄</p>
    </div>
    <div style='background:#0f172a;padding:12px;border-radius:8px;text-align:center;border-left:3px solid #f59e0b;'>
      <div style='font-size:1.6rem;'>🔍</div>
      <p style='color:#fcd34d;font-size:.72rem;margin-top:4px;'>Google 搜尋<br>關鍵字被記錄</p>
    </div>
    <div style='background:#0f172a;padding:12px;border-radius:8px;text-align:center;border-left:3px solid #f472b6;'>
      <div style='font-size:1.6rem;'>📷</div>
      <p style='color:#f9a8d4;font-size:.72rem;margin-top:4px;'>IG 上傳照片<br>臉部特徵被掃描</p>
    </div>
  </div>
</div>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:12px;'>
  <div style='background:#eff6ff;padding:12px;border-radius:8px;'>
    <p style='color:#1e40af;font-size:.88rem;font-weight:700;margin-bottom:6px;'>😱 你知道嗎？</p>
    <p style='color:#374151;font-size:.82rem;'>Google 知道你 5 年前在哪裡、搜尋什麼、看什麼影片。可至 myactivity.google.com 查看。</p>
  </div>
  <div style='background:#f0fdf4;padding:12px;border-radius:8px;'>
    <p style='color:#15803d;font-size:.88rem;font-weight:700;margin-bottom:6px;'>🛡️ 保護建議</p>
    <p style='color:#374151;font-size:.82rem;'>定期清除瀏覽記錄、使用私人瀏覽模式、檢視 App 所要求的權限。</p>
  </div>
</div>"""
    },
    {
        'id': 5, 'chapter': '第一章：個人資料與隱私', 'title': '隱私權的重要性',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>隱私權：現代社會的基本人權</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-bottom:16px;'>
  <div style='background:#eff6ff;padding:15px;border-radius:10px;'>
    <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>📰 真實案例</h3>
    <div style='display:flex;flex-direction:column;gap:8px;'>
      <div style='background:#fff;padding:10px;border-radius:8px;border-left:3px solid #dc2626;'>
        <p style='color:#dc2626;font-size:.82rem;font-weight:700;margin:0 0 3px;'>Facebook — Cambridge Analytica 醜聞</p>
        <p style='color:#374151;font-size:.78rem;margin:0;'>8700 萬用戶個資被用於操控美國總統選舉，Facebook 被罰 50 億美元。</p>
      </div>
      <div style='background:#fff;padding:10px;border-radius:8px;border-left:3px solid #f59e0b;'>
        <p style='color:#ea580c;font-size:.82rem;font-weight:700;margin:0 0 3px;'>台灣健保資料庫外洩事件</p>
        <p style='color:#374151;font-size:.78rem;margin:0;'>全民健保資料庫將 2,300 萬人的就醫資料提供學術研究使用，因未經當事人同意，2022 年憲法法庭判決部分違憲，要求建立獨立監督機制與退出權。</p>
      </div>
    </div>
  </div>
  <div style='background:#f0fdf4;padding:15px;border-radius:10px;'>
    <h3 style='color:#15803d;font-size:1rem;margin-bottom:10px;'>🛡️ 個人可以怎麼做？</h3>
    <div style='display:flex;flex-direction:column;gap:6px;font-size:.83rem;'>
      <div style='background:#dcfce7;padding:8px;border-radius:6px;color:#15803d;'>✅ 使用強密碼 + 兩步驟驗證</div>
      <div style='background:#dcfce7;padding:8px;border-radius:6px;color:#15803d;'>✅ 定期更新作業系統和 App</div>
      <div style='background:#dcfce7;padding:8px;border-radius:6px;color:#15803d;'>✅ 不使用公共 WiFi 進行金融交易</div>
      <div style='background:#dcfce7;padding:8px;border-radius:6px;color:#15803d;'>✅ 謹慎授權 App 存取相機/位置</div>
      <div style='background:#dcfce7;padding:8px;border-radius:6px;color:#15803d;'>✅ 不在社群媒體過度分享個人資訊</div>
    </div>
  </div>
</div>"""
    },
    {
        'id': 6, 'chapter': '第一章：個人資料與隱私', 'title': '個資外洩有多常見？',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>個資外洩：比你想像的還要普遍</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#fef2f2;padding:15px;border-radius:10px;border:1px solid #fecaca;margin-bottom:12px;'>
      <h3 style='color:#dc2626;font-size:1rem;margin-bottom:10px;'>🌍 全球重大外洩事件</h3>
      <table style='width:100%;border-collapse:collapse;font-size:.8rem;'>
        <tr style='background:#dc2626;color:#fff;'><th style='padding:6px;'>企業</th><th style='padding:6px;'>年份</th><th style='padding:6px;'>外洩筆數</th></tr>
        <tr><td style='padding:5px;color:#374151;'>Yahoo</td><td style='padding:5px;color:#374151;'>2016</td><td style='padding:5px;color:#dc2626;font-weight:700;'>30 億筆</td></tr>
        <tr style='background:#fef2f2;'><td style='padding:5px;color:#374151;'>LinkedIn</td><td style='padding:5px;color:#374151;'>2021</td><td style='padding:5px;color:#dc2626;font-weight:700;'>7億筆</td></tr>
        <tr><td style='padding:5px;color:#374151;'>Facebook</td><td style='padding:5px;color:#374151;'>2021</td><td style='padding:5px;color:#dc2626;font-weight:700;'>5.3億筆</td></tr>
        <tr style='background:#fef2f2;'><td style='padding:5px;color:#374151;'>台灣某電商</td><td style='padding:5px;color:#374151;'>2023</td><td style='padding:5px;color:#dc2626;font-weight:700;'>2,000萬筆</td></tr>
      </table>
    </div>
  </div>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>🔍 你的資料有沒有外洩？</h3>
      <p style='color:#374151;font-size:.88rem;margin-bottom:10px;'>可以使用 <strong>Have I Been Pwned</strong>（haveibeenpwned.com）輸入你的電子郵件，查詢是否出現在已知的外洩資料庫中。</p>
      <div style='background:#dbeafe;padding:10px;border-radius:8px;'>
        <p style='color:#1e40af;font-size:.82rem;margin:0;'>⚠️ 若帳號出現外洩，立即更改密碼並啟用兩步驟驗證！</p>
      </div>
    </div>
  </div>
</div>"""
    },
    {
        'id': 7, 'chapter': '第一章：個人資料與隱私', 'title': '🎯 第一章 隨堂測驗',
        'bg': 'purple', 'quiz': 'q1', 'chart': None, 'video': None,
        'html': """
<div style='text-align:center;padding:20px;'>
  <div style='font-size:56px;margin-bottom:15px;'>🎯</div>
  <h2 style='color:#fff;font-size:2rem;font-weight:800;margin-bottom:10px;'>第一章 隨堂測驗</h2>
  <p style='color:#e9d5ff;font-size:1.1rem;'>個人資料與隱私 ── 2 道題目，點擊作答！</p>
</div>"""
    },
    {
        'id': 8, 'chapter': '第二章：個資法與法律保護', 'title': '台灣個資法',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>台灣個人資料保護法</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>📜 重要條文</h3>
      <div class='layer-stack'>
        <div class='layer layer-user'><div class='layer-num'>§</div><div><div class='layer-name' style='color:#374151;'>蒐集須有特定目的</div><div class='layer-detail'>不能蒐集超出必要範圍的個資</div></div></div>
        <div class='layer layer-app'><div class='layer-num'>§</div><div><div class='layer-name' style='color:#374151;'>當事人查閱權</div><div class='layer-detail'>可要求查閱、更正自己的個資</div></div></div>
        <div class='layer layer-os'><div class='layer-num'>§</div><div><div class='layer-name' style='color:#374151;'>刪除與停止使用</div><div class='layer-detail'>可要求刪除不必要的個資</div></div></div>
        <div class='layer layer-hw'><div class='layer-num'>§</div><div><div class='layer-name' style='color:#374151;'>違反者民刑事責任</div><div class='layer-detail'>意圖不法利益而違法利用個資，最重可處 5 年以下有期徒刑</div></div></div>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:10px;'>⚖️ 歐盟 GDPR vs 台灣個資法</h3>
      <table style='width:100%;border-collapse:collapse;font-size:.8rem;'>
        <tr style='background:#15803d;color:#fff;'><th style='padding:6px;'>項目</th><th style='padding:6px;'>GDPR</th><th style='padding:6px;'>台灣個資法</th></tr>
        <tr><td style='padding:5px;color:#374151;'>執行</td><td style='padding:5px;color:#374151;'>2018</td><td style='padding:5px;color:#374151;'>2012 施行（2023 修正）</td></tr>
        <tr style='background:#f0fdf4;'><td style='padding:5px;color:#374151;'>被遺忘權</td><td style='padding:5px;color:#15803d;font-weight:700;'>✅</td><td style='padding:5px;color:#374151;'>部分支援</td></tr>
        <tr><td style='padding:5px;color:#374151;'>最高罰款</td><td style='padding:5px;color:#374151;'>2,000 萬歐元或全球營業額 4%</td><td style='padding:5px;color:#374151;'>1,500 萬台幣（2023 修法後）</td></tr>
      </table>
    </div>
  </div>
</div>"""
    },
    {
        'id': 9, 'chapter': '第二章：個資法與法律保護', 'title': '個資法實際案例',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>個資法違規的真實案例</h2>
<div style='display:flex;flex-direction:column;gap:12px;'>
  <div style='background:#fef2f2;padding:14px;border-radius:10px;border-left:4px solid #dc2626;'>
    <div style='display:flex;justify-content:space-between;align-items:start;'>
      <div>
        <p style='color:#dc2626;font-weight:700;font-size:.9rem;margin-bottom:5px;'>案例一：某補習班出售學生資料</p>
        <p style='color:#374151;font-size:.85rem;'>某補習班將學生姓名、電話、成績賣給其他業者行銷，違反個資法第20條。<br><strong>結果</strong>：負責人被起訴，處有期徒刑8個月，緩刑2年。</p>
      </div>
    </div>
  </div>
  <div style='background:#fff7ed;padding:14px;border-radius:10px;border-left:4px solid #f59e0b;'>
    <p style='color:#ea580c;font-weight:700;font-size:.9rem;margin-bottom:5px;'>案例二：員工盜用客戶個資</p>
    <p style='color:#374151;font-size:.85rem;'>銀行員工盜取客戶資料轉賣詐騙集團，被害人接到詐騙電話損失慘重。<br><strong>結果</strong>：涉案員工依個資法及詐欺罪起訴，判處4年有期徒刑。</p>
  </div>
  <div style='background:#eff6ff;padding:14px;border-radius:10px;border-left:4px solid #2563eb;'>
    <p style='color:#1e40af;font-weight:700;font-size:.9rem;margin-bottom:5px;'>案例三：蒐集超出必要範圍</p>
    <p style='color:#374151;font-size:.85rem;'>某電商平台在結帳時強制要求顧客填寫身分證字號，遭檢舉超出必要蒐集範圍。<br><strong>結果</strong>：被主管機關要求改善，並處以罰鍰。</p>
  </div>
</div>"""
    },
    {
        'id': 10, 'chapter': '第二章：個資法與法律保護', 'title': '網路著作權',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>網路著作權：你真的「擁有」那張圖嗎？</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>©️ 著作權基本概念</h3>
      <ul style='color:#374151;font-size:.85rem;padding-left:16px;'>
        <li>創作者完成作品即自動受到著作權保護</li>
        <li><strong>不需要</strong>特別標示 © 才受保護</li>
        <li>網路上的圖片、文章、音樂都有著作權</li>
        <li>保護期間：著作人生存期間 + 50 年</li>
      </ul>
    </div>
    <div style='background:#f0fdf4;padding:12px;border-radius:8px;'>
      <h3 style='color:#15803d;font-size:.95rem;margin-bottom:8px;'>✅ 合法使用方式</h3>
      <ul style='color:#374151;font-size:.83rem;padding-left:14px;'>
        <li>取得作者授權</li>
        <li>使用 Creative Commons 授權作品</li>
        <li>引用時標明來源</li>
        <li>合理使用（教育、評論、新聞）</li>
      </ul>
    </div>
  </div>
  <div>
    <div style='background:#fef2f2;padding:15px;border-radius:10px;'>
      <h3 style='color:#dc2626;font-size:1rem;margin-bottom:10px;'>❌ 常見違法行為</h3>
      <div style='display:flex;flex-direction:column;gap:8px;font-size:.83rem;'>
        <div style='background:#fee2e2;padding:8px;border-radius:6px;color:#dc2626;'>下載 YouTube 影片並重新上傳</div>
        <div style='background:#fee2e2;padding:8px;border-radius:6px;color:#dc2626;'>將 Google 搜到的圖片直接用於商業用途</div>
        <div style='background:#fee2e2;padding:8px;border-radius:6px;color:#dc2626;'>複製文章內容而不標明來源</div>
        <div style='background:#fee2e2;padding:8px;border-radius:6px;color:#dc2626;'>用 AI 生成歌手的假聲音</div>
      </div>
    </div>
  </div>
</div>"""
    },
    {
        'id': 11, 'chapter': '第二章：個資法與法律保護', 'title': '密碼安全',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>密碼安全：你的帳號有多安全？</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#fef2f2;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#dc2626;font-size:1rem;margin-bottom:10px;'>😱 最糟糕的密碼（每年都榜上有名）</h3>
      <div style='display:grid;grid-template-columns:1fr 1fr;gap:4px;font-size:.82rem;'>
        <div style='background:#fee2e2;padding:5px 8px;border-radius:5px;color:#dc2626;font-family:monospace;'>123456</div>
        <div style='background:#fee2e2;padding:5px 8px;border-radius:5px;color:#dc2626;font-family:monospace;'>password</div>
        <div style='background:#fee2e2;padding:5px 8px;border-radius:5px;color:#dc2626;font-family:monospace;'>qwerty</div>
        <div style='background:#fee2e2;padding:5px 8px;border-radius:5px;color:#dc2626;font-family:monospace;'>111111</div>
        <div style='background:#fee2e2;padding:5px 8px;border-radius:5px;color:#dc2626;font-family:monospace;'>abc123</div>
        <div style='background:#fee2e2;padding:5px 8px;border-radius:5px;color:#dc2626;font-family:monospace;'>iloveyou</div>
      </div>
      <p style='color:#dc2626;font-size:.78rem;margin-top:8px;'>這些密碼在 1 秒內即可被破解！</p>
    </div>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:10px;'>🔒 強密碼的標準</h3>
      <div style='display:flex;flex-direction:column;gap:6px;font-size:.83rem;'>
        <div style='background:#dcfce7;padding:6px;border-radius:5px;color:#15803d;'>✅ 長度至少 12 個字元</div>
        <div style='background:#dcfce7;padding:6px;border-radius:5px;color:#15803d;'>✅ 混合大小寫、數字、符號</div>
        <div style='background:#dcfce7;padding:6px;border-radius:5px;color:#15803d;'>✅ 不使用生日、姓名</div>
        <div style='background:#dcfce7;padding:6px;border-radius:5px;color:#15803d;'>✅ 每個網站使用不同密碼</div>
        <div style='background:#dcfce7;padding:6px;border-radius:5px;color:#15803d;'>✅ 啟用兩步驟驗證（2FA）</div>
        <div style='background:#dbeafe;padding:6px;border-radius:5px;color:#1e40af;'>💡 使用密碼管理器（Bitwarden）</div>
      </div>
    </div>
  </div>
</div>"""
    },
    {
        'id': 12, 'chapter': '第二章：個資法與法律保護', 'title': '🎯 第二章 隨堂測驗',
        'bg': 'purple', 'quiz': 'q2', 'chart': None, 'video': None,
        'html': """
<div style='text-align:center;padding:20px;'>
  <div style='font-size:56px;margin-bottom:15px;'>🎯</div>
  <h2 style='color:#fff;font-size:2rem;font-weight:800;margin-bottom:10px;'>第二章 隨堂測驗</h2>
  <p style='color:#e9d5ff;font-size:1.1rem;'>個資法與法律保護 ── 2 道題目，點擊作答！</p>
</div>"""
    },
    {
        'id': 13, 'chapter': '第三章：資安威脅與攻擊', 'title': '常見資安攻擊',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>資安威脅：認識攻擊手法</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:16px;'>
  <div style='display:flex;flex-direction:column;gap:10px;'>
    <div style='background:#fef2f2;padding:12px;border-radius:10px;border-left:4px solid #dc2626;'>
      <h3 style='color:#dc2626;font-size:.9rem;margin-bottom:5px;'>🎣 釣魚攻擊（Phishing）</h3>
      <p style='color:#374151;font-size:.82rem;'>假冒銀行、LINE、政府機關，發送偽造郵件或網頁，誘騙輸入帳密。台灣每年有數萬件釣魚詐騙。</p>
    </div>
    <div style='background:#fff7ed;padding:12px;border-radius:10px;border-left:4px solid #f59e0b;'>
      <h3 style='color:#ea580c;font-size:.9rem;margin-bottom:5px;'>💰 勒索軟體（Ransomware）</h3>
      <p style='color:#374151;font-size:.82rem;'>感染後加密所有檔案，要求支付比特幣解鎖。2017 WannaCry 攻擊影響全球 150 國、台灣醫院。</p>
    </div>
    <div style='background:#eff6ff;padding:12px;border-radius:10px;border-left:4px solid #2563eb;'>
      <h3 style='color:#1e40af;font-size:.9rem;margin-bottom:5px;'>🤖 殭屍網路（Botnet）</h3>
      <p style='color:#374151;font-size:.82rem;'>駭客入侵大量電腦組成「殭屍軍團」，用於發動攻擊或挖礦。你的電腦可能在你不知情時被控制。</p>
    </div>
  </div>
  <div style='display:flex;flex-direction:column;gap:10px;'>
    <div style='background:#fdf4ff;padding:12px;border-radius:10px;border-left:4px solid #7c3aed;'>
      <h3 style='color:#7c3aed;font-size:.9rem;margin-bottom:5px;'>🎭 社交工程（Social Engineering）</h3>
      <p style='color:#374151;font-size:.82rem;'>利用人類心理弱點（信任、恐懼、貪婪）騙取資訊，而非技術入侵。假裝 IT 人員要你提供密碼。</p>
    </div>
    <div style='background:#f0fdf4;padding:12px;border-radius:10px;border-left:4px solid #16a34a;'>
      <h3 style='color:#15803d;font-size:.9rem;margin-bottom:5px;'>🔓 SQL 注入攻擊</h3>
      <p style='color:#374151;font-size:.82rem;'>在網站輸入框插入惡意 SQL 指令，可繞過登入驗證或竊取整個資料庫。</p>
    </div>
    <div style='background:#fef9c3;padding:12px;border-radius:8px;'>
      <p style='color:#854d0e;font-size:.83rem;margin:0;'>🛡️ 最有效的防護：保持更新 + 不點可疑連結 + 強密碼</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 14, 'chapter': '第三章：資安威脅與攻擊', 'title': '深偽技術',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>Deepfake：眼見不為憑</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#1e293b;padding:18px;border-radius:12px;margin-bottom:12px;'>
      <h3 style='color:#94a3b8;font-size:.85rem;margin-bottom:14px;letter-spacing:.05em;'>什麼是 Deepfake？</h3>
      <p style='color:#e2e8f0;font-size:.9rem;line-height:1.7;'>利用 AI（深度學習）技術合成偽造的人臉影片或聲音，讓影片中的人說出或做出從未發生的事。</p>
      <div style='background:#0f172a;padding:10px;border-radius:8px;margin-top:10px;'>
        <p style='color:#f87171;font-size:.82rem;margin:0;'>⚠️ 已有詐騙集團用 Deepfake 偽造台灣政治人物視頻，詐騙民眾投資</p>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#fef2f2;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#dc2626;font-size:1rem;margin-bottom:10px;'>😨 Deepfake 的危害</h3>
      <ul style='color:#374151;font-size:.85rem;padding-left:16px;'>
        <li>散布假新聞與不實資訊</li>
        <li>偽造名人代言詐騙</li>
        <li>非法成人內容（未經同意）</li>
        <li>身分冒充詐欺</li>
        <li>破壞個人名譽</li>
      </ul>
    </div>
    <div style='background:#eff6ff;padding:10px;border-radius:8px;'>
      <h3 style='color:#1e40af;font-size:.9rem;margin-bottom:6px;'>🔍 如何辨識？</h3>
      <p style='color:#374151;font-size:.82rem;margin:0;'>注意臉部邊緣不自然、眨眼頻率異常、聲音與嘴型不吻合、場景光線矛盾。</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 15, 'chapter': '第三章：資安威脅與攻擊', 'title': '如何自我保護',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>資安自我防護清單</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:16px;'>
  <div>
    <h3 style='color:#374151;font-size:.95rem;margin-bottom:10px;'>📱 手機安全</h3>
    <div style='display:flex;flex-direction:column;gap:6px;font-size:.83rem;'>
      <div style='background:#dcfce7;padding:8px;border-radius:6px;color:#15803d;'>✅ 啟用螢幕鎖（PIN / 指紋）</div>
      <div style='background:#dcfce7;padding:8px;border-radius:6px;color:#15803d;'>✅ 只從官方商店下載 App</div>
      <div style='background:#dcfce7;padding:8px;border-radius:6px;color:#15803d;'>✅ 定期更新系統</div>
      <div style='background:#dcfce7;padding:8px;border-radius:6px;color:#15803d;'>✅ 謹慎授予 App 權限</div>
    </div>
  </div>
  <div>
    <h3 style='color:#374151;font-size:.95rem;margin-bottom:10px;'>💻 電腦安全</h3>
    <div style='display:flex;flex-direction:column;gap:6px;font-size:.83rem;'>
      <div style='background:#dcfce7;padding:8px;border-radius:6px;color:#15803d;'>✅ 安裝防毒軟體</div>
      <div style='background:#dcfce7;padding:8px;border-radius:6px;color:#15803d;'>✅ 啟用防火牆</div>
      <div style='background:#dcfce7;padding:8px;border-radius:6px;color:#15803d;'>✅ 不插不明隨身碟</div>
      <div style='background:#dcfce7;padding:8px;border-radius:6px;color:#15803d;'>✅ 定期備份重要資料</div>
    </div>
  </div>
</div>
<div style='margin-top:14px;display:grid;grid-template-columns:1fr 1fr;gap:16px;'>
  <div>
    <h3 style='color:#374151;font-size:.95rem;margin-bottom:10px;'>🌐 網路習慣</h3>
    <div style='display:flex;flex-direction:column;gap:6px;font-size:.83rem;'>
      <div style='background:#dcfce7;padding:8px;border-radius:6px;color:#15803d;'>✅ 避免公共 WiFi 進行金融操作</div>
      <div style='background:#dcfce7;padding:8px;border-radius:6px;color:#15803d;'>✅ 確認網址 https:// 才輸入資料</div>
      <div style='background:#fee2e2;padding:8px;border-radius:6px;color:#dc2626;'>❌ 不點陌生連結</div>
    </div>
  </div>
  <div>
    <h3 style='color:#374151;font-size:.95rem;margin-bottom:10px;'>🔑 帳號管理</h3>
    <div style='display:flex;flex-direction:column;gap:6px;font-size:.83rem;'>
      <div style='background:#dcfce7;padding:8px;border-radius:6px;color:#15803d;'>✅ 不同網站不同密碼</div>
      <div style='background:#dcfce7;padding:8px;border-radius:6px;color:#15803d;'>✅ 啟用兩步驟驗證</div>
      <div style='background:#fee2e2;padding:8px;border-radius:6px;color:#dc2626;'>❌ 不告訴他人密碼</div>
    </div>
  </div>
</div>"""
    },
    {
        'id': 16, 'chapter': '第三章：資安威脅與攻擊', 'title': '台灣資安現況',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>台灣的資安挑戰</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#fef2f2;padding:15px;border-radius:10px;border:1px solid #fecaca;margin-bottom:12px;'>
      <h3 style='color:#dc2626;font-size:1rem;margin-bottom:10px;'>⚔️ 台灣面臨的威脅</h3>
      <ul style='color:#374151;font-size:.85rem;padding-left:16px;'>
        <li>每月平均遭受 <strong>數百萬次</strong>網路攻擊</li>
        <li>政府機關是主要攻擊目標</li>
        <li>APT（進階持續性威脅）攻擊頻繁</li>
        <li>選舉期間假訊息與資安攻擊激增</li>
      </ul>
    </div>
  </div>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>🛡️ 台灣的應對</h3>
      <ul style='color:#374151;font-size:.85rem;padding-left:16px;'>
        <li>行政院資安處統籌資安政策</li>
        <li>數位部推動政府資安強化</li>
        <li>台灣資安大會：年度最重要資安盛會</li>
        <li>資安相關就業機會快速成長</li>
        <li>高中職資安課程推廣</li>
      </ul>
    </div>
  </div>
</div>"""
    },
    {
        'id': 17, 'chapter': '第三章：資安威脅與攻擊', 'title': '🎯 第三章 隨堂測驗',
        'bg': 'purple', 'quiz': 'q3', 'chart': None, 'video': None,
        'html': """
<div style='text-align:center;padding:20px;'>
  <div style='font-size:56px;margin-bottom:15px;'>🎯</div>
  <h2 style='color:#fff;font-size:2rem;font-weight:800;margin-bottom:10px;'>第三章 隨堂測驗</h2>
  <p style='color:#e9d5ff;font-size:1.1rem;'>資安威脅與攻擊 ── 2 道題目，點擊作答！</p>
</div>"""
    },
    {
        'id': 18, 'chapter': '第四章：資訊倫理', 'title': '什麼是資訊倫理？',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>資訊倫理：數位世界的行為準則</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>📐 PAPA 資訊倫理架構</h3>
      <div style='display:flex;flex-direction:column;gap:8px;'>
        <div style='background:#dbeafe;padding:8px;border-radius:6px;'><strong style='color:#1e40af;'>P</strong> rivacy（隱私）<span style='color:#374151;font-size:.82rem;'> — 尊重他人私密資訊</span></div>
        <div style='background:#dbeafe;padding:8px;border-radius:6px;'><strong style='color:#1e40af;'>A</strong> ccuracy（正確性）<span style='color:#374151;font-size:.82rem;'> — 確保資訊的真實</span></div>
        <div style='background:#dbeafe;padding:8px;border-radius:6px;'><strong style='color:#1e40af;'>P</strong> roperty（財產）<span style='color:#374151;font-size:.82rem;'> — 尊重智慧財產</span></div>
        <div style='background:#dbeafe;padding:8px;border-radius:6px;'><strong style='color:#1e40af;'>A</strong> ccessibility（近用性）<span style='color:#374151;font-size:.82rem;'> — 資訊公平取用</span></div>
      </div>
    </div>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:10px;'>🌱 資訊倫理的核心問題</h3>
      <ul style='color:#374151;font-size:.88rem;padding-left:16px;'>
        <li>我可以自由分享這個資訊嗎？</li>
        <li>這個資訊是真實的嗎？</li>
        <li>我有使用這個內容的授權嗎？</li>
        <li>這樣做會傷害到誰嗎？</li>
        <li>如果換作是我，我願意被這樣對待嗎？</li>
      </ul>
    </div>
  </div>
</div>"""
    },
    {
        'id': 19, 'chapter': '第四章：資訊倫理', 'title': 'AI 與倫理',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>AI 時代的新倫理挑戰</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:16px;'>
  <div style='display:flex;flex-direction:column;gap:10px;'>
    <div style='background:#eff6ff;padding:12px;border-radius:10px;border-left:4px solid #2563eb;'>
      <h3 style='color:#1e40af;font-size:.9rem;margin-bottom:5px;'>🎨 AI 生成內容著作權</h3>
      <p style='color:#374151;font-size:.82rem;'>用 AI 生成的圖片、文章著作權歸誰？台灣法律尚未明確，使用時需注意平台授權條款。</p>
    </div>
    <div style='background:#fdf4ff;padding:12px;border-radius:10px;border-left:4px solid #7c3aed;'>
      <h3 style='color:#7c3aed;font-size:.9rem;margin-bottom:5px;'>📝 學術誠信</h3>
      <p style='color:#374151;font-size:.82rem;'>用 AI 寫作業但不告知老師，是否違反學術誠信？各校規定不同，需了解學校政策。</p>
    </div>
  </div>
  <div style='display:flex;flex-direction:column;gap:10px;'>
    <div style='background:#fff7ed;padding:12px;border-radius:10px;border-left:4px solid #ea580c;'>
      <h3 style='color:#ea580c;font-size:.9rem;margin-bottom:5px;'>🔮 AI 偏見問題</h3>
      <p style='color:#374151;font-size:.82rem;'>AI 訓練資料若含偏見，輸出結果也會有偏見。例如某些 AI 招募系統歧視女性應徵者。</p>
    </div>
    <div style='background:#f0fdf4;padding:12px;border-radius:10px;border-left:4px solid #16a34a;'>
      <h3 style='color:#15803d;font-size:.9rem;margin-bottom:5px;'>🌍 AI 責任歸屬</h3>
      <p style='color:#374151;font-size:.82rem;'>自動駕駛發生事故，責任在車主、製造商還是 AI？全球正在建立新的法律框架。</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 20, 'chapter': '第四章：資訊倫理', 'title': '假訊息識別',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>假訊息：你能辨識真假嗎？</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#fef2f2;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#dc2626;font-size:1rem;margin-bottom:10px;'>😱 台灣假訊息現況</h3>
      <p style='color:#374151;font-size:.88rem;margin-bottom:8px;'>台灣每月被事實查核的假訊息超過 1,000 則，主要傳播管道：</p>
      <ul style='color:#374151;font-size:.83rem;padding-left:16px;'>
        <li>LINE 群組</li>
        <li>Facebook</li>
        <li>YouTube 留言</li>
        <li>PTT / Dcard</li>
      </ul>
    </div>
  </div>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>🔍 查核假訊息的方法</h3>
      <div style='display:flex;flex-direction:column;gap:6px;font-size:.83rem;'>
        <div style='background:#dbeafe;padding:8px;border-radius:6px;color:#1e40af;'>①檢查來源：有沒有可信媒體報導？</div>
        <div style='background:#dbeafe;padding:8px;border-radius:6px;color:#1e40af;'>②反查圖片：Google 圖片搜尋</div>
        <div style='background:#dbeafe;padding:8px;border-radius:6px;color:#1e40af;'>③查事實查核網站：MyGoPen、蘭姆酒吐司</div>
        <div style='background:#dbeafe;padding:8px;border-radius:6px;color:#1e40af;'>④注意情緒化標題：「驚爆！」「全部曝光」</div>
        <div style='background:#dbeafe;padding:8px;border-radius:6px;color:#1e40af;'>⑤不急著轉傳：未確認前先暫停</div>
      </div>
    </div>
  </div>
</div>"""
    },
    {
        'id': 21, 'chapter': '第四章：資訊倫理', 'title': '社群媒體與數位公民',
        'bg': 'white', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 class='slide-title'>負責任的數位公民</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div>
    <div style='background:#eff6ff;padding:15px;border-radius:10px;margin-bottom:12px;'>
      <h3 style='color:#1e40af;font-size:1rem;margin-bottom:10px;'>📱 社群媒體的影響力</h3>
      <ul style='color:#374151;font-size:.85rem;padding-left:16px;'>
        <li>一則 IG 貼文可以影響數百萬人</li>
        <li>網路霸凌對心理健康的衝擊</li>
        <li>演算法的「同溫層效應」</li>
        <li>數位足跡永遠留存</li>
      </ul>
    </div>
    <div style='background:#fef9c3;padding:10px;border-radius:8px;'>
      <p style='color:#854d0e;font-size:.85rem;margin:0;'>💡 你發出的每一則訊息都代表你的數位身分，未來雇主可能會看到。</p>
    </div>
  </div>
  <div>
    <div style='background:#f0fdf4;padding:15px;border-radius:10px;'>
      <h3 style='color:#15803d;font-size:1rem;margin-bottom:10px;'>🌱 成為好的數位公民</h3>
      <div style='display:flex;flex-direction:column;gap:6px;font-size:.83rem;'>
        <div style='background:#dcfce7;padding:6px;border-radius:5px;color:#15803d;'>✅ 思考後再發言，不衝動回應</div>
        <div style='background:#dcfce7;padding:6px;border-radius:5px;color:#15803d;'>✅ 尊重不同意見，不霸凌</div>
        <div style='background:#dcfce7;padding:6px;border-radius:5px;color:#15803d;'>✅ 分享前查核訊息真實性</div>
        <div style='background:#dcfce7;padding:6px;border-radius:5px;color:#15803d;'>✅ 保護自己與他人的隱私</div>
        <div style='background:#dcfce7;padding:6px;border-radius:5px;color:#15803d;'>✅ 注意螢幕使用時間</div>
      </div>
    </div>
  </div>
</div>"""
    },
    {
        'id': 22, 'chapter': '第四章：資訊倫理', 'title': '🎯 第四章 隨堂測驗',
        'bg': 'purple', 'quiz': 'q4', 'chart': None, 'video': None,
        'html': """
<div style='text-align:center;padding:20px;'>
  <div style='font-size:56px;margin-bottom:15px;'>🎯</div>
  <h2 style='color:#fff;font-size:2rem;font-weight:800;margin-bottom:10px;'>第四章 隨堂測驗</h2>
  <p style='color:#e9d5ff;font-size:1.1rem;'>資訊倫理 ── 2 道題目，點擊作答！</p>
</div>"""
    },
    {
        'id': 23, 'chapter': '分組實作', 'title': '分組實作：個資保護行動計畫',
        'bg': 'teal', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<h2 style='font-size:1.8rem;font-weight:800;color:#fff;margin-bottom:20px;text-align:center;'>🛡️ 分組實作：個資保護行動計畫</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
  <div style='background:rgba(255,255,255,0.15);padding:18px;border-radius:12px;'>
    <h3 style='color:#fff;font-size:1rem;margin-bottom:14px;'>📋 實作任務</h3>
    <div style='display:flex;flex-direction:column;gap:10px;'>
      <div style='background:rgba(255,255,255,0.2);padding:12px;border-radius:8px;'>
        <p style='color:#fff;font-weight:700;font-size:.9rem;margin:0 0 4px;'>任務一：個資稽查</p>
        <p style='color:#cffafe;font-size:.8rem;margin:0;'>列出你曾在哪些網站/App 填寫個人資料，評估哪些有過度蒐集的問題</p>
      </div>
      <div style='background:rgba(255,255,255,0.2);padding:12px;border-radius:8px;'>
        <p style='color:#fff;font-weight:700;font-size:.9rem;margin:0 0 4px;'>任務二：密碼安全評估</p>
        <p style='color:#cffafe;font-size:.8rem;margin:0;'>使用 haveibeenpwned.com 查詢班級同學（自願者）email 是否外洩</p>
      </div>
      <div style='background:rgba(255,255,255,0.2);padding:12px;border-radius:8px;'>
        <p style='color:#fff;font-weight:700;font-size:.9rem;margin:0 0 4px;'>任務三：假訊息偵測</p>
        <p style='color:#cffafe;font-size:.8rem;margin:0;'>選取 3 則 LINE 群組訊息，用事實查核方法驗證真偽，記錄過程</p>
      </div>
    </div>
  </div>
  <div>
    <div style='background:rgba(255,255,255,0.15);padding:15px;border-radius:12px;margin-bottom:12px;'>
      <h3 style='color:#fff;font-size:1rem;margin-bottom:10px;'>📊 報告格式</h3>
      <ul style='color:#cffafe;font-size:.85rem;padding-left:16px;'>
        <li>個資蒐集清單（截圖）</li>
        <li>密碼安全評估報告</li>
        <li>假訊息查核過程紀錄</li>
        <li>個人/小組的改善計畫</li>
      </ul>
    </div>
    <div style='background:rgba(255,255,255,0.15);padding:12px;border-radius:8px;'>
      <p style='color:#fff;font-size:.85rem;font-weight:700;margin-bottom:4px;'>🗓️ 繳交方式</p>
      <p style='color:#cffafe;font-size:.82rem;margin:0;'>Google 簡報（每組 6 頁以上）上傳至 Google Classroom</p>
    </div>
  </div>
</div>"""
    },
    {
        'id': 24, 'chapter': '分組實作', 'title': '保護自己，也保護他人',
        'bg': 'navy', 'quiz': None, 'chart': None, 'video': None,
        'html': """
<div style='text-align:center;padding:30px 20px;'>
  <div style='font-size:64px;margin-bottom:20px;'>🌐</div>
  <h1 style='font-size:2.2rem;font-weight:900;color:#fff;margin-bottom:12px;'>保護自己，也保護他人</h1>
  <h2 style='font-size:1.2rem;font-weight:400;color:#93c5fd;margin-bottom:24px;'>個資保護不只是法律義務，更是對他人的尊重</h2>
  <div style='background:rgba(255,255,255,0.1);padding:18px;border-radius:12px;margin-bottom:24px;max-width:600px;margin-left:auto;margin-right:auto;'>
    <p style='color:#e2e8f0;font-size:1rem;font-style:italic;line-height:1.7;margin:0;'>
      「Privacy is not something that I'm merely entitled to, it's an absolute prerequisite.」<br>
      <span style='font-size:.85rem;color:#94a3b8;'>— Marlon Brando</span>
    </p>
  </div>
  <div style='display:flex;justify-content:center;gap:12px;flex-wrap:wrap;'>
    <span style='background:rgba(255,255,255,0.12);color:#e0f2fe;padding:8px 18px;border-radius:20px;font-size:.9rem;'>了解個資法 ✅</span>
    <span style='background:rgba(255,255,255,0.12);color:#e0f2fe;padding:8px 18px;border-radius:20px;font-size:.9rem;'>認識資安攻擊 ✅</span>
    <span style='background:rgba(255,255,255,0.12);color:#e0f2fe;padding:8px 18px;border-radius:20px;font-size:.9rem;'>下一章見 👋</span>
  </div>
</div>"""
    },
]
