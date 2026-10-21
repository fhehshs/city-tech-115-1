# -*- coding: utf-8 -*-
# Week 9: 用 Google 試算表分析開放資料（從零開始）

CHAPTERS = [
    {'name': '封面', 'start': 1},
    {'name': '第一章：試算表入門與開放資料', 'start': 2},
    {'name': '第二章：基本函數', 'start': 8},
    {'name': '第三章：排序、篩選與樞紐分析表', 'start': 14},
    {'name': '第四章：圖表與趨勢線', 'start': 19},
    {'name': '個人練習', 'start': 24},
]

QUIZZES = {
    'q1': {
        'title': '第一章 隨堂測驗',
        'questions': [
            {
                'q': '「A2:A20」在試算表裡代表什麼？',
                'options': ['A2 和 A20 兩格', 'A 欄第 2 列到第 20 列的所有儲存格', '第 2 欄到第 20 欄', 'A2 除以 A20'],
                'answer': 1,
                'explain': '冒號表示「從…到…」的範圍。A2:A20 是 A 欄連續 19 格；如果只要 A2 和 A20 兩格，要寫成 A2,A20。',
            },
            {
                'q': '下面哪一種格式，是「欄位用逗號隔開、每筆資料一行」的純文字表格？',
                'options': ['JSON', 'PDF', 'CSV', 'JPG'],
                'answer': 2,
                'explain': 'CSV（Comma-Separated Values）用逗號分隔欄位、用換行分隔每筆資料，任何試算表都能直接開啟，是開放資料最常見的格式。JSON 則是「{屬性: 值}」的結構，常給程式讀取。',
            },
            {
                'q': '把 CSV 匯入 Google 試算表後，中文全部變成亂碼，最可能的原因是？',
                'options': ['檔案太大', '檔案的文字編碼不是 UTF-8（例如 Big5）', '沒有登入 Google', '儲存格寬度太窄'],
                'answer': 1,
                'explain': '有些政府 CSV 用 Big5 編碼。可以改下載平臺提供的 UTF-8 版本，或先用記事本「另存新檔 → 編碼選 UTF-8」再匯入。',
            },
        ]
    },
    'q2': {
        'title': '第二章 隨堂測驗',
        'questions': [
            {
                'q': 'B 欄是各縣市出生數，要算出「出生數超過 10000 的縣市有幾個」，應該用哪個公式？',
                'options': ['=SUM(B2:B23,">10000")', '=COUNTIF(B2:B23,">10000")', '=COUNT(B2:B23)', '=IF(B2>10000,1,0)'],
                'answer': 1,
                'explain': 'COUNTIF(範圍, 條件) 計算「符合條件的格子有幾個」。SUM 是加總、COUNT 只算有數字的格子數，IF 一次只判斷一格。',
            },
            {
                'q': 'A 欄是縣市、B 欄是出生數。要加總「臺北市」所有月份的出生數，應該用？',
                'options': ['=SUMIF(A:A,"臺北市",B:B)', '=COUNTIF(A:A,"臺北市")', '=SUM(A:A,B:B)', '=AVERAGE(B:B)'],
                'answer': 0,
                'explain': 'SUMIF(條件範圍, 條件, 加總範圍)：在 A 欄找「臺北市」，把同一列 B 欄的數字加起來。COUNTIF 只會算出臺北市出現幾次。',
            },
            {
                'q': 'C2 輸入 =B2/B$24，往下拉到 C3 時，公式會變成什麼？',
                'options': ['=B3/B$24', '=B3/B$25', '=B2/B$24', '=C3/C$25'],
                'answer': 0,
                'explain': '沒加 $ 的 B2 會跟著往下變成 B3；B$24 的 $ 鎖住列號，所以永遠除以第 24 列的合計。這就是「絕對參照」。',
            },
        ]
    },
    'q3': {
        'title': '第三章 隨堂測驗',
        'questions': [
            {
                'q': '想把 幾千列「各鄉鎮、各月份」的出生資料，變成「每個縣市一列的總數表」，最快的方法是？',
                'options': ['一格一格手動加', '插入 → 樞紐分析表，列放「縣市」、值放「出生數」加總', '把字體放大', '刪掉其他縣市'],
                'answer': 1,
                'explain': '樞紐分析表專門做「分組彙總」：選好要分組的欄位（列）和要計算的欄位（值），幾秒就完成，而且不會改到原始資料。',
            },
            {
                'q': '在 Google 試算表開啟「篩選器」，只勾選「臺中市」之後，其他縣市的資料會？',
                'options': ['被永久刪除', '暫時隱藏，取消篩選就會回來', '移到另一個工作表', '變成 0'],
                'answer': 1,
                'explain': '篩選只是「暫時不顯示」，資料都還在。所以篩選前不用擔心，但要記得：被隱藏的列 SUM 仍然會算進去。',
            },
            {
                'q': '樞紐分析表的「值」可以選擇的計算方式，下面哪一個不是？',
                'options': ['SUM 加總', 'AVERAGE 平均', 'COUNTA 計數', 'VLOOKUP 查詢'],
                'answer': 3,
                'explain': '「值」可以選加總、平均、計數、最大、最小等彙總方式。VLOOKUP 是查詢函數，不是彙總方式。',
            },
        ]
    },
    'q4': {
        'title': '第四章 隨堂測驗',
        'questions': [
            {
                'q': '想呈現「2016 到 2024 年全國出生數的變化」，最適合哪一種圖？',
                'options': ['圓餅圖', '折線圖', '散佈圖', '雷達圖'],
                'answer': 1,
                'explain': '「隨時間變化」用折線圖最清楚。圓餅圖用來看比例，散佈圖用來看兩個數值之間的關係。',
            },
            {
                'q': '長條圖和直方圖長得很像，差別在哪裡？',
                'options': ['完全一樣', '長條圖比較「類別」（如各縣市），直方圖看「數值的分布」（如幾個鄉鎮落在每個區間）', '直方圖只能畫一根', '長條圖不能有標題'],
                'answer': 1,
                'explain': '長條圖的橫軸是類別，長條之間有間隔；直方圖的橫軸是連續的數值區間，看資料集中在哪裡。',
            },
            {
                'q': '兩條趨勢線，一條 R² = 0.95、一條 R² = 0.40，哪一個說法正確？',
                'options': ['R² = 0.40 比較準', 'R² = 0.95 的趨勢線比較貼近資料點，用來預測比較可靠', 'R² 越大代表數字越大', 'R² 和預測無關'],
                'answer': 1,
                'explain': 'R²（判定係數）在 0 到 1 之間，越接近 1 代表趨勢線越能說明資料的變化。但它只說明「貼不貼近」，不代表因果關係，也不保證未來一定照這條線走。',
            },
            {
                'q': '資料顯示「冰淇淋賣越多的月份，溺水的人越多」，最合理的解讀是？',
                'options': ['吃冰淇淋會導致溺水', '兩者相關，但可能都是「天氣熱」造成的', '溺水會讓人想吃冰淇淋', '資料一定是錯的'],
                'answer': 1,
                'explain': '相關不等於因果。兩件事一起變化時，先想想有沒有「第三個因素」同時影響它們，這裡是夏天天氣熱。',
            },
        ]
    },
}

# ── 共用樣式 ─────────────────────────────────────────────
_TD = "padding:6px 8px;color:#374151;border-bottom:1px solid #e5e7eb;"
_TH = "padding:6px 8px;background:#1e40af;color:#fff;text-align:left;"


def _table(head, rows, font='0.85rem'):
    h = ''.join(f"<th style='{_TH}'>{c}</th>" for c in head)
    b = ''.join("<tr>" + ''.join(f"<td style='{_TD}'>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f"<table style='width:100%;border-collapse:collapse;font-size:{font};'><tr>{h}</tr>{b}</table>"


def _box(title, body, bg='#eff6ff', color='#1e40af'):
    return (f"<div style='background:{bg};padding:14px 16px;border-radius:10px;margin-bottom:12px;'>"
            f"<h3 style='color:{color};font-size:1rem;margin:0 0 8px;'>{title}</h3>"
            f"<div style='color:#374151;font-size:0.88rem;line-height:1.65;'>{body}</div></div>")


def _code(s):
    return f"<code style='background:#fff;color:#1e40af;padding:2px 6px;border-radius:4px;font-weight:700;'>{s}</code>"


def _two(left, right):
    return f"<div style='display:grid;grid-template-columns:1fr 1fr;gap:18px;'><div>{left}</div><div>{right}</div></div>"


def _steps(items):
    lis = ''.join(
        f"<div style='display:flex;gap:10px;align-items:flex-start;margin-bottom:8px;'>"
        f"<span style='background:#2563eb;color:#fff;border-radius:50%;min-width:26px;height:26px;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:0.85rem;'>{i}</span>"
        f"<span style='color:#374151;font-size:0.9rem;line-height:1.6;'>{t}</span></div>"
        for i, t in enumerate(items, 1))
    return lis


def _slide(i, chapter, title, html, bg='white', quiz=None):
    return {'id': i, 'chapter': chapter, 'title': title, 'bg': bg,
            'quiz': quiz, 'chart': None, 'video': None, 'html': html}


def _quiz_slide(i, chapter, n, cn, desc, k):
    return _slide(i, chapter, f'🎯 第{cn}章 隨堂測驗', f"""
<div style='text-align:center;padding:20px;'>
  <div style='font-size:56px;margin-bottom:15px;'>🎯</div>
  <h2 style='color:#fff;font-size:2rem;font-weight:800;margin-bottom:10px;'>第{cn}章 隨堂測驗</h2>
  <p style='color:#e9d5ff;font-size:1.1rem;'>{desc} ── {k} 道題目，點擊作答！</p>
</div>""", bg='purple', quiz=n)


C1 = '第一章：試算表入門與開放資料'
C2 = '第二章：基本函數'
C3 = '第三章：排序、篩選與樞紐分析表'
C4 = '第四章：圖表與趨勢線'
C5 = '個人練習'

# 全國出生數（內政部戶政司公布，約數，單位：萬人）
_BIRTHS = [(2016, 20.8), (2017, 19.4), (2018, 18.2), (2019, 17.8), (2020, 16.5),
           (2021, 15.4), (2022, 13.9), (2023, 13.6), (2024, 13.5)]

SLIDES = [
    _slide(1, '封面', '用 Google 試算表分析開放資料', """
<div style='text-align:center;padding:30px 20px;'>
  <div style='font-size:72px;margin-bottom:20px;'>📈</div>
  <h1 style='font-size:2.6rem;font-weight:900;color:#fff;margin-bottom:12px;'>用 Google 試算表分析開放資料</h1>
  <h2 style='font-size:1.4rem;font-weight:400;color:#93c5fd;margin-bottom:30px;'>從打開第一份 CSV 開始</h2>
  <div style='display:flex;justify-content:center;gap:16px;flex-wrap:wrap;margin-bottom:30px;'>
    <span style='background:rgba(255,255,255,0.15);color:#e0f2fe;padding:8px 18px;border-radius:20px;'>📥 下載與匯入</span>
    <span style='background:rgba(255,255,255,0.15);color:#e0f2fe;padding:8px 18px;border-radius:20px;'>🧮 基本函數</span>
    <span style='background:rgba(255,255,255,0.15);color:#e0f2fe;padding:8px 18px;border-radius:20px;'>🗂️ 樞紐分析表</span>
    <span style='background:rgba(255,255,255,0.15);color:#e0f2fe;padding:8px 18px;border-radius:20px;'>📉 圖表與趨勢線</span>
  </div>
  <p style='color:#bfdbfe;font-size:1.05rem;'>城市科技 — 第九章｜沒用過試算表也沒關係，一步一步來</p>
</div>""", bg='navy'),

    # ── 第一章 ─────────────────────────────
    _slide(2, C1, '認識 Google 試算表', "<h2 class='slide-title'>認識 Google 試算表</h2>" + _two(
        _box('🧭 從哪裡開始？', _steps([
            '用學校 Google 帳號登入，打開 <strong>雲端硬碟</strong>',
            '左上角 <strong>＋ 新增 → Google 試算表</strong>',
            '左上角點「未命名的試算表」改檔名，例如「1班01號_出生數分析」',
            '不用按儲存：<strong>每次修改都會自動存到雲端</strong>',
        ])),
        _box('🔤 先認識 5 個名詞', _table(['名詞', '意思'], [
            ['欄', '直的，用英文字母 A、B、C…'],
            ['列', '橫的，用數字 1、2、3…'],
            ['儲存格', '欄和列交叉的一格，例如 <strong>B3</strong>'],
            ['工作表', '下方的分頁，一個檔案可以有很多張'],
            ['公式列', '上方顯示格子內容或公式的地方'],
        ]), bg='#f0fdf4', color='#15803d')
    )),
    _slide(3, C1, '儲存格、範圍與第一個公式', "<h2 class='slide-title'>儲存格、範圍與第一個公式</h2>" + _two(
        _box('📐 範圍的寫法', _table(['寫法', '代表'], [
            [_code('B3'), '一格'],
            [_code('A2:A20'), 'A 欄第 2 到 20 列'],
            [_code('A2:C5'), '一個長方形區塊，共 12 格'],
            [_code('B:B'), '整個 B 欄'],
        ])),
        _box('✏️ 動手：在格子裡算數學', _steps([
            'A1 輸入 <strong>120</strong>、A2 輸入 <strong>80</strong>',
            'A3 輸入 ' + _code('=A1+A2') + '，按 Enter 得到 200',
            '把 A1 改成 150，A3 自動變 230：<strong>公式會跟著資料更新</strong>',
            '所有公式都用 <strong>=</strong> 開頭；加減乘除是 + − * /',
        ]), bg='#fefce8', color='#a16207')
    )),
    _slide(4, C1, '開放資料常見格式：CSV 與 JSON', "<h2 class='slide-title'>開放資料常見格式：CSV 與 JSON</h2>" + _two(
        _box('📄 CSV：逗號分隔值', "欄位之間用<strong>逗號</strong>隔開、每筆資料<strong>換一行</strong>。用記事本打開長這樣："
             "<pre style='background:#fff;padding:10px;border-radius:6px;font-size:0.8rem;margin:8px 0;'>年,縣市,出生數\n2024,臺北市,15xxx\n2024,新北市,24xxx</pre>"
             "✅ 試算表直接開啟　⚠️ 欄位很多、很多空白時逗號很難對齊"),
        _box('🧩 JSON：{屬性 : 值}', "每筆資料用大括號包起來，<strong>屬性</strong>就像欄位名稱："
             "<pre style='background:#fff;padding:10px;border-radius:6px;font-size:0.8rem;margin:8px 0;'>{\"縣市\": \"臺北市\",\n \"出生數\": 15000}</pre>"
             "文字要加雙引號，數字不用。YouBike 即時資料就是 JSON，常給程式和 App 讀取。", bg='#faf5ff', color='#6d28d9')
    ) + "<div style='background:#f1f5f9;padding:10px 14px;border-radius:8px;font-size:0.85rem;color:#374151;'>💡 這週我們都用 <strong>CSV</strong>；Ch10 的 YouBike 儀表板會看到 JSON 怎麼變成表格。</div>"),
    _slide(5, C1, '到政府資料開放平臺找資料', "<h2 class='slide-title'>到政府資料開放平臺找資料</h2>" + _two(
        _box('🔎 找資料四步驟', _steps([
            '打開 <strong>data.gov.tw</strong>（政府資料開放平臺）',
            '搜尋關鍵字，例如「<strong>嬰兒出生數</strong>」',
            '看清楚：<strong>提供機關</strong>（內政部戶政司）、<strong>更新頻率</strong>、<strong>欄位說明</strong>',
            '在資料資源找 <strong>CSV</strong>，下載到電腦',
        ])),
        _box('✅ 下載前先問自己', "<ul style='padding-left:18px;margin:0;'>"
             "<li>這份資料的<strong>年份</strong>是我要的嗎？</li>"
             "<li>有<strong>哪些欄位</strong>？單位是人、次、還是千元？</li>"
             "<li>授權是「<strong>政府資料開放授權條款</strong>」嗎？（可自由使用，要標示來源）</li>"
             "<li>找不到想要的？試試<strong>各縣市資料平臺</strong>，如臺北市資料大平臺</li></ul>",
             bg='#f0fdf4', color='#15803d')
    )),
    _slide(6, C1, '把 CSV 匯入 Google 試算表', "<h2 class='slide-title'>把 CSV 匯入 Google 試算表</h2>" + _two(
        _box('📥 匯入步驟', _steps([
            '開一個新的 Google 試算表',
            '<strong>檔案 → 匯入 → 上傳</strong>，選剛下載的 CSV',
            '匯入位置選「<strong>插入新工作表</strong>」，分隔符號選「自動偵測」',
            '<strong>檢視 → 凍結 → 1 列</strong>：往下捲時還看得到欄位名稱',
            '把這張工作表改名為「<strong>原始資料</strong>」，之後不要直接改它',
        ])),
        _box('🛠️ 常見狀況', _table(['看到…', '怎麼辦'], [
            ['中文變亂碼', '檔案是 Big5：改下載 UTF-8 版，或用記事本另存成 UTF-8'],
            ['數字靠左、不能加總', '被當成文字：選取欄 → <strong>格式 → 數字</strong>'],
            ['第一列不是欄位名稱', '刪掉上方的說明列'],
            ['有「合計」列', '先刪掉，不然加總會重複計算'],
        ], font='0.8rem'), bg='#fff7ed', color='#c2410c')
    )),
    _quiz_slide(7, C1, 'q1', '一', '試算表入門與開放資料', 3),

    # ── 第二章 ─────────────────────────────
    _slide(8, C2, '函數怎麼寫：SUM、AVERAGE、MAX、MIN', "<h2 class='slide-title'>函數怎麼寫：SUM、AVERAGE、MAX、MIN</h2>" + _two(
        _box('📌 函數的語法', "<div style='background:#fff;padding:10px;border-radius:6px;text-align:center;font-family:monospace;font-size:1.05rem;color:#1e40af;font-weight:700;'>=函數名稱(範圍或條件)</div>"
             "<ul style='padding-left:18px;margin:10px 0 0;'><li>一定用 <strong>=</strong> 開頭</li><li>輸入 =SU 就會跳出提示，按 Tab 補完</li><li>文字條件要加雙引號，例如 \"臺北市\"</li></ul>") +
        _box('📋 範例資料：2024 各縣市出生數（B2:B23）', "A 欄＝縣市、B 欄＝出生數，共 22 個縣市", bg='#f8fafc', color='#475569'),
        _box('🧮 四個最常用的函數', _table(['想知道', '公式'], [
            ['全國總共出生多少人', _code('=SUM(B2:B23)')],
            ['平均每個縣市', _code('=AVERAGE(B2:B23)')],
            ['最多的縣市有幾人', _code('=MAX(B2:B23)')],
            ['最少的縣市有幾人', _code('=MIN(B2:B23)')],
        ]) + "<p style='font-size:0.8rem;color:#6b7280;margin:8px 0 0;'>💡 小技巧：選取一欄數字，右下角就會顯示加總，可以拿來驗算。</p>",
             bg='#f0fdf4', color='#15803d')
    )),
    _slide(9, C2, '數一數：COUNT、COUNTA、COUNTIF', "<h2 class='slide-title'>數一數：COUNT、COUNTA、COUNTIF</h2>" + _two(
        _box('🔢 三種「數幾個」', _table(['函數', '數什麼'], [
            [_code('COUNT'), '有<strong>數字</strong>的格子'],
            [_code('COUNTA'), '<strong>不是空白</strong>的格子（文字也算）'],
            [_code('COUNTIF'), '<strong>符合條件</strong>的格子'],
        ])),
        _box('✏️ 用出生數資料練習', _table(['問題', '公式'], [
            ['資料裡有幾個縣市？', _code('=COUNTA(A2:A23)')],
            ['出生數超過 1 萬的縣市有幾個？', _code('=COUNTIF(B2:B23,">10000")')],
            ['名稱裡有「市」的有幾個？', _code('=COUNTIF(A2:A23,"*市")')],
        ], font='0.8rem') + "<p style='font-size:0.8rem;color:#6b7280;margin:8px 0 0;'>條件寫法：\"&gt;10000\"、\"&gt;=60\"、\"臺北市\"；* 代表任意文字。</p>",
             bg='#fefce8', color='#a16207')
    )),
    _slide(10, C2, '條件加總：SUMIF 與 COUNTIFS', "<h2 class='slide-title'>條件加總：SUMIF 與 COUNTIFS</h2>"
        "<p style='color:#374151;font-size:0.9rem;margin-bottom:12px;'>下載的原始資料通常是「<strong>每個縣市、每個月一列</strong>」，同一個縣市會出現 12 次。這時候就需要「有條件的加總」。</p>" + _two(
        _box('➕ SUMIF(條件範圍, 條件, 加總範圍)', _code('=SUMIF(B:B,"臺北市",D:D)') +
             "<p style='margin:8px 0 0;'>在 B 欄（縣市）找「臺北市」，把同一列 D 欄（出生數）全部加起來 → 臺北市一整年的出生數。</p>"),
        _box('🎯 多個條件：COUNTIFS、SUMIFS', _code('=SUMIFS(D:D,B:B,"臺北市",C:C,"1月")') +
             "<p style='margin:8px 0 0;'>同時符合「臺北市」和「1 月」才加總。<br>注意 SUMIF<strong>S</strong> 的加總範圍放在<strong>最前面</strong>。</p>",
             bg='#f0fdf4', color='#15803d')
    ) + "<div style='background:#f1f5f9;padding:10px 14px;border-radius:8px;font-size:0.85rem;color:#374151;'>🤔 22 個縣市要寫 22 次 SUMIF？太慢了——第三章的<strong>樞紐分析表</strong>一次搞定。</div>"),
    _slide(11, C2, 'IF：讓試算表幫你判斷', "<h2 class='slide-title'>IF：讓試算表幫你判斷</h2>" + _two(
        _box('🔀 IF(條件, 成立時, 不成立時)', _code('=IF(B2>=10000,"萬人以上","未滿萬人")') +
             "<p style='margin:8px 0 0;'>B2 大於等於 10000 就顯示「萬人以上」，否則顯示「未滿萬人」。寫好一格，往下拉就全部完成。</p>"),
        _box('📈 和去年比：增加還是減少？', "C 欄放 2023 年、B 欄放 2024 年：<br>" + _code('=IF(B2>C2,"增加","減少")') +
             "<p style='margin:8px 0 0;'>再用 " + _code('=COUNTIF(D2:D23,"增加")') + " 數出有幾個縣市出生數比去年多。</p>",
             bg='#fefce8', color='#a16207')
    )),
    _slide(12, C2, '往下拉公式與 $ 符號', "<h2 class='slide-title'>往下拉公式與 $ 符號</h2>" + _two(
        _box('↕️ 填滿：寫一格就夠', _steps([
            '在 C2 寫好公式',
            '滑鼠移到 C2 右下角的<strong>小藍點</strong>',
            '往下拖曳（或連點兩下），公式自動複製到每一列',
            'C3 的公式會自動變成 B3、C4 變成 B4…這叫<strong>相對參照</strong>',
        ])),
        _box('🔒 算比例要用 $ 鎖住', "B24 是全國合計，C 欄要算「各縣市占全國幾 %」：<br>" + _code('=B2/B$24') +
             "<p style='margin:8px 0 0;'>往下拉時 B2→B3→B4，但 <strong>B$24 不會跑掉</strong>。$ 放在列號前就鎖列、放在欄名前就鎖欄、"
             + _code('$B$24') + " 兩個都鎖。</p><p style='margin:6px 0 0;'>最後按工具列的 <strong>%</strong> 改成百分比格式。</p>",
             bg='#faf5ff', color='#6d28d9')
    )),
    _quiz_slide(13, C2, 'q2', '二', '基本函數', 3),

    # ── 第三章 ─────────────────────────────
    _slide(14, C3, '排序與篩選', "<h2 class='slide-title'>排序與篩選：先把資料看清楚</h2>" + _two(
        _box('⬇️ 排序', _steps([
            '點選要排序的欄（例如出生數）中任一格',
            '<strong>資料 → 排序範圍 → 進階排序範圍選項</strong>',
            '勾「資料包含標題列」，選欄位、Z→A 由大到小',
        ]) + "<p style='font-size:0.8rem;color:#dc2626;margin:4px 0 0;'>⚠️ 不要只選一欄排序，其他欄會對不上！要選整個資料範圍。</p>"),
        _box('🔽 篩選', _steps([
            '點資料範圍任一格 → <strong>資料 → 建立篩選器</strong>',
            '欄位名稱旁出現 ▼，點開只勾「臺中市」',
            '只看到臺中市的列，<strong>其他列只是隱藏</strong>',
            '再按一次「移除篩選器」就恢復',
        ]), bg='#f0fdf4', color='#15803d')
    )),
    _slide(15, C3, '樞紐分析表是什麼？', "<h2 class='slide-title'>樞紐分析表是什麼？</h2>"
        "<p style='color:#374151;font-size:0.9rem;margin-bottom:12px;'>把「很長的明細表」變成「分組彙總表」，<strong>不用寫公式、不會改到原始資料</strong>。</p>" + _two(
        _box('📋 原始資料（幾千列）', _table(['年月', '縣市', '鄉鎮', '出生數'], [
            ['113/01', '臺北市', '大安區', '…'], ['113/01', '臺北市', '信義區', '…'],
            ['113/01', '新北市', '板橋區', '…'], ['⋮', '⋮', '⋮', '⋮'],
        ], font='0.78rem'), bg='#f8fafc', color='#475569'),
        _box('🗂️ 樞紐分析表（22 列）', _table(['縣市', '出生數 加總'], [
            ['新北市', '…'], ['臺中市', '…'], ['桃園市', '…'], ['⋮', '⋮'],
        ], font='0.78rem') + "<p style='font-size:0.8rem;margin:8px 0 0;'>四個區域：<strong>列</strong>（分組）、<strong>欄</strong>（再分一層）、<strong>值</strong>（算什麼）、<strong>篩選器</strong>（只看哪些）</p>",
             bg='#eff6ff', color='#1e40af')
    )),
    _slide(16, C3, '樞紐分析表實作：各縣市出生數', "<h2 class='slide-title'>樞紐分析表實作：各縣市出生數</h2>" + _two(
        _box('🛠️ 跟著做', _steps([
            '點「原始資料」任一格 → <strong>插入 → 樞紐分析表</strong> → 新工作表',
            '<strong>列 → 新增「縣市」</strong>',
            '<strong>值 → 新增「出生數」</strong>，彙總方式選 SUM',
            '列的排序依據改成「出生數 的 SUM」、遞減',
            '想看男女？<strong>欄 → 新增「性別」</strong>',
        ])),
        _box('🔍 看表回答問題', "<ul style='padding-left:18px;margin:0;'>"
             "<li>哪個縣市出生數最多？最少？</li>"
             "<li>前 3 名加起來占全國多少？（用第二章的 $ 公式算）</li>"
             "<li>改成列放「月份」：哪個月出生最多？</li>"
             "<li>把「篩選器」加上縣市，只看自己住的縣市</li></ul>"
             "<p style='font-size:0.8rem;color:#6b7280;margin:8px 0 0;'>💡 原始資料更新後，樞紐分析表會自動重算。</p>",
             bg='#fefce8', color='#a16207')
    )),
    _slide(17, C3, '加分技巧：條件式格式', "<h2 class='slide-title'>加分技巧：條件式格式</h2>" + _two(
        _box('🎨 讓重點自己跳出來', _steps([
            '選取出生數那一欄',
            '<strong>格式 → 條件式格式設定</strong>',
            '「色階」：數字越大顏色越深，一眼看出多寡',
            '或「單色」：大於 10000 的格子標成綠色',
        ])),
        _box('✅ 什麼時候用？', "<ul style='padding-left:18px;margin:0;'>"
             "<li>找出<strong>特別大或特別小</strong>的數字</li>"
             "<li>標出「比去年減少」的縣市</li>"
             "<li>檢查資料：空白、0、怪怪的數字（可能是輸入錯誤）</li></ul>"
             "<p style='font-size:0.8rem;color:#6b7280;margin:8px 0 0;'>顏色最多 2–3 種，太多反而看不出重點。</p>",
             bg='#f0fdf4', color='#15803d')
    )),
    _quiz_slide(18, C3, 'q3', '三', '排序、篩選與樞紐分析表', 3),

    # ── 第四章 ─────────────────────────────
    _slide(19, C4, '選對圖表類型', "<h2 class='slide-title'>選對圖表類型</h2>" + _table(['圖表', '用來', '出生數資料的例子'], [
        ['📊 長條圖', '比較<strong>不同類別</strong>的大小', '各縣市出生數'],
        ['📶 直方圖', '看<strong>數值的分布</strong>（落在每個區間的數量）', '全國 368 個鄉鎮，出生數 0–100、100–200…各有幾個'],
        ['📈 折線圖', '看<strong>隨時間的變化</strong>', '2016–2024 年全國出生數'],
        ['🥧 圓餅圖', '看<strong>占整體的比例</strong>（類別 5 個以內）', '六都 vs 其他縣市占全國比例'],
        ['⚬ 散佈圖', '看<strong>兩個數值的關係</strong>、找分群或異常值', '各縣市人口數 vs 出生數'],
    ]) + "<div style='display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:12px;font-size:0.85rem;'>"
         "<div style='background:#eff6ff;padding:10px;border-radius:8px;'>💡 <strong>長條圖 vs 直方圖</strong>：長得像但用途不同；長條之間有空隙＝類別，連在一起＝數值區間。</div>"
         "<div style='background:#fef2f2;padding:10px;border-radius:8px;'>⚠️ 22 個縣市畫圓餅圖會切得太碎，改用由大到小排序的長條圖。</div></div>"),
    _slide(20, C4, '插入圖表與圖表編輯器', "<h2 class='slide-title'>插入圖表與圖表編輯器</h2>" + _two(
        _box('🛠️ 三步做出一張圖', _steps([
            '選取資料（包含欄位名稱那一列）',
            '<strong>插入 → 圖表</strong>，右邊出現圖表編輯器',
            '「設定」：換圖表類型、確認 X 軸和資料系列',
            '「自訂」：改<strong>圖表標題</strong>、<strong>軸標題</strong>、顏色',
        ])),
        _box('✅ 一張合格的圖要有', "<ul style='padding-left:18px;margin:0;'>"
             "<li><strong>標題</strong>：說出這張圖在講什麼，例如「2024 年各縣市出生數」</li>"
             "<li><strong>軸標題與單位</strong>：人？萬人？</li>"
             "<li><strong>資料來源</strong>：內政部戶政司，政府資料開放平臺</li>"
             "<li>長條圖的 Y 軸<strong>從 0 開始</strong>，避免誇大差距（Ch08 的「資料說謊」）</li></ul>",
             bg='#f0fdf4', color='#15803d')
    )),
    _slide(21, C4, '趨勢線與 R²', "<h2 class='slide-title'>趨勢線與 R²：讓資料說出走向</h2>" + _two(
        _box('📐 先用 5 筆資料練習', _table(['x', '3', '4', '5', '8', '10'], [['y', '8', '10', '11', '23', '21']], font='0.82rem') +
             _steps([
                 '輸入資料 → 插入 → 圖表 → 改成<strong>散佈圖</strong>',
                 '自訂 → 系列 → 勾<strong>趨勢線</strong>',
                 '標籤選「使用方程式」，再勾「顯示 R²」',
             ]) + "<p style='margin:4px 0 0;'>得到 <strong>y ≈ 2.21x + 1.36</strong>，R² ≈ 0.87。<br>預測 x = 20 時：y ≈ 2.21×20 + 1.36 ≈ <strong>45.5</strong></p>"),
        _box('📏 R² 怎麼看？', "<ul style='padding-left:18px;margin:0;'>"
             "<li>介於 <strong>0 到 1</strong>，越接近 1，趨勢線越貼近資料點</li>"
             "<li>趨勢線類型有：線性、指數、多項式、對數…<strong>哪一種較準「不一定」</strong>，比較 R² 再決定</li>"
             "<li>R² 高只代表「貼近」，<strong>不代表因果</strong>，也不保證未來照著走</li></ul>"
             "<p style='font-size:0.8rem;color:#6b7280;margin:8px 0 0;'>延伸練習：舊講義的「催化劑質量 vs 反應速率」實驗數據，也可以用同樣方法畫關係圖、求方程式。</p>",
             bg='#faf5ff', color='#6d28d9')
    )),
    _slide(22, C4, '用趨勢線看全國出生數', "<h2 class='slide-title'>用趨勢線看全國出生數</h2>" + _two(
        _box('📉 2016–2024 全國出生數（約，萬人）', _table(['年', '出生數'], [[str(y), f'{v}'] for y, v in _BIRTHS], font='0.8rem') +
             "<p style='font-size:0.75rem;color:#6b7280;margin:6px 0 0;'>資料來源：內政部戶政司（2024 年 134,856 人、2023 年 135,571 人），上課以下載的資料為準。</p>",
             bg='#f8fafc', color='#475569'),
        _box('🔍 畫成折線圖＋趨勢線之後…', "<ul style='padding-left:18px;margin:0;'>"
             "<li>9 年從約 20.8 萬降到 13.5 萬，<strong>幾乎每年都減少</strong></li>"
             "<li>加上線性趨勢線，R² 會很接近 1</li>"
             "<li>但照直線預測，幾十年後會變 0——<strong>這合理嗎？</strong>趨勢線只是數學，解讀要加上常識</li>"
             "<li>想想看：出生數減少，城市的學校、交通、長照會受到什麼影響？→ 這就是<strong>期末報告的題目方向</strong></li></ul>",
             bg='#fefce8', color='#a16207')
    )),
    _quiz_slide(23, C4, 'q4', '四', '圖表與趨勢線', 4),

    # ── 個人練習 ─────────────────────────────
    _slide(24, C5, '個人練習：我的第一份開放資料分析（課堂練習）', """
<h2 class='slide-title'>🧪 個人練習：我的第一份開放資料分析（課堂練習）</h2>
<div style='display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-bottom:14px;'>
  <div style='background:#eff6ff;padding:12px;border-radius:10px;'><p style='color:#1e40af;font-weight:700;margin:0 0 6px;'>① 下載</p><p style='font-size:0.82rem;color:#374151;margin:0;'>在 data.gov.tw 找「嬰兒出生數」或自己有興趣的資料，下載 CSV 匯入試算表</p></div>
  <div style='background:#f0fdf4;padding:12px;border-radius:10px;'><p style='color:#15803d;font-weight:700;margin:0 0 6px;'>② 彙總</p><p style='font-size:0.82rem;color:#374151;margin:0;'>用樞紐分析表或 SUMIF 做出分組總表，再用 SUM、MAX、COUNTIF 算 3 個數字</p></div>
  <div style='background:#fefce8;padding:12px;border-radius:10px;'><p style='color:#a16207;font-weight:700;margin:0 0 6px;'>③ 圖表</p><p style='font-size:0.82rem;color:#374151;margin:0;'>做 2 張不同類型的圖，有標題、軸標與資料來源；有時間資料就加趨勢線</p></div>
  <div style='background:#faf5ff;padding:12px;border-radius:10px;'><p style='color:#6d28d9;font-weight:700;margin:0 0 6px;'>④ 解讀</p><p style='font-size:0.82rem;color:#374151;margin:0;'>寫 1 句「我從資料發現…」，並想一個可能的原因</p></div>
</div>
<div style='background:#f1f5f9;padding:12px 16px;border-radius:10px;font-size:0.88rem;color:#374151;line-height:1.7;'>
  <p style='font-weight:700;color:#1e40af;margin:0 0 4px;'>📝 練習說明</p>
  這是課堂練習，<strong>不用繳交</strong>。這四個步驟就是<strong>期末報告「正文」的做法</strong>：今天練熟，期末換成你自己的題目和資料再做一次。卡關時先回去看第 6、10、16、21 頁。
</div>"""),
    _slide(25, C5, '本週重點回顧', """
<h2 style='font-size:1.8rem;font-weight:800;color:#fff;margin-bottom:20px;text-align:center;'>📖 Week 9 重點回顧</h2>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:15px;'>
  <div style='background:rgba(255,255,255,0.12);padding:14px;border-radius:10px;'>
    <h3 style='color:#93c5fd;font-size:1rem;margin-bottom:8px;'>第一章 入門與開放資料</h3>
    <ul style='color:#e2e8f0;font-size:0.85rem;padding-left:16px;margin:0;'>
      <li>欄、列、儲存格、範圍 A2:A20</li>
      <li>CSV 與 JSON 兩種格式</li>
      <li>data.gov.tw 下載 → 匯入 → 凍結標題列</li>
    </ul>
  </div>
  <div style='background:rgba(255,255,255,0.12);padding:14px;border-radius:10px;'>
    <h3 style='color:#93c5fd;font-size:1rem;margin-bottom:8px;'>第二章 基本函數</h3>
    <ul style='color:#e2e8f0;font-size:0.85rem;padding-left:16px;margin:0;'>
      <li>SUM、AVERAGE、MAX、MIN、COUNTIF</li>
      <li>SUMIF 條件加總、IF 判斷</li>
      <li>往下拉公式與 $ 絕對參照</li>
    </ul>
  </div>
  <div style='background:rgba(255,255,255,0.12);padding:14px;border-radius:10px;'>
    <h3 style='color:#93c5fd;font-size:1rem;margin-bottom:8px;'>第三章 排序、篩選、樞紐</h3>
    <ul style='color:#e2e8f0;font-size:0.85rem;padding-left:16px;margin:0;'>
      <li>排序要選整個範圍</li>
      <li>篩選只是暫時隱藏</li>
      <li>樞紐分析表：列、欄、值、篩選器</li>
    </ul>
  </div>
  <div style='background:rgba(255,255,255,0.12);padding:14px;border-radius:10px;'>
    <h3 style='color:#93c5fd;font-size:1rem;margin-bottom:8px;'>第四章 圖表與趨勢線</h3>
    <ul style='color:#e2e8f0;font-size:0.85rem;padding-left:16px;margin:0;'>
      <li>依目的選圖：比較、分布、變化、比例、關係</li>
      <li>趨勢線方程式與 R²</li>
      <li>相關不等於因果</li>
    </ul>
  </div>
</div>
<div style='background:rgba(255,255,255,0.1);padding:12px;border-radius:8px;margin-top:15px;text-align:center;'>
  <p style='color:#bfdbfe;font-size:0.95rem;margin:0;'>最後一週：<strong style='color:#fff;'>Google 試算表儀表板與期末總結</strong> ── 把圖表組成一頁儀表板，並開始期末報告</p>
</div>""", bg='navy'),
]
