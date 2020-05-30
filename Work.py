import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
songs = soup.select('#body-content > div.newest-list > div table > tbody > tr')

# movies (tr들) 의 반복문을 돌리기
for song in songs:
    # title의 공백없이 text만 가져오려면, 따로 text만 빼오고, 다음 지정 (아마..?)
    songname = song.select_one('td.info > a.title.ellipsis')
    # 잘 모르겠어요.. 
    ranke = song.select_one('td.number').text.split()[0]
    title = songname.text.strip()
    # $ . 과 같이 class 읽을때는 a. 인듯
    singer = song.select_one('td.info > a.artist.ellipsis').text
    print(ranke,title,singer)
     
