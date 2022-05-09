
import pandas as pd
import math
import json


radius = 6371

class referencePoint:
    def __init__(self, scrX, scrY, lat, lng):
        self.scrX = scrX
        self.scrY = scrY
        self.lat = lat
        self.lng = lng


# Calculate global X and Y for top-left reference point        
p0 = referencePoint(0, 0, 45.590231380357075, -73.68553872266351)
# Calculate global X and Y for bottom-right reference point
p1 = referencePoint(2244, 2060, 45.55443164693175, -73.59927931059248)
    

def main():

   createJSONfile('../data/ll/hans_01.tsv','../data/screen/hans_01.json')
   createJSONfile('../data/ll/hans_02.tsv','../data/screen/hans_02.json')
   createJSONfile('../data/ll/lagrandeporte.tsv','../data/screen/lagrandeporte.json')
   createJSONfile('../data/ll/mylene.tsv','../data/screen/mylene.json')

    

def createJSONfile(input,output):

    df = pd.read_table(input)


    all_pos = latlngToGlobalXY(df["latitude"],df["longitude"])

    global_x =all_pos['x'].to_numpy()
    global_y =all_pos['y'].to_numpy()

    df['global_x'] = global_x
    df['global_y'] = global_y

    dict = {} 

    dict['x'] = getAllScreenX(global_x)

    dict['y'] = getAllScreenY(global_y)


    # use json.dump to write the file
    with open(output, 'w') as file:
        json.dump(dict, file, indent=4)



def getAllScreenX(global_x):

    all_screen_x = []

    for i in range(0,len(global_x)):

        all_screen_x.append(getScreenX(global_x[i]))

    return all_screen_x

        
def getAllScreenY(global_y):

    all_screen_y = []

    for i in range(0,len(global_y)):

        all_screen_y.append(getScreenY(global_y[i]))

    return all_screen_y

def getScreenX(pos_x):

    p0_pos_ref = latlngToGlobalXY(p0.lat,p0.lng)

    p1_pos_ref = latlngToGlobalXY(p1.lat,p1.lng)

    perX = ((pos_x-p0_pos_ref['x'])/(p1_pos_ref['x'] -p0_pos_ref['x'] ))

    screen_x = p0.scrX + (p1.scrX - p0.scrX)*perX

    return screen_x/10


def getScreenY(pos_y):

    p0_pos_ref = latlngToGlobalXY(p0.lat,p0.lng)

    p1_pos_ref = latlngToGlobalXY(p1.lat,p1.lng)

    perY = ((pos_y-p0_pos_ref['y'])/(p1_pos_ref['y'] -p0_pos_ref['y'] ))

    screen_y = p0.scrY + (p1.scrY - p0.scrY)*perY

    return screen_y/10
    




# This function converts lat and lng coordinates to GLOBAL X and Y positions
def latlngToGlobalXY(lat, lng):
     # Calculates x based on cos of average of the latitudes
    x = radius*lng*math.cos((p0.lat + p1.lat)/2)
    # Calculates y based on latitude
    y = radius*lat
    return {'x': x, 'y': y}

if __name__ == "__main__":
    main()