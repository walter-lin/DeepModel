# DeepModel
彙整有關"類神經網路"的作品

# 操作說明

## 在本機執行

(1)請使用train_model_cnn.py
注意：訓練過程會使用大量運算資源，請務必先進行GPU設定(GPU需依型號安裝驅動程式)

## 在雲端上執行
Google提供的colab，除了支援iPython的格式(就是jupyter所使用的那種)，還有免費提供GPU，適合負擔訓練過程的龐大運算。

1. 請將資料整個打包至Google雲端硬碟 

2. 利用colab開啟train_model_cnn.ipynb(注意附檔名)
---
![ ](/md_image/open1.PNG "圈起來的地方 給他點下去")

---

![ ](/md_image/open2.PNG "配合我精美的提示 給他操作")

---

![ ](/md_image/open3.PNG "大功告成")


## 目錄說明

- trainImg為訓練素材，testImg為測試資料夾 
- 當中0為正確答案，1為錯誤答案
- **dataset.py**已有將資料縮放為固定大小，如欲調整大小請使用此檔案

# Colab操作說明

## 啟動GPU
![ ](/md_image/gpu1.PNG "")
![ ](/md_image/gpu2.PNG "")

## 啟動執行階段
![ ](/md_image/begin1.PNG "")

![ ](/md_image/begin2.PNG "")

## 終止執行階段
![ ](/md_image/end1.PNG "")
![ ](/md_image/end2.PNG "")

## 專案目錄

---

(1)![ ](/md_image/dir1.PNG "")
這裡可以查看目錄

---

(2)![ ](/md_image/dir2.PNG "上傳壓縮檔")
上傳壓縮檔

---
(3)![ ](/md_image/dir3.PNG "解壓縮後")
解壓縮後
