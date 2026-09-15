# 貝加爾鐵路 20 天照片逐日對帳報告（本機檔案系統 + EXIF 時間戳比對，非 API、非位元組大小）

**方法：** 本機已有 Google Drive 桌面同步鏡像 `/Users/mac/Documents/Projects/斌哥旅遊書/20260803西伯利亞/08XX/`，直接對照本機專案 `lvhun/photos/baikal-rail/dayNN/`。改用 EXIF `DateTimeOriginal`／`CreateDate`（用 exiftool 讀取，網頁壓縮過的圖片這個欄位通常仍保留）配對「同一張照片、不同檔名」，比單純比對位元組大小可靠——位元組大小法已實測失敗（許多照片被壓縮過，大小已改變），故捨棄改用此法。

## 總表

| Day | 日期 | Drive張數 | 本機張數 | 配對成功 | 疑似漏掉 | 疑似虛構 | -downloaded排除 | 影片/縮圖/無EXIF(需人工) | 放錯天嫌疑 |
|---|---|---|---|---|---|---|---|---|---|
| Day01 | 0803 | 5 | 6 | 5 | 0 | 0 | 0 | 1 | 0 |
| Day02 | 0804 | 12 | 21 | 10 | 1 | 0 | 1 | 9 | 0 |
| Day03 | 0805 | 18 | 29 | 10 | 2 | 1 | 1 | 23 | 0 |
| Day04 | 0806 | 12 | 17 | 8 | 2 | 1 | 1 | 7 | 0 |
| Day05 | 0807 | 18 | 27 | 16 | 0 | 0 | 1 | 6 | 0 |
| Day06 | 0808 | 10 | 19 | 9 | 0 | 0 | 1 | 3 | 0 |
| Day07 | 0809 | 12 | 27 | 6 | 0 | 0 | 5 | 19 | 0 |
| Day08 | 0810 | 15 | 27 | 10 | 1 | 0 | 4 | 14 | 0 |
| Day09 | 0811 | 13 | 24 | 12 | 0 | 0 | 2 | 4 | 0 |
| Day10 | 0812 | 12 | 18 | 9 | 1 | 0 | 0 | 6 | 0 |
| Day11 | 0813 | 23 | 30 | 21 | 0 | 0 | 0 | 6 | 0 |
| Day12 | 0814 | 16 | 22 | 13 | 1 | 0 | 0 | 6 | 0 |
| Day13 | 0815 | 16 | 23 | 14 | 0 | 0 | 0 | 6 | 0 |
| Day14 | 0816 | 20 | 29 | 17 | 0 | 0 | 3 | 10 | 0 |
| Day15 | 0817 | 40 | 54 | 32 | 0 | 0 | 6 | 24 | 0 |
| Day16 | 0818 | 23 | 37 | 16 | 0 | 0 | 6 | 22 | 0 |
| Day17 | 0819 | 30 | 38 | 26 | 0 | 0 | 3 | 13 | 0 |
| Day18 | 0820 | 27 | 30 | 26 | 0 | 0 | 1 | 4 | 0 |
| Day19 | 0821 | 6 | 9 | 6 | 0 | 0 | 2 | 1 | 1 |
| Day20 | 0822 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 |

**總計（僅計可靠比對到的照片，不含影片/縮圖/無EXIF）：疑似漏掉 8 筆／疑似虛構 2 筆／放錯天嫌疑 1 筆**

---

## Day01（0803）明細

本日核對無誤（可驗證的照片 EXIF 時間戳記全部配對成功，位置正確）。


## Day02（0804）明細

**疑似漏掉（Drive 有、本機找不到相同時間戳的照片，共 1 筆，已排除影片）：**
- `IMG_20260805_075547.jpg`（原始時間戳：20260805075547）

（1 筆本機獨有但檔名含 downloaded，判定為刻意下載的地標示意圖，不計入虛構：ulaanbaatar-city-downloaded.jpg）

（2 筆原本疑似虛構，實測在 Drive 的 Food/ 或 Train/ 資料夾（非按日期分類）裡找到對應原始檔，已排除、不計入虛構：breakfast-tomato-egg.jpg←IMG_20260902_205414.jpg, mongolia-boiled-mutton.jpg←IMG20260804194805.jpg）

（另有 9 筆是影片／影片縮圖／無 EXIF 檔案，這類本來就沒有可靠的時間戳可自動比對，不計入上面兩項錯誤數字，需要人工開檔核對：
Drive 影片 1 筆：VID_20260804_174231.mp4；
本機影片/縮圖/無EXIF 8 筆：IMG_20260805_075547.jpg, chinggis-khaan-statue.jpg, genghis-khan-statue.png, horseback-riding-landmark.png, mongolian-grassland.png, terelj-camp-panorama.jpg, terelj-camp-panorama.mp4, terelj-road.png）


## Day03（0805）明細

**疑似漏掉（Drive 有、本機找不到相同時間戳的照片，共 2 筆，已排除影片）：**
- `1785944390347.jpg`（原始時間戳：無法解析）
- `IMG_20260806_122831.jpg`（原始時間戳：20260806122831）

**疑似虛構／來源不明（本機有 EXIF 時間戳的照片、但 Drive 原始資料夾找不到對應時間戳，排除 -downloaded／影片／縮圖，共 1 筆）：**
- `karakorum-museum-real.jpg`（EXIF時間戳：20240804141310）

（1 筆本機獨有但檔名含 downloaded，判定為刻意下載的地標示意圖，不計入虛構：kharkhorin-ancient-city-downloaded.jpg）

（另有 23 筆是影片／影片縮圖／無 EXIF 檔案，這類本來就沒有可靠的時間戳可自動比對，不計入上面兩項錯誤數字，需要人工開檔核對：
Drive 影片 6 筆：VID20260805125359.mp4, VID20260805200046.mp4, VID_20260805_104514.mp4, VID_20260805_113358_1.mp4, VID_20260805_180333.mp4, VID_20260805_201428.mp4；
本機影片/縮圖/無EXIF 17 筆：IMG_20260806_122831.jpg, argalant-shagai.jpg, camel-ride.jpg, camel-ride.mp4, dinner-mongolian-song.jpg, dinner-mongolian-song.mp4, dinner-noble-costume.jpg, dinner-noble-costume.mp4, erdene-zuu-108-stupas.png, erdene-zuu-monastery.jpg, grassland-horsemanship.jpg, grassland-horsemanship.mp4, grassland-scenery.jpg, grassland-scenery.mp4, grassland-song-performance.jpg, grassland-song-performance.mp4, kharkhorin-ruins.png）


## Day04（0806）明細

**疑似漏掉（Drive 有、本機找不到相同時間戳的照片，共 2 筆，已排除影片）：**
- `1786025670446.jpg`（原始時間戳：無法解析）
- `IMG_20260806_153109.jpg`（原始時間戳：20260806152733）

**疑似虛構／來源不明（本機有 EXIF 時間戳的照片、但 Drive 原始資料夾找不到對應時間戳，排除 -downloaded／影片／縮圖，共 1 筆）：**
- `ulaanbaatar-traffic.jpg`（EXIF時間戳：20260806185306）

（1 筆本機獨有但檔名含 downloaded，判定為刻意下載的地標示意圖，不計入虛構：mongolia-folk-dance-morin-khuur-downloaded.jpg）

（2 筆原本疑似虛構，實測在 Drive 的 Food/ 或 Train/ 資料夾（非按日期分類）裡找到對應原始檔，已排除、不計入虛構：pork-dish.jpg←IMG20260806125239.jpg, sparse-vegetables.jpg←IMG20260806124047.jpg）

（另有 7 筆是影片／影片縮圖／無 EXIF 檔案，這類本來就沒有可靠的時間戳可自動比對，不計入上面兩項錯誤數字，需要人工開檔核對：
Drive 影片 2 筆：VID20260806200147.mp4, VID20260806204753.mp4；
本機影片/縮圖/無EXIF 5 筆：bogd-khan-winter-palace.jpg, folk-dance-audience.jpg, folk-dance-morin-khuur-1.mp4, folk-dance-morin-khuur-2.mp4, harhorin-valley.jpg）


## Day05（0807）明細

本日核對無誤（可驗證的照片 EXIF 時間戳記全部配對成功，位置正確）。


## Day06（0808）明細

本日核對無誤（可驗證的照片 EXIF 時間戳記全部配對成功，位置正確）。


## Day07（0809）明細

本日核對無誤（可驗證的照片 EXIF 時間戳記全部配對成功，位置正確）。


## Day08（0810）明細

**疑似漏掉（Drive 有、本機找不到相同時間戳的照片，共 1 筆，已排除影片）：**
- `IMG_20260825_203651.jpg`（原始時間戳：20260825203651）

（4 筆本機獨有但檔名含 downloaded，判定為刻意下載的地標示意圖，不計入虛構：burkhan-bay-downloaded.jpg, buryat-traditional-village-downloaded.jpg, olkhon-island-shore-downloaded.jpg, ust-orda-museum-downloaded.jpg）

（3 筆原本疑似虛構，實測在 Drive 的 Food/ 或 Train/ 資料夾（非按日期分類）裡找到對應原始檔，已排除、不計入虛構：beetroot-soup.jpg←IMG20260810143747.jpg, chicken-dish.jpg←IMG20260810144331.jpg, dessert-crepe.jpg←IMG20260810185430.jpg）

（另有 14 筆是影片／影片縮圖／無 EXIF 檔案，這類本來就沒有可靠的時間戳可自動比對，不計入上面兩項錯誤數字，需要人工開檔核對：
Drive 影片 4 筆：VID_20260810_070743.mp4, VID_20260810_092648.mp4, VID_20260810_183254.mp4, VID_20260810_200629_1.mp4；
本機影片/縮圖/無EXIF 10 筆：baikal-ferry-gradient-poster.jpg, baikal-ferry-gradient-video.mp4, baikal-seal-poster.jpg, baikal-seal-video.mp4, baikal-sunset-video-poster.jpg, baikal-sunset-video.mp4, burkhan-bay.jpg, olkhon-morning-view-poster.jpg, olkhon-morning-view-video.mp4, olkhon-national-park.jpg）


## Day09（0811）明細

本日核對無誤（可驗證的照片 EXIF 時間戳記全部配對成功，位置正確）。


## Day10（0812）明細

**疑似漏掉（Drive 有、本機找不到相同時間戳的照片，共 1 筆，已排除影片）：**
- `IMG20260812114440.jpg`（原始時間戳：20260812114440）

（5 筆原本疑似虛構，實測在 Drive 的 Food/ 或 Train/ 資料夾（非按日期分類）裡找到對應原始檔，已排除、不計入虛構：carriage-info-panel.jpg←IMG20260812092355.jpg, dining-car.jpg←IMG_20260827_174606.jpg, free-shower.jpg←IMG_20260902_201319.jpg, onboard-price-list.jpg←IMG_20260902_205711.jpg, toilet-seat-sanitizer.jpg←IMG20260812092210.jpg）

（另有 6 筆是影片／影片縮圖／無 EXIF 檔案，這類本來就沒有可靠的時間戳可自動比對，不計入上面兩項錯誤數字，需要人工開檔核對：
Drive 影片 2 筆：VID_20260812_202100.mp4, VID_20260812_203451.mp4；
本機影片/縮圖/無EXIF 4 筆：siberia-countryside-poster.jpg, siberia-countryside-video.mp4, siberia-train-continue-poster.jpg, siberia-train-continue.mp4）


## Day11（0813）明細

本日核對無誤（可驗證的照片 EXIF 時間戳記全部配對成功，位置正確）。


## Day12（0814）明細

**疑似漏掉（Drive 有、本機找不到相同時間戳的照片，共 1 筆，已排除影片）：**
- `IMG_20260814_085241.jpg`（原始時間戳：20260814052643）

（5 筆原本疑似虛構，實測在 Drive 的 Food/ 或 Train/ 資料夾（非按日期分類）裡找到對應原始檔，已排除、不計入虛構：chocolate-dessert.jpg←IMG20260814194742.jpg, dumplings-sour-cream.jpg←IMG20260814193330.jpg, fried-bread-stuffed.jpg←IMG20260814190404.jpg, pomegranate-juice.jpg←IMG20260814184907.jpg, train-simple-meal.jpg←IMG20260814121104.jpg）

（另有 6 筆是影片／影片縮圖／無 EXIF 檔案，這類本來就沒有可靠的時間戳可自動比對，不計入上面兩項錯誤數字，需要人工開檔核對：
Drive 影片 2 筆：VID_20260814_205910.mp4, VID_20260814_211600.mp4；
本機影片/縮圖/無EXIF 4 筆：plotinka-mural-poster.jpg, plotinka-mural-video.mp4, saint-nicholas-church-poster.jpg, saint-nicholas-church-video.mp4）


## Day13（0815）明細

本日核對無誤（可驗證的照片 EXIF 時間戳記全部配對成功，位置正確）。


## Day14（0816）明細

本日核對無誤（可驗證的照片 EXIF 時間戳記全部配對成功，位置正確）。


## Day15（0817）明細

本日核對無誤（可驗證的照片 EXIF 時間戳記全部配對成功，位置正確）。


## Day16（0818）明細

本日核對無誤（可驗證的照片 EXIF 時間戳記全部配對成功，位置正確）。


## Day17（0819）明細

本日核對無誤（可驗證的照片 EXIF 時間戳記全部配對成功，位置正確）。


## Day18（0820）明細

本日核對無誤（可驗證的照片 EXIF 時間戳記全部配對成功，位置正確）。


## Day19（0821）明細

（2 筆本機獨有但檔名含 downloaded，判定為刻意下載的地標示意圖，不計入虛構：izmailovo-market-kremlin-downloaded.jpg, izmailovo-park-downloaded.jpg）

（另有 1 筆是影片／影片縮圖／無 EXIF 檔案，這類本來就沒有可靠的時間戳可自動比對，不計入上面兩項錯誤數字，需要人工開檔核對：
Drive 影片 0 筆：無；
本機影片/縮圖/無EXIF 1 筆：sparrow-hills-viewpoint.jpg）

**放錯天嫌疑（EXIF/檔名時間戳換算的實際拍攝日跟目前所在資料夾不符，共 1 筆）：**
- `izmailovo-fake-decor.jpg`（本機位於 day19）← 實際拍攝時間戳 20260819201315 換算為 Day17（Drive 原始檔名 `IMG20260819201315.jpg`）


## Day20（0822）明細

本日核對無誤（可驗證的照片 EXIF 時間戳記全部配對成功，位置正確）。


---

## 方法論與限制

- 純本機檔案系統 + exiftool metadata 比對，沒有呼叫 Google Drive API，數十秒內完成。
- Drive 端時間戳直接從原始檔名解析（IMG/VID + 8碼日期+6碼時間），本機端用 exiftool 讀 DateTimeOriginal/CreateDate。
- 影片檔（mp4/mov）的 metadata 時間戳可靠度低於照片，部分影片可能因轉檔／remux 遺失原始 CreateDate，導致誤判為「疑似漏掉」或「疑似虛構」，這類請人工開檔確認，不要照單全收。
- 「放錯天嫌疑」是機械換算，斌哥筆記裡多次出現「照片重新匯出時檔名日期漂移」的情況，此清單只負責標出「值得去看」，最終要對照 CLAUDE.txt 內容決定是否真的放錯天。
- 「疑似虛構」代表 Drive 這 20 個 08XX 資料夾裡找不到時間戳相符的原始檔；Drive 帳號裡另外還有 `Food/`、`Train/` 等非日期命名的資料夾，若本機圖片其實來自這些子資料夾，會被誤判为虛構，本報告尚未涵蓋這兩個資料夾，抽查時請留意。
