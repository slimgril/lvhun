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

> **第二卷 Hero 已鎖定（Owner 2026-11-05）：** `vol2/index.html` 的 hero 不得改動，見下方「Owner 裁示（2026-11-05）」。

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

> **【2026-11-08 標註】與「山東 11-06 裁示」衝突處已被取代，見本檔「描述文規則（山東，Owner 2026-11-06／11-08 裁示）」。衝突不明確處未自行判斷，已列在 R005。**

`.site-desc` 與 `.day-closing` 禁用「你、我、他、她、牠、它」（「其他」等複合詞不算）。動物、物件改用名詞或省略主詞。

## 描述文文風放寬規則（2026-10-12 Owner 裁示，取代舊的逐字堆砌寫法）

> **【2026-11-08 標註】與「山東 11-06 裁示」衝突處已被取代，見本檔「描述文規則（山東，Owner 2026-11-06／11-08 裁示）」。衝突不明確處未自行判斷，已列在 R005。**

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

## 描述文規則 v2（2026-11-05 Owner 裁示；取代上面三節中與本節衝突的部分）

> **【2026-11-08 標註】與「山東 11-06 裁示」衝突處已被取代，見本檔「描述文規則（山東，Owner 2026-11-06／11-08 裁示）」。衝突不明確處未自行判斷，已列在 R005。**

> 起因：Y冰哥認為 Day 5–7 放寬後的寫法「硬邦邦」，不像原本的調性。Owner 解除關西凍結區，Day 5／6／7 已依本節重寫（47 則 `.site-desc`＋3 則 `day-closing`）。上面「描述文字數」（90–110）、「禁用人稱代名詞」（僅限自寫文字的部分仍有效）、「文風放寬規則」（`.site-desc` 一律不再套用其結尾與清單式寫法）與本節衝突處，**一律以本節為準**。

1. **風格：** 以 Owner 抒情風格（A）為準，依 `travel-site/.ai-kos/CONTENT_STYLE.md` v1.2（身在現場切入、資訊順口帶出、結尾留一句感受）。約 100 字（**80–120 皆可**，去標籤去空白）；人與景融合，人物以「一人／左側／中間」帶過；冥想／幻想**每則最多一句**；比喻式結尾**每天不超過 1／3**，其餘用景物或平實感受收尾。
2. **有 reference 就引用：** 若有 Y冰哥 FB 原文（檔名可能是 `reference.md`、`CLAUDE.txt`、`ref.pdf`）→ **逐字引用**，不加「貼文寫」「他說」等標註，直接當描述文；原文中的「你我他她」照抄、不改、**不納入代名詞掃描**；交件時標「引用」並對照原檔逐字核對（不憑記憶或前次轉錄）。**沒有 reference** → 全部自寫，**禁用你我他她牠它**（「其他」除外）。
3. **不設特別篇名：** 不自創「美食篇」「火車篇」「天文篇」等分段或標籤，除非 Y冰哥指定。
4. **只寫畫面可證實的：** 不確定的不寫（魚種、肉種、看不清的字、建築名稱等一律保守）；不寫聲音、氣味、味道（「沉靜」「空曠」之類氛圍用語可）。畫面上的字（招牌、價目卡、說明牌）照實寫，不算引用。
5. **`note*.jpg`（FB 貼文截圖）只作時間、地點參考，不放進頁面、不當引文。** 影片只抽到少數畫面時，不寫「駛來／離去」之類看不準的動態順序。
6. **照片依 EXIF／浮水印時間順序**，維持 ✦早／中／晚；時段標籤與時間對不上時只列出、不自行改結構。
7. **`day-closing` 用散文式**（比照 Day 1–4），保留時間與地點事實；同樣適用本節規則。
8. **用語重複：** 同一天內「分明／醒目／特別／層層／一根接一根／格外／碎光／笑得很開」這類高頻詞各最多 1 次；同一件衣著寫法在同日一致，看不準顏色就只寫「車隊球衣」。
9. **與 `travel-site/CLAUDE.md`「Travel Notes Writing Rules」的關係：** 該節 Rule 1（Facts First）在本專案以本節第 4 條為準——可有一句冥想／幻想與平實感受收尾，但不得編造畫面看不到的事實、聲音、氣味、味道。（`travel-site/CLAUDE.md` 本身未改，另案處理。）
10. **既有 Owner 裁示（2026-11-05）第 5、6 條保留**；其中第 6 條的「逐字核對」現在適用於任何引用（reference 原文）。

## 描述文規則（山東，Owner 2026-11-06／11-08 裁示；與 v2、10-12、10-06 三節衝突處以本節為準）

1. **文風母版：** 以 `vol1/shanxi.html` 目前已上線、Y冰哥也認可的實際成品為準；先重讀山西卡片，從成品掌握句型、資訊密度、語氣。80–120 字僅供參考、不是限制，照片重要程度不同，長短可有彈性。
2. **代名詞：** 「你、我、他」不嚴格禁止，但盡量少用、非必要不用（取代「禁用人稱代名詞」）。
3. **旅遊雜記，不是照片圖說。** 「心裡想…」「忍不住幻想…」不公式化、不全面禁止：只有在有真實依據（NOTE、reference、現場背景如行程表／畫面文字）時才自然使用；沒有依據就不替旅人編心理活動，回到看得見的現場＋可證實的背景＋自然的旅行語氣。不確定的專有名詞、人物關係、故事背景不補。
4. **NOTE 只在幕後提供記憶與感觸**，成品永遠不以 NOTE、兵哥說、兵哥寫等形式出現。
5. 沿用不衝突者：有 reference（FB 原文）逐字引用、不加標註；`note*.jpg` 只作時間地點參考；照片依 EXIF／浮水印時間排序、維持 ✦早／中／晚；不自創篇名；`day-closing` 散文式；畫面上的字照實寫；不確定的（魚種、建築名、看不清的字）不寫。
6. **照片／影片時間判斷（I006，2026-11-08）：** 優先順序 ①畫面水印時間 ②EXIF 拍攝時間 ③檔名時間（最後手段）。檔名是拍攝者自取，不一定準。水印決定 Day 歸屬、早／中／晚時段、卡片先後；三者不一致時以水印為準並記入衝突清單；只能用 ②③ 的照片在審稿檔標「時間不確定」。影片同理（畫面水印或內嵌拍攝時間，抓不到標「時間不確定」）。同一天內水印時間與畫面內容明顯矛盾（相機時鐘可能設錯）時，不自行判斷，列出回報由 Owner 決定。
7. 描述文成品完成後，一律用 `_交換區/review_extract.py` 從 `vol2/shandong.html` 產生 `_交換區/描述文審稿.md`，HTML 改動後須重新產生，不可手改。
8. **公開照片 GPS 清除（標準程序，Owner 2026-11-08）：** 山東 Day 3–8 的每一批新照片，寫入公開網站（`photos/shandong/dayNN/`）之後、commit 之前，一律對「公開副本」執行 `_交換區/gps_clean_check.sh photos/shandong/dayNN`：只移除 GPS 位置欄位、其他 metadata 不動，並複查 0 件含位置資訊才可 commit。Drive 原始照片永不修改、搬動或覆寫；報告只列處理張數與檢查結果，不寫座標。
9. **版面（Owner 2026-11-08 15:39 裁示）：** 沒有照片／影片的時段不顯示（山東頁以此為準，取代「早／中／晚固定都要有」；其他趟次頁面不動）。
10. **美食、藝術類卡片（Owner 2026-11-08 16:45 裁示）：** 可寫色香味與雀躍感受（旅遊雜記，不是美食節目）；菜名、食材、做法須有依據，具體動作與外部連結不寫。
11. **影片卡標題（Owner 2026-11-09 裁示）：** 所有影片卡片的標題不加「（影片）」後綴（左上角已有「影片」標籤）；影片描述文 35–45 字，交代地點＋鏡頭帶到的景物。

## 共用規則（SSOT 在 `travel-site/CLAUDE.md`，本專案同樣適用）

以下規則定義在 `travel-site/CLAUDE.md`，明文「全專案（含 lvhun、travel-site）」適用，不在本檔重複貼一份避免兩邊內容日後不同步，要看細節直接去讀那邊：

| 規則 | 章節 |
|------|------|
| 原圖不可改／同圖不兩處／足跡圖國名字級 | 「冰哥／斌哥圖檔與足跡圖三原則」 |
| 使用者提供影音素材＝完成品，禁止二次加工（僅允許格式轉換／必要時壓縮以符合平台大小限制，例如 GitHub 單檔 100MB 硬限制時） | 「使用者提供影音素材＝完成品」 |
| Travel Notes Writing Rules（內容該寫什麼、不該寫什麼，10 條規則＋品質自檢） | 「Travel Notes Writing Rules」 |

## 派工給 Codex 時的驗收清單

把任務寫進 `/Users/mac/Documents/Projects/旅遊/TASK_DISPATCH.md` 時，規格裡直接引用本檔對應章節（例如「比照 CLAUDE.md『Day Page 版型 HARD RULE』」），不要只口述。審查 Codex 回報時，照上面「範本選用」「Day Page 版型」「描述文字數」三節逐條核對，核對不過就寫修改意見打回去，不要自己先改掉再說 Codex 做錯。

## 交換區（Cowork Claude ⇄ Claude Code，2026-11-05 起）

新工作一律走 `~/dev/lvhun/_交換區/`（規則全文見該資料夾 `README.md`）；`~/dev/REVIEW_DISPATCH.md` 保留當歷史，不再派新工作。

- **資料夾**：`instructions/`（Cowork 寫 `I###_主題.md`）、`reports/`（Claude Code 寫 `R###_主題.md`，與 I 同號）、`archive/`（驗收通過後 I／R 成對移入）。
- **觸發**：Owner 說「執行交換區指令」→ 做 `instructions/` 裡編號最小、尚無對應 R 的那一份（一次一份）；標了「前置條件」而未達成的，只回報、不開工。
- **回報**：報告前 10 行是摘要（結論／完成狀態／需 Owner 決定／驗收用數字），細節放後面；不確定就寫「不確定」。
- **驗收前不 push、不部署**；Owner 另有指示時連本地 commit 也不做。
- **不公開**：`_交換區/`、`vol2/shandong/source/`（行程表 PDF，含電話）已列 `.gitignore`；`render.yaml` 的 `staticPublishPath: ./` 會公開 repo 根目錄所有檔案，內部文件一律不得 commit。

**Owner 2026-11-05 裁示：** 山東頁名維持「山東賞紅葉」；`photos/destination-preview/shandong/dayNN/` 空資料夾先不 chmod 鎖定，等 Owner 放入照片後再鎖。

## Owner 裁示（2026-11-05，HARD RULE）

1. **第二卷 Hero 已定案，不得再改。** 範圍：`vol2/index.html` 的 hero（含九寨溝、關西自由行、山東三趟），Owner 與 Y冰哥都已同意。只有單一趟頁面（例如 `kansai.html`）自己的 hero 可依該趟需要修改；第二卷封面提案（I001 T3）已取消，不要再提。對第二卷 hero 有疑問，先問 Owner，不要自己判斷。
2. **內部文件不公開。** repo 根目錄會被 Render 公開；`vol2/task.md`、`vol2/photo-reconciliation-report.md` 已移出追蹤、搬到 `_交換區/archive/`。之後的派工單、稽核報告、行程表一律放 `_交換區/` 或其他已 `.gitignore` 的位置。`CLAUDE.md` 保留追蹤（GitHub 備份）。
3. **貝加爾文字與照片不符（I001 T4 #1–#4）等 Y冰哥回覆後才處理；#5、#6 不處理。** 關西凍結區（Day 5／6 人味重寫、Day 6 晚間 3 張、10/11 Columbia 吊牌照）照舊不動。
4. **關西「完結」標示（hero-badge、「更新中」、`vol2/index.html` 的「連載中」）先不改**，等凍結區處理完。
5. **Day 6 晚上 3 張大阪照片不補**（Y冰哥回覆，Owner 2026-11-05 決定）。第 3 條凍結區裡的「Day 6 晚間 3 張」就此定案：不上架、不再列為待裁示。
6. **`note*.jpg`（貼文截圖）只作時間、地點與貼文文字的參考，不放進頁面**；頁面圖片以大圖（Drive 原始照片）為主。貼文原句要逐字照抄（例如「最後一餐就吃**個**日本料理」，不可漏字），逐字核對對照 `note*.jpg` 原圖，不憑記憶或前次轉錄。

## Wake commands

| 指令 | 行為 |
|------|------|
| **開工** | 先讀本檔，再讀 `/Users/mac/Documents/Projects/旅遊/CLAUDE.md` 的 Current Status |
| **Ingest** | 跨文件相關內容同步：這份文件本身也要跟著最新的結構性 commit 更新，不要讓範本說明自己過時 |
| **執行交換區指令** | 依上方「交換區」一節，做編號最小、尚無 R 的那份 I，報告寫進 `_交換區/reports/` |
