#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Landmark 資產守護校驗腳本。

用途：貝加爾鐵路（baikal-rail）全站唯一 11 張非斌哥 OPPO 手機拍攝的
地標示意圖（Landmark 資產，斌哥本人或委託尋找的景點鋪陳照片），
清單與基準雜湊記錄在 scripts/landmark_manifest.json。

任何任務（人類或 AI）在修改、搬移、刪除 photos/baikal-rail/ 底下檔案，
或修改 vol1/baikal.html 之前／之後，都必須執行本腳本：

    python3 scripts/verify_landmarks.py

若回報 FAIL，代表這 11 張 Landmark 圖檔或它們在網頁上的卡片被動過了，
必須立刻停止手上的任務、回報使用者，取得明確同意後才能繼續 ——
不要自行「修好」或略過這個錯誤。

這是校驗／示警工具，不是作業系統層級的強制鎖（作業系統層級的鎖是
另外對這 11 個檔案做 chmod 444，兩者搭配使用）。
"""
import hashlib
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST_PATH = os.path.join(ROOT, "scripts", "landmark_manifest.json")
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
            failures.append(f"[消失] {rel_path} — 檔案不存在，已知 Landmark 檔案不應被刪除。")
            continue

        actual_sha = sha256_of(abs_path)
        if actual_sha != entry["sha256"]:
            failures.append(
                f"[內容變更] {rel_path} — SHA-256 對不上基準值\n"
                f"    基準: {entry['sha256']}\n"
                f"    目前: {actual_sha}\n"
                f"    檔案被覆寫、重新編碼或替換過，Landmark 原圖不可改。"
            )
            continue

        src_needle = f"../photos/baikal-rail/{rel_path.split('photos/baikal-rail/')[-1]}"
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

    print(f"已核對 {checked} 張 Landmark 資產（清單見 scripts/landmark_manifest.json）")

    if failures:
        print(f"\n❌ FAIL — 發現 {len(failures)} 項異常：\n")
        for f_ in failures:
            print(f"  {f_}\n")
        print("請立刻停止手上的任務並回報使用者，取得明確同意後才能繼續，不要自行修復或略過。")
        sys.exit(1)
    else:
        print("✅ PASS — 全部 Landmark 資產與基準快照一致，沒有被搬移、刪除或改動。")
        sys.exit(0)


if __name__ == "__main__":
    main()
