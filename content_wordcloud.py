import sys
import jieba
from wordcloud import WordCloud

STOPWORDS = [
        '，', '。', '？']
def load_file(file_path):
    if sys.version.startswith('2.'):
        with open(file_path) as f:
            lines = f.readlines()
    else:
        with open(file_path, encoding='utf-8') as f:
            lines = f.readlines()
    content = ''
    for line in lines:
        line = line.encode('unicode-escape').decode('unicode-escape')
        line = line.strip().rstrip('\n')
        content += line
    words = jieba.cut(content)
    l = []
    for w in words:
        # 如果词的长度小于 2，则舍去
        #if len(w) < 2: continue
        l.append(w)
    return ' '.join(l)
if __name__ == '__main__':
    file_path = '/Users/aada/Desktop/cl_project/content_cleaned.txt'
    content = load_file(file_path)
    wc = WordCloud(
            font_path="/Users/aada/Downloads/SimHei.ttf",
            stopwords=STOPWORDS,
            width=2000, height=1200)
    wc.generate(content)
    wc.to_file("wordcloud.jpg")