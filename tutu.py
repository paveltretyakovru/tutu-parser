#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import urllib2 as UL
from datetime import datetime as dt
from BeautifulSoup import BeautifulSoup as BS

# Get current datetime
hourNow = int(dt.strftime(dt.now(), '%H'))
minuteNow = int(dt.strftime(dt.now(), '%M'))
time = dict(h =  hourNow, m = minuteNow)
time['full'] = '%s:%s'%(time['h'],time['m'])

print(time)

url = 'http://www.tutu.ru/spb/rasp.php?st1=%s&st2=%s&date=today'
stationsIndex = dict(ivanovskaya = 0, moscovski = 1, ribackoe = 2)
stationsIds = [35704, 35004, 36204]

# Show stations
print(stationsIndex)
# Input station from
start = stationsIds[input('From station:')]
end = stationsIds[input('To station:')]

# start = stationsIds[1]
# end = stationsIds[2]

r = UL.urlopen(url%(start,end))
print(url%(start,end))
dom = BS(r.read())
tbody = dom.find('table', {'id' : 'schedule_table'}).find('tbody');
trs = tbody.findAll('tr')

lines = []

for tr in trs:
    line = []
    links = tr.findAll('a')

    for link in links:
        string = link.string
        line.append(string.encode('utf-8'))

    lines.append(line)

for line in lines:
    ds = line[0].split(':') #date Start
    de = line[1].split(':') #date End
    sf = line[2] #station From
    st = line[3] #station To

    if int(ds[0]) >= time['h']:
        if int(ds[1]) >= time['m']:
            print(' >>> %s:%s %s:%s %s %s'%(ds[0],ds[1],de[0],de[1],sf,st))
        else:
            print('%s:%s %s:%s %s %s'%(ds[0],ds[1],de[0],de[1],sf,st))
    else:
        print('%s:%s %s:%s %s %s'%(ds[0],ds[1],de[0],de[1],sf,st))
    # for val in line:
    #     print(val)
