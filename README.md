### Jieba 中文斷字斷詞

### Package
* Jieba
~~~
pip install jieba
~~~

### Import Library
~~~
import jieba
import jieba.analyse as jalz
import jieba.posseg as japseg
~~~

### 使用者定義詞庫 
~~~
jieba.load_userdict('user_dict.txt') 
~~~

### 分詞
* 精確模式 ：將句子最精確地切開，適合文本分析。
~~~
words = jieba.cut(content, cut_all=False)
~~~   
* 全模式：句子中所有的可以成詞的詞語都掃描出來, 速度快。
~~~
words = jieba.cut(content, cut_all=True)
~~~   
* 搜索引勤模式：在精確模式的基礎上針對長詞再次進行切分，提高召回率，適合用於搜尋引擎分詞。
~~~
jieba.cut_for_search(Content)
~~~

### 斷詞
