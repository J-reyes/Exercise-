import re

def main():
    weatherData = "/Users/lalovazquez/Desktop/Projects/practice/w.data.dat"

    with open(weatherData) as file:
        line = file.readline()[:-1]
        for i in range(6):
            line = file.readline() 
        day = line.split()[0]

        lowestSpread = get_temp_spread(line.split()[1], line.split()[2])
        lowestSpreadDay = day
        for count, line in enumerate(file):
            
            if(count > 4 and line.split()[0] != "mo" and line.split()[0] != "</pre>"  ):
                day = line.split()[0]
                maxTemp = line.split()[1]
                lowTemp = line.split()[2]
                tempSpread = get_temp_spread(maxTemp, lowTemp)
                
                if (tempSpread < lowestSpread):
                  lowestSpread = tempSpread
                  lowestSpreadDay = day
       
        print("The lowest spread was {} on June {}, 2002.".format(lowestSpread, lowestSpreadDay))


def get_temp_spread(max_temp, low_temp):
    # Calculate spread
    spread = int(re.sub("\D", "",max_temp)) - int(re.sub("\D", "", low_temp))
    
    return spread

if __name__ == "__main__":
    main()



# print("Line {}: {}".format(count, line))
# return format(count, line)