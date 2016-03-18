#!/usr/bin/env python3.3
import requests
import sys

def grab_stdin():
    '''Get input stations from stdin.'''
    stns = []
    locx = []
    locy = []
    for line in sys.stdin:
        elems = line.split()
        stns.append(elems[0]) #station name
        locx.append(float(elems[1]))
        locy.append(float(elems[2]))
    return stns, locx, locy

def grab_forecast_data():
    '''Get raw data as HTML string from the NOAA website.'''
    url = 'http://www.nws.noaa.gov/mdl/gfslamp/lavlamp.shtml'
    page = requests.get(url)
    return page.text

def get_station_temp(temp_data, stn):
    '''We have a list of Illinois stations from the sites loaded previously.
       We need to load the data for each of those sites and store these data 
       locally.  There are a lot of data included here, but we are only 
       interested in one:  the current temperature, located at the index
       offset 169 and of length 2 (found by examination).
    '''
    tag_start = temp_data.find(stn)
    if tag_start == -1:
        T = float('NaN')
        return
    tag_end = tag_start + 1720 #each text block is 1720 characters long
    T = float(temp_data[tag_start+169:tag_start+172])
    return T

if __name__ == '__main__':
    stns, locx, locy = grab_stdin()
    temp_data = grab_forecast_data()
    for stn,lat,lon in zip(stns, locx, locy):
        try:
            temp = get_station_temp(temp_data, stn)
            print('%s\t%f\t%f\t%f'%(stn,lon,lat,temp))
        except:
            pass
            #print(stn,lat,lon)
            #print('Could not parse line\n\t%s'%line)