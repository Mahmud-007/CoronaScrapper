from urllib.request import urlopen,Request
from bs4 import BeautifulSoup


header={"user-Agent":"Mozila"}
req=Request("https://www.worldometers.info/coronavirus/country/bangladesh/",headers=header)
infos=urlopen(req)
obj=BeautifulSoup(infos,features="html.parser")
newCases=obj.find("li", {"class":"news_li"}).strong.text.split()[0]
newDeaths=list(obj.find("li", {"class":"news_li"}).strong.next_siblings)[1].text.split()[0]
message="New Cases: "+newCases+"\nNew Deaths: "+newDeaths
