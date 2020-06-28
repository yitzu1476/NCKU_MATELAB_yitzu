# How to Mask R-CNN
資料來源：https://github.com/matterport/Mask_RCNN

## Test
可使用 `Mask_RCNN/samples/demo.ipynb` 進行測試<br>
如有錯誤, 參見環境建置錯誤修復章節<br>

## To Train Custom Database
可使用 `Mask_RCNN/samples/training_red_pyramid.py` 訓練自製資料庫<br>
檔案有部分程式碼需修改, 詳細行數及內容如下：<br>
1.  `#54` <br>
    ```python
    NUM_CLASSES = 1 + '欲訓練資料庫之目標物數量'
    ```
2.  `#122` <br>
    ```python
    self.add_class("shapes", 1, "目標物名稱 ")
    ```
    可自行增加目標物<br>
3.  `#162` <br>
    ```python
    if labels[i].find("目標物名稱 ") != -1
    ```
4.  `#163` <br>
    ```python
    labels_form.append("目標物名稱 ")
    ```
    若增加目標物, 可於 `#163` 之後增加<br>
    ```python
    elif labels[i].find("目標物名稱2") != -1:
      labels_form.append("目標物名稱2")
    ```
5.  `#182` <br>
    此為訓練用資料夾位置<br>
    ```python
    dataset_root_path = "training_data/訓練用資料夾名稱/"
    ```

## To Build Training Database
訓練自製資料庫前, 須先建立訓練用資料夾。<br>
參考資料：https://tn00343140a.pixnet.net/blog/post/319064126-mask-rcnn%E4%BD%BF%E7%94%A8%E7%AF%87
1.  建立環境<br>
    利用 `Command Prompt` 或者 `Anaconda Prompt` 建立<br>
    ```python
    > conda create --name=labelme
    > activate labelme
    > pip install labelme==3.10.0
    > deacticate
    ```
2.  測試是否安裝成功<br>
    利用 `Command Prompt` 或者 `Anaconda Prompt` 輸入：<br>
    ```python
    > labelme
    ```
    若成功開啟視窗則安裝成功。<br>
3.  建立資料夾<br>
    * 根據參考資料中之步驟建立訓練用資料夾, 將資料夾存放於 `Mask_RCNN/samples/training_data/建立之資料夾`<br>
    資料夾中應有 `cv2_mask` 、 `json` 、 `label_json` 、 `pic` 四個資料夾<br>
    如 `Mask_RCNN/samples/training_data/red_pyramid_training_data` 範例。<br>
    * 若欲使用 `Mask_RCNN/samples/training_data/red_pyramid_training_data` 進行測試, 需先將 `red_pyramid_training_data/labelme_json` 中之 `labelme_json.rar` 解壓縮, 形成 `red_pyramid_training_data/01_json` 、 `red_pyramid_training_data/02_json` ...等多個資料夾。<br>
    資料夾建立完成即可使用 `To Train Custom Database` 步驟進行訓練。

## To Test Custom Database
* 完成自製資料庫訓練, 可使用 `Mask_RCNN/samples/balloon/red_pyramid_detection.py` 測試<br>
內容有部分需要更改, 已標示於 `Mask_RCNN/samples/balloon/red_pyramid_detection.py` 檔案內部。<br>
自行訓練之資料庫訓練結果會存於 `Mask_RCNN/samples/logs/` 中之最新資料夾, 欲使用, 需將資料夾最後一訓練權重 `(通常名為 mask_rcnn_shapes_0040.h5)` 移至 `Mask_RCNN/logs/`中。<br>
* 部分已訓練之權重資料可於 https://drive.google.com/drive/folders/1XXj5kIRH6lV4Ljy6PhTljwZ0JIphIVMF?usp=sharing 中下載, 下載後之資料應置於 `Mask_RCNN/logs/` 中, 如下範例；<br>
```
> Mask_RCNN/logs/
>> case__blue_pyramid_database/
>>> mask_rcnn_shapes_0040.h5
>> case_red_pyramid_database/
>>> mask_rcnn_shapes_0040.h5
```

## Addition Function
1.  本版本之 `Mask_RCNN/mrcnn/visualize.py` 檔案中有增加一副程式： `display_instances_save` , 其參數如下<br>
    ```python
    def display_instances_save(image, boxes, masks, class_ids, class_names,
        scores=None, title="", figsize=(16, 16), ax=None,
        show_mask=True, show_bbox=True, colors=None, captions=None, save_dir=None, boxwidth=2, textsize=11):
    ```
    增加辨識結果圖片儲存位置 `save_dir` , 及辨識結果外框及百分比數字大小 `boxwidth` 、 `textsize` , 可應用於辨識程式最後之顯示步驟。<br>
2.  config參數設定<br>
    辨識程式中
