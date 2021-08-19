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
        print(visitors)

        # rows = ["122":"241"]
        # df = pd.DataFrame(rows =rows, columns=columns)
        # df.head()
        YM = visitors["Month"].str.split(" ", n=1, expand=True)
        print(YM)
        visitors = visitors.assign(Year=YM[1])
        print(YM)
        visitors = visitors.assign(Month=YM[2])
        print(YM)
        plt.style.use("dark_background")

    def viewData(self):
        print(self.international)

    def viewUsageByYear(self, year):
        yearStats = self.international[self.international["Year"] == str(year)]
        print(yearStats)

    def viewTotalUsageByYear(self, year):
        yearStats = self.international[self.international["Year"] == str(year)].groupby("Year").sum().reset_index()
        print(yearStats)

    #def plotLineChartByYear(self, year):
        # yearStat= self.international[self.international"Year"] == str(year)]
        # plt.plot(yearStats["Quarter"], yearStats["volume_of_international_data"], label=year)
        # plt.title("international vistor in " + str(year))
        # plt.xlabel("Year")
        # plt.ylabel("vistors")
        # plt.legend()
        # plt.show()

    #def barChartByYear(self):
        #yearStats = self.international.groupby("Year").sum().reset_index()

        #plt.bar(yearStats["Year"], yearStats["vistor"])
        #plt.title("international vistors by Year")
        #plt.xlabel("Year")
        #plt.ylabel("vistors")
        #plt.show()






# USE THE FOLLOWING CODE TO TEST YOUR SOLUTION OUT

mds = international()
# mds.viewData()
# mds.viewUsageByYear(2012)
# mds.viewTotalUsageByYear(2012)
# mds.plotLineChartByYear(2012)
# mds.barChartByYear()
# mds.pieChartByYear()
# mds.scatterChart()


