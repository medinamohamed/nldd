from fileinput import filename
import urls
import sys
import pandas as pd
from urllib.parse import urlsplit, parse_qs


def main():

    mylene = urls.mylene
    hans_01 = urls.hans_01
    lagrandeporte = urls.lagrandeporte
    hans_02 = urls.hans_02

    create_csv(mylene,'../data/ll/mylene.tsv')
    create_csv(hans_01,'../data/ll/hans_01.tsv')
    create_csv(lagrandeporte,'../data/ll/lagrandeporte.tsv')
    create_csv(hans_02,'../data/ll/hans_02.tsv')

def get_ll(url):
    
    query = urlsplit(url).query
    params = parse_qs(query)

    lng = list(str(params['ll'][0]).split(","))[0]
    lat = list(str(params['ll'][0]).split(","))[1]

    return {'lng': lng,'lat': lat}


def get_lat(url):
    lat_arr = []
    for i in url:
   
        lat_arr.append(get_ll(i)['lat'])

    return lat_arr


def get_lng(url):
    lng_arr = []
    for i in url:
    
        lng_arr.append(get_ll(i)['lng'])

    return lng_arr

def create_csv(classe,filename):

    lat_arr = get_lat(classe)

    lng_arr = get_lng(classe)

    data = {'latitude':lng_arr, 'longitude':lat_arr }
    df = pd.DataFrame(data)

    df.to_csv(filename , sep = '\t')



if __name__ == "__main__": 
    
    main()