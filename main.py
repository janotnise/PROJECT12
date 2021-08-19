import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class international:


    def __init__(self):
        file = "Project_File.xlsx"
        columns = [0, 13, 14, 15, 16, 17, 18, 30, 31, 32, 33, 34]
        names = ["Month", "India", "Pakistan", "Sri Lanka", "Saudi Arabia", "Kuwait", "UAE", "USA", "Canada", "Australia", "New Zealand", "Africa"]

        xls = pd.ExcelFile(file)
        visitors = xls.parse(0, usecols=columns, names=names)

        # rows = ["122":"241"]
        # df = pd.DataFrame(rows =rows, columns=columns)
        # df.head()
        YM = visitors["Month"].str.split(" ", n=1, expand=True)
        #print(YM)
        visitors = visitors.assign(Year=YM[0])
        visitors = visitors.assign(Month2=YM[1])
        #print(visitors)
        self.targetVisitors = visitors[(visitors["Year"].astype(int) >= 1980) & (visitors["Year"].astype(int) <= 1998) ]
        print(self.targetVisitors)

        plt.style.use("dark_background")

    def viewData(self):
        pass
        #print(self.international)

    #def viewUsageByYear(self, year):
        #yearStats = self.international[self.international["Year"] == str(year)]
        #print(yearStats)

    #def viewTotalUsageByYear(self, year):
       # yearStats = self.international[self.international["Year"] == str(year)].groupby("Year").sum().reset_index()
        #print(yearStats)


    # GET THE MEDIAN RELEASE YEAR
    def getMedianMonthVisitors(self):
        #print (self.targetVisitors.iloc[:, [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]])
       return self.targetVisitors["Australia"].median()

    # GET THE MEAN RELEASE YEAR


#ffff


    # GET THE NUMBER OF M18 GAMES RELEASED IN A PARTICULAR YEAR

    #def getNumberOfM18GamesReleasedInYear(self, year):
        #mgames = self.games[(self.games["rating"] == "Mature 18") & (self.games["year_release"] == year)]
        #return len(mgames)

    # GET THE NUMBER OF SWITCH GAMES RELEASED IN A PARTICULAR YEAR
    #def getNumberOfSwitchGamesReleasedInYear(self, year):
       # sgames = self.games[(self.games["platform"].str.contains("Nintendo Switch")) & (self.games["year_release"] == year)]
        #return len(sgames)


# USE THE FOLLOWING CODE TO TEST YOUR SOLUTION OUT


vgs = international()
#vgs.getGamesTitles()
#vgs.getM18Games()
#vgs.getNintendoSwitchGames()

#vgs.getGamesByReleaseYear(2018)

# print("\n")
# print("The top three countries " + str(vgs.getNumberOfM18Games()))
print("Median Visitors for Australia is: " + str(vgs.getMedianMonthVisitors()))
print("Mean Vistor for Australia is: " + str(vgs.getMeanMonthVistors()))
#print("M18 Games Released in 2018: " + str(vgs.getNumberOfM18GamesReleasedInYear(2018)))
#print("Switch Games Released in 2018: " + str(vgs.getNumberOfSwitchGamesReleasedInYear(2018)))


#aaaa



