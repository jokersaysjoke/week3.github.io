import urllib.request as request
import json
from winreg import DisableReflectionKey
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    # data=response.read().decode("utf-8") 用json不用decode
    data=json.load(response)

# 將2015年以前的資料過濾掉
touristAttraction=data["result"]["results"]
with open("data.csv", "w", encoding="utf-8") as file:
    for i in touristAttraction:

        if i["xpostDate"][0:4] >= '2015' :
            # split(' ')
            # 如果 split() 指定了不存在的分隔符號的話會回傳長度為 1 的 list，
            # 回傳的這個 list 第一個元素即為原本的字串。
            https = i["file"].split('https')
            # print(https[1])
            # print("https"+https[1])       
            
# 要求(一) 景點名稱,區域,經度,緯度,第一張圖檔網址

            # file.write(i["xpostDate"]+',')
            file.write(i["stitle"]+',')
            file.write(i["address"][5:8]+',')
            file.write(i["longitude"]+',')
            file.write(i["latitude"]+',')
            file.write("https"+https[1]+'\n')
