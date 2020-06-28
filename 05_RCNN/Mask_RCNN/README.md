# How to Mask R-CNN

## Test
可使用 `Mask_RCNN/samples/demo.ipynb` 進行測試<br>
如有錯誤, 參見環境建置錯誤修復章節<br>

## To Train custom database
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
參考資料：https://tn00343140a.pixnet.net/blog/post/319064126-mask-rcnn%E4%BD%BF%E7%94%A8%E7%AF%87
1.  建立環境
