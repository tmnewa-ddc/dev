## Code Rule of Machine Learning

程式類別與檔案格式，主要是大方向，實作的部分再各自努力

### 基礎架構

* 檔案架構
  * main.py（操作腳本)
  * DataMeta.py (資料元)
  * DataModel.py（資料模組)
  * Pipfile (使用模組紀錄，可以透過pipenv操作)
  * config/: 設定參數
  * run/ (操作細節，若需要)
  * src/ (程式相關)
    * pp/: 資料前處理
    * model/: 演算法邏輯
  * file/ (資料相關) git只紀錄資料夾結構或非敏感範例檔(*.eg)
    * origin: 原始資料，模型的主要素材；若是 excel，請先轉成 csv/txt
    * ref: 參考資料，像是代碼表之類的東西；若是 excel，請先轉成 csv/txt
    * input: 模型輸入資料
    * train: 模型相關資料


參考 [dev-mlRule]


### 初始階段

在 DataMeta.py 制定一個 DataMeta dataclasses 包含 **演算法邏輯/原始資料/參考資料** 的屬性，並記錄演算法邏輯及其對應的資料項目


* DataMeta: dataclasses，初始化資料規範
  * 屬性: 
    * alg: 指定要使用哪一個演算法邏輯
    * org: 原始資料項目(名稱, 對應的範例檔名)
    * ref: 參考資料項目(名稱, 對應的範例檔名)
    * org_x: 簡化的原始資料項目，只為了產出X（若為None，直接參考 org)
    * ref_x: 簡化的參考資料項目，只為了產出X（若為None，直接參考 ref)
* ALG_{NAME}: int，用來記錄演算法邏輯
* META_{NAME}: DataMeta，用來記錄資料元


在 DataModel.py 制定一個 DataModel Class 包含 **預備/訓練/驗證/預測** 的程式介面


* DataModel(meta: DataMeta): Class，初始化使用模型
  * 參數:
    * **meta**: 指定要使用哪一個資料元(演算法邏輯/原始資料/參考資料)
  * 屬性: 
    * __meta: 用來記錄初始化參數meta
    * __model: 用來記錄選定的模型邏輯
  * 方法:
    * prepare: 原始資料轉換成輸入資料的前處理
    * train: 利用輸入資料(X, Y)，訓練出模型/中繼資料
    * load / loadPath: 讀取模型/中繼資料
    * predict: 利用輸入資料(X)，預測結果(Y)
    * validate: 驗證


### 資料處理

根據不同的 *__meta.alg* 跟 *cate* 可能會有不同的 *refs*/*origins*

* 方法
  * prepare(cate, origins, refs, save) -> X, Y
    * **cate** *(int)*: 使用目的
      * 0: 訓練用, x有值, y有值
      * 1: 預測用, x有值, y為None
    * origins *(dict)*: 原始資料
    * refs *(dict)*: 參考資料
    * save *(bool)*: 儲存資料夾路徑，None為不儲存，預設為file/input
    * X *(pd.DataFrame)*: 自變數
    * Y *(pd.DataFrame)*: 應變數
* 檔案
  * {save}/{alg}_{cate}_ppX.parq: 自變數的檔案
  * {save}/{alg}_{cate}_ppY.parq: 應變數的檔案


### 模型訓練

註解處稍微條列一下 模型/中繼資料 各紀錄了什麼

* 方法
  * train(X, Y, save) -> modelData, pipeData
    * X *(pd.DataFrame)*: 自變數
    * Y *(pd.DataFrame)*: 應變數
    * save *(bool)*: 儲存資料夾路徑，None為不儲存，預設為file/train
    * modelData: 模型資料
    * pipeData: 中繼資料
* 檔案
  * {save}/{alg}_modelData.pickle: 模型資料檔案
  * {save}/{alg}_pipeData.pickle: 中繼資料檔案


### 模型載入

* 方法
  * load(modelData, pipeData)
    * modelData: 模型資料
    * pipeData: 中繼資料
  * loadPath(modelPath, pipePath)
    * modelData: 模型資料檔案路徑
    * pipeData: 中繼資料檔案路徑


### 模型預測

需要先有模型/中繼資料，透過訓練或載入取得

* 方法
  * predict(X, save) -> Y
    * X *(pd.DataFrame)*: 自變數
    * save *(bool)*: 儲存資料夾路徑，None為不儲存，預設為file/train
* 檔案
  *  {save}/{alg}_pdY.parq: 預測資料


### 模型驗證

需要先有模型/中繼資料，透過訓練或載入取得

* 方法
  * validate(X, Y) -> scores
    * X *(pd.DataFrame)*: 自變數
    * Y *(pd.DataFrame)*: 應變數
    * scores: 驗證結果


[dev-mlRule]: https://github.com/tmnewa-ddc/dev-mlRule  "code rule of ml"