
import pandas as pd
import math
import json

df = pd.read_table('nldd_classe.tsv')

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


# def getScreenXY(pos_x,pos_y):
    
#     p0_pos_ref = latlngToGlobalXY(p0.lat,p0.lng)

#     p1_pos_ref = latlngToGlobalXY(p1.lat,p1.lng)

#     perX = ((pos_x-p0_pos_ref['x'])/(p1_pos_ref['x'] -p0_pos_ref['x'] ))

#     perY = ((pos_y-p0_pos_ref['y'])/(p1_pos_ref['y'] -p0_pos_ref['y'] ))

#     screen_x = p0.scrX + (p1.scrX - p0.scrX)*perX
#     screen_y = p0.scrY + (p1.scrY - p0.scrY)*perY

#     return {'x': screen_x/10, 'y': screen_y/10}

def getScreenX(pos_x):

    p0_pos_ref = latlngToGlobalXY(p0.lat,p0.lng)

    p1_pos_ref = latlngToGlobalXY(p1.lat,p1.lng)

    perX = ((pos_x-p0_pos_ref['x'])/(p1_pos_ref['x'] -p0_pos_ref['x'] ))

    screen_x = p0.scrX + (p1.scrX - p0.scrX)*perX

    return screen_x/10


    

def main():

    all_pos = latlngToGlobalXY(df["latitude"],df["longitude"])

    global_x =all_pos['x'].to_numpy()
    global_y =all_pos['y'].to_numpy()

    df['global_x'] = global_x
    df['global_y'] = global_y

    dict = getAllScreenXY(global_x,global_y)

    # use json.dump to write the file
    with open('./screenXY.json', 'w') as file:
        json.dump(dict, file, indent=4)

    


def getAllScreenXY(global_x,global_y):

    dict = {}

    for i in range(0,len(global_x)):

        index = 'point' + str(i)

        test = getScreenXY(global_x[i],global_y[i])

        dict[index] = test

    return dict

# This function converts lat and lng coordinates to GLOBAL X and Y positions
def latlngToGlobalXY(lat, lng):
     # Calculates x based on cos of average of the latitudes
    x = radius*lng*math.cos((p0.lat + p1.lat)/2)
    # Calculates y based on latitude
    y = radius*lat
    return {'x': x, 'y': y}

if __name__ == "__main__":
    main()