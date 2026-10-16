# lvhun（旅魂）— Agent guidance

## Workspace（canonical — HARD RULE）

```
CANONICAL PROJECT ROOT: /Users/mac/dev/lvhun （2026-10-16 起，取代舊路徑）
部署：Render static site（lvhun.onrender.com），git push 到 main 後自動部署
render.yaml 的 name: lushun-travel-memoir 跟書名拼音 lvhun 對不上，是 2026-08-30
自己手誤的舊名，不是抄別的專案；會不會改看 Owner 之後要不要處理，目前不動它
```

**路徑變更記錄（2026-10-16）：** 舊路徑 `/Users/mac/Documents/Projects/旅遊/lvhun` 因 Google Drive 同步把 `.git` 等整批檔案移進垃圾桶、且無法用 AppleScript「Put Back」或本機工具還原，Owner 已停用該資料夾的 Google Drive 同步，改從 GitHub（`github.com/slimgril/lvhun`）重新 clone 到 `~/dev/lvhun`（不在 Documents、不在任何雲端同步路徑下），設為新的正式工作位置。舊路徑殘留內容（`index.html`、`vol2/`）暫留未刪，待 Owner 確認新位置穩定後手動清除；之後所有對話一律以 `~/dev/lvhun` 為準，不要回去舊路徑。

**與 `travel-site` 的關係：** 兩個是獨立的 Git 專案、獨立部署（`travel-site` 是 Cloudflare Pages），但共用同一套「AI KOS」設計語言與寫作規則。`travel-site/CLAUDE.md` 裡標註「全專案（含 lvhun、travel-site）」的規則，對本專案同樣是 HARD RULE，見下方「共用規則」。

**知識讀序（開工必循）：** 本檔 → 下方「共用規則」連結到的 `travel-site/CLAUDE.md` 對應章節 → 要動工的那個 `volN/*.html` 本身的既有內容（抄既有頁面的版型時，先看它的 git log，不要只看 mtime——`baltic.html`／`shanxi.html` 已經停在初版很久沒再更新，`baikal.html` 才是持續迭代中的版本，見下方「範本選用」）。

**AI-KOS 治理（R4，2026-10-06 補記）：** 旅魂（lvhun）同樣受 AI-KOS 治理。開工時 `travel-site/.ai-kos/` 必讀順序：`WORKSPACE.md` → `RESUME_CONTEXT.md` → `DAILY_TRAVEL_UPDATE.md` → `CONTENT_STYLE.md` → `STATUS.md`。

---

## 範本選用 HARD RULE（2026-10-02 · 實測教訓）

> **血淚教訓：** 建 `vol2/kansai.html` 時抄了 `vol1/baltic.html`，結果漏掉 `baikal.html` 在 2026-09-16（commit `6b92bc9`，Owner 指示）做過的 Phase B 改版。`baltic.html`／`shanxi.html` 從 9/13 之後只有一次無關痛癢的小修，`baikal.html` 有 19 次 commit、持續在迭代——**檔案 mtime 新舊不等於內容新舊，一定要查 `git log --oneline -- <檔案>`，commit 數最多、最近仍有實質修改的那個才是目前的標準範本。**

- 新增任何 `volN/*.html` trip page 之前，先確認三件事：(1) `vol1/baikal.html` 是不是還是 commit 數最多的那個（`git log --oneline -- vol1/*.html` 逐一比對），(2) 它最近一次「結構性」commit 改了什麼（不是看 commit 數字，是看 diff 內容），(3) 本頁要複製的是哪一段結構，直接從那個 commit 的 diff 裡取，不要憑印象從舊頁面手動搬。
- 這條規則本身也要跟著維護：每次有新的結構性 commit，把下面「Day Page 版型」更新成最新狀態，不要讓這份文件自己也變成過時的範本說明。

## Day Page 版型 HARD RULE（Owner 最終版型，2026-10-06 定案）

> **此為 Owner 最終版型，任何 AI 不得以「沒有固定」為由更動；有疑問先問 Owner。**
> 取代 2026-10-02 統整的舊寫法（舊版「條件式生成」的規定全部廢止，不再依素材有無省略景點導覽或時段分區）。溯源 2026-09-16 commit `6b92bc9`。

每個 trip page（`volN/<trip>.html`）的逐日內容，固定三個時段，順序不得變：

```
day-section
├── day-header（day-badge／date／route／accommodation）
├── （有行前行程規劃的旅程限定）section-divider "✦ 景點導覽" + sites-grid sites-grid--preview
│     Owner 依行程表預先挑選的純景點照（無人入鏡），放 photos/destination-preview/<行程>/dayNN/，
│     上架即鎖定（檔案 chmod 444／目錄 chmod 555），不得與旅人照片混放、不得替換或刪除
├── ① section-divider "✦ 早" + sites-grid sites-grid--fast（旅人實拍）  ← 固定有
├── section-divider "✦ 中" + sites-grid sites-grid--fast                 ← 固定有
└── section-divider "✦ 晚" + sites-grid sites-grid--fast                 ← 固定有
```

**景點導覽區（R5，2026-10-06 Owner 裁決，取代同日稍早的 R3-2 寫法）：** 景點導覽區**限有行前行程規劃的旅程**（Owner 依既定行程表預先挑圖）每天必有；**自由行（無事先行程規劃，例如關西自由行）整趟不設景點導覽區**，Day Page 直接從 ✦ 早／中／晚 旅人實拍開始，不放空骨架或「製作中」字樣占位。新開一個 trip page 時，先確認這趟是不是自由行，再決定要不要生這一段。

- **✦ 早／中／晚三個時段分區固定都要有**：某時段沒有照片時，保留分隔線，下方放一行灰字「（本時段無照片）」，不得省略分區。
- **每行 5 張**：旅人實拍一律 `sites-grid sites-grid--fast`（桌機鎖 5 欄），不得用舊的 `sites-grid`／`sites-grid--pair`。
- **描述文一律「展開更多」摺疊**：由頁尾 Video Renderer script 負責；新頁面必須連 script 一起複製。

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

**照片 Lightbox（HARD，不得省略，2026-10-03 補記）：** 這是**另一支獨立的 `<script>`**，跟上面的 Video Renderer 不是同一段，兩個都要複製，缺一個都會造成卡片點了沒反應。見 `vol1/baikal.html` 結尾的 `#lightbox` 區塊：
```html
<div id="lightbox">
  <span class="lightbox-close">&times;</span>
  <img src="" alt="" loading="lazy" decoding="async">
  <div class="lightbox-caption"></div>
</div>
```
加上緊接在後的 `<script>`（監聽 `.site-img.photo, .live-img` 的 click，排除 `.video-card`，點擊放大一般照片卡；CSS 已在 `base.css` 的 `#lightbox` 區塊共用，不用另外寫）。
**血淚教訓：** `vol2/kansai.html` 建頁當天只複製了 Video Renderer（影片卡 Lightbox），漏了這段照片 Lightbox，Day1、Day2 上線後一般照片卡點擊完全沒反應，直到 2026-10-03 才發現補回。新建 trip page 時，`</body>` 前檢查清單至少要有「Video Renderer」＋「照片 Lightbox」兩支 script，缺一不可。

## 描述文字數 HARD RULE（2026-10-02 · Owner 定案；2026-10-06 補硬性區間）

單張卡片 `.site-desc` 為 **90–110 字硬性區間**（去除 HTML 標籤與空白後計算），低於 90 或高於 110 視為不合格，不要忽長忽短（實測教訓：同一天卡片曾經從 20 字到 143 字都有，版面閱讀節奏被破壞）。例外：有特殊紀念意義的景點可超出區間，但必須在該卡的 HTML 註解寫明理由，否則不得超出。寫作內容規則本身（身在現場、觀察優先於介紹、禁導覽詞等）見 `travel-site/CLAUDE.md` 的「Travel Notes Writing Rules」，兩本書共用同一套，不要各自為政。

## 描述文禁用人稱代名詞 HARD RULE（2026-10-02 Owner 要求，2026-10-06 補記）

`.site-desc` 與 `.day-closing` 禁用「你、我、他、她、牠、它」（「其他」等複合詞不算）。動物、物件改用名詞或省略主詞。

## 描述文文風放寬規則（2026-10-12 Owner 裁示，取代舊的逐字堆砌寫法）

> 起因：斌哥反映 Day 5 描述文「很彆扭」；Owner 裁示放鬆寫法，目標是讀起來流暢像一段散文，不是物品清單。Day 5／Day 6 已依此規則重寫過（共 42 則），**Day 7 起新寫的卡片直接照這套規則寫，不用再回頭重寫舊卡**。

**底線不變（仍是 HARD RULE，不因放寬而鬆動）：**
1. 只寫畫面／影片／浮水印能證實的事實；不編聲音、味道、體感、心情、別人的動作、推測的抵達／出發／交通方式。
2. 看不清的字不寫；地點只寫有證據的（浮水印、招牌、立牌）。
3. `.site-desc` 90–110 字（去標籤去空白，算法：`len(re.sub(r'<[^>]+>|\s','',text))`，**注意要去空白**——英文站名、品牌名中間的空格也要算進去扣除，不是單純去 HTML 標籤）；禁代名詞（見上一節）。
4. 結構、媒體、日期、時間軸規則不變，仍依本檔其餘 HARD RULE。

**放寬的寫法（新，2026-10-12 起適用）：**
1. **句子要連貫成一小段散文，不要寫成「物品清單」**。每則最多點 3–4 個最具代表性的物件，其餘不必寫盡、不必把畫面細節塞滿。
2. **人物主詞要補上**：用「畫面中一人」「照片裡的人」「同行的人」等，禁止出現沒有主詞、憑空接動詞的句子（例如「雙手叉腰站在台前」「站在一旁抬頭看著」——讀起來像沒頭沒尾）。
3. **少用相機語氣**：避免「鏡頭先…接著鏡頭轉向…」這種分鏡式寫法；影片卡改寫成「影片從…（到）…最後…」或直接照時間先後描述畫面內容。**改寫時務必核對影片實際的畫面先後順序**，不要憑印象排，順序寫反屬事實錯誤（2026-10-12 複核教訓：Day 6 傘松公園影片卡順序一度寫反，被總監察抓出）。
4. **開頭從最醒目的畫面切入，結尾用一句可見的畫面收束**（光線、顏色、整體構圖），不下結論、不寫心情、不寫「只能…」這類帶情緒收尾的句子。
5. 可用中性連接詞與轉場（「遠處」「靠近鏡頭的一側」「畫面右方」）讓句子順，不要為了文風硬塞形容詞。
6. **去掉純粹為了湊字數硬補的細節**（例如「木邊緣露出原木色澤」「兩隻猛禽身形相近」這類讀不出資訊量的句子），改用流暢、確實看得到的觀察把字數補到 90 字以上；**湊字用的句子若語意和前文重複（例如「藍天白雲」講兩次、「天空飄著大片白雲，雲層厚實」）一樣算違規**，要刪。

**範例（Day 5 #9 大極殿金色屋脊飾，總監察 2026-10-12 示範）：**
> 改前：殿內一座金色裝飾立在展示台上，…站在一旁抬頭看著這件飾物，黑色護欄圍出一道安全距離。…
> 改後：殿內展示台上立著一座金色飾物，造型像展開的羽翼，頂端的細長金條向外放射，多道金屬條交錯其上。台前圍著黑色護欄，左側立有日文說明牌；畫面中一人站在護欄外，抬頭望著這件飾物。

**改寫流程提醒：** 整則改完後務必重算字數（含空格的那個算法）、重掃代名詞，兩者都過才算完成；不要只憑感覺判斷字數落在 90–110。

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
