#キャンプ場の予約サイトをスクレイピングして、空きが出たらLINEに通知してくれるシステム
from turtle import title
import requests
from bs4 import BeautifulSoup
import time

campURL= "https://fumotoppara.secure.force.com/RS_Top"

def campTracking():
    campPage = requests.get(campURL)
    soup = BeautifulSoup(campPage.content, "html.parser")
    #print(soup)

    mark = soup.find("td",class_="td_itemvalue tbl_top_td3 limit_cnt").get_text()
    print(mark)
    camp2022 = "△"


    if(mark != camp2022):
        sendLineNotify()

def sendLineNotify():
    print("lineに通知がいきました。")
    lineNotifyToken = "ライントークンを入れる"
    lineNotifyApi = "heeps://notify-api.line.me/api/notify" 
    headers = {"Authorization": f"Bearer{lineNotifyToken}" }
    data = {"message":"今なら予約できるよ!https://fumotoppara.secure.force.com/RS_Top"}
    requests.post(lineNotifyApi, headers=headers, data=data)

while(True):
    print("トラッキングしました。")
    time.sleep(60 * 60)
    campTracking()