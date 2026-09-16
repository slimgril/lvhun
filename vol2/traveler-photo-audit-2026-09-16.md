# 旅人實拍照片上架稽核

## 批次 01：`baikal-rail` 前 50 個媒體檔案

稽核日期：2026-09-16  
批次狀態：進行中，**本報告不是 380 筆完整稽核結果**。

### 批次範圍

- 對象目錄：`lvhun/photos/baikal-rail/`
- 取樣規則：只納入照片／影片副檔名，依相對路徑使用 `LC_ALL=C sort` 字典序排序後取前 50 筆。
- 排序邊界：`day01/IMG20260803105200.jpg` 至 `day04/sparse-vegetables.jpg`。
- 不納入：`.DS_Store`、`CLAUDE.txt` 等非照片／影片檔案，以及第 51 筆之後的媒體檔案。
- manifest：`drive_traveler_photo_manifest.json`，確認為 380 筆、生成日 `2026-09-16`。

### 判定方法

1. 對本批 50 個本機媒體檔案計算 SHA-256，與 380 筆 manifest 逐筆比對。
2. SHA-256 沒有吻合時，用 `exiftool` 讀取 `DateTimeOriginal`、`CreateDate`、`MediaCreateDate`、`TrackCreateDate`；時間先正規化，同一分鐘視為候選相同檔案。
3. 對已找到 manifest 對應的本機檔案，檢查相對路徑是否以 `img src`、`video src` 或 `background-image:url(...)` 形式出現在 `lvhun/vol1/baikal.html`。
4. 本批未連線 Google Drive，未修改 HTML、圖片或 `photos/destination-preview/`。

## 批次統計

下表的「manifest 總數」是該群組完整清單數；「本批找到本機對應」只計入前 50 個本機媒體檔案，因此剩餘數量不代表已判定為遺失。

| drive_group | 對應網站區段 | manifest 總數 | 本批找到本機對應 | 已上架 | 本機有但沒上架 | 尚未納入本批 |
|---|---:|---:|---:|---:|---:|---:|
| 0803 | Day01 | 5 | 5 | 5 | 0 | 0 |
| 0804 | Day02 | 12 | 11 | 11 | 0 | 1 |
| 0805 | Day03 | 18 | 12 | 12 | 0 | 6 |
| 0806 | Day04 | 12 | 9 | 8 | 1 | 3 |
| Food | Food 池 | 29 | 4 | 4 | 0 | 25 |
| **本批合計** |  | **76** | **41** | **40** | **1** | **35** |

`Day05` 至 `Day20` 及 `Train` 本批沒有涵蓋，不能由本批結果判定為 0。

## 本機有檔案，但沒有上架成卡片

本批共 1 筆。以下是完整本機相對路徑；它已用 EXIF 分鐘級比對到 manifest，但其路徑沒有出現在 `baikal.html`：

- `day04/chinggis-khaan-hotel.jpg`（對應 `0806/IMG20260806185306.jpg`；HTML 未找到引用）

## 本機完全找不到對應檔案

本批以「前 50 個本機媒體檔案」為處理單位，沒有把尚未掃描的本機範圍誤列為 Drive 缺檔。  
因此本批對 Drive manifest 的「本機完全找不到」數字為：**未判定**。

尚未納入本批的 manifest 筆數如下，這些不是本批的缺檔結論：

- `0804`：1 筆
- `0805`：6 筆
- `0806`：3 筆
- `Food`：25 筆
- `Day05` 至 `Day20`、`Train`：尚未開始

## 本機檔案未能依規格對應 manifest

以下 9 個檔案屬於本批已掃描的本機媒體，但沒有 SHA-256 或 EXIF 分鐘級吻合的 manifest 項目。它們不直接等同於「Drive 缺檔」；其中包含重新命名／轉製的影片或網站衍生素材，需在後續批次或人工內容核對時另行處理。

- `day02/terelj-camp-panorama.mp4`
- `day03/camel-ride.mp4`
- `day03/dinner-mongolian-song.mp4`
- `day03/dinner-noble-costume.mp4`
- `day03/grassland-horsemanship.mp4`
- `day03/grassland-scenery.mp4`
- `day03/grassland-song-performance.mp4`
- `day04/folk-dance-morin-khuur-1.mp4`
- `day04/folk-dance-morin-khuur-2.mp4`

這 9 筆中有 9 筆的本機路徑仍出現在 `baikal.html`；本批只記錄路徑引用，不以檔名或卡片敘述猜測其 Drive 原始檔對應關係。

## 本批正常項目摘要

- 可對應到 manifest 且已在 HTML 上架：**40 筆**
- 可對應到 manifest、本機存在但 HTML 未引用：**1 筆**
- 已掃描但無法以 SHA-256／EXIF 分鐘級對應 manifest：**9 筆**
- 本批已掃描本機媒體總數：**50 筆**
- 本批尚未涵蓋的完整稽核範圍：其餘 `baikal-rail` 媒體、以及尚未處理的 Drive manifest 項目。

## 後續批次界線

本報告只完成第一批，不代表 Day01–Day20、Food、Train 全部稽核完成。後續批次應延續相同排序規則處理第 51 筆之後的媒體，並在所有 Drive manifest 項目都完成比對後，才可填寫完整的「本機完全找不到」清單與完整任務結論。

---

## 批次 02：第 51–100 個媒體檔案

稽核日期：2026-09-16  
批次狀態：已完成，仍不是 380 筆完整稽核結果。

### 批次範圍

- 排序規則與第一批相同：依 `baikal-rail` 媒體檔案相對路徑字典序排序。
- 範圍：`day04/ulaanbaatar-traffic.jpg` 至 `day07/buryat-singing-video.mp4`。
- 本批共處理本機媒體：`50` 個。

### 批次統計

| 項目 | 數字 |
|---|---:|
| 本機媒體檔案 | 50 |
| 以 SHA-256／EXIF 對應到 manifest | 40 |
| 已上架 | 40 |
| 本機有但沒上架 | 0 |
| 本機未能直接對應 manifest | 10 |

本批 40 個可對應項目全部在 `baikal.html` 找到對應路徑。10 個未能直接對應的檔案中，5 個是影片 poster，5 個是影片檔；影片卡片的 `<video src>` 均已在 HTML 中引用，不能據此判定為 Drive 缺檔。

### 本批未能直接對應 manifest 的本機素材

以下素材均已在 HTML 引用；poster 是影片卡片的背景縮圖，影片則沒有可靠的可比對 EXIF：

- `day05/mongolian-scenery-poster.jpg`
- `day05/mongolian-scenery.mp4`
- `day05/zaisan-memorial-poster.jpg`
- `day05/zaisan-memorial-video.mp4`
- `day06/angara-river-video-poster.jpg`
- `day06/angara-river-video.mp4`
- `day07/buryat-dance-poster.jpg`
- `day07/buryat-dance-video.mp4`
- `day07/buryat-singing-poster.jpg`
- `day07/buryat-singing-video.mp4`

### 依 manifest 群組統計

| drive_group | 對應網站區段 | 本批找到本機對應 | 已上架 | 本機有但沒上架 |
|---|---|---:|---:|---:|
| 0806 | Day04 | 1 | 1 | 0 |
| 0807 | Day05 | 16 | 16 | 0 |
| 0808 | Day06 | 9 | 9 | 0 |
| Food | Food 池 | 4 | 4 | 0 |
| Train | Train 池 | 10 | 10 | 0 |

---

## 批次 03：第 101–200 個媒體檔案

稽核日期：2026-09-16  
批次狀態：已完成，仍不是 380 筆完整稽核結果。

### 批次範圍

- 排序規則與前兩批相同：依 `baikal-rail` 媒體檔案相對路徑字典序排序。
- 範圍：`day07/buryat-village-carving.jpg` 至 `day11/ram-rotary-snowplow.jpg`。
- 本批共處理本機媒體：`100` 個。
- 所有 SHA-256 與 EXIF 比對在單一背景 Python 程序內完成；終端機只輸出最後統計，未輸出逐檔中間資料。

### 批次統計

| 項目 | 數字 |
|---|---:|
| 本機媒體檔案 | 100 |
| 以 SHA-256／EXIF 對應到 manifest | 74 |
| 已上架 | 74 |
| 本機有但沒上架 | 0 |
| 本機未能直接對應 manifest | 26 |
| 其中：已上架但無可靠 EXIF 的影片 | 13 |
| 其中：影片 poster 衍生素材 | 13 |

### 依 manifest 群組統計

| drive_group | 對應網站區段 | 本批找到本機對應 | 已上架 | 本機有但沒上架 |
|---|---|---:|---:|---:|
| 0809 | Day07 | 6 | 6 | 0 |
| 0810 | Day08 | 11 | 11 | 0 |
| 0811 | Day09 | 12 | 12 | 0 |
| 0812 | Day10 | 10 | 10 | 0 |
| 0813 | Day11 | 15 | 15 | 0 |
| Food | Food 池 | 8 | 8 | 0 |
| Train | Train 池 | 12 | 12 | 0 |

### 本批已上架但無可靠 EXIF 的影片

以下 13 個影片檔的 HTML `<video src>` 均存在；其 EXIF 只有空值／零時間，依任務規格按已上架影片處理：

- `day07/cabin-video.mp4`
- `day07/jeep-ride-video.mp4`
- `day07/kazanskaya-church-video.mp4`
- `day07/shaman-ritual-video.mp4`
- `day08/baikal-ferry-gradient-video.mp4`
- `day08/baikal-seal-video.mp4`
- `day08/baikal-sunset-video.mp4`
- `day08/olkhon-morning-view-video.mp4`
- `day09/kirov-square-video.mp4`
- `day10/siberia-countryside-video.mp4`
- `day10/siberia-train-continue.mp4`
- `day11/fd20-steam-locomotive-video.mp4`
- `day11/polar-zoo-video.mp4`

### 本批影片 poster 衍生素材

以下 13 個檔案是上述影片卡片的 poster 背景圖，均已在 HTML 的 `background-image:url(...)` 引用，但沒有獨立的 SHA-256／EXIF manifest 對應；不列為 Drive 缺檔：

- `day07/cabin-video-poster.jpg`
- `day07/jeep-ride-poster.jpg`
- `day07/kazanskaya-church-video-poster.jpg`
- `day07/shaman-ritual-poster.jpg`
- `day08/baikal-ferry-gradient-poster.jpg`
- `day08/baikal-seal-poster.jpg`
- `day08/baikal-sunset-video-poster.jpg`
- `day08/olkhon-morning-view-poster.jpg`
- `day09/kirov-square-poster.jpg`
- `day10/siberia-countryside-poster.jpg`
- `day10/siberia-train-continue-poster.jpg`
- `day11/fd20-steam-locomotive-poster.jpg`
- `day11/polar-zoo-poster.jpg`

---

## 分批進度

| 批次 | 本機媒體範圍 | 處理數 | manifest 對應且已上架 | 本機有但沒上架 | 衍生／特殊素材 |
|---|---|---:|---:|---:|---:|
| 01 | 1–50 | 50 | 40 | 1 | 9 |
| 02 | 51–100 | 50 | 40 | 0 | 10 |
| 03 | 101–200 | 100 | 74 | 0 | 26 |
| **累計** | **1–200** | **200** | **154** | **1** | **45** |

此為批次 03 當下的中途狀態：當時尚未完成 Day12–Day20 與後續 manifest 項目，因此尚未判定完整 380 筆 manifest 的「本機完全找不到」清單。最終完整結論見文末「最終完整稽核總結：manifest 380 筆」。

---

## 批次 04：manifest 第 251–300 筆

稽核日期：2026-09-16  
批次狀態：已完成，仍不是 380 筆完整稽核結果。

### 批次範圍

- 對象：`drive_traveler_photo_manifest.json` 的 `files[250:300]`，即第 251–300 筆。
- `drive_group` 範圍：`0818`（Day16）、`0819`（Day17）、`0820`（Day18）。
- 僅使用本機 `lvhun/photos/baikal-rail/`、`lvhun/vol1/baikal.html` 與已匯出的 manifest；未執行同步腳本，未連線 Google Drive 或其他雲端服務。
- 先以 SHA-256 比對；無 SHA-256 命中時，以 `exiftool` 讀取本機 EXIF，正規化後按同秒／同分鐘比對。
- 對應成功後，以本機相對路徑檢查 `<img src>`、`<video src>` 或 CSS `background-image:url(...)` 是否出現在 `baikal.html`。

### 批次統計

| 項目 | 數字 |
|---|---:|
| manifest 檔案 | 50 |
| SHA-256／EXIF 對應到本機 | 41 |
| 已上架 | 41 |
| 本機有但沒上架 | 0 |
| 本機完全找不到對應檔案 | 9 |

### 依 manifest 群組統計

| drive_group | 對應網站區段 | 總數 | 已上架 | 本機有但沒上架 | 本機找不到 |
|---|---|---:|---:|---:|---:|
| 0818 | Day16 | 15 | 10 | 0 | 5 |
| 0819 | Day17 | 30 | 26 | 0 | 4 |
| 0820 | Day18 | 5 | 5 | 0 | 0 |
| **本批合計** |  | **50** | **41** | **0** | **9** |

### 本機完全找不到對應檔案

以下 9 筆是本批實際以 manifest 項目核對後，在 `lvhun/photos/baikal-rail/` 找不到 SHA-256 命中，也找不到 EXIF 同秒／同分鐘命中的本機檔案：

#### 0818（Day16）

- `VID_20260818_145058.mp4`
- `VID_20260818_164733.mp4`
- `VID_20260818_161049.mp4`
- `VID_20260818_143307.mp4`
- `VID_20260818_162520.mp4`

#### 0819（Day17）

- `VID_20260819_203108 (1).mp4`
- `VID_20260819_200237 (1).mp4`
- `VID_20260819_174616 (1).mp4`
- `VID_20260819_151238 (1).mp4`

### 本批本機有但沒上架

本批：**0 筆**。

第 251–300 筆中，所有成功以 SHA-256／EXIF 對應到本機的 41 筆，其本機路徑均可在 `lvhun/vol1/baikal.html` 找到引用。上述 9 筆未對應項目沒有本機路徑，因此不列入「本機有但沒上架」。

### 本批上架對應摘要

- `0818`：10 筆已上架；本機找不到 5 筆。
- `0819`：26 筆已上架；本機找不到 4 筆。
- `0820`：5 筆已上架；本機找不到 0 筆。

此為批次 04 當下的中途狀態：本批完成時已落檔的批次進度為第 1–200 筆，加上本批第 251–300 筆；第 201–250 筆及第 301–380 筆當時仍未在本報告中完成正式批次紀錄。後續已補齊，最終完整結論見文末「最終完整稽核總結：manifest 380 筆」。

---

## 批次 04A：manifest 第 201–250 筆補錄

稽核日期：2026-09-16  
批次狀態：已完成，仍不是 380 筆完整稽核結果。

### 批次範圍

- 對象：`drive_traveler_photo_manifest.json` 的 `files[200:250]`，即第 201–250 筆。
- `drive_group` 範圍：`0816`（Day14）、`0817`（Day15）、`0818`（Day16）。
- 僅使用本機 `lvhun/photos/baikal-rail/`、`lvhun/vol1/baikal.html` 與已匯出的 manifest；未執行同步腳本，未連線 Google Drive 或其他雲端服務。
- 比對規則同批次 04：先 SHA-256，未命中再用本機 EXIF 同秒／同分鐘比對，成功後檢查本機相對路徑是否出現在 `baikal.html`。

### 批次統計

| 項目 | 數字 |
|---|---:|
| manifest 檔案 | 50 |
| SHA-256／EXIF 對應到本機 | 40 |
| 已上架 | 40 |
| 本機有但沒上架 | 0 |
| 本機完全找不到對應檔案 | 10 |

### 依 manifest 群組統計

| drive_group | 對應網站區段 | 總數 | 已上架 | 本機有但沒上架 | 本機找不到 |
|---|---|---:|---:|---:|---:|
| 0816 | Day14 | 2 | 2 | 0 | 0 |
| 0817 | Day15 | 40 | 32 | 0 | 8 |
| 0818 | Day16 | 8 | 6 | 0 | 2 |
| **本批合計** |  | **50** | **40** | **0** | **10** |

### 本機完全找不到對應檔案

#### 0817（Day15）

- `VID_20260817_225915.mp4`
- `VID_20260817_161532.mp4`
- `VID_20260817_203553.mp4`
- `VID_20260817_170427_1.mp4`
- `VID_20260817_213747.mp4`
- `VID_20260817_214222.mp4`
- `VID_20260817_161847.mp4`
- `VID_20260817_223749.mp4`

#### 0818（Day16）

- `VID_20260818_144038.mp4`
- `VID_20260818_164507_1.mp4`

### 本批本機有但沒上架

本批：**0 筆**。

---

## 批次 05：manifest 第 301–350 筆

稽核日期：2026-09-16  
批次狀態：已完成，仍不是 380 筆完整稽核結果。

### 批次範圍

- 對象：`drive_traveler_photo_manifest.json` 的 `files[300:350]`，即第 301–350 筆。
- `drive_group` 範圍：`0820`（Day18）、`0821`（Day19）、`Food`。
- 僅使用本機 `lvhun/photos/baikal-rail/`、`lvhun/vol1/baikal.html` 與已匯出的 manifest；未執行同步腳本，未連線 Google Drive 或其他雲端服務。

### 批次統計

| 項目 | 數字 |
|---|---:|
| manifest 檔案 | 50 |
| SHA-256／EXIF 對應到本機 | 49 |
| 已上架 | 49 |
| 本機有但沒上架 | 0 |
| 本機完全找不到對應檔案 | 1 |

### 依 manifest 群組統計

| drive_group | 對應網站區段 | 總數 | 已上架 | 本機有但沒上架 | 本機找不到 |
|---|---|---:|---:|---:|---:|
| 0820 | Day18 | 22 | 21 | 0 | 1 |
| 0821 | Day19 | 6 | 6 | 0 | 0 |
| Food | Food 池 | 22 | 22 | 0 | 0 |
| **本批合計** |  | **50** | **49** | **0** | **1** |

### 本機完全找不到對應檔案

#### 0820（Day18）

- `VID_20260820_202454.mp4`

### 本批本機有但沒上架

本批：**0 筆**。

---

## 批次 06：manifest 第 351–380 筆

稽核日期：2026-09-16  
批次狀態：已完成；manifest 第 201–380 筆缺口已全部補齊。

### 批次範圍

- 對象：`drive_traveler_photo_manifest.json` 的 `files[350:380]`，即第 351–380 筆。
- `drive_group` 範圍：`Food`、`Train`。
- 僅使用本機 `lvhun/photos/baikal-rail/`、`lvhun/vol1/baikal.html` 與已匯出的 manifest；未執行同步腳本，未連線 Google Drive 或其他雲端服務。

### 批次統計

| 項目 | 數字 |
|---|---:|
| manifest 檔案 | 30 |
| SHA-256／EXIF 對應到本機 | 30 |
| 已上架 | 30 |
| 本機有但沒上架 | 0 |
| 本機完全找不到對應檔案 | 0 |

### 依 manifest 群組統計

| drive_group | 對應網站區段 | 總數 | 已上架 | 本機有但沒上架 | 本機找不到 |
|---|---|---:|---:|---:|---:|
| Food | Food 池 | 7 | 7 | 0 | 0 |
| Train | Train 池 | 23 | 23 | 0 | 0 |
| **本批合計** |  | **30** | **30** | **0** | **0** |

### 本批本機完全找不到對應檔案

本批：**0 筆**。

### 本批本機有但沒上架

本批：**0 筆**。

---

## 最終完整稽核總結：manifest 380 筆

稽核日期：2026-09-16  
狀態：完整覆蓋 `drive_traveler_photo_manifest.json` 共 380 筆。

### 總體結論

| 項目 | 數字 |
|---|---:|
| manifest 總數 | 380 |
| 本機有檔案且已上架 | 337 |
| 本機有檔案但沒上架 | 1 |
| 本機完全找不到對應檔案 | 42 |

### 依 drive_group 完整統計

| drive_group | 對應網站區段 | 總數 | 本機有檔案且已上架 | 本機有但沒上架 | 本機找不到 |
|---|---|---:|---:|---:|---:|
| 0803 | Day01 | 5 | 5 | 0 | 0 |
| 0804 | Day02 | 12 | 11 | 0 | 1 |
| 0805 | Day03 | 18 | 12 | 0 | 6 |
| 0806 | Day04 | 12 | 8 | 1 | 3 |
| 0807 | Day05 | 18 | 16 | 0 | 2 |
| 0808 | Day06 | 10 | 9 | 0 | 1 |
| 0809 | Day07 | 12 | 6 | 0 | 6 |
| 0810 | Day08 | 15 | 11 | 0 | 4 |
| 0811 | Day09 | 13 | 12 | 0 | 1 |
| 0812 | Day10 | 12 | 10 | 0 | 2 |
| 0813 | Day11 | 23 | 21 | 0 | 2 |
| 0814 | Day12 | 16 | 14 | 0 | 2 |
| 0815 | Day13 | 16 | 14 | 0 | 2 |
| 0816 | Day14 | 20 | 17 | 0 | 3 |
| 0817 | Day15 | 40 | 32 | 0 | 8 |
| 0818 | Day16 | 23 | 16 | 0 | 7 |
| 0819 | Day17 | 30 | 26 | 0 | 4 |
| 0820 | Day18 | 27 | 26 | 0 | 1 |
| 0821 | Day19 | 6 | 6 | 0 | 0 |
| 0822 | Day20 | 0 | 0 | 0 | 0 |
| Food | Food 池 | 29 | 29 | 0 | 0 |
| Train | Train 池 | 23 | 23 | 0 | 0 |
| **合計** |  | **380** | **337** | **1** | **42** |

註：`drive_traveler_photo_manifest.json` 本次匯出的 380 筆中沒有 `0822`（Day20）項目，因此 Day20 以 0 筆列示。

### 本機有檔案但沒上架

#### 0806（Day04）

- `IMG20260806185306.jpg`

### 本機完全找不到對應檔案

#### 0804（Day02）

- `VID_20260804_174231.mp4`

#### 0805（Day03）

- `VID_20260805_113358_1.mp4`
- `VID20260805200046.mp4`
- `VID_20260805_201428.mp4`
- `VID_20260805_104514.mp4`
- `VID20260805125359.mp4`
- `VID_20260805_180333.mp4`

#### 0806（Day04）

- `VID20260806204753.mp4`
- `IMG_20260806_153109.jpg`
- `VID20260806200147.mp4`

#### 0807（Day05）

- `VID_20260807_172824.mp4`
- `VID20260807091253.mp4`

#### 0808（Day06）

- `VID20260808184850.mp4`

#### 0809（Day07）

- `VID20260809100501.mp4`
- `VID20260809184004.mp4`
- `VID_20260809_121337.mp4`
- `VID20260809174706.mp4`
- `VID20260809173622.mp4`
- `VID20260809120108.mp4`

#### 0810（Day08）

- `VID_20260810_200629_1.mp4`
- `VID_20260810_070743.mp4`
- `VID_20260810_092648.mp4`
- `VID_20260810_183254.mp4`

#### 0811（Day09）

- `VID_20260811_173531.mp4`

#### 0812（Day10）

- `VID_20260812_203451.mp4`
- `VID_20260812_202100.mp4`

#### 0813（Day11）

- `VID_20260813_133743.mp4`
- `VID_20260813_175432.mp4`

#### 0814（Day12）

- `VID_20260814_211600.mp4`
- `VID_20260814_205910.mp4`

#### 0815（Day13）

- `VID_20260815_182356_1.mp4`
- `VID_20260815_134506.mp4`

#### 0816（Day14）

- `VID_20260816_162204.mp4`
- `VID_20260817_013246.mp4`
- `VID20260816152923.mp4`

#### 0817（Day15）

- `VID_20260817_225915.mp4`
- `VID_20260817_161532.mp4`
- `VID_20260817_203553.mp4`
- `VID_20260817_170427_1.mp4`
- `VID_20260817_213747.mp4`
- `VID_20260817_214222.mp4`
- `VID_20260817_161847.mp4`
- `VID_20260817_223749.mp4`

#### 0818（Day16）

- `VID_20260818_144038.mp4`
- `VID_20260818_164507_1.mp4`
- `VID_20260818_145058.mp4`
- `VID_20260818_164733.mp4`
- `VID_20260818_161049.mp4`
- `VID_20260818_143307.mp4`
- `VID_20260818_162520.mp4`

#### 0819（Day17）

- `VID_20260819_203108 (1).mp4`
- `VID_20260819_200237 (1).mp4`
- `VID_20260819_174616 (1).mp4`
- `VID_20260819_151238 (1).mp4`

#### 0820（Day18）

- `VID_20260820_202454.mp4`

#### 0803、0821、0822、Food、Train

本機完全找不到：**0 筆**。

### 稽核限制與交付狀態

- 本報告只使用本機 `drive_traveler_photo_manifest.json`、`lvhun/photos/baikal-rail/` 與 `lvhun/vol1/baikal.html`。
- 未執行 `sync_baikal_photos.py`。
- 未嘗試連線 Google Drive 或任何雲端服務。
- 未修改 `lvhun/vol1/baikal.html`、`lvhun/photos/`、`photos/destination-preview/` 或 manifest。
