import urls
import sys
import pandas as pd
from urllib.parse import urlsplit, parse_qs


def main():

    url_classe = urls.classe

    lat_arr = get_lat(url_classe)

    lng_arr = get_lng(url_classe)

    create_csv(lng_arr,lat_arr)

def getll(url):
    
    query = urlsplit(url).query
    params = parse_qs(query)

    lng = list(str(params['ll'][0]).split(","))[0]
    lat = list(str(params['ll'][0]).split(","))[1]

    return {'lng': lng,'lat': lat}


def get_lat(url):
    lat_arr = []
    for i in url:
   
        lat_arr.append(getll(i)['lat'])

    return lat_arr


def get_lng(url):
    lng_arr = []
    for i in url:
    
        lng_arr.append(getll(i)['lng'])

    return lng_arr

def create_csv(lng_arr,lat_arr):

    data = {'latitude':lng_arr, 'longitude':lat_arr }
    df = pd.DataFrame(data)

    df.to_csv(f"nldd_classe.tsv", sep = '\t')



if __name__ == "__main__": 
    
    main()