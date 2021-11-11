import ssl
#ssl.create_default_https_context = ssl.create_unverified_context()
import json
import urllib.request
handle =urllib.request.urlopen("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.geojson")
data = handle.read()
eData = json.loads(data)
earthquakeList=eData.get('features')

def makeMagList(quakeData):
    mList = []
    quakes = quakeData.get('features')
    for i in range(len(quakes)):
        quake=quakes[i]
        prop=quake.get('properties')
        mag=prop.get('mag')
        mList.append(mag)
    return mList

magList =makeMagList(eData)
import statistics
print(len(magList))
print(min(magList))
print(max(magList))
print(statistics.mean(magList))
