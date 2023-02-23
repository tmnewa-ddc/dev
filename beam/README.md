# Beam Intro

參考 [Beam][beam_url]、[DataFlow][data_flow_url] 的說明

## Pipeline Flow Intro

展示 pipeline 上的資料處理節點如何操作

* Pipeline 
* PCollection
* PTransform

### 合併不同的 PCollections 有兩個做法，可以見 [Design Your Pipeline: Merging PCollections][beam_ppl_intro]:

* Flatten
* Join: 更靈活，在範例展示中


[beam_url]: https://beam.apache.org/ "intro of Beam"
[beam_ppl_intro]: https://beam.apache.org/documentation/pipelines/design-your-pipeline/#merging-pcollections "pipline intro of Bear"
[data_flow_url]: https://cloud.google.com/dataflow/docs/about-dataflow?hl=zh-cn "intro of DataFlow"