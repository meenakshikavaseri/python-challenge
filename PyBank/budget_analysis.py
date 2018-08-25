# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')
print(csvpath)

#set the counter
counter = -1

#Your task is to create a Python script that analyzes the records to calculate each of the following:
#The total number of months included in the dataset
with open(csvpath, newline="") as csvfile:
   reader = csv.reader(csvfile,delimiter=',')
   for Cols in reader:
    mydate=Cols[0]
    counter = counter+1
print("Total number of months incl in the dataset = "+ str(counter))

#The total net amount of "Profit/Losses" over the entire period
totalP_L=0
with open(csvpath, newline="") as csvfile:
   reader = csv.reader(csvfile,delimiter=',')
   csv_header = next(reader)
   for Cols in reader:
        myP_L=Cols[1]
        totalP_L=totalP_L+int(Cols[1])
print ("The total net amount of over the entire period = "+ str(totalP_L))

#The average change in "Profit/Losses" between months over the entire period
changeP_Lamt=0
Colsnum=0
priormonthP_L=0
with open(csvpath, newline="") as csvfile:
   reader = csv.reader(csvfile,delimiter=',')
   csv_header = next(reader)
   for Cols in reader:
       Current_Val=int(Cols[1])
       print(Current_Val)
       if(Colsnum == 0):
           priormonthP_L=Current_Val
       else:
           print("values:" + str(Current_Val) + " " + str(Colsnum)+" "+str(priormonthP_L))
           changeP_Lamt += Current_Val - priormonthP_L
           priormonthP_L= Current_Val
       
       Colsnum = Colsnum + 1
print(changeP_Lamt)
print (counter)
avg_change=changeP_Lamt/(counter-1)
print(avg_change)
print("The average change in Profit/Losses between months over the entire period = $" + str(avg_change))


#The greatest increase in profits (date and amount) over the entire period 
Current_Val=0
Colsnum=0
priormonthP_L=0
maxvalue=0
diff=0
MaxValueDate=""
with open(csvpath, newline="") as csvfile:
   reader = csv.reader(csvfile,delimiter=',')
   csv_header = next(reader)
   for Cols in reader:
    Current_Val=int(Cols[1])
    if(Colsnum == 0):
        priormonthP_L=Current_Val
    else:
        diff = Current_Val - priormonthP_L 
        priormonthP_L= Current_Val
        
        if (diff> 0):
           if(maxvalue == 0):
            maxvalue=diff
            MaxValueDate= Cols[0]
           else:
                if(diff > maxvalue):
                    maxvalue = diff
                    MaxValueDate=Cols[0]
    Colsnum = Colsnum + 1                
print(maxvalue)
print(MaxValueDate)
print("The greatest increase in profits date =" + MaxValueDate + " and amount $" + str(maxvalue) +" over the entire period" )
#The greatest decrease in losses (date and amount) over the entire period