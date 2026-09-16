#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
景點導覽（destination_preview，舊稱 Landmark）資產守護校驗腳本。

用途：貝加爾鐵路（baikal-rail）全站確認查無斌哥 Google Drive 來源、
屬於行前蒐集的景點導覽示意圖（非斌哥本人 OPPO 手機實拍），
清單與基準雜湊記錄在 scripts/destination_preview_manifest.json。

任何任務（人類或 AI）在修改、搬移、刪除 photos/baikal-rail/ 或
photos/destination-preview/ 底下檔案，或修改 vol1/baikal.html 之前／
之後，都必須執行本腳本：

    python3 scripts/verify_destination_preview.py

若回報 FAIL，代表清單裡的景點導覽圖檔或它們在網頁上的卡片被動過了，
必須立刻停止手上的任務、回報使用者，取得明確同意後才能繼續 ——
不要自行「修好」或略過這個錯誤。

這是校驗／示警工具，不是作業系統層級的強制鎖（作業系統層級的鎖是
另外對這些檔案做 chmod 444、對資料夾做 chmod 555，兩者搭配使用）。
"""
import hashlib
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST_PATH = os.path.join(ROOT, "scripts", "destination_preview_manifest.json")
HTML_PATH = os.path.join(ROOT, "vol1", "baikal.html")


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def main():
    with open(MANIFEST_PATH, encoding="utf-8") as f:
        manifest = json.load(f)

    with open(HTML_PATH, encoding="utf-8") as f:
        html = f.read()

    failures = []
    checked = 0

    for entry in manifest["files"]:
        rel_path = entry["path"]
        abs_path = os.path.join(ROOT, rel_path)
        checked += 1

        if not os.path.isfile(abs_path):
            failures.append(f"[消失] {rel_path} — 檔案不存在，已知景點導覽檔案不應被刪除。")
            continue

        actual_sha = sha256_of(abs_path)
        if actual_sha != entry["sha256"]:
            failures.append(
                f"[內容變更] {rel_path} — SHA-256 對不上基準值\n"
                f"    基準: {entry['sha256']}\n"
                f"    目前: {actual_sha}\n"
                f"    檔案被覆寫、重新編碼或替換過，景點導覽原圖不可改。"
            )
            continue

        # rel_path 本身就是從 lvhun/ 起算的完整相對路徑（例如
        # "photos/baikal-rail/day01/xxx.jpg" 或搬遷後的
        # "photos/destination-preview/baikal-rail/day01/xxx.jpg"），
        # HTML 裡的 img src 都是從 vol1/ 往上一層看，所以直接補上 "../" 前綴即可，
        # 不寫死任何資料夾名稱，資料夾改名／搬遷後不需要再改這支腳本。
        src_needle = f"../{rel_path}"
        currently_referenced = src_needle in html
        expected = entry["expect_referenced_in_html"]
        if currently_referenced != expected:
            state = "被引用" if currently_referenced else "未被引用"
            expected_state = "被引用" if expected else "未被引用"
            note = f"（{entry['note']}）" if entry.get("note") else ""
            failures.append(
                f"[引用狀態改變] {rel_path} — 目前在 vol1/baikal.html 裡{state}，"
                f"跟基準快照記錄的「應該{expected_state}」不一致。{note}"
            )

    print(f"已核對 {checked} 張景點導覽資產（清單見 scripts/destination_preview_manifest.json）")

    if failures:
        print(f"\n❌ FAIL — 發現 {len(failures)} 項異常：\n")
        for f_ in failures:
            print(f"  {f_}\n")
        print("請立刻停止手上的任務並回報使用者，取得明確同意後才能繼續，不要自行修復或略過。")
        sys.exit(1)
    else:
        print("✅ PASS — 全部景點導覽資產與基準快照一致，沒有被搬移、刪除或改動。")
        sys.exit(0)


if __name__ == "__main__":
    main()
