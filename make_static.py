#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 Flask 課程網站匯出成靜態網頁（docs/），供 GitHub Pages 使用。
用法：python make_static.py   （之後內容有更新，重跑一次再 push 即可）"""
import json, os, re, shutil
from app import app, load_ch, apply_enhancements, N_CHAPTERS

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'docs')

def main():
    shutil.rmtree(OUT, ignore_errors=True)
    os.makedirs(os.path.join(OUT, 'data'), exist_ok=True)
    client = app.test_client()

    # 首頁
    html = client.get('/').get_data(as_text=True)
    html = re.sub(r'href="/ch/\$\{ch\.n\}"', 'href="ch${ch.n}.html"', html)
    html = html.replace('href="/rubric"', 'href="rubric.html"')
    open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8').write(html)

    # 評量規準
    html = client.get('/rubric').get_data(as_text=True)
    html = html.replace('href="/"', 'href="index.html"')
    open(os.path.join(OUT, 'rubric.html'), 'w', encoding='utf-8').write(html)

    # 各章頁面 + 資料
    for n in range(1, N_CHAPTERS + 1):
        html = client.get(f'/ch/{n}').get_data(as_text=True)
        html = html.replace(f"fetch('/api/slides/{n}')", f"fetch('data/slides-{n}.json')")
        html = html.replace(f"fetch('/api/quizzes/{n}')", f"fetch('data/quizzes-{n}.json')")
        assert '/api/' not in html, f'ch{n} 仍有未轉換的 /api/ 路徑'
        open(os.path.join(OUT, f'ch{n}.html'), 'w', encoding='utf-8').write(html)
        ch = load_ch(n)
        json.dump(apply_enhancements(ch.SLIDES, n),
                  open(os.path.join(OUT, f'data/slides-{n}.json'), 'w', encoding='utf-8'),
                  ensure_ascii=False)
        json.dump(ch.QUIZZES,
                  open(os.path.join(OUT, f'data/quizzes-{n}.json'), 'w', encoding='utf-8'),
                  ensure_ascii=False)

    open(os.path.join(OUT, '.nojekyll'), 'w').close()
    print(f'✅ 靜態網站已輸出到 docs/（{len(os.listdir(OUT))} 個項目）')

if __name__ == '__main__':
    main()
