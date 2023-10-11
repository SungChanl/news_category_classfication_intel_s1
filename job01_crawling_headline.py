from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import datetime

category = ['Politics', 'Economy', 'Social', 'Culture', 'World', 'IT']
url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100'


headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"}
# resp = requests.get(url, headers=headers)    # webpage를 응답으로 받아옴
# # print(list(resp))
# print(type(resp))
# soup = BeautifulSoup(resp.text, 'html.parser')
# # print(soup)
# title_tags = soup.select('.sh_text_headline')               # 해당 클래스를 가지는 애들만
# print(title_tags)
# print(len(title_tags))
# print(type(title_tags[0]))
# titles = []
# for titles_tag in title_tags:
#     titles.append(re.compile('[^가-힣|a-z|A-Z]').sub(' ', titles_tag.text))   # 모든 한글 조합 문자, 모든 영어 소문자, 모든 영어 대문자 수집
# print(titles)                                                                   앞에 지정한 값 이외에는 다 지우고 그자리를 빈칸으로 나둔다
# print(len(titles))

# df_titles = pd.DataFrame()
# re_title = re.compile('[^가-힣|a-z|A-Z]')
#
# for i in range(6):
#     resp = requests.get('https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=10{}'.format(i), headers=headers) # {} 자리를 i로 채워줌
#     soup = BeautifulSoup(resp.text, 'html.parser')
#     title_tags = soup.select('.sh_text.headline')
#     titles = []
#     for title_tags in title_tags:
#         titles.append(re.compile('[^가-힣|a-z|A-Z]').sub(' ', title_tags.text))
#     df_section_titles = pd.DataFrame(titles, columns=['titles'])
#     df_section_titles['category'] = category[i]
#     df_titles = pd.concat([df_titles, df_section_titles], axis='rows', ignore_index=True)                          # 인덱스 중복 방지
#
# print(df_titles.head())
# df_titles.info()
# print(df_titles['category'].value_counts())
# df_titles.to_csv('./crawling_data/naver_headline_news_{}.csv'.format(
#     datetime.datetime.now().strftime('%Y%m%d')), index=False)

df_titles = pd.DataFrame()
re_title = re.compile('[^가-힣|a-z|A-Z]')

for i in range(6):
    resp = requests.get('https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=10{}'.format(i), headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')
    title_tags = soup.select('.sh_text_headline')
    titles = []
    for title_tags in title_tags:
        titles.append(re.compile('[^가-힣|a-z|A-Z]').sub(' ', title_tags.text))
    df_section_titles = pd.DataFrame(titles, columns=['titles'])
    df_section_titles['category'] = category[i]
    df_titles = pd.concat([df_titles, df_section_titles], axis='rows', ignore_index=True)

print(df_titles.head())
df_titles.info()
print(df_titles['category'].value_counts())
df_titles.to_csv('./crawling_data/naver_headline_news_{}.csv'.format(
    datetime.datetime.now().strftime('%Y%m%d')), index=False)