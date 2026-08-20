# -*- coding: utf-8 -*-
"""
enhancements.py — 各章節豐富化內容
結構：ENHANCEMENTS[章節編號][投影片id] = {
    'video': {...}          # 覆蓋原始 video 欄位
    'html_append': '...'    # 附加在原始 html 後面
}
"""

# ── 通用 HTML 元件 ──────────────────────────────────────────────────────────

def _life(title, body):
    return f"""
<div style='background:linear-gradient(135deg,#eff6ff,#dbeafe);border-radius:12px;padding:14px 16px;margin-top:14px;border-left:4px solid #3b82f6;'>
  <h4 style='color:#1d4ed8;font-size:.85rem;font-weight:700;margin:0 0 8px;'>💡 生活實例：{title}</h4>
  {body}
</div>"""

def _innov(title, body):
    return f"""
<div style='background:linear-gradient(135deg,#f0fdf4,#dcfce7);border-radius:12px;padding:14px 16px;margin-top:14px;border-left:4px solid #22c55e;'>
  <h4 style='color:#15803d;font-size:.85rem;font-weight:700;margin:0 0 8px;'>🚀 創新應用：{title}</h4>
  {body}
</div>"""

def _data(title, body):
    return f"""
<div style='background:linear-gradient(135deg,#faf5ff,#ede9fe);border-radius:12px;padding:14px 16px;margin-top:14px;border-left:4px solid #8b5cf6;'>
  <h4 style='color:#6d28d9;font-size:.85rem;font-weight:700;margin:0 0 8px;'>📊 數據說話：{title}</h4>
  {body}
</div>"""

def _vid_search(query, title, desc):
    return {'type': 'search', 'query': query, 'title': title, 'desc': desc}

def _vid_yt(vid_id, title):
    return {'type': 'youtube', 'id': vid_id, 'title': title}

def _vid_both(vid_id, query, title, desc='在 YouTube 搜尋同主題其他教學影片', search_title=None):
    """雙模式：上方嵌入乾淨播放器（youtube-nocookie，無廣告干擾），下方保留搜尋備援
    嵌入的影片若失效，學生仍可透過下方按鈕搜尋替代內容。"""
    return {
        'type': 'both',
        'id': vid_id,
        'title': title,
        'query': query,
        'desc': desc,
        'search_title': search_title or '想看更多相關影片',
    }

def _mini_cards(*cards):
    """cards = list of (emoji, title, value, color)"""
    items = ''.join(
        f"<div style='background:#fff;padding:8px 10px;border-radius:8px;text-align:center;'>"
        f"<div style='font-size:1.4rem;'>{e}</div>"
        f"<p style='font-size:.72rem;font-weight:700;color:#374151;margin:4px 0 2px;'>{t}</p>"
        f"<p style='font-size:.75rem;color:{c};font-weight:600;margin:0;'>{v}</p></div>"
        for e, t, v, c in cards
    )
    return f"<div style='display:grid;grid-template-columns:repeat({len(cards)},1fr);gap:8px;'>{items}</div>"


def _ref(title, items):
    """延伸閱讀 / 參考資料連結區塊
    items = list of (icon, label, url, note)
    """
    lis = ''.join(
        f"<li style='margin-bottom:6px;line-height:1.55;'>"
        f"<span style='margin-right:6px;'>{i}</span>"
        f"<a href='{u}' target='_blank' rel='noopener' "
        f"style='color:#0d9488;font-weight:600;text-decoration:none;border-bottom:1px dashed #0d9488;'>{lb}</a>"
        f"<span style='color:#6b7280;font-size:.75rem;'> — {n}</span></li>"
        for i, lb, u, n in items
    )
    return f"""
<div style='background:linear-gradient(135deg,#fff7ed,#ffedd5);border-radius:12px;padding:14px 16px;margin-top:14px;border-left:4px solid #f97316;'>
  <h4 style='color:#c2410c;font-size:.85rem;font-weight:700;margin:0 0 8px;'>📚 延伸閱讀：{title}</h4>
  <ul style='list-style:none;padding:0;margin:0;font-size:.82rem;color:#374151;'>{lis}</ul>
</div>"""


def _reveal(question, hint, answer):
    """CSS-only 點擊揭曉小挑戰（用 <details>）"""
    return f"""
<div style='background:linear-gradient(135deg,#ecfeff,#cffafe);border-radius:12px;padding:14px 16px;margin-top:14px;border-left:4px solid #06b6d4;'>
  <h4 style='color:#0e7490;font-size:.85rem;font-weight:700;margin:0 0 8px;'>🧩 小挑戰</h4>
  <p style='font-size:.85rem;color:#374151;margin:0 0 6px;'><strong>Q：</strong>{question}</p>
  <p style='font-size:.78rem;color:#6b7280;margin:0 0 8px;'>💡 提示：{hint}</p>
  <details style='cursor:pointer;'>
    <summary style='color:#0e7490;font-weight:700;font-size:.82rem;user-select:none;'>👀 點我看答案</summary>
    <div style='margin-top:8px;background:#fff;padding:10px 12px;border-radius:8px;font-size:.85rem;color:#374151;line-height:1.6;'>{answer}</div>
  </details>
</div>"""


def _quiz_click(question, options, correct_idx, explain):
    """即時互動選擇題（onclick 顯示對錯）— options: list of str, correct_idx: 0-based"""
    import uuid
    gid = 'q' + uuid.uuid4().hex[:8]
    btns = ''.join(
        f"<button onclick=\"(function(b){{"
        f"var ok={('true' if i == correct_idx else 'false')};"
        f"b.style.background=ok?'#16a34a':'#dc2626';b.style.color='#fff';"
        f"var box=document.getElementById('{gid}_r');"
        f"box.style.display='block';"
        f"box.innerHTML=(ok?'✅ 答對了！':'❌ 再想想...')+'<br><span style=\\'font-size:.78rem;color:#6b7280\\'>' + '{explain.replace(chr(39), chr(92)+chr(39))}' + '</span>';"
        f"}})(this)\" "
        f"style='background:#fff;border:2px solid #cbd5e1;color:#374151;padding:8px 12px;border-radius:8px;font-size:.82rem;cursor:pointer;text-align:left;transition:all .15s;'>"
        f"{chr(65+i)}. {opt}</button>"
        for i, opt in enumerate(options)
    )
    return f"""
<div style='background:linear-gradient(135deg,#faf5ff,#f3e8ff);border-radius:12px;padding:14px 16px;margin-top:14px;border-left:4px solid #8b5cf6;'>
  <h4 style='color:#6d28d9;font-size:.85rem;font-weight:700;margin:0 0 8px;'>🎮 互動小測驗</h4>
  <p style='font-size:.85rem;color:#374151;margin:0 0 10px;line-height:1.5;'>{question}</p>
  <div style='display:grid;grid-template-columns:1fr 1fr;gap:6px;'>{btns}</div>
  <div id='{gid}_r' style='display:none;margin-top:10px;background:#fff;padding:10px 12px;border-radius:8px;font-size:.85rem;color:#111827;font-weight:600;'></div>
</div>"""


# ── Ch01：科技演進與硬體 ─────────────────────────────────────────────────────

_ch01 = {
    3: {  # 摩爾定律
        'video': _vid_search('摩爾定律 CPU 科技進化 教學', '▶ 摩爾定律動畫解說', '觀看科技演進速度動畫'),
        'html_append': _life('你的手機比登月火箭強多少？',
            _mini_cards(
                ('📱', 'iPhone 17 Pro', '每秒 2 兆次', '#2563eb'),
                ('🚀', '阿波羅登月', '每秒 4.3 萬次', '#dc2626'),
                ('⬆️', '差距倍數', '約 4,400 萬倍', '#16a34a'),
                ('⏱️', '摩爾定律', '每 2 年翻倍', '#d97706'),
            )
        ),
    },
    5: {  # 台積電
        # ✅ 已驗證：台積創新館官方頻道「晶圓廠導覽」
        'video': _vid_both(
            'WTZiT_asKLM',
            '台積電 半導體 台灣 故事 紀錄片 中文',
            '台積公司—晶圓廠導覽（台積創新館官方）',
            desc='想找更多台積電/半導體介紹？點下方搜尋',
            search_title='▶ 更多半導體與台積電中文影片',
        ),
        'html_append': _innov('台積電如何改變世界？',
            "<p style='font-size:.82rem;color:#374151;line-height:1.6;margin:0;'>"
            "全球 <strong>90%</strong> 最先進晶片（3nm 以下）由台積電生產。"
            "iPhone、NVIDIA GPU、特斯拉 FSD 晶片全依賴台積電。"
            "台積電市值（2025）超過 <strong>新台幣 25 兆元</strong>，相當於台灣 GDP 的 1.3 倍。</p>"
        ),
    },
    9: {  # CPU vs GPU
        'video': _vid_search('CPU vs GPU 差異 工作原理 動畫 中文', '▶ CPU vs GPU 誰更快？', '用動畫理解 CPU 與 GPU 的分工'),
        'html_append': _life('為什麼打遊戲要看 GPU？',
            "<div style='font-size:.82rem;color:#374151;line-height:1.6;'>"
            "<p style='margin:0 0 6px;'>🎮 <strong>遊戲</strong>：每秒要計算數百萬個像素顏色 → GPU 同時處理比 CPU 快 100 倍</p>"
            "<p style='margin:0 0 6px;'>🤖 <strong>AI 訓練</strong>：ChatGPT 訓練用了 10,000 個 NVIDIA A100 GPU</p>"
            "<p style='margin:0;'>📱 <strong>手機</strong>：A17 晶片內建 CPU + GPU + NPU（AI 加速），全部整合在指甲大小</p></div>"
        ),
    },
    13: {  # HDD vs SSD
        'video': _vid_search('SSD HDD 差異 運作原理 速度比較', '▶ SSD vs HDD 速度大比拼', '看看 SSD 比 HDD 快多少倍'),
        'html_append': _data('存取速度比較',
            _mini_cards(
                ('💾', 'HDD 傳統硬碟', '讀寫 150 MB/s', '#dc2626'),
                ('⚡', 'SATA SSD', '讀寫 550 MB/s', '#d97706'),
                ('🚀', 'NVMe SSD', '讀寫 7,000 MB/s', '#16a34a'),
                ('📱', '手機快閃記憶體', '讀寫 3,500 MB/s', '#2563eb'),
            ) +
            "<p style='font-size:.75rem;color:#6b7280;margin:8px 0 0;'>NVMe SSD 比傳統 HDD 快 <strong>46 倍</strong>，開機時間從 60 秒縮短到 5 秒</p>"
        ),
    },
    11: {  # 主機板與連接介面（新增互動）
        'html_append': _quiz_click(
            "你買了一台新的 4K 螢幕，準備接到筆電上。下列哪個連接介面「不能」傳輸影像？",
            ["HDMI", "USB-C（DisplayPort 模式）", "USB-A", "Thunderbolt 4"],
            2,
            "USB-A 是舊型接口，只能傳資料。要接螢幕請認明 HDMI、DisplayPort、USB-C 或 Thunderbolt。"
        ),
    },
    19: {  # 手機的硬體
        'html_append': _innov('未來的晶片技術',
            "<div style='display:grid;grid-template-columns:1fr 1fr;gap:8px;font-size:.8rem;'>"
            "<div style='background:#fff;padding:10px;border-radius:8px;border-left:3px solid #22c55e;'>"
            "<p style='font-weight:700;color:#15803d;margin:0 0 4px;'>⚛️ 2nm 製程（2025）</p>"
            "<p style='color:#374151;margin:0;'>一枚晶片容納 500 億個電晶體，比人類頭髮細 35,000 倍</p></div>"
            "<div style='background:#fff;padding:10px;border-radius:8px;border-left:3px solid #22c55e;'>"
            "<p style='font-weight:700;color:#15803d;margin:0 0 4px;'>🤖 AI 晶片內建</p>"
            "<p style='color:#374151;margin:0;'>手機 NPU 每秒執行 380 兆次 AI 運算，讓即時翻譯、人臉辨識成真</p></div>"
            "<div style='background:#fff;padding:10px;border-radius:8px;border-left:3px solid #22c55e;'>"
            "<p style='font-weight:700;color:#15803d;margin:0 0 4px;'>🌡️ 散熱突破</p>"
            "<p style='color:#374151;margin:0;'>石墨烯散熱材料讓手機滿載時維持 40°C 以下</p></div>"
            "<div style='background:#fff;padding:10px;border-radius:8px;border-left:3px solid #22c55e;'>"
            "<p style='font-weight:700;color:#15803d;margin:0 0 4px;'>🔋 快充進化</p>"
            "<p style='color:#374151;margin:0;'>240W 快充，8 分鐘充滿 4,500mAh 電池</p></div>"
            "</div>"
        ),
    },
    24: {  # 結尾補延伸閱讀
        'html_append': _ref('科技演進與硬體 — 延伸閱讀', [
            ('🇹🇼', '台積電官網（教育資源）', 'https://www.tsmc.com/chinese', '認識半導體產業'),
            ('📖', '維基百科：摩爾定律', 'https://zh.wikipedia.org/wiki/摩尔定律', '完整歷史背景'),
            ('🎬', 'YouTube：晶片是怎麼做的', 'https://www.youtube.com/results?search_query=晶片如何製造+動畫', '看晶片如何從沙子做成'),
            ('📊', 'PassMark CPU 效能排行', 'https://www.cpubenchmark.net/', '選購筆電時查 CPU 效能'),
        ]),
    },
}

# ── Ch02：AI 時代的數位創作者（NEW，原本無 enhancements） ─────────────────

_ch02 = {
    3: {  # 類比訊號 vs 數位訊號
        'video': _vid_search('類比訊號 數位訊號 差異 動畫 教學 中文',
                             '▶ 類比 vs 數位 動畫解說',
                             '用動畫理解類比與數位訊號的差別'),
        'html_append': _life('黑膠唱片為什麼又流行了？',
            "<p style='font-size:.82rem;color:#374151;line-height:1.6;margin:0;'>"
            "數位音樂（Spotify、Apple Music）方便、無損；但黑膠唱片是<strong>類比訊號</strong>，"
            "聲波是連續的波形，被許多樂迷認為「更溫暖、更有層次」。"
            "2024 年全球黑膠銷量突破 <strong>4,900 萬張</strong>，是 1990 年代以來新高。"
            "💡 數位不一定等於更好，看用途選擇工具。</p>"
        ),
    },
    4: {  # ASCII 與 Unicode
        'html_append': _reveal(
            "把英文字 A 存入電腦，其實電腦記錄的是「數字 65」。那你名字裡的中文「王」，電腦怎麼存？",
            "ASCII 只能存英文；中文要用 Unicode（如 UTF-8）",
            "中文「王」在 Unicode 是 U+738B，UTF-8 編碼為 3 個 byte：E7 8E 8B。"
            "所以中文檔案比英文檔案佔更多空間。"
        ),
    },
    6: {  # 儲存單位與進位系統
        'video': _vid_search('二進位 十六進位 轉換 教學 中文 動畫',
                             '▶ 二進位、十六進位怎麼算？',
                             '5 分鐘搞懂進位系統'),
        'html_append': _quiz_click(
            "下列哪個檔案最大？",
            ["一張手機拍的照片（約 3 MB）",
             "一首 MP3 歌曲（約 4 MB）",
             "一部 1 小時 1080p 影片（約 2 GB）",
             "一份 Word 報告（約 200 KB）"],
            2,
            "1 GB ≈ 1,024 MB。影片是最大宗——這也是為什麼手機容量常常不夠用。"
        ),
    },
    7: {  # 電腦只懂 0 和 1
        'html_append': _reveal(
            "8 位元的二進位數 1010 1010 換算成十進位是多少？",
            "從右邊起，位元權重是 1, 2, 4, 8, 16, 32, 64, 128",
            "1010 1010 = 128 + 32 + 8 + 2 = <strong>170</strong>。"
            "電腦裡所有資料（文字、圖片、音樂）最終都被拆成這樣的 0/1 序列。"
        ),
    },
    8: {  # 像素、解析度與色彩深度
        'html_append': _life('你的手機拍多少像素？',
            _mini_cards(
                ('📱', 'iPhone 17 Pro', '4,800 萬像素', '#2563eb'),
                ('📺', '4K 電視', '約 830 萬像素', '#8b5cf6'),
                ('🖥️', 'Full HD 螢幕', '約 207 萬像素', '#d97706'),
                ('👁️', '人眼分辨極限', '約 5.76 億像素', '#16a34a'),
            ) +
            "<p style='font-size:.75rem;color:#6b7280;margin:8px 0 0;'>"
            "像素越多越清晰，但檔案也越大。同一張照片存成 4K 是 Full HD 的 4 倍大。</p>"
        ),
    },
    9: {  # 聲音與視訊的數位表示
        'video': _vid_search('取樣頻率 位元深度 音訊 教學 中文',
                             '▶ CD 音質為什麼是 44.1kHz？',
                             '了解音訊如何被數位化'),
    },
    10: {  # 進位系統與顏色編碼
        'html_append': _reveal(
            "網頁顏色代碼 #FF0000 是什麼顏色？（提示：RGB 三個兩位十六進位）",
            "FF = 255（滿），00 = 0（無）。RGB 的順序是紅、綠、藍。",
            "#FF0000 = R=255, G=0, B=0 = <strong style='color:#ff0000;'>純紅色</strong>。"
            "同理：#00FF00 = 純綠、#0000FF = 純藍、#FFFFFF = 白、#000000 = 黑。"
            "你在 Canva、PPT 選色時就是輸入這種色碼。"
        ),
    },
    11: {  # 選對格式
        'html_append': _life('學校老師常見錯誤',
            "<div style='font-size:.82rem;color:#374151;line-height:1.6;'>"
            "<div style='background:#fef2f2;padding:8px 10px;border-radius:8px;margin-bottom:6px;border-left:3px solid #ef4444;'>"
            "<p style='color:#dc2626;font-weight:700;margin:0 0 3px;'>❌ 用 Word (.docx) 傳給不同版本電腦 → 排版跑掉</p>"
            "<p style='margin:0;'>✅ 改用 PDF：所有裝置看起來都一樣。</p></div>"
            "<div style='background:#fef2f2;padding:8px 10px;border-radius:8px;margin-bottom:6px;border-left:3px solid #ef4444;'>"
            "<p style='color:#dc2626;font-weight:700;margin:0 0 3px;'>❌ 上傳 BMP 大圖到臉書 → 檔案 30MB 傳不上去</p>"
            "<p style='margin:0;'>✅ 改用 JPEG 或 WebP：品質幾乎一樣，檔案小 10 倍。</p></div>"
            "<div style='background:#f0fdf4;padding:8px 10px;border-radius:8px;border-left:3px solid #22c55e;'>"
            "<p style='color:#15803d;font-weight:700;margin:0 0 3px;'>✅ Logo/圖示：用 SVG（向量圖）</p>"
            "<p style='margin:0;'>放大不會模糊，且檔案通常只有 1–5 KB。</p></div>"
            "</div>"
        ),
    },
    14: {  # AI 如何生成圖片
        'video': _vid_search('AI 圖片生成 擴散模型 原理 中文 教學',
                             '▶ AI 如何從噪點畫出圖？',
                             '用 3 分鐘看懂擴散模型'),
        'html_append': _innov('AI 生圖技術演進速度',
            _mini_cards(
                ('🖼️', '2021 DALL·E 1', '解析度粗糙、人物變形', '#6b7280'),
                ('✨', '2023 Midjourney v5', '照片級擬真', '#d97706'),
                ('🎨', '2025 主流工具', '影片、3D、可控細節', '#16a34a'),
                ('🚀', '2026', '即時對話式生成、可編輯', '#8b5cf6'),
            )
        ),
    },
    16: {  # AI 擴散模型原理
        # ✅ 已驗證：Vox 頻道「AI art, explained」（英文，可開自動中文字幕）
        'video': _vid_both(
            'SVcsDDABEkM',
            'AI 擴散模型 圖片生成 原理 動畫 中文',
            'AI art, explained（Vox，可開中文字幕）',
            desc='想聽中文原生解說？點下方搜尋',
            search_title='▶ AI 生圖原理中文教學搜尋',
        ),
    },
    18: {  # AI 模型作品比較
        'html_append': _ref('主流 AI 生圖平台試用連結', [
            ('🎨', 'Microsoft Designer（免費）', 'https://designer.microsoft.com/', '無需付費、支援中文'),
            ('🖌️', 'Adobe Firefly（免費額度）', 'https://firefly.adobe.com/', '訓練資料為授權素材、商用較安全'),
            ('🌈', 'Bing Image Creator（免費）', 'https://www.bing.com/create', 'DALL·E 3 引擎、中文提示可用'),
            ('🖼️', 'Google ImageFX（免費）', 'https://labs.google/fx/tools/image-fx', 'Google Imagen 引擎'),
        ]),
    },
    20: {  # AI 幻覺
        'html_append': _life('AI 幻覺真實案例',
            "<div style='font-size:.82rem;color:#374151;line-height:1.6;'>"
            "<div style='background:#fef2f2;padding:8px 10px;border-radius:8px;margin-bottom:6px;border-left:3px solid #ef4444;'>"
            "<p style='color:#dc2626;font-weight:700;margin:0 0 3px;'>⚖️ 2023 美國律師案例</p>"
            "<p style='margin:0;'>紐約律師 Schwartz 用 ChatGPT 寫訴狀，AI 引用了 6 個「不存在」的判例。"
            "法官罰款 5,000 美元並公開懲處，成為 AI 幻覺經典案例。</p></div>"
            "<div style='background:#fef9c3;padding:8px 10px;border-radius:8px;border-left:3px solid #f59e0b;'>"
            "<p style='color:#92400e;font-weight:700;margin:0 0 3px;'>🛡️ 如何避免？</p>"
            "<p style='margin:0;'>① 任何數字、日期、引用都要交叉查證<br>"
            "② 使用具「網頁搜尋」功能的 AI（如 ChatGPT Search、Perplexity）<br>"
            "③ 遇到專業內容問專家，AI 只當第一稿助手</p></div>"
            "</div>"
        ),
    },
    22: {  # AI 正在改變哪些職業
        'html_append': _data('AI 對台灣職場的影響（2025 世界經濟論壇）',
            _mini_cards(
                ('📉', '將被 AI 取代', '約 22% 傳統文書', '#dc2626'),
                ('📈', '新增職缺', 'AI 訓練師、Prompt 工程師', '#16a34a'),
                ('🔄', '工作型態改變', '85% 現有工作內容重組', '#d97706'),
                ('🎓', '最重要技能', '學習力 > 特定技術', '#8b5cf6'),
            )
        ),
    },
    23: {  # AI 輔助 vs AI 代工
        'html_append': _quiz_click(
            "以下哪一種做法比較「AI 輔助」而不是「AI 代工」？",
            ["把老師的作業題目丟給 ChatGPT，複製貼上交出去",
             "先自己寫草稿，再請 AI 幫忙檢查邏輯與錯字",
             "整份心得請 AI 生成，只改標題",
             "考試偷用 AI 回答問答題"],
            1,
            "AI 輔助的核心是「保留自己的思考」。AI 用來檢查、擴展、翻譯，而不是完全替代。"
            "許多老師與教育部（2025 指引）都採「透明宣告 AI 使用範圍」原則。"
        ),
    },
    26: {  # 智慧財產權
        'html_append': _reveal(
            "同學把你的 IG 貼文截圖放到自己的 IG 限動、還加上自己的評論——這樣算侵權嗎？",
            "想一下：原創、來源標示、營利與否",
            "① 若是「合理引用」（有標示、少量、非營利、有評論）通常可接受；"
            "② 但直接盜用照片不標示來源，就算沒賺錢也可能構成著作權侵害；"
            "③ 建議做法：加上原作者標籤 @xxx 或「來源：@xxx」，並取得對方同意最保險。"
        ),
    },
    30: {  # CC0 公眾領域與免費素材
        'html_append': _ref('高中生做報告可用的免費素材網站', [
            ('📷', 'Unsplash（照片，CC0）', 'https://unsplash.com/', '高品質商用免費照片'),
            ('🎨', 'Pixabay（照片/影片/音樂）', 'https://pixabay.com/zh-tw/', '中文介面、數十萬素材'),
            ('🎵', 'YouTube Audio Library（音樂）', 'https://www.youtube.com/audiolibrary', '影片配樂免版稅'),
            ('🖼️', 'Icons8 / Flaticon（圖示）', 'https://icons8.com/', '簡報用圖示、部分免費'),
            ('🎭', 'Openverse（Creative Commons 搜尋）', 'https://openverse.org/', 'CC 授權統整搜尋'),
        ]),
    },
    33: {  # 合理引用四大原則
        'html_append': _life('學校報告怎麼合理引用？',
            "<div style='font-size:.82rem;color:#374151;line-height:1.6;'>"
            "<p style='margin:0 0 8px;'>合理引用四原則（著作權法第 65 條）：</p>"
            "<div style='display:flex;flex-direction:column;gap:5px;'>"
            "<div style='background:#fff;padding:7px 10px;border-radius:6px;border-left:2px solid #3b82f6;'>① <strong>目的</strong>：教育、研究、評論而非營利</div>"
            "<div style='background:#fff;padding:7px 10px;border-radius:6px;border-left:2px solid #3b82f6;'>② <strong>性質</strong>：原作是否已公開發表</div>"
            "<div style='background:#fff;padding:7px 10px;border-radius:6px;border-left:2px solid #3b82f6;'>③ <strong>比例</strong>：引用份量佔全文的比例（不能全文照抄）</div>"
            "<div style='background:#fff;padding:7px 10px;border-radius:6px;border-left:2px solid #3b82f6;'>④ <strong>影響</strong>：對原作市場價值的影響</div>"
            "</div>"
            "<p style='color:#dc2626;font-weight:600;margin:8px 0 0;font-size:.78rem;'>💡 最保險做法：引用時<strong>加註來源</strong>（作者、標題、網址、日期）</p>"
            "</div>"
        ),
    },
    34: {  # AI 生成圖著作權
        'html_append': _innov('AI 生圖著作權：全球最新爭議',
            "<div style='font-size:.82rem;color:#374151;line-height:1.6;'>"
            "<p style='margin:0 0 6px;'>🇺🇸 <strong>美國</strong>（2023）：純 AI 生成無人類創意輸入，<strong>不受著作權保護</strong></p>"
            "<p style='margin:0 0 6px;'>🇹🇼 <strong>台灣智慧局</strong>（2023 說明）：AI 產出「無著作權」，但「人類選擇、編輯、修改後」的成果可主張</p>"
            "<p style='margin:0 0 6px;'>🇨🇳 <strong>中國</strong>（2024 廣州判例）：AI 生成圖若有「人類創意選擇」，可享有著作權</p>"
            "<p style='margin:0;color:#d97706;font-weight:600;'>⚖️ 目前全球尚無統一標準，作品標示「AI 生成」是最安全做法</p>"
            "</div>"
        ),
    },
}

# ── Ch03：個人資料保護與資訊倫理 ────────────────────────────────────────────

_ch03 = {
    3: {  # Cookie 是什麼
        'video': _vid_search('Cookie 瀏覽器 是什麼 追蹤 隱私 教學', '▶ Cookie 如何追蹤你？', '了解 Cookie 是怎麼記錄你的行為'),
        'html_append': _life('你每天被追蹤幾次？',
            "<p style='font-size:.82rem;color:#374151;line-height:1.6;margin:0 0 8px;'>"
            "打開任何新聞網站，右鍵「檢視」→ 應用程式 → Cookie，你會看到 <strong>50–200 個</strong> 追蹤器同時運作。</p>"
            + _mini_cards(
                ('🛍️', 'Amazon', '平均存 287 個 Cookie', '#d97706'),
                ('📰', '新聞網站', '平均存 123 個 Cookie', '#dc2626'),
                ('📱', 'Instagram', '存 1st party Cookie', '#8b5cf6'),
                ('🔍', 'Google', '跨站追蹤你的足跡', '#2563eb'),
            )
        ),
    },
    4: {  # 數位足跡
        'html_append': _life('一天的數位足跡有多長？',
            "<div style='font-size:.82rem;color:#374151;line-height:1.8;'>"
            "<p style='margin:0 0 4px;'>☀️ <strong>早上</strong>：開 IG 看限時動態 → 廣告商知道你的作息時間</p>"
            "<p style='margin:0 0 4px;'>📍 <strong>搭車</strong>：Google 地圖導航 → 記錄你的通勤路線</p>"
            "<p style='margin:0 0 4px;'>🍜 <strong>午餐</strong>：外送 App 訂餐 → 記錄你的飲食偏好與居住地點</p>"
            "<p style='margin:0 0 4px;'>🎵 <strong>下課</strong>：Spotify → 分析你的情緒和喜好</p>"
            "<p style='margin:0;'>😴 <strong>晚上</strong>：Netflix → 知道你幾點睡覺、看什麼類型影片</p>"
            "<p style='font-size:.75rem;color:#dc2626;margin:8px 0 0;font-weight:600;'>⚠️ 你產生的數位足跡，可以讓 AI 精準預測你的下一步行為</p>"
            "</div>"
        ),
    },
    6: {  # 個資外洩有多常見
        'html_append': _data('全球個資外洩規模（2024）',
            _mini_cards(
                ('🔓', '每天外洩', '300 萬筆個資', '#dc2626'),
                ('💸', '平均損失', '每次 435 萬美元', '#d97706'),
                ('🇹🇼', '台灣排名', '亞太區第 3 高風險', '#8b5cf6'),
                ('⏱️', '偵測時間', '平均 204 天才發現', '#6b7280'),
            ) +
            "<p style='font-size:.75rem;color:#374151;margin:8px 0 0;'>來源：IBM Cost of a Data Breach Report 2024</p>"
        ),
    },
    13: {  # 常見資安攻擊
        'video': _vid_search('釣魚攻擊 社交工程 資安 詐騙 教學 辨識', '▶ 釣魚攻擊真實案例解析', '學會辨識常見的社交工程攻擊手法'),
    },
    14: {  # 深偽技術
        'video': _vid_search('Deepfake 深偽技術 如何運作 危害 AI 換臉', '▶ Deepfake 如何以假亂真？', '了解 AI 深偽技術的原理與風險'),
        'html_append': _life('身邊的 Deepfake 案例',
            "<div style='font-size:.82rem;color:#374151;line-height:1.6;'>"
            "<div style='background:#fef2f2;padding:10px;border-radius:8px;margin-bottom:8px;border-left:3px solid #ef4444;'>"
            "<p style='font-weight:700;color:#dc2626;margin:0 0 4px;'>🚨 2024 台灣真實案例</p>"
            "<p style='margin:0;'>以「知名主播林某某」Deepfake 影片詐騙，受害者以為是真人推薦投資，損失逾 <strong>3,000 萬元</strong></p></div>"
            "<div style='background:#fef9c3;padding:10px;border-radius:8px;border-left:3px solid #f59e0b;'>"
            "<p style='font-weight:700;color:#92400e;margin:0 0 4px;'>🛡️ 如何辨識</p>"
            "<p style='margin:0;'>注意眨眼頻率異常、嘴型對不上聲音、背景模糊邊緣，使用 Deepware Scanner 工具檢測</p></div>"
            "</div>"
        ),
    },
    19: {  # AI 與倫理
        'html_append': _innov('AI 倫理正在改變法律',
            "<div style='font-size:.82rem;color:#374151;line-height:1.6;'>"
            "<p style='margin:0 0 6px;'>🇪🇺 <strong>EU AI Act（2024）</strong>：全球首部 AI 法規，要求 AI 系統標示、禁止操控性 AI</p>"
            "<p style='margin:0 0 6px;'>🇹🇼 <strong>台灣 AI 基本法（2025 草案）</strong>：規範 AI 生成內容需標示、保護勞工不被 AI 取代</p>"
            "<p style='margin:0;'>🤖 <strong>你的作業</strong>：使用 AI 寫報告要標示「AI 輔助」，未來可能成為學術誠信的基本要求</p>"
            "</div>"
        ),
    },
    20: {  # 假訊息識別
        'html_append': _life('這則新聞是真的嗎？',
            "<div style='font-size:.82rem;color:#374151;'>"
            "<p style='font-weight:700;margin:0 0 8px;'>🔍 查核 SOP（30 秒快速辨識）</p>"
            "<div style='display:flex;flex-direction:column;gap:5px;'>"
            "<div style='background:#fff;padding:7px 10px;border-radius:6px;border-left:2px solid #3b82f6;'>① 看來源：媒體有沒有版權頁、聯絡方式？</div>"
            "<div style='background:#fff;padding:7px 10px;border-radius:6px;border-left:2px solid #3b82f6;'>② 查時間：標題寫「最新」但文章日期是 3 年前？</div>"
            "<div style='background:#fff;padding:7px 10px;border-radius:6px;border-left:2px solid #3b82f6;'>③ 反搜圖：右鍵搜尋圖片來源，看是否盜用舊照</div>"
            "<div style='background:#fff;padding:7px 10px;border-radius:6px;border-left:2px solid #3b82f6;'>④ 交叉比對：台灣事實查核中心（tfc-taiwan.org.tw）</div>"
            "</div></div>"
        ) + _quiz_click(
            "以下哪一則訊息「最可能是假訊息」？",
            ["中央氣象署：明日午後有雷陣雨，請攜帶雨具（附連結）",
             "『LINE 群組轉發』：喝檸檬水可以治癌！99% 醫生都在推薦！快分享",
             "衛福部食藥署發布最新食安通報（衛福部官網）",
             "教育部公告：學測日期為 X 月 X 日（官方新聞稿）"],
            1,
            "假訊息常見特徵：① 訴諸情緒（快分享！）② 沒有可信來源 ③ 用『99%』『所有』等絕對詞 "
            "④ 常出現在 LINE 群組轉發。真訊息通常有官方連結、明確日期、記者署名。"
        ),
    },
    11: {  # 密碼安全（新增互動題）
        'html_append': _quiz_click(
            "下列哪一個密碼「最安全」？",
            ["Password123",
             "MyDog2010",
             "P@ssw0rd!",
             "correct-horse-battery-staple（4 個隨機英文單字）"],
            3,
            "密碼長度比複雜度更重要！四個隨機英文單字組合的長密碼（passphrase），"
            "電腦需要 500+ 年才能破解；反而『P@ssw0rd!』只要 4 小時。"
            "另建議：不同網站不同密碼，並開啟兩步驟驗證。"
        ),
    },
    24: {  # 章末延伸閱讀
        'html_append': _ref('個資保護與資訊倫理 — 延伸閱讀', [
            ('🇹🇼', '個人資料保護委員會（籌備處）', 'https://www.pdpc.gov.tw/', '個資法官方權威資訊'),
            ('🔍', '台灣事實查核中心', 'https://tfc-taiwan.org.tw/', '免費查核假訊息'),
            ('🛡️', 'Have I Been Pwned（英）', 'https://haveibeenpwned.com/', '查你的 Email 有沒有被外洩'),
            ('🔐', 'iPASS 密碼強度檢測', 'https://bitwarden.com/password-strength/', '線上測你的密碼多久會被破解'),
            ('📱', '刑事局 165 反詐騙專線', 'https://165.npa.gov.tw/', '接到詐騙訊息可查詢'),
        ]),
    },
}

# ── Ch04：Google Workspace 文書應用 ─────────────────────────────────────────

_ch04 = {
    3: {  # Google vs Microsoft
        'html_append': _life('你的班上用哪個？',
            "<p style='font-size:.82rem;color:#374151;line-height:1.6;margin:0 0 8px;'>"
            "根據 2024 調查，台灣高中職有 <strong>78%</strong> 採用 Google Workspace for Education（免費版），"
            "理由是「免費、好協作、不用安裝」。但職場上 Microsoft 365 仍佔 <strong>85%</strong> 市佔率。"
            "所以兩個都要學！</p>"
            + _mini_cards(
                ('📚', '台灣學校', '78% 用 Google', '#2563eb'),
                ('🏢', '台灣企業', '85% 用 MS 365', '#0284c7'),
                ('🌐', '全球學生', '17 億人用 Google Workspace', '#16a34a'),
                ('💰', '費用差距', 'Google 免費 vs MS $300/年', '#d97706'),
            )
        ),
    },
    5: {  # Google 帳號安全
        'video': _vid_search('Google 帳號 雙重驗證 安全設定 教學 2FA', '▶ Google 帳號安全設定實作', '5 分鐘強化你的 Google 帳號安全'),
    },
    13: {  # 即時協作
        'video': _vid_search('Google 文件 即時協作 共同編輯 教學 技巧', '▶ Google 文件協作功能完整教學', '看看多人即時協作怎麼運作'),
        'html_append': _life('期末報告不再 Email 傳來傳去',
            "<div style='font-size:.82rem;color:#374151;line-height:1.6;'>"
            "<div style='background:#fef2f2;padding:8px 10px;border-radius:8px;margin-bottom:8px;'>"
            "<p style='color:#dc2626;font-weight:700;margin:0 0 3px;'>😫 舊方法（傳統 Word）</p>"
            "<p style='margin:0;'>小明改完傳給小華 → 小華改完再傳 → 最後搞不清楚哪個是最新版 → 合併版本花了 2 小時</p></div>"
            "<div style='background:#f0fdf4;padding:8px 10px;border-radius:8px;'>"
            "<p style='color:#15803d;font-weight:700;margin:0 0 3px;'>✅ Google 文件</p>"
            "<p style='margin:0;'>5 個人同時在同一份文件編輯，看到彼此游標顏色，留言討論，一份文件搞定</p></div>"
            "</div>"
        ),
    },
    14: {  # 版本歷史
        'html_append': _life('版本歷史救了我的報告',
            "<div style='font-size:.82rem;color:#374151;line-height:1.6;'>"
            "<p style='margin:0 0 6px;'>📖 <strong>真實場景</strong>：期末報告改到一半，不小心刪掉了一大段辛苦寫的內容，存檔後才發現！</p>"
            "<p style='margin:0 0 6px;'>✅ <strong>解決方法</strong>：檔案 → 版本歷史 → 查看版本歷史記錄 → 找到刪除前的版本 → 還原 ✨</p>"
            "<p style='margin:0;color:#6b7280;'>Google 文件每隔幾分鐘自動存版本，永遠不怕誤刪。Microsoft Word Online 也有同樣功能。</p>"
            "</div>"
        ),
    },
    17: {  # Google 試算表
        'video': _vid_search('Google 試算表 基礎教學 函數 VLOOKUP 中文', '▶ Google 試算表實用功能教學', '快速學會試算表最常用的技巧'),
    },
    21: {  # 生產力工作流程
        'html_append': _innov('Workspace + AI = 超強生產力',
            "<div style='font-size:.82rem;color:#374151;line-height:1.6;'>"
            "<p style='margin:0 0 6px;'>✨ <strong>Gemini in Google Workspace</strong>（2025）：</p>"
            "<div style='display:flex;flex-direction:column;gap:5px;'>"
            "<div style='background:#fff;padding:7px 10px;border-radius:6px;'>📄 <strong>文件</strong>：「幫我把這份報告摘要成 5 個重點」→ 一鍵完成</div>"
            "<div style='background:#fff;padding:7px 10px;border-radius:6px;'>📊 <strong>試算表</strong>：「分析這份資料，找出趨勢」→ 自動產生圖表</div>"
            "<div style='background:#fff;padding:7px 10px;border-radius:6px;'>📑 <strong>簡報</strong>：「用這份文件建立 10 張投影片」→ 自動排版</div>"
            "<div style='background:#fff;padding:7px 10px;border-radius:6px;'>📧 <strong>Gmail</strong>：「草擬一封婉拒的回信」→ 維持你的語氣</div>"
            "</div></div>"
        ),
    },
    24: {  # 雲端改變了工作方式
        'video': _vid_search('遠端工作 雲端協作 未來趨勢 Google Workspace', '▶ 雲端如何改變未來工作方式', '看看頂尖企業如何利用雲端協作'),
        'html_append': _data('雲端辦公的影響',
            _mini_cards(
                ('🏠', '遠端工作者', '全球 16% 已全遠端', '#2563eb'),
                ('✈️', '數位遊牧', '全球 3,500 萬人', '#8b5cf6'),
                ('⏱️', '省時', '減少 30% 開會時間', '#16a34a'),
                ('💻', '台灣', '68% 企業有遠端政策', '#d97706'),
            )
        ) + _ref('Google Workspace — 延伸閱讀', [
            ('📘', 'Google Workspace 學習中心', 'https://support.google.com/a/users/', '官方教學（中文）'),
            ('🎓', 'Google 教育中心', 'https://edu.google.com/intl/ALL_tw/', '免費 Google 教育版'),
            ('⌨️', 'Google 快捷鍵一覽', 'https://support.google.com/docs/answer/179738', '效率翻倍'),
            ('✨', 'Google 認證能力測驗', 'https://cloud.google.com/learn/certification', '有免費 Level 1 認證'),
        ]),
    },
}

# ── Ch05：合併列印與表單應用 ─────────────────────────────────────────────────

_ch05 = {
    2: {  # 什麼是合併列印
        'video': _vid_search('Word 合併列印 教學 功能變數 step by step 中文', '▶ Word 合併列印完整教學', '跟著影片一步步完成合併列印'),
    },
    4: {  # 生活中的合併列印
        'html_append': _life('學校裡的合併列印',
            "<div style='font-size:.82rem;color:#374151;line-height:1.6;'>"
            "<div style='display:grid;grid-template-columns:1fr 1fr;gap:8px;'>"
            "<div style='background:#fff;padding:8px;border-radius:8px;border-top:3px solid #3b82f6;'>"
            "<p style='font-weight:700;color:#1d4ed8;margin:0 0 4px;'>🏫 學校每學期使用</p>"
            "<p style='color:#374151;margin:0;font-size:.78rem;'>成績通知單 × 全校 1,200 份<br>活動邀請函 × 家長 1,200 份<br>社團報名確認函 × 300 份</p></div>"
            "<div style='background:#fff;padding:8px;border-radius:8px;border-top:3px solid #3b82f6;'>"
            "<p style='font-weight:700;color:#1d4ed8;margin:0 0 4px;'>💡 手動 vs 合併列印</p>"
            "<p style='color:#374151;margin:0;font-size:.78rem;'>手動輸入 1,200 份：約 40 小時<br>合併列印：設定 1 小時，列印 20 分鐘<br>節省 <strong>97.5%</strong> 時間！</p></div>"
            "</div></div>"
        ),
    },
    8: {  # 成績通知單實作
        'video': _vid_search('Word 合併列印 成績單 實作 資料來源 Excel 中文', '▶ 合併列印成績通知單實作', '實際示範從 Excel 到 Word 合併列印'),
    },
    13: {  # 認識 Google 表單
        'video': _vid_search('Google 表單 製作 教學 問卷 設定 中文', '▶ Google 表單完整製作教學', '從零開始建立一份 Google 問卷'),
    },
    19: {  # 問卷設計原則
        'html_append': _life('設計一份好問卷的眉角',
            "<div style='font-size:.82rem;color:#374151;'>"
            "<p style='margin:0 0 8px;'>研究顯示問卷長度直接影響完成率：</p>"
            + _mini_cards(
                ('✅', '5 分鐘以內', '完成率 80%+', '#16a34a'),
                ('⚠️', '10 分鐘', '完成率 約 50%', '#d97706'),
                ('❌', '20 分鐘', '完成率 < 20%', '#dc2626'),
                ('💡', '最佳長度', '7–10 題', '#2563eb'),
            ) +
            "<p style='font-size:.75rem;color:#6b7280;margin:8px 0 0;'>設計原則：從容易問到難 → 避免引導性問法 → 一題只問一件事</p>"
            "</div>"
        ),
    },
    21: {  # 調查報告撰寫
        'html_append': _innov('資料 → 故事 → 行動',
            "<p style='font-size:.82rem;color:#374151;line-height:1.6;margin:0 0 8px;'>"
            "Google 表單 + 試算表 + 簡報 = 完整的資料說故事流程</p>"
            "<div style='font-size:.8rem;text-align:center;'>"
            "<div style='display:flex;align-items:center;justify-content:center;gap:6px;flex-wrap:wrap;'>"
            "<span style='background:#dbeafe;color:#1d4ed8;padding:5px 10px;border-radius:8px;font-weight:700;'>📋 表單收集</span>"
            "<span style='color:#6b7280;'>→</span>"
            "<span style='background:#dcfce7;color:#15803d;padding:5px 10px;border-radius:8px;font-weight:700;'>📊 試算表分析</span>"
            "<span style='color:#6b7280;'>→</span>"
            "<span style='background:#fde68a;color:#92400e;padding:5px 10px;border-radius:8px;font-weight:700;'>📈 圖表視覺化</span>"
            "<span style='color:#6b7280;'>→</span>"
            "<span style='background:#ede9fe;color:#6d28d9;padding:5px 10px;border-radius:8px;font-weight:700;'>📑 簡報呈現</span>"
            "</div></div>"
        ),
    },
    24: {  # 章末延伸閱讀
        'html_append': _ref('合併列印與表單 — 延伸閱讀', [
            ('📄', 'Microsoft 官方合併列印教學', 'https://support.microsoft.com/zh-tw/office/', '看不懂就查這裡'),
            ('📋', 'Google 表單完整說明', 'https://support.google.com/docs/topic/9055404', '所有題型/邏輯的用法'),
            ('📊', 'Google 表單範本庫', 'https://docs.google.com/forms/', '直接改範本比較快'),
            ('🎓', 'SurveyCake（台製問卷平台）', 'https://www.surveycake.com/', '進階問卷分析工具'),
        ]),
    },
}

# ── Ch06：網際網路運作原理 ───────────────────────────────────────────────────

_ch06 = {
    4: {  # OSI 七層模型
        'video': _vid_search('OSI 七層模型 TCP/IP 網路協定 教學 動畫 中文', '▶ OSI 模型動畫教學', '用動畫搞懂七層網路模型'),
    },
    5: {  # 台灣網路基礎設施
        # 使用「雙模式」：上方嵌入乾淨播放器（Code.org 官方，非營利穩定），下方保留搜尋備援
        'video': _vid_both(
            'ZhEf7e4kopM',  # Code.org: The Internet - Wires, Cables & Wifi (long-running)
            '網際網路 如何運作 原理 教學 中文 動畫',
            '網際網路：電線、電纜與 Wi-Fi（Code.org）',
            desc='想聽中文解說？改搜尋更多相關影片',
            search_title='▶ 更多網際網路教學（中文）',
        ),
        'html_append': _data('台灣網路有多快？（2025）',
            _mini_cards(
                ('🏆', '全球排名', '寬頻速度 Top 5', '#d97706'),
                ('⚡', '平均速度', '固網 320 Mbps', '#2563eb'),
                ('📱', '行動網路', '5G 覆蓋率 89%', '#16a34a'),
                ('🌊', '海纜數量', '連接全球 15 條海纜', '#8b5cf6'),
            )
        ),
    },
    13: {  # DNS
        'html_append': _life('打 google.com 背後發生了什麼？',
            "<div style='font-size:.82rem;color:#374151;line-height:1.8;'>"
            "<p style='font-weight:700;margin:0 0 6px;'>你按下 Enter 後的 0.02 秒：</p>"
            "<p style='margin:0 0 3px;'>① 瀏覽器查本機快取：有沒有記過 google.com 的 IP？</p>"
            "<p style='margin:0 0 3px;'>② 問 DNS 伺服器（通常是中華電信 168.95.1.1）</p>"
            "<p style='margin:0 0 3px;'>③ DNS 回答：google.com = 142.250.185.68</p>"
            "<p style='margin:0 0 3px;'>④ 瀏覽器連線到 142.250.185.68，Google 伺服器回傳網頁</p>"
            "<p style='margin:0;color:#2563eb;font-weight:600;'>⏱️ 全程不到 50 毫秒完成！</p>"
            "</div>"
        ),
    },
    14: {  # HTTP vs HTTPS
        # ✅ 已驗證：PowerCert Animated Videos「SSL, TLS, HTTP, HTTPS Explained」
        'video': _vid_both(
            'hExRDVZHhig',
            'HTTPS SSL TLS 加密 運作 原理 教學 中文',
            'SSL, TLS, HTTP, HTTPS 動畫解說（PowerCert）',
            desc='想找中文教學？點下方搜尋',
            search_title='▶ HTTPS 中文教學搜尋',
        ),
        'html_append': _life('為什麼不要在咖啡店用 HTTP 網站？',
            "<p style='font-size:.82rem;color:#374151;line-height:1.6;margin:0;'>"
            "連上咖啡店 Wi-Fi，同網段的人可以用 Wireshark 軟體「嗅探」流量。"
            "如果網站是 HTTP（無加密），你的帳號密碼會以<strong>明文</strong>傳輸，直接被看光。"
            " HTTPS 的 TLS 加密讓竊聽者只看到亂碼。"
            "🔐 記得：網址列出現鎖頭圖示 = 安全</p>"
        ),
    },
    19: {  # 4G→5G→6G
        'html_append': _data('行動通訊速度演進',
            _mini_cards(
                ('📶', '3G（2003）', '2 Mbps，網頁', '#6b7280'),
                ('📱', '4G（2012）', '100 Mbps，影片', '#d97706'),
                ('⚡', '5G（2020）', '10 Gbps，IoT', '#2563eb'),
                ('🚀', '6G（預計2030）', '1 Tbps，XR 全息', '#16a34a'),
            ) +
            "<p style='font-size:.75rem;color:#374151;margin:8px 0 0;'>5G 延遲僅 1ms，讓自駕車、遠端手術、工廠自動化成為可能</p>"
        ),
    },
    21: {  # Starlink 台灣
        'html_append': _life('颱風停電還能上網？',
            "<p style='font-size:.82rem;color:#374151;line-height:1.6;margin:0 0 8px;'>"
            "2024 年凱米颱風重創台灣，部分山區光纖全斷。"
            "使用 Starlink 衛星網路的農民依然能上網通報狀況、聯繫救援。</p>"
            "<div style='display:grid;grid-template-columns:1fr 1fr;gap:8px;font-size:.8rem;'>"
            "<div style='background:#fff;padding:8px;border-radius:8px;border-left:3px solid #3b82f6;'>"
            "<p style='font-weight:700;margin:0 0 3px;'>🛰️ Starlink 規格</p>"
            "<p style='color:#374151;margin:0;'>速度：100–200 Mbps<br>延遲：25–50ms<br>台灣月租：NT$1,399</p></div>"
            "<div style='background:#fff;padding:8px;border-radius:8px;border-left:3px solid #3b82f6;'>"
            "<p style='font-weight:700;margin:0 0 3px;'>🌐 衛星數量</p>"
            "<p style='color:#374151;margin:0;'>已發射超過 6,000 顆<br>覆蓋全球 100+ 國家<br>2025 年台灣正式開放</p></div>"
            "</div>"
        ),
    },
    8: {  # IPv4 位址（新增互動）
        'html_append': _quiz_click(
            "下列哪一個「不是」合法的 IPv4 位址？",
            ["192.168.1.1", "8.8.8.8", "300.10.5.1", "255.255.255.0"],
            2,
            "IPv4 每一段介於 0–255（8 位元 = 2^8 = 256 個值），所以 300 超出範圍就不合法。"
            "192.168.x.x 是家用私有位址；8.8.8.8 是 Google DNS；255.255.255.0 常見於子網路遮罩。"
        ),
    },
    11: {  # 埠號與常見服務（新增互動題）
        'html_append': _reveal(
            "打開瀏覽器輸入 https://www.google.com，系統預設會用哪個 Port（埠號）？",
            "HTTP 是 80，HTTPS 是它的加密版",
            "HTTPS 預設 Port = <strong>443</strong>。若使用 HTTP（沒加 s），預設 Port = 80。"
            "其他常見 Port：SSH=22、FTP=21、SMTP=25、DNS=53。"
        ),
    },
    24: {  # 章末延伸閱讀
        'html_append': _ref('網際網路 — 延伸閱讀', [
            ('🌐', 'How the Internet Works（Code.org）', 'https://www.youtube.com/playlist?list=PLzdnOPI1iJNfMRZm5DDxco3UdsFegvuB7', '動畫短片，超入門'),
            ('📊', 'Speedtest 測速工具', 'https://www.speedtest.net/', '測你家網速'),
            ('🔒', 'HTTPS 憑證檢查（SSL Labs）', 'https://www.ssllabs.com/ssltest/', '看網站加密強度'),
            ('📡', 'Cloudflare Learning', 'https://www.cloudflare.com/zh-tw/learning/', '網路知識中文百科'),
            ('🎓', '教育部資安宣導', 'https://cissnet.edu.tw/', '學生資安素養'),
        ]),
    },
}

# ── Ch07：新興科技應用 ─────────────────────────────────────────

_ch07 = {
    3: {
        'html_append': "\n<div style='background:linear-gradient(135deg,#eff6ff,#dbeafe);border-radius:12px;padding:14px 16px;margin-top:14px;border-left:4px solid #3b82f6;'>\n  <h4 style='color:#1d4ed8;font-size:.85rem;font-weight:700;margin:0 0 8px;'>💡 生活實例：你家可能已經有 IoT 設備</h4>\n  <div style='font-size:.82rem;color:#374151;'><div style='display:grid;grid-template-columns:repeat(4,1fr);gap:8px;'><div style='background:#fff;padding:8px 10px;border-radius:8px;text-align:center;'><div style='font-size:1.4rem;'>📺</div><p style='font-size:.72rem;font-weight:700;color:#374151;margin:4px 0 2px;'>智慧電視</p><p style='font-size:.75rem;color:#2563eb;font-weight:600;margin:0;'>連網、記錄觀看習慣</p></div><div style='background:#fff;padding:8px 10px;border-radius:8px;text-align:center;'><div style='font-size:1.4rem;'>🔊</div><p style='font-size:.72rem;font-weight:700;color:#374151;margin:4px 0 2px;'>智慧音箱</p><p style='font-size:.75rem;color:#8b5cf6;font-weight:600;margin:0;'>Alexa/Siri 隨時在聽</p></div><div style='background:#fff;padding:8px 10px;border-radius:8px;text-align:center;'><div style='font-size:1.4rem;'>📡</div><p style='font-size:.72rem;font-weight:700;color:#374151;margin:4px 0 2px;'>Wi-Fi 路由器</p><p style='font-size:.75rem;color:#d97706;font-weight:600;margin:0;'>分析家中流量</p></div><div style='background:#fff;padding:8px 10px;border-radius:8px;text-align:center;'><div style='font-size:1.4rem;'>📷</div><p style='font-size:.72rem;font-weight:700;color:#374151;margin:4px 0 2px;'>網路攝影機</p><p style='font-size:.75rem;color:#dc2626;font-weight:600;margin:0;'>門鈴、監視器</p></div></div><p style='font-size:.75rem;color:#374151;margin:8px 0 0;'>全球 2025 年 IoT 設備數量已突破 <strong>200 億台</strong>，平均每人擁有 2.5 台</p></div>\n</div>",
    },
    5: {
        'video': {'type': 'search', 'query': 'IoT 資安 攻擊 智慧家庭 風險 駭客 案例', 'title': '▶ IoT 設備如何被駭客入侵', 'desc': '了解智慧家電的資安弱點'},
        'html_append': "\n<div style='background:linear-gradient(135deg,#eff6ff,#dbeafe);border-radius:12px;padding:14px 16px;margin-top:14px;border-left:4px solid #3b82f6;'>\n  <h4 style='color:#1d4ed8;font-size:.85rem;font-weight:700;margin:0 0 8px;'>💡 生活實例：你的智慧音箱在偷聽嗎？</h4>\n  <div style='font-size:.82rem;color:#374151;line-height:1.6;'><p style='margin:0 0 6px;'>2023 年研究發現，Amazon Echo 在沒有喚醒詞的情況下，每天平均有 <strong>19 次</strong>「誤喚醒」並錄音上傳。</p><p style='margin:0;color:#d97706;font-weight:600;'>🛡️ 自保方法：定期查看 Alexa/Siri 錄音紀錄，設定自動刪除</p></div>\n</div>",
    },
    6: {
        # ✅ 已驗證：IBM Technology 官方「What is edge computing?」
        'video': _vid_both(
            'cEOUeItHDdo',
            '邊緣運算 Edge Computing 介紹 教學 中文',
            'What is edge computing?（IBM Technology）',
            desc='想聽中文？點下方搜尋更多',
            search_title='▶ 邊緣運算中文教學搜尋',
        ),
        'html_append': "\n<div style='background:linear-gradient(135deg,#f0fdf4,#dcfce7);border-radius:12px;padding:14px 16px;margin-top:14px;border-left:4px solid #22c55e;'>\n  <h4 style='color:#15803d;font-size:.85rem;font-weight:700;margin:0 0 8px;'>🚀 創新應用：特斯拉自駕就是邊緣運算</h4>\n  <p style='font-size:.82rem;color:#374151;line-height:1.6;margin:0;'>特斯拉每輛車有一台 FSD 電腦（72 TOPS 算力），每秒處理 <strong>2,300 個影格</strong>的攝影機畫面，<strong>不傳到雲端</strong>，本地即時判斷。如果要傳到雲端再回傳，光網路延遲就夠讓車撞牆了。這就是邊緣運算的關鍵：<strong>低延遲 × 本地處理 = 生死之差</strong></p>\n</div>",
    },
    9: {
        'html_append': "\n<div style='background:linear-gradient(135deg,#eff6ff,#dbeafe);border-radius:12px;padding:14px 16px;margin-top:14px;border-left:4px solid #3b82f6;'>\n  <h4 style='color:#1d4ed8;font-size:.85rem;font-weight:700;margin:0 0 8px;'>💡 生活實例：台灣農民用 AIoT 種草莓</h4>\n  <div style='font-size:.82rem;color:#374151;line-height:1.6;'><p style='margin:0 0 6px;'>苗栗大湖草莓農場導入 AIoT 系統：</p><div style='display:flex;flex-direction:column;gap:5px;'><div style='background:#fff;padding:6px 10px;border-radius:6px;border-left:2px solid #22c55e;'>🌡️ 土壤感測器每 10 分鐘回傳溫度、濕度、pH 值</div><div style='background:#fff;padding:6px 10px;border-radius:6px;border-left:2px solid #22c55e;'>📱 AI 分析後自動灌溉，減少 40% 用水量</div><div style='background:#fff;padding:6px 10px;border-radius:6px;border-left:2px solid #22c55e;'>📸 攝影機辨識病蟲害，早期預警比人眼快 3 天</div><div style='background:#fff;padding:6px 10px;border-radius:6px;border-left:2px solid #22c55e;'>💰 產量提升 25%，人力成本降低 30%</div></div></div>\n</div>",
    },
    15: {
        # ✅ 已驗證：Simplilearn「Cloud Computing In 6 Minutes」
        'video': _vid_both(
            'M988_fsOSWo',
            '雲端運算 SaaS PaaS IaaS 介紹 教學 中文',
            'Cloud Computing In 6 Minutes（Simplilearn）',
            desc='想聽中文？點下方搜尋更多',
            search_title='▶ 雲端運算中文教學搜尋',
        ),
    },
    18: {
        'video': {'type': 'search', 'query': '量子電腦 原理 量子位元 教學 中文 淺顯易懂', 'title': '▶ 量子電腦是什麼？', 'desc': '用簡單比喻理解量子電腦原理'},
        'html_append': "\n<div style='background:linear-gradient(135deg,#f0fdf4,#dcfce7);border-radius:12px;padding:14px 16px;margin-top:14px;border-left:4px solid #22c55e;'>\n  <h4 style='color:#15803d;font-size:.85rem;font-weight:700;margin:0 0 8px;'>🚀 創新應用：量子電腦 vs 一般電腦</h4>\n  <div style='display:grid;grid-template-columns:repeat(4,1fr);gap:8px;'><div style='background:#fff;padding:8px 10px;border-radius:8px;text-align:center;'><div style='font-size:1.4rem;'>💻</div><p style='font-size:.72rem;font-weight:700;color:#374151;margin:4px 0 2px;'>一般電腦</p><p style='font-size:.75rem;color:#6b7280;font-weight:600;margin:0;'>位元：0 或 1</p></div><div style='background:#fff;padding:8px 10px;border-radius:8px;text-align:center;'><div style='font-size:1.4rem;'>⚛️</div><p style='font-size:.72rem;font-weight:700;color:#374151;margin:4px 0 2px;'>量子電腦</p><p style='font-size:.75rem;color:#8b5cf6;font-weight:600;margin:0;'>量子位元：0+1 疊加</p></div><div style='background:#fff;padding:8px 10px;border-radius:8px;text-align:center;'><div style='font-size:1.4rem;'>🔐</div><p style='font-size:.72rem;font-weight:700;color:#374151;margin:4px 0 2px;'>破解 RSA</p><p style='font-size:.75rem;color:#dc2626;font-weight:600;margin:0;'>一般：宇宙年齡也算不完</p></div><div style='background:#fff;padding:8px 10px;border-radius:8px;text-align:center;'><div style='font-size:1.4rem;'>⚡</div><p style='font-size:.72rem;font-weight:700;color:#374151;margin:4px 0 2px;'>量子電腦</p><p style='font-size:.75rem;color:#d97706;font-weight:600;margin:0;'>2048-bit RSA：數小時</p></div></div><p style='font-size:.75rem;color:#374151;margin:8px 0 0;'>Google 2023 年量子電腦用 <strong>200 秒</strong>完成傳統電腦需 47 年的計算</p>\n</div>",
    },
    19: {
        'html_append': "\n<div style='background:linear-gradient(135deg,#f0fdf4,#dcfce7);border-radius:12px;padding:14px 16px;margin-top:14px;border-left:4px solid #22c55e;'>\n  <h4 style='color:#15803d;font-size:.85rem;font-weight:700;margin:0 0 8px;'>🚀 創新應用：台北的智慧城市計畫</h4>\n  <div style='font-size:.82rem;color:#374151;line-height:1.6;'><div style='display:grid;grid-template-columns:1fr 1fr;gap:8px;'><div style='background:#fff;padding:8px;border-radius:8px;border-top:3px solid #22c55e;'><p style='font-weight:700;color:#15803d;margin:0 0 4px;'>🚦 智慧交通</p><p style='font-size:.78rem;margin:0;'>AI 即時調整號誌時序，尖峰時段車流量降低 15%</p></div><div style='background:#fff;padding:8px;border-radius:8px;border-top:3px solid #22c55e;'><p style='font-weight:700;color:#15803d;margin:0 0 4px;'>♻️ 智慧垃圾桶</p><p style='font-size:.78rem;margin:0;'>感測滿載度，清運路線優化，減少 30% 油耗</p></div><div style='background:#fff;padding:8px;border-radius:8px;border-top:3px solid #22c55e;'><p style='font-weight:700;color:#15803d;margin:0 0 4px;'>💧 漏水偵測</p><p style='font-size:.78rem;margin:0;'>AI 分析管線聲音，提早發現水管破裂，每年省數億元</p></div><div style='background:#fff;padding:8px;border-radius:8px;border-top:3px solid #22c55e;'><p style='font-weight:700;color:#15803d;margin:0 0 4px;'>🌡️ 熱島效應</p><p style='font-size:.78rem;margin:0;'>感測器全市佈建，找出熱點種樹降溫</p></div></div></div>\n</div>",
    },
}

# ── Ch08：巨量資料與資料科學 ─────────────────────────────────────────

_ch08 = {
    2: {
        # 雙模式：IBM 官方大數據介紹 + 搜尋備援
        'video': _vid_both(
            'j-0cUmUyb-Y',
            '大數據 Big Data 是什麼 教學 生活應用 中文',
            'What Is Big Data?（IBM Technology，可開自動字幕）',
            desc='想聽中文？點下方搜尋更多',
            search_title='▶ 大數據中文入門搜尋',
        ),
        'html_append': "\n<div style='background:linear-gradient(135deg,#eff6ff,#dbeafe);border-radius:12px;padding:14px 16px;margin-top:14px;border-left:4px solid #3b82f6;'>\n  <h4 style='color:#1d4ed8;font-size:.85rem;font-weight:700;margin:0 0 8px;'>💡 生活實例：Netflix 怎麼知道你想看什麼？</h4>\n  <p style='font-size:.82rem;color:#374151;line-height:1.6;margin:0 0 8px;'>Netflix 每天蒐集 <strong>1,億</strong> 筆用戶行為數據：</p><div style='font-size:.8rem;color:#374151;display:flex;flex-direction:column;gap:4px;'><div style='background:#fff;padding:6px 10px;border-radius:6px;border-left:2px solid #dc2626;'>🎬 你暫停在哪個時間點（代表那個鏡頭讓你有情緒）</div><div style='background:#fff;padding:6px 10px;border-radius:6px;border-left:2px solid #dc2626;'>⏩ 你跳過了片頭曲（代表你是老用戶）</div><div style='background:#fff;padding:6px 10px;border-radius:6px;border-left:2px solid #dc2626;'>🔄 你在哪一集棄劇（幫助他們改善劇本）</div><div style='background:#fff;padding:6px 10px;border-radius:6px;border-left:2px solid #dc2626;'>📸 縮圖用哪張你最容易點擊（A/B 測試）</div></div>\n</div>",
    },
    5: {
        'html_append': "\n<div style='background:linear-gradient(135deg,#f0fdf4,#dcfce7);border-radius:12px;padding:14px 16px;margin-top:14px;border-left:4px solid #22c55e;'>\n  <h4 style='color:#15803d;font-size:.85rem;font-weight:700;margin:0 0 8px;'>🚀 創新應用：資料科學在台灣的職缺</h4>\n  <p style='font-size:.82rem;color:#374151;line-height:1.6;margin:0 0 8px;'>根據 104 人力銀行 2025 數據：</p><div style='display:grid;grid-template-columns:repeat(4,1fr);gap:8px;'><div style='background:#fff;padding:8px 10px;border-radius:8px;text-align:center;'><div style='font-size:1.4rem;'>💼</div><p style='font-size:.72rem;font-weight:700;color:#374151;margin:4px 0 2px;'>資料分析師</p><p style='font-size:.75rem;color:#2563eb;font-weight:600;margin:0;'>平均月薪 NT$58,000</p></div><div style='background:#fff;padding:8px 10px;border-radius:8px;text-align:center;'><div style='font-size:1.4rem;'>🤖</div><p style='font-size:.72rem;font-weight:700;color:#374151;margin:4px 0 2px;'>機器學習工程師</p><p style='font-size:.75rem;color:#8b5cf6;font-weight:600;margin:0;'>平均月薪 NT$85,000</p></div><div style='background:#fff;padding:8px 10px;border-radius:8px;text-align:center;'><div style='font-size:1.4rem;'>📊</div><p style='font-size:.72rem;font-weight:700;color:#374151;margin:4px 0 2px;'>BI 分析師</p><p style='font-size:.75rem;color:#d97706;font-weight:600;margin:0;'>平均月薪 NT$55,000</p></div><div style='background:#fff;padding:8px 10px;border-radius:8px;text-align:center;'><div style='font-size:1.4rem;'>🔬</div><p style='font-size:.72rem;font-weight:700;color:#374151;margin:4px 0 2px;'>資料科學家</p><p style='font-size:.75rem;color:#16a34a;font-weight:600;margin:0;'>平均月薪 NT$95,000</p></div></div>\n</div>",
    },
    6: {
        'html_append': "\n<div style='background:linear-gradient(135deg,#eff6ff,#dbeafe);border-radius:12px;padding:14px 16px;margin-top:14px;border-left:4px solid #3b82f6;'>\n  <h4 style='color:#1d4ed8;font-size:.85rem;font-weight:700;margin:0 0 8px;'>💡 生活實例：健保資料庫救了多少人？</h4>\n  <p style='font-size:.82rem;color:#374151;line-height:1.6;margin:0 0 8px;'>台灣健保資料庫是全球最完整的醫療大數據之一，涵蓋 <strong>2,300 萬人</strong> 30 年的就醫紀錄。</p><div style='font-size:.8rem;display:flex;flex-direction:column;gap:5px;'><div style='background:#dbeafe;padding:7px 10px;border-radius:6px;'>🦠 COVID-19：台灣用健保大數據在疫情爆發前 3 天預測高風險族群</div><div style='background:#dbeafe;padding:7px 10px;border-radius:6px;'>💊 新藥副作用：比傳統臨床試驗快 10 倍發現罕見副作用</div><div style='background:#dbeafe;padding:7px 10px;border-radius:6px;'>🏥 醫療資源分配：找出偏鄉醫療缺口，派遣醫師支援</div></div>\n</div>",
    },
    10: {
        # ✅ 已驗證：數位發展部 moda 官方「開啟 Open Data 百寶箱！」
        'video': _vid_both(
            'ceYhPm_JGls',
            '開放資料 open data 應用 台灣 案例 教學',
            '開啟 Open Data 百寶箱！（數位發展部 moda 官方）',
            desc='想看更多開放資料應用案例？',
            search_title='▶ 更多台灣開放資料應用',
        ),
        'html_append': "\n<div style='background:linear-gradient(135deg,#f0fdf4,#dcfce7);border-radius:12px;padding:14px 16px;margin-top:14px;border-left:4px solid #22c55e;'>\n  <h4 style='color:#15803d;font-size:.85rem;font-weight:700;margin:0 0 8px;'>🚀 創新應用：政府開放資料能做什麼？</h4>\n  <p style='font-size:.82rem;color:#374151;line-height:1.6;margin:0 0 8px;'>data.gov.tw 有超過 <strong>46,000 個</strong> 開放資料集，學生可以免費使用：</p><div style='display:grid;grid-template-columns:1fr 1fr;gap:7px;font-size:.78rem;'><div style='background:#fff;padding:7px;border-radius:6px;'>🚌 公車即時位置 → App 開發</div><div style='background:#fff;padding:7px;border-radius:6px;'>🌦️ 空氣品質指數 → 警示系統</div><div style='background:#fff;padding:7px;border-radius:6px;'>🏘️ 房價歷史資料 → 趨勢分析</div><div style='background:#fff;padding:7px;border-radius:6px;'>📊 選舉開票資料 → 視覺化地圖</div></div>\n</div>",
    },
    19: {
        # ✅ 已驗證：蔡興正老師「Google 試算表的圖表製作」
        'video': _vid_both(
            'VyTFgQiR2eY',
            'Google 試算表 圖表 製作 教學 中文',
            'Google 試算表的圖表製作（蔡興正）',
            desc='想找進階圖表技巧？',
            search_title='▶ 更多 Google 試算表圖表教學',
        ),
    },
    20: {
        'html_append': "\n<div style='background:linear-gradient(135deg,#eff6ff,#dbeafe);border-radius:12px;padding:14px 16px;margin-top:14px;border-left:4px solid #3b82f6;'>\n  <h4 style='color:#1d4ed8;font-size:.85rem;font-weight:700;margin:0 0 8px;'>💡 生活實例：台灣資料新聞學的興起</h4>\n  <p style='font-size:.82rem;color:#374151;line-height:1.6;margin:0 0 6px;'>《報導者》、《天下雜誌》等媒體用資料視覺化說故事：</p><div style='font-size:.8rem;display:flex;flex-direction:column;gap:5px;'><div style='background:#fff;padding:7px 10px;border-radius:6px;border-left:2px solid #8b5cf6;'>📍 台灣房價地圖：用顏色顯示每坪價格，一眼看出哪裡最貴</div><div style='background:#fff;padding:7px 10px;border-radius:6px;border-left:2px solid #8b5cf6;'>👶 少子化趨勢：動態圖表顯示各縣市出生率 10 年變化</div><div style='background:#fff;padding:7px 10px;border-radius:6px;border-left:2px solid #8b5cf6;'>🌡️ 極端氣候：台灣各地高溫天數逐年增加的視覺化</div></div>\n</div>",
    },
    21: {
        'html_append': "\n<div style='background:linear-gradient(135deg,#eff6ff,#dbeafe);border-radius:12px;padding:14px 16px;margin-top:14px;border-left:4px solid #3b82f6;'>\n  <h4 style='color:#1d4ed8;font-size:.85rem;font-weight:700;margin:0 0 8px;'>💡 生活實例：這張圖在騙你！</h4>\n  <div style='font-size:.82rem;color:#374151;line-height:1.6;'><div style='display:grid;grid-template-columns:1fr 1fr;gap:8px;'><div style='background:#fef2f2;padding:8px;border-radius:8px;border-top:3px solid #ef4444;'><p style='font-weight:700;color:#dc2626;margin:0 0 4px;'>❌ 常見誤導手法</p><p style='font-size:.78rem;margin:0;'>Y 軸不從 0 開始 → 微小差距看起來很大<br>截斷 X 軸 → 隱藏不利的時間段</p></div><div style='background:#f0fdf4;padding:8px;border-radius:8px;border-top:3px solid #22c55e;'><p style='font-weight:700;color:#15803d;margin:0 0 4px;'>✅ 看圖 SOP</p><p style='font-size:.78rem;margin:0;'>① 看座標軸起點<br>② 確認樣本數（n=?）<br>③ 找資料來源</p></div></div></div>\n</div>",
    },
}

# ── Ch09：資料分析實作 ─────────────────────────────────────────

_ch09 = {
    3: {
        'video': {'type': 'search', 'query': 'Excel 函數 SUM AVERAGE COUNTIF 基礎教學 中文', 'title': '▶ Excel 最常用函數實作教學', 'desc': '快速學會試算表基礎函數'},
    },
    4: {
        'html_append': '\n<div style=\'background:linear-gradient(135deg,#eff6ff,#dbeafe);border-radius:12px;padding:14px 16px;margin-top:14px;border-left:4px solid #3b82f6;\'>\n  <h4 style=\'color:#1d4ed8;font-size:.85rem;font-weight:700;margin:0 0 8px;\'>💡 生活實例：期末成績單的實際用途</h4>\n  <div style=\'font-size:.82rem;color:#374151;line-height:1.6;\'><p style=\'margin:0 0 6px;\'>假設班上 30 人成績已輸入試算表，你可以用一個公式回答：</p><div style=\'display:flex;flex-direction:column;gap:5px;\'><div style=\'background:#dbeafe;padding:7px 10px;border-radius:6px;\'><code style=\'color:#1d4ed8;\'>=COUNTIF(B2:B31,">=60")</code> → 及格人數</div><div style=\'background:#dbeafe;padding:7px 10px;border-radius:6px;\'><code style=\'color:#1d4ed8;\'>=COUNTIF(B2:B31,">=90")</code> → 優秀人數（90分以上）</div><div style=\'background:#dcfce7;padding:7px 10px;border-radius:6px;\'><code style=\'color:#15803d;\'>=SUMIF(C2:C31,"男",B2:B31)</code> → 男生總分（計算平均用）</div></div></div>\n</div>',
    },
    9: {
        # ✅ 已驗證：Excel Campus - Jon「Excel Vlookup Tutorial - Everything You Need To Know」
        'video': _vid_both(
            'd3BYVQ6xIE4',
            'VLOOKUP 函數 教學 Excel 中文 實例',
            'Excel VLOOKUP Tutorial（Excel Campus，可開自動中文字幕）',
            desc='想找中文教學？點下方搜尋',
            search_title='▶ VLOOKUP 中文教學搜尋',
        ),
        'html_append': "\n<div style='background:linear-gradient(135deg,#eff6ff,#dbeafe);border-radius:12px;padding:14px 16px;margin-top:14px;border-left:4px solid #3b82f6;'>\n  <h4 style='color:#1d4ed8;font-size:.85rem;font-weight:700;margin:0 0 8px;'>💡 生活實例：VLOOKUP 的最強使用場景</h4>\n  <div style='font-size:.82rem;color:#374151;line-height:1.6;'><p style='margin:0 0 6px;'>📋 <strong>情境</strong>：你有 300 個學號，要從另一張表找出對應的姓名和班級</p><p style='margin:0 0 6px;'>手動複製貼上：需要 <strong>300 個步驟</strong>，容易出錯</p><p style='margin:0;'>用 VLOOKUP：<code style='color:#1d4ed8;background:#dbeafe;padding:2px 6px;border-radius:4px;'>=VLOOKUP(A2,學生名冊!$A:$C,2,0)</code> → <strong>1 個公式向下拉，30 秒完成</strong></p></div>\n</div>",
    },
    13: {
        'video': {'type': 'search', 'query': '樞紐分析表 Excel 教學 入門 實例 中文', 'title': '▶ 樞紐分析表 5 分鐘入門', 'desc': '快速掌握樞紐分析表的核心操作'},
        'html_append': "\n<div style='background:linear-gradient(135deg,#eff6ff,#dbeafe);border-radius:12px;padding:14px 16px;margin-top:14px;border-left:4px solid #3b82f6;'>\n  <h4 style='color:#1d4ed8;font-size:.85rem;font-weight:700;margin:0 0 8px;'>💡 生活實例：老闆要每月業績報表，你怎麼做？</h4>\n  <div style='font-size:.82rem;color:#374151;line-height:1.6;'><p style='margin:0 0 4px;'>原始資料：12,000 筆銷售記錄（日期、產品、業務員、金額）</p><p style='margin:0 0 4px;color:#dc2626;'>😓 手動整理：要用 SUMIF 一個一個算，花 3 小時</p><p style='margin:0;color:#15803d;font-weight:600;'>✅ 樞紐分析表：拖拉 3 個欄位，10 秒看到每月每業務的業績表</p></div>\n</div>",
    },
    19: {
        'html_append': "\n<div style='background:linear-gradient(135deg,#eff6ff,#dbeafe);border-radius:12px;padding:14px 16px;margin-top:14px;border-left:4px solid #3b82f6;'>\n  <h4 style='color:#1d4ed8;font-size:.85rem;font-weight:700;margin:0 0 8px;'>💡 生活實例：用趨勢線預測明年成績</h4>\n  <p style='font-size:.82rem;color:#374151;line-height:1.6;margin:0 0 8px;'>如果你有過去 5 年學測平均分數的資料，加上趨勢線後，Excel 可以用 <code style='color:#6d28d9;background:#ede9fe;padding:1px 5px;border-radius:3px;'>FORECAST</code> 函數預測明年的分數走向。</p><p style='font-size:.82rem;color:#374151;margin:0;'>企業用同樣方法預測下季業績、庫存需求、電力用量。資料 + 趨勢線 = 讓過去的數字預測未來。</p>\n</div>",
    },
    21: {
        'html_append': "\n<div style='background:linear-gradient(135deg,#f0fdf4,#dcfce7);border-radius:12px;padding:14px 16px;margin-top:14px;border-left:4px solid #22c55e;'>\n  <h4 style='color:#15803d;font-size:.85rem;font-weight:700;margin:0 0 8px;'>🚀 創新應用：相關不等於因果！</h4>\n  <div style='font-size:.82rem;color:#374151;line-height:1.6;'><p style='margin:0 0 8px;font-weight:700;'>📈 以下相關係數都很高，但邏輯上沒有因果關係：</p><div style='display:flex;flex-direction:column;gap:5px;'><div style='background:#fef9c3;padding:7px 10px;border-radius:6px;border-left:2px solid #f59e0b;'>🍦 夏天冰淇淋銷量 vs 溺水人數（r = 0.97）→ 真正原因：夏天</div><div style='background:#fef9c3;padding:7px 10px;border-radius:6px;border-left:2px solid #f59e0b;'>📽️ 尼可拉斯凱吉電影數 vs 游泳池溺水數（r = 0.87）</div><div style='background:#fef9c3;padding:7px 10px;border-radius:6px;border-left:2px solid #f59e0b;'>🧀 起司消費量 vs 被棉被悶死人數（r = 0.95）</div></div><p style='color:#d97706;font-weight:700;margin:8px 0 0;'>⚠️ 看到高相關時，永遠問：「有沒有第三個變數在作怪？」</p></div>\n</div>",
    },
}

# ── Ch10：Power BI 與期末總結 ─────────────────────────────────────────

_ch10 = {
    2: {
        # ✅ 已驗證：Microsoft Power BI 官方「What is Power BI?」
        'video': _vid_both(
            'yKTSLffVGbk',
            'Power BI 是什麼 教學 入門 儀表板 中文',
            'What is Power BI?（Microsoft Power BI 官方）',
            desc='想看中文完整教學？',
            search_title='▶ Power BI 中文入門教學搜尋',
        ),
        'html_append': "\n<div style='background:linear-gradient(135deg,#eff6ff,#dbeafe);border-radius:12px;padding:14px 16px;margin-top:14px;border-left:4px solid #3b82f6;'>\n  <h4 style='color:#1d4ed8;font-size:.85rem;font-weight:700;margin:0 0 8px;'>💡 生活實例：台積電用 Power BI 管理全球供應鏈</h4>\n  <p style='font-size:.82rem;color:#374151;line-height:1.6;margin:0;'>台積電在全球有數百個供應商，每天產生數百萬筆採購、庫存、品質數據。Power BI 儀表板讓採購主管在同一個畫面看到：全球庫存水位、交期達成率、品質不良率。以前要開 10 個 Excel 花 2 小時整理，現在開 Power BI 即時更新，<strong>節省 80% 報表時間</strong>。</p>\n</div>",
    },
    4: {
        'html_append': "\n<div style='background:linear-gradient(135deg,#faf5ff,#ede9fe);border-radius:12px;padding:14px 16px;margin-top:14px;border-left:4px solid #8b5cf6;'>\n  <h4 style='color:#6d28d9;font-size:.85rem;font-weight:700;margin:0 0 8px;'>📊 數據說話：Power BI 在台灣的滲透率</h4>\n  <div style='display:grid;grid-template-columns:repeat(4,1fr);gap:8px;'><div style='background:#fff;padding:8px 10px;border-radius:8px;text-align:center;'><div style='font-size:1.4rem;'>🏭</div><p style='font-size:.72rem;font-weight:700;color:#374151;margin:4px 0 2px;'>製造業</p><p style='font-size:.75rem;color:#2563eb;font-weight:600;margin:0;'>55% 已導入 BI 工具</p></div><div style='background:#fff;padding:8px 10px;border-radius:8px;text-align:center;'><div style='font-size:1.4rem;'>🏦</div><p style='font-size:.72rem;font-weight:700;color:#374151;margin:4px 0 2px;'>金融業</p><p style='font-size:.75rem;color:#16a34a;font-weight:600;margin:0;'>72% 使用資料儀表板</p></div><div style='background:#fff;padding:8px 10px;border-radius:8px;text-align:center;'><div style='font-size:1.4rem;'>🛒</div><p style='font-size:.72rem;font-weight:700;color:#374151;margin:4px 0 2px;'>零售業</p><p style='font-size:.75rem;color:#d97706;font-weight:600;margin:0;'>即時庫存 × 銷售分析</p></div><div style='background:#fff;padding:8px 10px;border-radius:8px;text-align:center;'><div style='font-size:1.4rem;'>💰</div><p style='font-size:.72rem;font-weight:700;color:#374151;margin:4px 0 2px;'>節省成本</p><p style='font-size:.75rem;color:#8b5cf6;font-weight:600;margin:0;'>平均減少 35% 報表人力</p></div></div><p style='font-size:.75rem;color:#374151;margin:8px 0 0;'>來源：IDC 台灣企業資料分析調查 2024</p>\n</div>",
    },
    6: {
        'html_append': "\n<div style='background:linear-gradient(135deg,#f0fdf4,#dcfce7);border-radius:12px;padding:14px 16px;margin-top:14px;border-left:4px solid #22c55e;'>\n  <h4 style='color:#15803d;font-size:.85rem;font-weight:700;margin:0 0 8px;'>🚀 創新應用：一張好的儀表板長什麼樣？</h4>\n  <div style='font-size:.82rem;color:#374151;'><div style='display:grid;grid-template-columns:1fr 1fr;gap:8px;'><div style='background:#f0fdf4;padding:8px;border-radius:8px;border-top:3px solid #22c55e;'><p style='font-weight:700;color:#15803d;font-size:.8rem;margin:0 0 4px;'>✅ 好的設計</p><p style='font-size:.75rem;margin:0;'>3 秒內看懂主要結論<br>顏色不超過 3 種<br>最重要數字放左上角<br>KPI 一眼比較達標/未達標</p></div><div style='background:#fef2f2;padding:8px;border-radius:8px;border-top:3px solid #ef4444;'><p style='font-weight:700;color:#dc2626;font-size:.8rem;margin:0 0 4px;'>❌ 常見錯誤</p><p style='font-size:.75rem;margin:0;'>塞滿 20 個圖表<br>3D 圓餅圖讓人看不懂比例<br>顏色太多造成混亂<br>沒有時間軸脈絡</p></div></div></div>\n</div>",
    },
    9: {
        # ✅ 已驗證：簡單實驗室「Power BI 教學入門｜從零開始做出銷售儀表板」（2025，中文）
        'video': _vid_both(
            'rAupdv0I_Us',
            'Power BI 連接資料 教學 中文',
            'Power BI 教學入門｜從零做出銷售儀表板（簡單實驗室）',
            desc='想比較不同教學風格？',
            search_title='▶ 更多 Power BI 中文教學',
        ),
    },
    19: {
        'html_append': "\n<div style='background:linear-gradient(135deg,#eff6ff,#dbeafe);border-radius:12px;padding:14px 16px;margin-top:14px;border-left:4px solid #3b82f6;'>\n  <h4 style='color:#1d4ed8;font-size:.85rem;font-weight:700;margin:0 0 8px;'>💡 生活實例：你是幾星級的數位公民？</h4>\n  <div style='font-size:.82rem;color:#374151;'><div style='display:flex;flex-direction:column;gap:6px;'><div style='background:#fef9c3;padding:8px 12px;border-radius:8px;border-left:3px solid #f59e0b;'><p style='font-weight:700;color:#92400e;margin:0 0 2px;'>⭐ 初級：會用工具</p><p style='font-size:.78rem;margin:0;'>Office、Google Workspace、手機 App 基本操作</p></div><div style='background:#dcfce7;padding:8px 12px;border-radius:8px;border-left:3px solid #22c55e;'><p style='font-weight:700;color:#15803d;margin:0 0 2px;'>⭐⭐ 中級：能創造價值</p><p style='font-size:.78rem;margin:0;'>資料分析、視覺化、自動化流程、資訊判讀</p></div><div style='background:#dbeafe;padding:8px 12px;border-radius:8px;border-left:3px solid #3b82f6;'><p style='font-weight:700;color:#1d4ed8;margin:0 0 2px;'>⭐⭐⭐ 高級：懂倫理與影響</p><p style='font-size:.78rem;margin:0;'>理解 AI 偏見、個資保護、數位落差、科技社會責任</p></div></div></div>\n</div>",
    },
    21: {
        'html_append': "\n<div style='background:linear-gradient(135deg,#f0fdf4,#dcfce7);border-radius:12px;padding:14px 16px;margin-top:14px;border-left:4px solid #22c55e;'>\n  <h4 style='color:#15803d;font-size:.85rem;font-weight:700;margin:0 0 8px;'>🚀 創新應用：AI 不會取代你，懂 AI 的人才會</h4>\n  <div style='font-size:.82rem;color:#374151;line-height:1.6;'><p style='margin:0 0 8px;'>2025 WEF（世界經濟論壇）報告：未來 5 年，<strong>85% 的工作會被 AI 改變</strong>，但只有 <strong>14%</strong> 工作會完全消失。</p><p style='font-weight:700;margin:0 0 6px;'>AI 時代最需要的技能：</p><div style='display:grid;grid-template-columns:1fr 1fr;gap:6px;font-size:.78rem;'><div style='background:#fff;padding:7px;border-radius:6px;'>🎯 <strong>提問力</strong>：懂得給 AI 好的 Prompt</div><div style='background:#fff;padding:7px;border-radius:6px;'>🔍 <strong>判斷力</strong>：驗證 AI 輸出是否正確</div><div style='background:#fff;padding:7px;border-radius:6px;'>🤝 <strong>溝通力</strong>：AI 無法替代人際關係</div><div style='background:#fff;padding:7px;border-radius:6px;'>🎨 <strong>創意力</strong>：定義問題比解題更重要</div></div></div>\n</div>",
    },
    24: {
        'html_append': _ref('Power BI 與後續學習資源', [
            ('📊', 'Microsoft Power BI（免費）', 'https://powerbi.microsoft.com/zh-tw/', '個人版完全免費'),
            ('🎓', 'Microsoft Learn — Power BI', 'https://learn.microsoft.com/zh-tw/training/', '官方免費中文課程'),
            ('🏆', 'PL-300 認證考試', 'https://learn.microsoft.com/zh-tw/certifications/exams/pl-300', '學生半價考證照'),
            ('🌱', 'Kaggle 資料科學競賽', 'https://www.kaggle.com/', '免費練習資料集'),
            ('📚', 'Google 數據分析專業認證', 'https://www.coursera.org/professional-certificates/google-data-analytics', 'Coursera 熱門課程'),
        ]),
    },
}

# ── 為 Ch07/Ch08/Ch09 追加章末延伸閱讀與 Ch09 VLOOKUP 互動練習 ─────────
_ch07[24] = {
    'html_append': _ref('新興科技 — 延伸閱讀', [
        ('🏙️', '台北市智慧城市', 'https://smartcity.taipei/', '台灣智慧城市案例'),
        ('🌍', 'IBM 量子電腦體驗（免費）', 'https://quantum.ibm.com/', '線上寫量子程式'),
        ('📡', 'IoT for Beginners（Microsoft）', 'https://microsoft.github.io/IoT-For-Beginners/', '免費入門教材'),
        ('🎓', 'Coursera 新興科技課程', 'https://www.coursera.org/browse/information-technology', '進階學習'),
    ]),
}
_ch08[24] = {
    'html_append': _ref('巨量資料與資料科學 — 延伸閱讀', [
        ('🇹🇼', '政府資料開放平台 data.gov.tw', 'https://data.gov.tw/', '4.6 萬筆免費資料集'),
        ('📊', 'Our World in Data（英）', 'https://ourworldindata.org/', '全球最好的資料視覺化'),
        ('📰', '報導者 The Reporter（資料新聞）', 'https://www.twreporter.org/', '台灣資料新聞範例'),
        ('🎨', 'Flourish 免費視覺化工具', 'https://flourish.studio/', '做動態圖表超好用'),
    ]),
}
_ch09[24] = {
    'html_append': _ref('資料分析實作 — 延伸閱讀', [
        ('📗', 'Excel 官方教學', 'https://support.microsoft.com/zh-tw/excel', '所有函數說明'),
        ('🎓', 'ExcelJet 函數速查', 'https://exceljet.net/', '英文但範例超豐富'),
        ('📺', 'PAPAYA 電腦教室（YouTube）', 'https://www.youtube.com/@papayaclass', '中文 Excel 教學'),
        ('🧮', 'Google 試算表函數清單', 'https://support.google.com/docs/table/25273', '官方函數字典'),
    ]),
}
# Ch9 slide 9：VLOOKUP 之後加入互動練習題
_ch09[9] = {
    # ✅ 已驗證：Excel Campus - Jon「Excel Vlookup Tutorial」
    'video': _vid_both(
        'd3BYVQ6xIE4',
        'VLOOKUP 函數 教學 Excel 中文 實例',
        'Excel VLOOKUP Tutorial（Excel Campus，可開自動中文字幕）',
        desc='想找中文教學？點下方搜尋',
        search_title='▶ VLOOKUP 中文教學搜尋',
    ),
    'html_append': _ch09[9]['html_append'] + _quiz_click(
        "公式 =VLOOKUP(A2, 資料!$A$2:$C$100, 3, 0) 意思是？",
        ["找 A2 的值，回傳第 3 列",
         "在「資料」工作表 A 欄找 A2，找到後回傳同一列的「第 3 欄」，需完全符合",
         "把 A2 到 A100 的第 3 欄相加",
         "把 3 個欄位複製到 A2"],
        1,
        "VLOOKUP(要找的值, 查詢範圍, 回傳第幾欄, 精確符合?)。"
        "$ 是絕對參照，往下拉公式時範圍不會跑掉；最後參數 0（或 FALSE）代表要精確符合。"
    ),
}

# ── 總彙整 ─────────────────────────────────────────────────────────────

ENHANCEMENTS = {
    1:  _ch01,
    2:  _ch02,
    3:  _ch03,
    4:  _ch04,
    5:  _ch05,
    6:  _ch06,
    7:  _ch07,
    8:  _ch08,
    9:  _ch09,
    10: _ch10,
}
