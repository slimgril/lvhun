# TASK — 全站圖片存在性稽核（交給 Codex CLI 執行）

## 你的角色與工作區

你（Codex CLI）跟 Claude Code 共用同一個工作區：

```
/Users/mac/Documents/Projects/旅遊/
├── lvhun/         ← 《旅魂》電子書網站（Render 部署，git push 後自動部署）
└── travel-site/   ← 旅遊網站（Cloudflare Pages 部署）
```

分工協作模式（重要，請遵守）：
1. Claude Code 派工（本檔案）
2. **Codex 施工** ← 你現在的角色
3. Claude Code 驗收，確認沒問題才會 commit / push / 部署

**請不要自行執行 `git commit`、`git push` 或任何部署指令。** 你只需要完成下面的稽核任務，並把結果寫回本檔案最下方「完成摘要」區塊。不要修改任何現有的 `.html` 或圖片檔案——這次任務只做盤點與回報，不要順手修正。

## 為什麼先做這個

準備要幫第二卷《漸見》的 Hero 換上真實封面照片，但在動那個之前，要先確認現有素材（照片）本身沒有缺失——如果原始素材有殘缺，後面做的東西都是建立在錯誤基礎上，所以圖片稽核是優先於封面/Hero 工作的第一步。

## 任務目標

掃描 `lvhun/` 與 `travel-site/` 兩個專案裡，所有 `.html` 檔案中引用的圖片（`<img src="...">`、CSS `background-image: url(...)`、`srcset` 都要含括），逐一檢查對應的圖片檔案是否真的存在於檔案系統上。找出：

1. **Broken reference（優先）**：HTML 裡引用了、但實際檔案不存在的路徑
2. **格式不符**：副檔名跟實際檔案格式對不上的情形（例如某張 `.jpg` 其實是 PNG 格式）——`lvhun/photos/hero/vol1-cover.jpg` 這一個已知是刻意保留的特例（原本美工交付檔就是這樣），**不用重複回報這一個**，但如果掃描到其他類似情況要列出來
3. **孤兒檔案**（次要，非必要）：圖片檔案存在但完全沒有任何 HTML 引用到，時間許可再做，不強制

## 範圍

- `/Users/mac/Documents/Projects/旅遊/lvhun/` 底下所有 `.html`
- `/Users/mac/Documents/Projects/旅遊/travel-site/` 底下所有 `.html`，包含 `dist/` 跟 `dist-surge-upload/`（這兩個是 build 產物，如果掃到問題請在報告裡註明是「原始碼」還是「build 產物」，因為 `dist-surge-upload/` 才是實際部署來源，`dist/` 只是本地暫存 build）
- 不用檢查 `node_modules`、`.git` 內部檔案

## 已知問題（請驗證現況並列入報告，不用重新發現）

- `lvhun/photos/baikal-rail/day03/IMG20260805103339.jpg`，alt 文字是「講解遊牧遷移的表演」——先前發現這張圖疑似破損或遺失，請確認目前實際狀況
- `lvhun` 與 `travel-site` 兩邊的貝加爾鐵路（baikal-rail）頁面內容有大約 2 筆卡片／圖說對不上，請具體列出差異在哪裡（哪一筆、兩邊分別寫了什麼）

## 建議做法

可以寫一個一次性的 Python 或 Node 腳本做掃描（掃完要不要留著或刪掉你自己決定，只要不動到專案內其他既有檔案即可）。

## 回報格式（請直接寫在下面「完成摘要」區塊，不要留白）

- 用清單列出每一筆問題：`引用來源 html 路徑` → `對應圖片路徑` → `問題類型（遺失／格式不符／孤兒檔案）`
- 已知問題的兩項請明確回覆現況（確認屬實／已經不是問題了／有新發現）
- 結尾用一兩句話說明你用什麼方法掃描的（腳本邏輯簡述即可）
- 如果整站都沒發現異常，也要明確寫「掃描完成，未發現異常」，不要什麼都不寫

**另外請務必再寫一份「工作摘要與總結報告」**（見下方獨立區塊）——這份是要直接轉交給專案負責人（斌哥）看的，跟上面給 Claude Code 驗收用的技術清單分開：
- 用白話文說明這次做了什麼、範圍多大（掃了幾個檔案、幾張圖片）
- 結論：整體素材完整度如何（例如「99% 正常，僅 X 處需要處理」）
- 對自己找到的結果有多少把握（掃描方法能不能涵蓋所有引用方式，有沒有遺漏風險）
- 如果有需要人工決定的事項（例如某張圖到底要補件還是刪除引用），明確列出來請斌哥／Claude Code 決定，不要自己直接下結論

---

## 完成摘要（由 Codex 填寫，技術細節，給 Claude Code 驗收用）

稽核日期：2026-09-15。已完成；僅更新本檔兩個 Codex 回報區塊，未修改既有 HTML、CSS、JavaScript、圖片或建置產物，未 commit／push／部署。下列路徑皆相對於 `/Users/mac/Documents/Projects/旅遊/`，冒號後為來源行號。

### 1. 範圍與結論

共掃描 **44 個 HTML**。必要的 HTML／CSS 本機圖片引用為 **3,556 處**；另補查 4 份山西播放器 `data.js`、每份 239 筆圖片，共 **956 處**。合計 **4,512 處本機圖片引用**，對應 **3,805 個不同目標路徑**，其中 **3,618 個存在、187 個不存在**；不存在的路徑共被引用 **194 次**。

| 區域與性質 | HTML 數 | 本機引用次數（含播放器） | 已存在的不同圖片路徑 | 失效引用次數 | 庫存圖片檔數 |
|---|---:|---:|---:|---:|---:|
| `lvhun/`（原始碼） | 8 | 745 | 738 | 0 | 754 |
| `travel-site/`（原始碼／參考／預生成頁，排除下列 build） | 12 | 575 | 381 | 194 | 1,315 |
| `travel-site/dist/`（本地暫存 build） | 8 | 1,064 | 833 | 0 | 935 |
| `travel-site/dist-surge-upload/`（實際部署來源 build） | 8 | 1,064 | 833 | 0 | 939 |
| `travel-site/dist-prototype/`（額外納入的原型 build） | 8 | 1,064 | 833 | 0 | 935 |
| **合計** | **44** | **4,512** | **3,618** | **194** | **4,878** |

**《旅魂》及三份 build 的本機圖片引用全部存在，沒有發現 broken reference。** 194 處失效引用集中在兩個原始碼區／參考頁，並非 194 張部署圖片遺失。延伸檢查全部 **4,878 個圖片檔案路徑**（含未引用素材及跨專案／build 副本），主影像皆可解碼；另有 1 項真正的副檔名不符（5 個副本）與 2 項未直接引用素材的附加縮圖資訊異常（8 個副本），詳列如下。

### 2. Broken reference 完整清單

#### 2.1 原始碼區預生成頁：`travel-site/content/bldh-trio/estonia-journal.html`

共 **52 處／52 個目標**。此檔使用 `photos/...`，直接以目前所在目錄解析會指向不存在的 `content/bldh-trio/photos/...`；`scripts/build.py` 會將它複製到 build 根目錄，而三份 build 的 `estonia-journal.html` 對應的 52 張照片均存在。這是**原始碼位置直接預覽時的失效引用**，不是部署成品缺圖，也不是照片素材遺失。

- `travel-site/content/bldh-trio/estonia-journal.html:117` → `travel-site/content/bldh-trio/photos/bldh-trio/day07/ahhaa-rocket-bingge.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:132` → `travel-site/content/bldh-trio/photos/bldh-trio/day07/tartu-leaning-house.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:147` → `travel-site/content/bldh-trio/photos/bldh-trio/day07/kissing-students-fountain-bingge.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:162` → `travel-site/content/bldh-trio/photos/bldh-trio/day07/tartu-university.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:177` → `travel-site/content/bldh-trio/photos/bldh-trio/day07/tartu-supreme-court-seal.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:192` → `travel-site/content/bldh-trio/photos/bldh-trio/day07/tartu-cathedral-ruins-bingge.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:207` → `travel-site/content/bldh-trio/photos/bldh-trio/day07/tartu-cathedral-tower-bingge.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:222` → `travel-site/content/bldh-trio/photos/bldh-trio/day07/tartu-town-hall-bingge.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:237` → `travel-site/content/bldh-trio/photos/bldh-trio/day07/viljandi-lake-diving-board.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:252` → `travel-site/content/bldh-trio/photos/bldh-trio/day07/viljandi-man-and-dog-sculpture.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:267` → `travel-site/content/bldh-trio/photos/bldh-trio/day07/viljandi-water-tower.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:282` → `travel-site/content/bldh-trio/photos/bldh-trio/day07/viljandi-cat-sculpture-bingge.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:297` → `travel-site/content/bldh-trio/photos/bldh-trio/day08/parnu-locomotive-no5.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:312` → `travel-site/content/bldh-trio/photos/bldh-trio/day08/parnu-street-tower.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:327` → `travel-site/content/bldh-trio/photos/bldh-trio/day08/parnu-cafe-grand.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:342` → `travel-site/content/bldh-trio/photos/bldh-trio/day08/parnu-orthodox-tower-bingge.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:357` → `travel-site/content/bldh-trio/photos/bldh-trio/day08/parnu-st-catherine-church-bingge.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:372` → `travel-site/content/bldh-trio/photos/bldh-trio/day08/parnu-kihnu-jonn-statue.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:387` → `travel-site/content/bldh-trio/photos/bldh-trio/day08/parnu-hands-sculpture-bingge.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:402` → `travel-site/content/bldh-trio/photos/bldh-trio/day08/parnu-yacht-jaalind.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:417` → `travel-site/content/bldh-trio/photos/bldh-trio/day08/estonia-duck-lunch.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:432` → `travel-site/content/bldh-trio/photos/bldh-trio/day08/tallinn-moon-restoran.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:447` → `travel-site/content/bldh-trio/photos/bldh-trio/day08/michelin-dinner.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:462` → `travel-site/content/bldh-trio/photos/bldh-trio/day08/tallinn-movie-wolf-bingge.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:477` → `travel-site/content/bldh-trio/photos/bldh-trio/day08/tallinn-delice-fruit-cart.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:492` → `travel-site/content/bldh-trio/photos/bldh-trio/day09/tallinn-viru-gate-bingge.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:507` → `travel-site/content/bldh-trio/photos/bldh-trio/day09/tallinn-town-hall-dragon-spout.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:522` → `travel-site/content/bldh-trio/photos/bldh-trio/day09/tallinn-holy-ghost-clock.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:537` → `travel-site/content/bldh-trio/photos/bldh-trio/day09/tallinn-art-nouveau-gable.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:552` → `travel-site/content/bldh-trio/photos/bldh-trio/day09/tallinn-blackheads-door.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:567` → `travel-site/content/bldh-trio/photos/bldh-trio/day09/tallinn-three-sisters-bingge.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:582` → `travel-site/content/bldh-trio/photos/bldh-trio/day09/tallinn-town-hall-square-bingge.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:597` → `travel-site/content/bldh-trio/photos/bldh-trio/day09/tallinn-maiasmokk-cafe-bingge.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:612` → `travel-site/content/bldh-trio/photos/bldh-trio/day09/tallinn-town-hall-pharmacy-bingge.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:627` → `travel-site/content/bldh-trio/photos/bldh-trio/day09/tallinn-victory-column.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:642` → `travel-site/content/bldh-trio/photos/bldh-trio/day09/tallinn-kiek-in-de-kok.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:657` → `travel-site/content/bldh-trio/photos/bldh-trio/day09/tallinn-city-wall-towers.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:672` → `travel-site/content/bldh-trio/photos/bldh-trio/day09/tallinn-alexander-nevsky-bingge.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:687` → `travel-site/content/bldh-trio/photos/bldh-trio/day09/tallinn-cow-bench-bingge.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:702` → `travel-site/content/bldh-trio/photos/bldh-trio/day09/tallinn-danish-king-garden-monks.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:717` → `travel-site/content/bldh-trio/photos/bldh-trio/day09/tallinn-kaarli-church.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:732` → `travel-site/content/bldh-trio/photos/bldh-trio/day09/tallinn-olde-hansa-exterior.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:747` → `travel-site/content/bldh-trio/photos/bldh-trio/day09/tallinn-olde-hansa-interior-bingge.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:762` → `travel-site/content/bldh-trio/photos/bldh-trio/day09/tallinn-olde-hansa-meat-feast.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:777` → `travel-site/content/bldh-trio/photos/bldh-trio/day10/tallinn-open-air-thatch-roof-bingge.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:792` → `travel-site/content/bldh-trio/photos/bldh-trio/day10/tallinn-open-air-farmhouse-bingge.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:807` → `travel-site/content/bldh-trio/photos/bldh-trio/day10/tallinn-open-air-well-sweep.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:822` → `travel-site/content/bldh-trio/photos/bldh-trio/day10/tallinn-open-air-cat-bingge.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:837` → `travel-site/content/bldh-trio/photos/bldh-trio/day10/tallinn-baltic-sea-bingge.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:852` → `travel-site/content/bldh-trio/photos/bldh-trio/day10/estonia-chicken-skewer-lunch.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:867` → `travel-site/content/bldh-trio/photos/bldh-trio/day10/tallinn-balti-jaama-turg-bingge.jpg` → **遺失（原始碼位置的相對路徑）**。
- `travel-site/content/bldh-trio/estonia-journal.html:882` → `travel-site/content/bldh-trio/photos/bldh-trio/day10/tallinn-fish-market-berries.jpg` → **遺失（原始碼位置的相對路徑）**。

#### 2.2 舊參考頁：`travel-site/reference/shanxi-golden.html`

共 **142 處引用／135 個目標**。舊頁的裸檔名及 `丫斌哥山西遊記/photos/...` 都依目前 `reference/` 所在位置解析，因此找不到。除 `43_平遙炒碗托.jpg` 外，其餘引用的同名檔可在 `travel-site/photos/` 下找到；這僅證明同名素材存在，不代表可不經確認直接替換。`43_平遙炒碗托.jpg` 在兩個專案均無同名檔，而 `ASSET_CHECKLIST.md:54` 記錄現行 day06 已移除該卡片；現行 build 的山西頁沒有這筆失效引用。

- `travel-site/reference/shanxi-golden.html:377` → `travel-site/reference/yabin-wuxi.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:399` → `travel-site/reference/yabin-dalat.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:653` → `travel-site/reference/img-pusanding.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:660` → `travel-site/reference/img-tayuan.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:667` → `travel-site/reference/img-xiantong.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:674` → `travel-site/reference/img-luohou.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:696` → `travel-site/reference/丫斌哥山西遊記/photos/02_太原晨景.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:703` → `travel-site/reference/丫斌哥山西遊記/photos/03_太原街景.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:710` → `travel-site/reference/丫斌哥山西遊記/photos/04_五台山入口.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:718` → `travel-site/reference/丫斌哥山西遊記/photos/05_俯瞰台懷鎮.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:725` → `travel-site/reference/丫斌哥山西遊記/photos/06_菩薩頂匾額.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:732` → `travel-site/reference/丫斌哥山西遊記/photos/07_文殊足印碑.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:740` → `travel-site/reference/丫斌哥山西遊記/photos/08_顯通寺無量殿.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:747` → `travel-site/reference/丫斌哥山西遊記/photos/09_顯通寺銅殿.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:754` → `travel-site/reference/丫斌哥山西遊記/photos/10_顯通寺山門.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:779` → `travel-site/reference/img-hengshan.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:786` → `travel-site/reference/img-xuankong.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:808` → `travel-site/reference/丫斌哥山西遊記/photos/12_北嶽恒山牌樓.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:815` → `travel-site/reference/丫斌哥山西遊記/photos/13_恒山登山道.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:822` → `travel-site/reference/丫斌哥山西遊記/photos/14_恒山觀景台.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:829` → `travel-site/reference/丫斌哥山西遊記/photos/15_金龍口.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:836` → `travel-site/reference/丫斌哥山西遊記/photos/16_虎風口.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:843` → `travel-site/reference/丫斌哥山西遊記/photos/17_恒山崖刻.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:850` → `travel-site/reference/丫斌哥山西遊記/photos/18_懸空寺遠景.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:857` → `travel-site/reference/丫斌哥山西遊記/photos/19_懸空寺特寫.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:864` → `travel-site/reference/丫斌哥山西遊記/photos/20_懸空寺碑.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:871` → `travel-site/reference/丫斌哥山西遊記/photos/21_懸空寺牌匾.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:878` → `travel-site/reference/丫斌哥山西遊記/photos/22_懸空寺迴廊.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:886` → `travel-site/reference/丫斌哥山西遊記/photos/23_霞客遺蹤.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:911` → `travel-site/reference/img-yungang.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:918` → `travel-site/reference/img-yingxian.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:940` → `travel-site/reference/丫斌哥山西遊記/photos/24_雲岡石窟外觀.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:947` → `travel-site/reference/丫斌哥山西遊記/photos/25_雲岡寺飛簷.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:954` → `travel-site/reference/丫斌哥山西遊記/photos/26_雲岡彩繪菩薩.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:961` → `travel-site/reference/丫斌哥山西遊記/photos/27_雲岡龕像佛坐像.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:968` → `travel-site/reference/丫斌哥山西遊記/photos/28_雲岡立佛雙菩薩.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:975` → `travel-site/reference/丫斌哥山西遊記/photos/30_雲岡大佛祈福.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:982` → `travel-site/reference/丫斌哥山西遊記/photos/29_雲岡大佛合影.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:989` → `travel-site/reference/丫斌哥山西遊記/photos/31_應縣木塔內佛像.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:996` → `travel-site/reference/丫斌哥山西遊記/photos/32_應縣木塔飛簷.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1003` → `travel-site/reference/丫斌哥山西遊記/photos/33_應縣木塔全景.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1010` → `travel-site/reference/丫斌哥山西遊記/photos/34_應縣木塔合影.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1035` → `travel-site/reference/丫斌哥山西遊記/photos/38_雁門關城樓匾額.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1042` → `travel-site/reference/丫斌哥山西遊記/photos/40_雁門關內長城敵樓遠眺.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1064` → `travel-site/reference/丫斌哥山西遊記/photos/35_雁門關天險門仰望.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1072` → `travel-site/reference/丫斌哥山西遊記/photos/36_雁門關箭窗遠眺.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1079` → `travel-site/reference/丫斌哥山西遊記/photos/37_雁門關內城紅旗飛簷.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1086` → `travel-site/reference/丫斌哥山西遊記/photos/38_雁門關城樓匾額.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1093` → `travel-site/reference/丫斌哥山西遊記/photos/39_長城雁門關段石碑.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1100` → `travel-site/reference/丫斌哥山西遊記/photos/40_雁門關內長城敵樓遠眺.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1107` → `travel-site/reference/丫斌哥山西遊記/photos/41_太原暮色空拍.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1132` → `travel-site/reference/丫斌哥山西遊記/photos/52_城牆俯瞰古城.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1139` → `travel-site/reference/丫斌哥山西遊記/photos/48_日昇昌票號.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1146` → `travel-site/reference/丫斌哥山西遊記/photos/42_平遙觀風樓.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1168` → `travel-site/reference/丫斌哥山西遊記/photos/42_平遙觀風樓.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1175` → `travel-site/reference/丫斌哥山西遊記/photos/43_平遙炒碗托.jpg` → **遺失（原始碼／舊參考頁）**；兩個專案均無同名檔；僅舊參考頁仍引用。
- `travel-site/reference/shanxi-golden.html:1182` → `travel-site/reference/丫斌哥山西遊記/photos/44_縣衙親民堂.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1190` → `travel-site/reference/丫斌哥山西遊記/photos/45_縣衙明鏡高懸.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1197` → `travel-site/reference/丫斌哥山西遊記/photos/46_縣衙木枷.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1204` → `travel-site/reference/丫斌哥山西遊記/photos/47_山西老陳醋.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1211` → `travel-site/reference/丫斌哥山西遊記/photos/48_日昇昌票號.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1219` → `travel-site/reference/丫斌哥山西遊記/photos/49_同興公鏢局.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1226` → `travel-site/reference/丫斌哥山西遊記/photos/50_丫斌哥鏢車合影.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1233` → `travel-site/reference/丫斌哥山西遊記/photos/51_市樓古炮合影.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1240` → `travel-site/reference/丫斌哥山西遊記/photos/52_城牆俯瞰古城.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1247` → `travel-site/reference/丫斌哥山西遊記/photos/53_市樓夜景.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1285` → `travel-site/reference/丫斌哥山西遊記/photos/54_文廟學宮牌匾.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1292` → `travel-site/reference/丫斌哥山西遊記/photos/55_文廟萬仞牆.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1299` → `travel-site/reference/丫斌哥山西遊記/photos/56_大成殿合影.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1306` → `travel-site/reference/丫斌哥山西遊記/photos/57_大成殿孔子像.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1313` → `travel-site/reference/丫斌哥山西遊記/photos/58_文廟鰲陽石.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1320` → `travel-site/reference/丫斌哥山西遊記/photos/59_城隍廟廊道.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1327` → `travel-site/reference/丫斌哥山西遊記/photos/60_城隍廟壁畫.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1334` → `travel-site/reference/丫斌哥山西遊記/photos/61_馬家大院城樓.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1341` → `travel-site/reference/丫斌哥山西遊記/photos/63_馬家大院門廊.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1348` → `travel-site/reference/丫斌哥山西遊記/photos/62_馬家大院合影.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1355` → `travel-site/reference/丫斌哥山西遊記/photos/67_平遙博物館夜景.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1362` → `travel-site/reference/丫斌哥山西遊記/photos/64_又見平遙劇場.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1369` → `travel-site/reference/丫斌哥山西遊記/photos/65_又見平遙攀牆.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1376` → `travel-site/reference/丫斌哥山西遊記/photos/66_平遙市樓夜人潮.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1401` → `travel-site/reference/img-xiaoxitian.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1408` → `travel-site/reference/img-hukou.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1431` → `travel-site/reference/丫斌哥山西遊記/photos/68_小西天入口合影.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1438` → `travel-site/reference/丫斌哥山西遊記/photos/69_小西天别有天.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1445` → `travel-site/reference/丫斌哥山西遊記/photos/70_小西天懸塑群佛.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1452` → `travel-site/reference/丫斌哥山西遊記/photos/71_小西天主佛龕.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1459` → `travel-site/reference/丫斌哥山西遊記/photos/72_小西天護法神將.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1466` → `travel-site/reference/丫斌哥山西遊記/photos/73_小西天懸塑全景.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1473` → `travel-site/reference/丫斌哥山西遊記/photos/74_小西天佛字壁.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1480` → `travel-site/reference/丫斌哥山西遊記/photos/75_壺口瀑布合影.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1487` → `travel-site/reference/丫斌哥山西遊記/photos/76_壺口瀑布全景.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1494` → `travel-site/reference/丫斌哥山西遊記/photos/77_壺口瀑布凝視.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1501` → `travel-site/reference/丫斌哥山西遊記/photos/78_壺口河灘小橋.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1508` → `travel-site/reference/丫斌哥山西遊記/photos/79_吉縣酒店客房.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1515` → `travel-site/reference/丫斌哥山西遊記/photos/80_隰縣玉露香梨.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1540` → `travel-site/reference/img-linfen.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1547` → `travel-site/reference/img-huamen.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1569` → `travel-site/reference/丫斌哥山西遊記/photos/81_汾城古塔合影.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1576` → `travel-site/reference/丫斌哥山西遊記/photos/82_汾城橋星門.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1583` → `travel-site/reference/丫斌哥山西遊記/photos/83_汾城下馬碑.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1590` → `travel-site/reference/丫斌哥山西遊記/photos/84_汾城古柏殿堂.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1597` → `travel-site/reference/丫斌哥山西遊記/photos/85_汾城廟前合影.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1604` → `travel-site/reference/丫斌哥山西遊記/photos/86_汾城鑒客坊.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1611` → `travel-site/reference/丫斌哥山西遊記/photos/87_汾城縣衙大門.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1618` → `travel-site/reference/丫斌哥山西遊記/photos/88_華門正面.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1625` → `travel-site/reference/丫斌哥山西遊記/photos/89_華門合影.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1632` → `travel-site/reference/丫斌哥山西遊記/photos/90_華門門洞.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1657` → `travel-site/reference/img-taihang.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1678` → `travel-site/reference/丫斌哥山西遊記/photos/91_八泉峽入口.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1685` → `travel-site/reference/丫斌哥山西遊記/photos/92_峽谷湖景棧道.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1692` → `travel-site/reference/丫斌哥山西遊記/photos/93_峽谷遊船.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1699` → `travel-site/reference/丫斌哥山西遊記/photos/94_天然拱門觀景台.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1706` → `travel-site/reference/丫斌哥山西遊記/photos/95_溪流木棧道.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1713` → `travel-site/reference/丫斌哥山西遊記/photos/96_峽谷溪流.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1720` → `travel-site/reference/丫斌哥山西遊記/photos/97_瀑布溪流特寫.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1727` → `travel-site/reference/丫斌哥山西遊記/photos/98_峽谷瀑布.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1734` → `travel-site/reference/丫斌哥山西遊記/photos/99_纜車雲霧.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1741` → `travel-site/reference/丫斌哥山西遊記/photos/100_峽谷俯瞰.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1748` → `travel-site/reference/丫斌哥山西遊記/photos/101_雲霧山峰.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1755` → `travel-site/reference/丫斌哥山西遊記/photos/102_峭壁千仞.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1762` → `travel-site/reference/丫斌哥山西遊記/photos/103_懸崖電梯建築.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1769` → `travel-site/reference/丫斌哥山西遊記/photos/104_高空俯瞰全景.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1776` → `travel-site/reference/丫斌哥山西遊記/photos/105_觀景台眺望.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1783` → `travel-site/reference/丫斌哥山西遊記/photos/106_世界紀錄證書.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1790` → `travel-site/reference/丫斌哥山西遊記/photos/107_電梯排隊.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1797` → `travel-site/reference/丫斌哥山西遊記/photos/108_懸崖電梯仰拍.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1822` → `travel-site/reference/img-taihang.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1836` → `travel-site/reference/丫斌哥山西遊記/photos/100_紅豆峽石碑人像.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1840` → `travel-site/reference/丫斌哥山西遊記/photos/101_紅豆峽入口石碑.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1844` → `travel-site/reference/丫斌哥山西遊記/photos/102_紅豆峽奇峰.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1848` → `travel-site/reference/丫斌哥山西遊記/photos/103_紅豆峽水潭坐姿.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1852` → `travel-site/reference/丫斌哥山西遊記/photos/104_紅豆峽峽谷人像.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1856` → `travel-site/reference/丫斌哥山西遊記/photos/105_紅豆峽溶洞.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1860` → `travel-site/reference/丫斌哥山西遊記/photos/106_紅豆峽撐竹筏.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1864` → `travel-site/reference/丫斌哥山西遊記/photos/107_紅豆峽倒影石碑.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1868` → `travel-site/reference/丫斌哥山西遊記/photos/108_峽谷木棧道.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1895` → `travel-site/reference/img-taihang.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1919` → `travel-site/reference/img-jinci.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1926` → `travel-site/reference/img-jinci2.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1933` → `travel-site/reference/img-jinci3.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1964` → `travel-site/reference/img-museum.jpg` → **遺失（原始碼／舊參考頁）**。
- `travel-site/reference/shanxi-golden.html:1971` → `travel-site/reference/img-taiyuan.jpg` → **遺失（原始碼／舊參考頁）**。

### 3. 格式不符與解碼結果

#### 3.1 確認的格式不符：立陶宛紀念品拼貼圖

`lithuania-souvenirs-collage.png` 五份副本的內容完全一致（SHA-256 相同），實際均為 **JPEG、900 × 755、185,886 bytes**，`file --mime-type` 也回報 `image/jpeg`；主影像可正常解碼。這是 1 項素材格式問題，分布在 5 個檔案路徑。指定排除的既有封面特例未列入問題及以下統計。

- `lvhun/vol1/baltic.html:267` → `lvhun/photos/bldh-trio/day02/lithuania-souvenirs-collage.png` → **格式不符（`.png` 實為 JPEG）**；原始碼。
- `travel-site/dist/trips/bldh-trio.html:267` → `travel-site/dist/photos/bldh-trio/day02/lithuania-souvenirs-collage.png` → **格式不符（`.png` 實為 JPEG）**；build 產物。
- `travel-site/dist-prototype/trips/bldh-trio.html:267` → `travel-site/dist-prototype/photos/bldh-trio/day02/lithuania-souvenirs-collage.png` → **格式不符（`.png` 實為 JPEG）**；build 產物。
- `travel-site/dist-surge-upload/trips/bldh-trio.html:267` → `travel-site/dist-surge-upload/photos/bldh-trio/day02/lithuania-souvenirs-collage.png` → **格式不符（`.png` 實為 JPEG）**；build 產物。
- 無 HTML 直接引用（原始素材；由 `travel-site/scripts/build.py:544` 的拼貼／唱片元件產生引用） → `travel-site/photos/bldh-trio/day02/lithuania-souvenirs-collage.png` → **格式不符（`.png` 實為 JPEG）**。

#### 3.2 JPEG／MPO 複查：避免把格式名稱差異誤當破圖

另有 **20 個 `.jpg`** 被 Pillow 標為 MPO。抽查各內容類型的 `file` 結果均為 `image/jpeg`，且 20 個檔案皆通過 JPEG 主影像解碼，所以不把單純 MPO 標記算成副檔名不符或網站破圖。其中 `taoyuan-airport-terminal-2.jpg` 與 `vilnius-university.jpg` 的附加影格讀取出現 `No data found for frame`，共 8 個副本；MPF 宣告的附加縮圖索引／資料不完整，但主圖可讀，且這 8 份沒有被任何本次 HTML／山西播放器清單直接引用。

- `lvhun/vol1/baikal.html:1062` → `lvhun/photos/baikal-rail/day07/shaman-rock-landmark-downloaded.jpg` → **JPEG/MPO 格式變體；主圖及附加影格正常**（原始碼／素材；不計入 broken reference）。
- `lvhun/vol1/baltic.html:270` → `lvhun/photos/bldh-trio/reference/kgb-museum.jpg` → **JPEG/MPO 格式變體；主圖及附加影格正常**（原始碼／素材；不計入 broken reference）。
- 無 HTML／山西播放器清單直接引用 → `travel-site/dist/photos/baikal-rail/day06/lake-baikal-shaman-rock-downloaded.jpg` → **JPEG/MPO 格式變體；主圖及附加影格正常**（build 產物；不計入 broken reference）。
- `travel-site/dist/trips/baikal-rail.html:985` → `travel-site/dist/photos/baikal-rail/day07/shaman-rock-landmark-downloaded.jpg` → **JPEG/MPO 格式變體；主圖及附加影格正常**（build 產物；不計入 broken reference）。
- `travel-site/dist/trips/bldh-trio.html:270` → `travel-site/dist/photos/bldh-trio/reference/kgb-museum.jpg` → **JPEG/MPO 格式變體；主圖及附加影格正常**（build 產物；不計入 broken reference）。
- 無 HTML／山西播放器清單直接引用 → `travel-site/dist/photos/bldh-trio/reference/taoyuan-airport-terminal-2.jpg` → **附加縮圖資訊異常；主 JPEG 正常**（build 產物；不計入 broken reference）。
- 無 HTML／山西播放器清單直接引用 → `travel-site/dist/photos/bldh-trio/reference/vilnius-university.jpg` → **附加縮圖資訊異常；主 JPEG 正常**（build 產物；不計入 broken reference）。
- 無 HTML／山西播放器清單直接引用 → `travel-site/dist-prototype/photos/baikal-rail/day06/lake-baikal-shaman-rock-downloaded.jpg` → **JPEG/MPO 格式變體；主圖及附加影格正常**（build 產物；不計入 broken reference）。
- `travel-site/dist-prototype/trips/baikal-rail.html:985` → `travel-site/dist-prototype/photos/baikal-rail/day07/shaman-rock-landmark-downloaded.jpg` → **JPEG/MPO 格式變體；主圖及附加影格正常**（build 產物；不計入 broken reference）。
- `travel-site/dist-prototype/trips/bldh-trio.html:270` → `travel-site/dist-prototype/photos/bldh-trio/reference/kgb-museum.jpg` → **JPEG/MPO 格式變體；主圖及附加影格正常**（build 產物；不計入 broken reference）。
- 無 HTML／山西播放器清單直接引用 → `travel-site/dist-prototype/photos/bldh-trio/reference/taoyuan-airport-terminal-2.jpg` → **附加縮圖資訊異常；主 JPEG 正常**（build 產物；不計入 broken reference）。
- 無 HTML／山西播放器清單直接引用 → `travel-site/dist-prototype/photos/bldh-trio/reference/vilnius-university.jpg` → **附加縮圖資訊異常；主 JPEG 正常**（build 產物；不計入 broken reference）。
- `travel-site/dist-surge-upload/trips/bldh-trio.html:270` → `travel-site/dist-surge-upload/photos/bldh-trio/reference/kgb-museum.jpg` → **JPEG/MPO 格式變體；主圖及附加影格正常**（build 產物；不計入 broken reference）。
- 無 HTML／山西播放器清單直接引用 → `travel-site/dist-surge-upload/photos/bldh-trio/reference/taoyuan-airport-terminal-2.jpg` → **附加縮圖資訊異常；主 JPEG 正常**（build 產物；不計入 broken reference）。
- 無 HTML／山西播放器清單直接引用 → `travel-site/dist-surge-upload/photos/bldh-trio/reference/vilnius-university.jpg` → **附加縮圖資訊異常；主 JPEG 正常**（build 產物；不計入 broken reference）。
- 無 HTML／山西播放器清單直接引用 → `travel-site/photos/baikal-rail/day06/lake-baikal-shaman-rock-downloaded.jpg` → **JPEG/MPO 格式變體；主圖及附加影格正常**（原始碼／素材；不計入 broken reference）。
- 無 HTML／山西播放器清單直接引用 → `travel-site/photos/baikal-rail/day07/shaman-rock-landmark-downloaded.jpg` → **JPEG/MPO 格式變體；主圖及附加影格正常**（原始碼／素材；不計入 broken reference）。
- 無 HTML／山西播放器清單直接引用 → `travel-site/photos/bldh-trio/reference/kgb-museum.jpg` → **JPEG/MPO 格式變體；主圖及附加影格正常**（原始碼／素材；不計入 broken reference）。
- 無 HTML／山西播放器清單直接引用 → `travel-site/photos/bldh-trio/reference/taoyuan-airport-terminal-2.jpg` → **附加縮圖資訊異常；主 JPEG 正常**（原始碼／素材；不計入 broken reference）。
- 無 HTML／山西播放器清單直接引用 → `travel-site/photos/bldh-trio/reference/vilnius-university.jpg` → **附加縮圖資訊異常；主 JPEG 正常**（原始碼／素材；不計入 broken reference）。

### 4. 已知問題的現況

#### 4.1 「講解遊牧遷移的表演」：目前不是遺失或破損問題

- `lvhun/vol1/baikal.html:514` → `lvhun/photos/baikal-rail/day03/IMG20260805103339.jpg`：存在，JPEG，**1200 × 900、378,784 bytes**；通過結構驗證與完整像素解碼，亦已目視確認照片有正常草原、犛牛與木輪車隊畫面。
- `travel-site/dist/trips/baikal-rail.html:444`、`travel-site/dist-surge-upload/trips/baikal-rail.html:444`、`travel-site/dist-prototype/trips/baikal-rail.html:444` → 各自 build 下的 `photos/baikal-rail/day03/IMG20260805103339.jpg`：全部存在、可解碼，皆為 JPEG，**4096 × 3072、6,704,897 bytes**。
- `travel-site/photos/baikal-rail/day03/IMG20260805103339.jpg` 原始素材同樣存在且可解碼；原稿引用位於 `travel-site/content/baikal-rail/day03.md:21`。目前本機狀況不能支持「這張照片遺失／破損」的說法；未實測線上伺服器或快取狀態。

#### 4.2 貝加爾卡片／圖說：確認有差異，且超過原先估計的約 2 筆

以圖片相對路徑配對 `.site-card`，比較圖上標籤、卡片標題、說明及整張卡片文字。`lvhun/vol1/baikal.html` 有 **417 張帶圖卡片**，travel-site 三份 build 各 **415 張**；三份 build 的卡片資料逐筆相同。共有 **4 張共用圖片的卡片文字不同**（3 張有實質敘述差異、1 張只有標題措辭差異），另有 **2 張只出現在 lvhun**。以下行號為卡片起始位置；travel-site 欄以實際部署來源 `dist-surge-upload/` 為主。

**差異 1：`day09/siberian-apple.jpg`**

- 《旅魂》：`lvhun/vol1/baikal.html:1430`；圖上標籤／卡片標題均為「西伯利亞蘋果」。說明：「路邊有人賣蘋果，非常小顆，比台灣的小蘋果還小一號。剝開來，蘋果的香味和正常大小的蘋果一模一樣。導遊說這是西伯利亞本地品種，因為生長季節短，所以長不大，但甜度反而很集中。這顆蘋果把整個西伯利亞夏天的時間濃縮在裡面了。」
- 旅遊網站：`travel-site/dist-surge-upload/trips/baikal-rail.html:1346`；圖上標籤／卡片標題均為「西伯利亞蘋果」。說明：「不是路邊小販在賣，是道路兩旁的野生蘋果樹，滿樹都結著這種小蘋果，非常小顆，比台灣的小蘋果還小一號。剝開來，蘋果的香味和正常大小的蘋果一模一樣。導遊說這是西伯利亞本地品種，因為生長季節短，所以長不大，但甜度反而很集中。這顆蘋果把整個西伯利亞夏天的時間濃縮在裡面了。」
- 判讀：兩邊敘述不同，需由斌哥／Claude Code 核對正確版本；本次未判定哪一邊正確。

**差異 2：`day11/cherepanov-locomotive-monument.jpg`**

- 《旅魂》：`lvhun/vol1/baikal.html:1611`；圖上標籤／卡片標題均為「ЛВ型蒸汽貨運機車」。說明：「車身銘牌寫著 1955 年沃羅希洛夫格勒十月革命機車廠出品，車輪旁的說明牌也寫明這是蘇聯 ЛВ 型貨運蒸汽機車，並非傳說中的切爾潘諾夫父子原型車。這輛機車曾行駛於蘇聯全境鐵路網，直到 2001 年才由西西伯利亞鐵路局送進博物館保存。」
- 旅遊網站：`travel-site/dist-surge-upload/trips/baikal-rail.html:1527`；圖上標籤／卡片標題均為「切列帕諾夫蒸汽車紀念碑」。說明：「Cherepanov 父子在 1833 年製造了俄羅斯第一輛蒸汽機車，這座紀念碑向那個開端致敬。看著它，想像十九世紀中期鐵路出現在西伯利亞時，當地人是什麼感受——從馬背到蒸汽機，在一代人之內。」
- 判讀：兩邊敘述不同，需由斌哥／Claude Code 核對正確版本；本次未判定哪一邊正確。

**差異 3：`day13/lunch-waitress.jpg`**

- 《旅魂》：`lvhun/vol1/baikal.html:1988`；圖上標籤／卡片標題均為「歐亞分界合影」。說明：「我在歐洲，我又在亞洲——就這麼簡單的一塊石碑，讓人可以用幾秒鐘橫跨兩個大洲。從台北出發，穿越了整個亞洲，現在踏進歐洲了。」
- 旅遊網站：`travel-site/dist-surge-upload/trips/baikal-rail.html:1904`；圖上標籤／卡片標題均為「臨時代班的葉卡捷琳堡導遊」。說明：「合影的時候才知道，今天這位導遊其實是臨時代班上場的。國語不算流利，講到一半常常要想一下詞，導覽內容也明顯準備得不夠充分，好幾個地標都講得簡略。即使如此，她還是撐完了整段行程，笑容沒垮下來過。旅程裡這種計畫外的小插曲，事後回想起來，反而比順順利利的導覽更有記憶點。」
- 判讀：兩邊敘述不同，需由斌哥／Claude Code 核對正確版本；本次未判定哪一邊正確。

**差異 4：`day13/europe-asia-border-photo.jpg`**

- 《旅魂》：`lvhun/vol1/baikal.html:1962`；圖上標籤／卡片標題均為「午餐熱情招待員」。說明：「午餐餐廳的招待員非常熱情，餐點結束前還主動出來送行，這種溫度在俄羅斯的餐廳裡不常見，讓人印象深刻。」
- 旅遊網站：`travel-site/dist-surge-upload/trips/baikal-rail.html:1878`；圖上標籤／卡片標題均為「午餐餐廳的熱情招待員」。說明：「午餐餐廳的招待員非常熱情，餐點結束前還主動出來送行，這種溫度在俄羅斯的餐廳裡不常見，讓人印象深刻。」
- 判讀：只有「餐廳的」等標題措辭差異，說明相同；不宜當作內容事實衝突。

**差異 5：《旅魂》獨有卡片「成吉思汗飯店」**

- 《旅魂》：`lvhun/vol1/baikal.html:763` → `lvhun/photos/baikal-rail/day04/chinggis-khaan-hotel.jpg`；標籤／標題「成吉思汗飯店」，說明：「折騰一整天之後，踏進房間看到兩張鋪好的床，什麼都不想再說了。飯店整潔，大廳派頭十足，有個像樣的地方躺下已是最好的結尾。」
- 旅遊網站：三份 build 的 `trips/baikal-rail.html` 均沒有此圖片／標題的卡片，對應日的現行 Markdown 也沒有該卡片。這是卡片增減差異；圖片檔本身存在，並非 broken reference。

**差異 6：《旅魂》獨有卡片「斯帕斯卡亞教堂」**

- 《旅魂》：`lvhun/vol1/baikal.html:1068` → `lvhun/photos/baikal-rail/day07/spasskaya-church-downloaded.jpg`；標籤／標題「斯帕斯卡亞教堂」，說明：「1710 年動工，東西伯利亞第一棟石造建築，之前全是木頭。外牆的紅磚在陽光下顯出橘紅，白色線腳把窗框和拱廊勾出來，整棟建築不大，卻有一種壓住地面的穩。伊爾庫次克建城三百多年，這棟建築見過哥薩克的劍、沙皇的聖旨、十二月黨人的流亡、蘇聯的標語，如今還在原地。」
- 旅遊網站：三份 build 的 `trips/baikal-rail.html` 均沒有此圖片／標題的卡片，對應日的現行 Markdown 也沒有該卡片。這是卡片增減差異；圖片檔本身存在，並非 broken reference。

travel-site 上述 4 張共用卡片的文字與現行原稿一致，原稿位置：`content/baikal-rail/day09.md:34`、`day11.md:15`、`day13.md:34`、`day13.md:25`。比對只能確定版本差異，沒有以檔名猜測人物／景物身分，也沒有自行改稿。

### 5. 涵蓋方式、限制與驗證

- 遞迴遍歷兩個完整專案，含隱藏／被 gitignore 忽略的目錄及三份 build，只排除 `node_modules`、`.git`；因此沒有漏掉被忽略的 `dist/`。
- 解析 HTML DOM 中的 `img src`、`img/source srcset`、行內 `style` 與 `<style>` 的 CSS `url(...)`，並補查本機連結 CSS、圖片 lazy 屬性、SVG image、video poster、圖片 metadata／icon 等。現有檔案實際 **沒有 srcset 候選**；本機靜態引用為 `img src` 1,336 處、行內 CSS 2,219 處、style 區塊 CSS 1 處。CSS `background` 簡寫及 `background-image` 都包含在內。
- 相對路徑按 HTML／CSS 所在目錄解析；以 `/` 開頭的路徑按專案或各 build 根目錄解析，支援 HTML entity、URL 百分比解碼及移除 query／fragment。另核對實際路徑大小寫，未發現僅因本機檔案系統大小寫寬鬆而誤判存在的引用。
- 16 個空 `img src` 是 lightbox／播放器待 JavaScript 填入的占位；1 個 SVG data URI、1 個頁內片段引用不視為磁碟路徑。另排除 5 個 Google Fonts CSS URL 及舊參考頁 2 個外部 `og:image`／`twitter:image` URL，未進行遠端 HTTP 驗證。
- 靜態山西播放器清單已補查 956 筆，均存在。`travel-site/player/bingge/index.html` 從 `/api/themes/.../photos` 取得執行時圖片網址，無法由本機 HTML 確認 API 資料或使用者後續上傳的圖片；本次沒有啟動服務、操作 API 或執行網站互動。因此可確認本機靜態引用與已知清單，不宣稱涵蓋所有執行時／線上載入方式。
- 全部 4,878 個庫存圖片檔做格式辨識及主像素解碼，SVG 用 XML 解析確認根元素；對 MPO 額外檢查附加影格，將主圖損壞與附加縮圖異常分開。這不是逐張人工審美或全站圖說正確性驗證。
- 孤兒檔案為選做項目，本次未做全站孤兒定案：原始 Markdown、build 複製流程及播放器也會使用素材，不能僅因「無 HTML 直接引用」就判定可刪。上面只標明格式複查時遇到的未直接引用素材，沒有刪除建議。
- 稽核前後以 SHA-256 核對全部既有 HTML、CSS、JavaScript 及圖片內容，確認未改動；兩個 git 工作區原有狀態維持，僅本 `task.md` 的兩個 Codex 區塊更新。Claude Code 驗收回饋區保留未填。
- 重現資料放在專案外：`/private/tmp/lvhun-image-audit-20260915/audit.py`、`audit.json`、`before.json`（暫存資料，系統清理後可能消失）；本檔已保留完整問題清單，不依賴暫存檔才能驗收。

方法簡述：以 Python／BeautifulSoup 抽取 HTML 與 CSS 圖片網址、展開 srcset 及已知播放器清單，依各檔案所在位置與 build 根目錄逐一核對磁碟；再用 Pillow、JPEG 解碼器及 `file` 複查格式，並以圖片路徑配對貝加爾卡片文字。全程僅讀取素材，結果寫回本任務檔。

---

## 工作摘要與總結報告（由 Codex 填寫，給斌哥看的版本，務必填寫）

稽核日期：2026-09-15。這次已把《旅魂》與旅遊網站的 **44 個網頁檔案**全部納入，連同本地 build、實際部署來源 `dist-surge-upload/` 及原型 build 一起檢查。總共核對 **4,512 處本機圖片使用位置**，並檢查素材庫 **4,878 個圖片檔案**是否能讀取；這些數字包含同一照片在不同專案、build 中的副本，不代表有 4,878 張不同照片。

**整體素材完整度良好：在《旅魂》及三份 build 裡，這次能從本機確認的圖片引用 100% 找得到，主圖也都能解碼。** 指定追查的「講解遊牧遷移的表演」目前照片完整，也已目視確認畫面正常。不過仍有以下需要處理或決定的事項，所以不能說全站完全沒有異常：

- **兩個原始碼／舊參考頁共 194 處路徑失效。** 其中愛沙尼亞頁 52 處是因為網頁預備放在 build 根目錄，在原始碼目錄直接開啟才找不到；搬進三份 build 後全部正常。舊山西參考頁另有 142 處舊路徑失效，包含一張已由現行頁移除的舊圖。若連這些原始碼直接預覽也納入，4,512 處引用中有 4,318 處可找到，約 **95.7%**；這個比例不代表部署網站缺了 4.3% 的照片。
- **立陶宛紀念品拼貼圖的副檔名不符。** 檔名是 PNG，內容其實是 JPEG，五個副本都一樣。目前可解碼，是否轉成真正 PNG 或調整檔名及引用，請斌哥／Claude Code 決定。
- **貝加爾頁有 6 項卡片差異。** 西伯利亞蘋果、蒸汽機車、葉卡捷琳堡合影這 3 張的敘述不同；另 1 張招待員卡片只有標題措辭不同，以及 2 張卡片只有《旅魂》有。技術清單已逐筆列出兩邊原文，請確認要採哪個版本、哪些差異是刻意保留。
- **另有兩張未直接用於這些 HTML／山西播放器的參考素材，附加縮圖資訊不完整。** 共 8 個副本，主照片能正常讀取，沒有證據顯示它們造成網站破圖。是否整理附加資訊，留給 Claude Code 評估。

對「本機靜態引用是否存在、檔案格式及主圖能否讀取」的結論有高把握：這次不是抽樣，已掃過所有 HTML，也涵蓋 CSS 背景、srcset 檢查及可解析的播放器清單，還核對了路徑大小寫。限制是**沒有測試線上網站、快取或 API 動態回傳的圖片，也沒有逐張判斷所有照片是否配對正確的圖說**；因此不能把這份結果當作所有瀏覽器、線上服務及內容正確性的保證。

待斌哥／Claude Code 決定：兩個原始碼／參考頁是否需要能直接預覽；拼貼圖採哪種格式統一方式；貝加爾 6 項差異如何同步；兩張參考素材的附加縮圖資訊是否值得整理。本次只完成盤點與回報，未補圖、刪圖、改網頁、commit、push 或部署。

---

## Claude Code 驗收回饋（由 Claude Code 填寫）

**驗收日期：2026-09-15。驗收通過。**

抽查以下主張，結果與 Codex 回報完全一致：
- `lvhun/photos/baikal-rail/day03/IMG20260805103339.jpg`：實測確為 JPEG、1200×900，EXIF 顯示 OPPO Find X8 拍攝於 2026:08:05 10:33:39——確認完整無損，不是破圖，已知問題解除。
- `lvhun/photos/bldh-trio/day02/lithuania-souvenirs-collage.png`：實測 `file` 判定確為 JPEG image data、900×755，副檔名 `.png` 屬實不符，格式不符問題成立。
- `git status`（lvhun、travel-site 兩個 repo）：確認除本檔（`vol2/task.md`，新增）與既有跟本任務無關的 3 個 `.mp4` 未追蹤檔外，沒有任何 `.html`／圖片被修改；未 commit／push／部署，符合任務規範。

**判定：** 這次稽核方法紮實（全站掃描而非抽樣、有交代涵蓋範圍與限制、格式問題有做二次複查避免誤判 MPO 為破圖），結論可信賴。194 處失效引用經確認集中在「原始碼直接開啟」與「舊參考頁」，不影響實際上線內容，不需要修復部署站。

**留給斌哥決定的事項（已请 Codex 列出，這裡不代為決定）：**
1. `lithuania-souvenirs-collage.png` 五個副本要轉成真正 PNG，還是改副檔名成 `.jpg`？
2. 貝加爾鐵路頁 4 張共用卡片裡有 3 張兩邊文字內容不同（西伯利亞蘋果／蒸汽機車／葉卡捷琳堡合影），要以哪一邊為準同步過去？
3. 《旅魂》多出的 2 張卡片（成吉思汗飯店、斯帕斯卡亞教堂）要不要也補進 travel-site？

此任務先歸檔為已完成，`vol2/task.md` 將 commit 進 lvhun repo 保留紀錄（純文件，不影響網站內容）。

**斌哥裁決（2026-09-15）：**
1. 立陶宛 `lithuania-souvenirs-collage.png` 五個副本 → 特效測試，不予理會，維持原狀
2. `estonia-journal.html` 52 處 → 確認是建置前樣板、build 後正常，維持現狀不動
3. `shanxi-golden.html` 142 處（舊參考頁）→ 已 `git mv` 到 `travel-site/archive/shanxi-golden.html` 集中歸檔，並同步更新 `scripts/extract_shanxi.py` 裡的路徑常數，避免之後對不上

貝加爾鐵路 6 項卡片差異（西伯利亞蘋果／蒸汽機車／葉卡捷琳堡合影／招待員標題／成吉思汗飯店／斯帕斯卡亞教堂）尚未裁決，留待下一輪。第二卷封面／Hero 換真實照片的任務，等斌哥對這幾項卡片差異給意見後再派下一輪。
