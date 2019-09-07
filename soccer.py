import re

def main():
    goalsData = "/Users/lalovazquez/Desktop/Projects/practice/soccer.dat"

    with open(goalsData) as file:
        line = file.readline()[:-1]

        for i in range(3):
             line = file.readline() 
        team = line.split()[1]

        lowestDifference = get_difference(line.split()[6],line.split()[8])
        lowestTeam = team
        for count, line in enumerate(file):
            
            if(not (line.strip().startswith("--") or line.startswith("<"))):
                team = line.split()[1]
                goalsFor = line.split()[6]
                goalsAgaist = line.split()[8]
                difference = get_difference(goalsFor, goalsAgaist) 
                if(difference < lowestDifference):
                    lowestDifference = difference
                    lowestTeam = team
        print("The team with the lowest difference in goals is {} with a difference of {}".format(lowestTeam.replace("_", " "), lowestDifference))
        
            
def get_difference(goals_made, goals_against):
    # Calculate lowest difference
    diff = abs(int(goals_made) - int(goals_against))
    
    return diff


if __name__ == "__main__":
    main()    