import bs4
import requests
#getting data from all the polling stations of one district
def getdata(url):
    site=requests.get(url)
    if site.text.find("Інформація щодо цієї сторінки відсутня")>0: ##for districts with no data; mostly means occupied territories of Ukraine
        print('Skipped...')
    else:
        sitebs=bs4.BeautifulSoup(site.text)
        listing=sitebs.findAll('tr')
        datastr=[]
        for item in listing:
            datastr.append(item.text)
        datastr[0]=datastr[0].replace('\n', '')
        datastr[0]=datastr[0].replace('\xa0', '')
        print(datastr[0])
        file=open(datastr[0]+'.csv', encoding='utf-8', mode="w") #naming a file by the name of the district and the region
        datastr[2]=datastr[2].replace(',', '')
        datastr[2]=datastr[2].replace('\n', ',')
        datastr[2]=datastr[2].rstrip(',')
        datastr[2]=datastr[2].lstrip(',')
        file.write(datastr[2]+'\n')
        datastr=datastr[3:(len(datastr)-1)]
        for data in datastr:
            data=data.replace('\n', ',')
            data=data.rstrip(',')
            data=data.lstrip(',')
            file.write(data+'\n')
            print(data)
            
for j in range (1, 227):
    getdata('http://www.cvk.gov.ua/pls/vp2014/wp336?pt001f01=702&pt005f01='+str(j)) ##getting data for all the 226 disrticts
    
