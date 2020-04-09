from bs4 import BeautifulSoup
from urllib import request
from urllib import parse
import time
import send_email as send
from tqdm import tqdm

url = "https://srh.bankofchina.com/search/whpj/search_cn.jsp"
Form_Data = {}
Form_Data['erectDate'] = ''
Form_Data['nothing'] = ''
aus = 500
bri = 1000
cnt = 0
while True:
    cnt = cnt+1
    try:
        Form_Data['pjname'] = '英镑'
        data = parse.urlencode(Form_Data).encode('utf-8')
        html = request.urlopen(url,data).read()
        soup = BeautifulSoup(html,'html.parser')
        div = soup.find('div', attrs = {'class':'BOC_main publish'})
        table = div.find('table')
        # print(type(table))
        tr = table.find_all('tr')
        td = tr[1].find_all('td')
        # print(td)
        msg = '英镑 '+td[-1].get_text()+" "+td[3].get_text()
#        print(msg)
        if float(td[3].get_text())<bri or cnt%720==0:
            send.send_mail(msg,["Your email address1", "Your email address2",...])
            print(msg)
            print('已发送')
            bri = float(td[3].get_text())
        time.sleep(30)
#        for i in tqdm(range(30)):
#            pass
#            time.sleep(1)

        Form_Data['pjname'] = '澳大利亚元'
        data = parse.urlencode(Form_Data).encode('utf-8')
        html = request.urlopen(url,data).read()
        soup = BeautifulSoup(html,'html.parser')
        div = soup.find('div', attrs = {'class':'BOC_main publish'})
        table = div.find('table')
        # print(type(table))
        tr = table.find_all('tr')
        td = tr[1].find_all('td')
        # print(td)
        # print('澳元',td[-1].get_text(),td[3].get_text())
        msg = '澳元 '+td[-1].get_text()+" "+td[3].get_text()
#        print(msg)
        if float(td[3].get_text())<aus or cnt%720==0:
            send.send_mail(msg,["2651528990@qq.com", "1065323367@qq.com"])
            print(msg)
            print('已发送')
            aus = float(td[3].get_text())
        time.sleep(30)
#        for i in tqdm(range(30)):
#            pass
#            time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(30)
#        for i in tqdm(range(30)):
#            pass
#            time.sleep(1)
        continue
