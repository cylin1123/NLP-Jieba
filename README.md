### Jieba 中文斷字斷詞

### Package
* Jieba
~~~
pip install jieba
~~~
* NLTK
~~~
pip install nltk
~~~
### Import Library
~~~
import jieba
import jieba.analyse as jalz
import jieba.posseg as japseg
~~~

### 使用者定義詞庫 
詞典格式 : 一個詞一行；每一行分三部分：詞語、詞頻（可省略）、詞性（可省略），用空格隔開，順序不可顛倒。
~~~
jieba.load_userdict('user_dict.txt') 
~~~

### 分詞

需要分词的字符串；cut_all 参数用来控制是否采用全模式；HMM 参数用来控制是否使用 HMM 模型

* 精確模式 ：將句子最精確地切開，適合文本分析。
~~~
words = jieba.cut(content, cut_all=False)
~~~   
* 全模式：句子中所有的可以成詞的詞語都掃描出來, 速度快。
~~~
words = jieba.cut(content, cut_all=True)
~~~   
* 搜索引勤模式：在精確模式的基礎上針對長詞再次進行切分，提高召回率，適合用於搜尋引擎分詞。
  需要分词的字符串；是否使用 HMM 模型
~~~
jieba.cut_for_search(Content)
~~~

### 新建自訂分詞器
新建自訂分詞器，可用於同時使用不同詞典。jieba.dt 為默認分詞器，所有全域分詞相關函數都是該分詞器的映射
~~~
jieba.Tokenizer(dictionary=DEFAULT_DICT)
~~~
