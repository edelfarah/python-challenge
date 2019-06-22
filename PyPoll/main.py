import os
import csv

csvpath = os.path.join('election_data.csv')

totalvotes = 0
candidate = []
candidates_dict = {}


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:

        candy = row[2]
        candidate.append(row[2])
        totalvotes += 1

        if candy not in candidates_dict:
            candidates_dict[candy] = 1
        else:
            candidates_dict[candy] += 1

winner = max(set(candidate), key=candidate.count)


print("Election Results")
print("---------------------------")
print("Total Votes: " + str(totalvotes))
print("---------------------------")


for x in candidates_dict:
     print(x + ": " + str(round((candidates_dict[x]/totalvotes)*100,2)) + "%" + "  (" + str(candidates_dict[x]) + ")")
     

print("---------------------------")    
print("Winner: " + winner)
print("---------------------------")   

text_file = open("PyPoll.txt","w",newline='')

text_file.write(("Election Results\n"))
text_file.write("---------------------------\n")
text_file.write(("Total Votes: " + str(totalvotes)) + "\n")
text_file.write("---------------------------\n")
for x in candidates_dict:
    print(x + ": " + str(round((candidates_dict[x]/totalvotes)*100,2)) + "%" + "  (" + str(candidates_dict[x]) + ")")
    text_file.write(((x + ": " + str(round((candidates_dict[x]/totalvotes)*100,2)) + "%" + "  (" + str(candidates_dict[x]) + ")")+ "\n"))
text_file.write("---------------------------\n")
text_file.write("Winner: " + winner + "\n")
text_file.write("---------------------------\n")
text_file.close()
