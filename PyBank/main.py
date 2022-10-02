#The total number of months included in the dataset.
# The net total amount of "Profit/Losses" over the entire period.
# The changes in "Profit/Losses" over the entire period, and 
# then the average of those changes.
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period

# Modules
import os
import csv

# Set path for file
budget_csv = os.path.join( "Resources", "budget_data.csv")

#Declare and Initialize the variables
total_month = 0
date= []
profit_losses = []
previous_row =0
net_total=0

# Read the CSV file
with open(budget_csv) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Read the header row first
    csv_header = next(csvreader)
    
    # # Read each row of data after the header
    for row in csvreader:
        
         # add date
        date.append(row[0])
        
        if total_month== 0:
            
            # add zero if its first row
            profit_losses.append(0)
        else:
                # add profit losses 
            profit_losses.append(int(row[1])-previous_row)
        
        #Calculated total number of months included in the dataset
        total_month= total_month + 1
        
        #net total amount of "Profit/Losses" over the entire period
        net_total = net_total + int(row[1])
        
        previous_row = int(row[1])
        
            
        
print(f"Total Month: {total_month}") 
print(f"Total : ${net_total} ")    
print(f"Average change :{round(sum(profit_losses)/(total_month -1) , 2)}")
max_value= max(profit_losses)
min_value= min(profit_losses)


max_index=profit_losses.index(max_value)
min_index=profit_losses.index(min_value)


print(f"Greatest Increase in Profits:{(date[max_index])} (${max_value})")
print(f"Greatest Decrease in Profits:{(date[min_index])} (${min_value})")


    

file1 = open("analysis/budget_analysis.txt" , "w")


output = (
          "Financial Analysis\n"
          "--------------------------------\n"
         f"Total Months: {total_month}\n"
         f"Total: ${net_total}\n"
         f"Average change :{round(sum(profit_losses)/(total_month -1) , 2)}\n"
         f"Greatest Increase in Profits:{(date[max_index])} (${max_value})\n"
         f"Greatest Decrease in Profits:{(date[min_index])} (${min_value})\n"
          )


file1.write(output)



file1.close()
