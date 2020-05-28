from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import nltk
from konlpy.tag import Okt
from matplotlib import font_manager, rc

path = "c:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=path).get_name()
rc('font', family=font_name)

t = Okt()
file = open('20190814-224121.txt', encoding='utf-8')
text = file.read()
file.close()

token = t.nouns(text) ##분리

words_b = nltk.Text(token, name = '세제')

words = nltk.Text(words_b)
words.vocab().most_common(50)

stop_words = ['세제', '세탁', '것', '수', '저', '더', '제', '이', '거','요', '그', '종']
words = [each_word for each_word in words_b if each_word not in stop_words]

words = nltk.Text(words)
words.vocab().most_common(100)

import matplotlib.pyplot as plt
plt.figure(figsize=(16,8))
words.plot(50)
plt.axis("off")
plt.show()

import matplotlib.cm as cm
from wordcloud import WordCloud
text =""
for s in words:
    text = text + s + ' '

wc = WordCloud(font_path='c:/Windows/Fonts/malgun.ttf',
               relative_scaling = 0.2,
               background_color='white',
               colormap = cm.viridis,
               repeat = True).generate(text)
plt.axis("off")
plt.imshow(wc, interpolation="bilinear") #interpolation : 보간 지정
plt.show()
