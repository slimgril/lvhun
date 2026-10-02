# lvhun（旅魂）— Agent guidance

## Workspace（canonical — HARD RULE）

```
CANONICAL PROJECT ROOT: /Users/mac/Documents/Projects/旅遊/lvhun
部署：Render static site（lvhun.onrender.com），git push 到 main 後自動部署
render.yaml 的 name: lushun-travel-memoir 跟書名拼音 lvhun 對不上，是 2026-08-30
自己手誤的舊名，不是抄別的專案；會不會改看 Owner 之後要不要處理，目前不動它
```

**與 `travel-site` 的關係：** 兩個是獨立的 Git 專案、獨立部署（`travel-site` 是 Cloudflare Pages），但共用同一套「AI KOS」設計語言與寫作規則。`travel-site/CLAUDE.md` 裡標註「全專案（含 lvhun、travel-site）」的規則，對本專案同樣是 HARD RULE，見下方「共用規則」。

**知識讀序（開工必循）：** 本檔 → 下方「共用規則」連結到的 `travel-site/CLAUDE.md` 對應章節 → 要動工的那個 `volN/*.html` 本身的既有內容（抄既有頁面的版型時，先看它的 git log，不要只看 mtime——`baltic.html`／`shanxi.html` 已經停在初版很久沒再更新，`baikal.html` 才是持續迭代中的版本，見下方「範本選用」）。

---

## 範本選用 HARD RULE（2026-10-02 · 實測教訓）

> **血淚教訓：** 建 `vol2/kansai.html` 時抄了 `vol1/baltic.html`，結果漏掉 `baikal.html` 在 2026-09-16（commit `6b92bc9`，Owner 指示）做過的 Phase B 改版。`baltic.html`／`shanxi.html` 從 9/13 之後只有一次無關痛癢的小修，`baikal.html` 有 19 次 commit、持續在迭代——**檔案 mtime 新舊不等於內容新舊，一定要查 `git log --oneline -- <檔案>`，commit 數最多、最近仍有實質修改的那個才是目前的標準範本。**

- 新增任何 `volN/*.html` trip page 之前，先確認三件事：(1) `vol1/baikal.html` 是不是還是 commit 數最多的那個（`git log --oneline -- vol1/*.html` 逐一比對），(2) 它最近一次「結構性」commit 改了什麼（不是看 commit 數字，是看 diff 內容），(3) 本頁要複製的是哪一段結構，直接從那個 commit 的 diff 裡取，不要憑印象從舊頁面手動搬。
- 這條規則本身也要跟著維護：每次有新的結構性 commit，把下面「Day Page 版型」更新成最新狀態，不要讓這份文件自己也變成過時的範本說明。

## Day Page 版型 HARD RULE（2026-10-02 統整，溯源 2026-09-16 commit `6b92bc9`）

每個 trip page（`volN/<trip>.html`）的逐日內容，固定結構：

```
day-section
├── day-header（day-badge／date／route／accommodation）
├── [有景點導覽圖才有] section-divider "✦ 景點導覽" + sites-grid sites-grid--preview
│     （行前預建的純景點照，無人入鏡，鎖定資產，不得替換或刪除；沒有準備
│       景點導覽圖的天數——例如本書關西自由行全系列——就不生這一段，
│       不強加空分隔線，見 baikal.html Day10-13 先例）
├── section-divider "✦ 早" + sites-grid sites-grid--fast（旅人實拍，依拍攝時刻分組）
├── [有的話] section-divider "✦ 中" + sites-grid sites-grid--fast
└── [有的話] section-divider "✦ 晚" + sites-grid sites-grid--fast
      （早/中/晚三節都是「有內容才生該節」，沒有晚間照片就不生「✦ 晚」，
       不要為了版型完整而留白或硬湊）
```

**卡片屬性（HARD）：** 每張 `.site-card` 都要有 `data-photo-type="destination_preview"` 或 `"traveler_photo"`、`data-counted="true/false"`（景點導覽固定 `false`，旅人實拍固定 `true`）——這是 `baikal.html` Video Renderer script 用的屬性系統，**跟 `travel-site`／`jiuzhaigou.html` 用的 `data-egg-type`／`data-fold-video` 靜態屬性是兩套不同系統，不要混用**：lvhun 的頁面一律用這一套，由 `<script>` 在 `init()` 時動態補上預設值，寫死在 HTML 裡也可以但不是必要。

**照片 `<img>` 寫法（2026-10-02 起 HARD，取代舊的 CSS 背景圖寫法）：**
```html
<div class="site-img photo"><img src="路徑" alt="跟 img-label 一致的文字" loading="lazy" decoding="async" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;"><div class="img-label">...</div></div>
```
影片卡的 `.video-card` 維持原本的 inline `background-image` 寫法不變（Video Renderer script 的 `measure()`／`stage()` 依賴這個）。

**5 欄快速網格：** 旅人實拍一律用 `sites-grid sites-grid--fast`（`base.css`，手機彈性欄數、桌機鎖定 5 欄），不要用舊的 `sites-grid`／`sites-grid--pair`（那是景點導覽 `sites-grid--preview` 專用，或未套用 Phase B 的舊頁面殘留，新頁面不要再生這個）。

**長文摺疊／彩蛋骨架／影片 Lightbox（HARD，不得省略）：** 每個 trip page 的 `</body>` 前必須包含完整的「Video Renderer」`<script>`（見 `vol1/baikal.html` 或 `vol1/baltic.html` 結尾）。這段負責：
1. `.site-desc` 超過三行自動摺疊＋「展開更多 ▾」按鈕（`.site-desc--foldable`／`.is-collapsed`／`.is-expanded`，CSS 在 `base.css`）
2. 彩蛋骨架：每張卡片補 `data-egg-type="none"`／`data-egg-source=""`，完全展開時若非 none 觸發 `.has-surprise` 動畫（素材就位前都是 `none`，骨架先預埋）
3. 影片卡點擊開全螢幕 Lightbox 播放，不是卡內直接播放
**新建 trip page 時直接整段複製這支 script，不要只抄卡片的靜態 HTML——這是 2026-10-02 當天實測犯過的錯，複製範本時「連 script 一起」是檢查清單的第一條。**

## 描述文字數 HARD RULE（2026-10-02 · Owner 定案）

單張卡片 `.site-desc` 抓 **100 字左右**（90–110 字為佳），不要忽長忽短（實測教訓：同一天卡片曾經從 20 字到 143 字都有，版面閱讀節奏被破壞）。例外：有特殊紀念意義、需要多介紹典故的景點可以多一點，但也要有節制，不是沒有上限。寫作內容規則本身（身在現場、觀察優先於介紹、禁導覽詞等）見 `travel-site/CLAUDE.md` 的「Travel Notes Writing Rules」，兩本書共用同一套，不要各自為政。

## 共用規則（SSOT 在 `travel-site/CLAUDE.md`，本專案同樣適用）

以下規則定義在 `travel-site/CLAUDE.md`，明文「全專案（含 lvhun、travel-site）」適用，不在本檔重複貼一份避免兩邊內容日後不同步，要看細節直接去讀那邊：

| 規則 | 章節 |
|------|------|
| 原圖不可改／同圖不兩處／足跡圖國名字級 | 「冰哥／斌哥圖檔與足跡圖三原則」 |
| 使用者提供影音素材＝完成品，禁止二次加工（僅允許格式轉換／必要時壓縮以符合平台大小限制，例如 GitHub 單檔 100MB 硬限制時） | 「使用者提供影音素材＝完成品」 |
| Travel Notes Writing Rules（內容該寫什麼、不該寫什麼，10 條規則＋品質自檢） | 「Travel Notes Writing Rules」 |

## 派工給 Codex 時的驗收清單

把任務寫進 `/Users/mac/Documents/Projects/旅遊/TASK_DISPATCH.md` 時，規格裡直接引用本檔對應章節（例如「比照 CLAUDE.md『Day Page 版型 HARD RULE』」），不要只口述。審查 Codex 回報時，照上面「範本選用」「Day Page 版型」「描述文字數」三節逐條核對，核對不過就寫修改意見打回去，不要自己先改掉再說 Codex 做錯。

## Wake commands

| 指令 | 行為 |
|------|------|
| **開工** | 先讀本檔，再讀 `/Users/mac/Documents/Projects/旅遊/CLAUDE.md` 的 Current Status |
| **Ingest** | 跨文件相關內容同步：這份文件本身也要跟著最新的結構性 commit 更新，不要讓範本說明自己過時 |
