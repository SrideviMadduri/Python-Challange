#  The total number of votes cast
#  A complete list of candidates who received votes
#  The percentage of votes each candidate won
#  The total number of votes each candidate won
#  The winner of the election based on popular vote.


# Modules
import os
import csv

# Set path for file
election_csv = os.path.join( "Resources", "election_data.csv")

#Diclare and initialize variables
total_votes =0
dict_candidates= {}
percentage=0
percentage_list= []
winner =0

#Read CSV file
with open(election_csv) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Read the header row first
    csv_header = next(csvreader)
    
    #  Read each row of data after the header
    for row in csvreader:
        
        # Calculate total number of vote casted
         total_votes = total_votes +1
        
         if row[2] in dict_candidates:
             dict_candidates[row[2]] = dict_candidates[row[2]] +1
         else: 
                     
           dict_candidates[row[2]] =1
           
    #Winner of election based on popular vote.       
    winner= max(dict_candidates, key=dict_candidates.get)
    
    percentage_list = list(dict_candidates.values())
    
    #percentage of votes each candidate won.
    for x in range(len(percentage_list)):
        percentage_list[x]= round((percentage_list[x]/total_votes)*100 ,3)  
         
                       
       
divider = "-------------------------\n"

output="Election Results\n"
output += divider
output += f"Total Votes: {total_votes}\n"
output += divider

for name, per, tot in zip(dict_candidates.keys(),percentage_list,dict_candidates.values()):
    output += f"{name}: {per}% ({tot})\n"   
    
output += divider
output += f"Winner: {winner}\n"
output += divider

print(output)
file1 = open("analysis/election_analysis.txt" , "w")

file1.write(output)  


file1.close()


