
import pandas as pd
import math

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




def main():

    all_pos = latlngToGlobalXY(df["latitude"],df["longitude"])

    global_x =all_pos['x'].to_numpy()
    global_y =all_pos['y'].to_numpy()

    df['global_x'] = global_x
    df['global_y'] = global_y

    pos_a_x = global_x[1]
    pos_a_y = global_y[1]

    p0_pos_ref = latlngToGlobalXY(p0.lat,p0.lng)

    p1_pos_ref = latlngToGlobalXY(p1.lat,p1.lng)

    perX = ((pos_a_x-p0_pos_ref['x'])/(p1_pos_ref['x'] -p0_pos_ref['x'] ))

    perY = ((pos_a_y-p0_pos_ref['y'])/(p1_pos_ref['y'] -p0_pos_ref['y'] ))

    test_x = p0.scrX + (p1.scrX - p0.scrX)*perX
    test_y = p0.scrY + (p1.scrY - p0.scrY)*perY

    print(test_x,test_y)

    # print("pos_a_x", pos_a_x)

    # print("p0_pos_ref['x']", p0_pos_ref['x'])

    # print("(p1_pos_ref['x']", p1_pos_ref['x'])

    # print("p0_pos_ref['x']", p0_pos_ref['x'])



    # df.to_json(r'nldd_xy_classe.json')



# This function converts lat and lng coordinates to GLOBAL X and Y positions
def latlngToGlobalXY(lat, lng):
     # Calculates x based on cos of average of the latitudes
    x = radius*lng*math.cos((p0.lat + p1.lat)/2)
    # Calculates y based on latitude
    y = radius*lat
    return {'x': x, 'y': y}

if __name__ == "__main__":
    main()