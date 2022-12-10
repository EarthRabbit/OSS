from getRequest import getRequest
import re
import matplotlib.pyplot as plt

news_titles = getRequest('https://news.naver.com/', 'div.cjs_news_tw')

text = []
text1 = []
count = {}

# re.split을 통해 명사를 부각하기 위해 특정 특수기호, 공백과 접속사를 제거시킨다.
for i, element in enumerate(news_titles):
    text1 = re.split('[은을를의로에라니하는·\"\':….?~’”‘“+:, ]', (element.find('div').text.strip()))
    text = text + text1
    
# 의미가 없는 문자들은 제거한다.
while '' in text:
    text.remove('')
while '[' in text:
    text.remove('[')
while ']' in text:
    text.remove(']')

# count Dict에 key가 존재하지 않는 경우 0 리턴. 존재하는 경우 count 1 증가
for word in text:
    count[word] = count.get(word, 0) + 1
    keys = sorted(count.keys())

# 한 번만 나온 단어는 결과값에서 제외한다.
overOnce = dict({key:value for key, value in count.items() if value > 1})
overTwice = dict({key:value for key, value in count.items() if value > 2})
print(overOnce)
lists0 = sorted(overOnce.items())
lists1 = sorted(overTwice.items())

testList0 = [(wordList, wordCount) for wordList, wordCount in lists0]
testList1 = [(wordList, wordCount) for wordList, wordCount in lists1]

plt.rcParams['font.family'] = 'Malgun Gothic'

plt.title('뉴스 기사에서 3번 이상 사용된 단어')
plt.xlabel('사용된 단어')
plt.xlim([0,15])
plt.ylim([0,8])
plt.scatter(*zip(*testList1))
plt.show()

plt.title('뉴스 기사에서 2번 이상 사용된 단어')
plt.xlabel('사용된 단어')
plt.ylabel('단어의 사용된 횟수')
plt.xlim([0,60])
plt.ylim([0,8])
plt.scatter(*zip(*testList0))
plt.show()