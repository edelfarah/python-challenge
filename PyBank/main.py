import os

import csv

totalprofit = 0
avgchange = []
row_num = 0
csvpath = os.path.join('budget_data.csv')
date = []
profit = []

with open(csvpath, newline="") as csvfile:
 csvreader = csv.reader(csvfile, delimiter=',')
 header = next(csvreader)

 for row in csvreader:
   date.append(row[0])
   profit.append(row[1])
   totalprofit +=int(row[1])
   currProfitFromThisRow = int(profit[len(profit)-1])
   profitFromLastRow = int(profit[len(profit)-2])
   if len(profit) == 1: #hack
     continue
   else:
    avgchange.append(currProfitFromThisRow-profitFromLastRow)
  
import numpy as np
avgChangeMinIndx = np.argmin(avgchange) + 1 #lmao wut
avgChangeMaxIndx = np.argmax(avgchange) + 1 #lmao wut  


print("Financial Analysis")
print("------------------------")
print("Total Months: " + str(len(date)))
print("Total: " + "$"+str((totalprofit)))
print("Average Change: $" + str(round(sum(avgchange)/len(avgchange),2)))
print("Greatest Increase in Profits: " + str((date[avgChangeMaxIndx])) + "($" +  str(max(avgchange)) + ")")
print("Greatest Decrease in Profits: " + str((date[avgChangeMinIndx])) + "($" +  str(min(avgchange)) + ")")

text_file = open("PyBank.txt","w",newline='')

text_file.write(("Finacial Analysis\n"))
text_file.write("---------------------------\n")
text_file.write("Total Months: " + str(len(date)) + "\n")
text_file.write("Total: $" + str(totalprofit)+ "\n")
text_file.write("Average Change: $" + str(round(sum(avgchange)/len(avgchange),2)) + "\n")
text_file.write("Greates Increase in Profits: " + str((date[avgChangeMaxIndx])) +" ($" + str(max(avgchange)) + ")\n")
text_file.write("Greates Decrease in Profits: " + str((date[avgChangeMinIndx])) +" ($" + str(min(avgchange)) + ")\n")
text_file.close()