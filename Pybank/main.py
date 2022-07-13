import math
import os
import csv


csvpath = os.path.join("Resources", "budget_data.csv")
txtpath = os.path.join("Analysis", "analysis.txt")

dates = []
pnls = []
max_pnl = -math.inf
max_date = None
min_pnl = math.inf
max_date = None


with open (csvpath) as csvfile:

        csvreader = csv.DictReader(csvfile, fieldnames=['date','pnl'], delimiter=',')
        
        next(csvreader)
        
        for row in csvreader:
            dates.append(row['date'])
            pnls.append(float(row['pnl']))
            
            if float(row['pnl']) > max_pnl:
                max_pnl = float(row['pnl'])
                max_date = str(row['date'])
            
            if float(row['pnl']):
                min_pnl = float(row['pnl'])
                min_date = str(row['date'])
                
                
            
total_months = len(dates)
total_pnl = sum(pnls)
avg_pnl = total_pnl / total_months
max_pnl = max(pnls)
min_pnl = min(pnls)


with open (txtpath, 'w') as txtfile:
    # txtfile.write('Financial Analysis \n')
    txtfile.write('Financial Analysis \n')
    txtfile.write('----------------------------\n')
    txtfile.write(f"Total Months: {total_months} \n \n")
    txtfile.write(f"Total: $ {total_pnl:.2f} \n \n")
    txtfile.write(f"Average Change: $ {avg_pnl:.2f} \n \n")
    txtfile.write(f"Greatest PnL Increase: $ {max_pnl:.2f}  ({max_date}) \n \n")
    txtfile.write(f"Greatest PnL Decrease: $ {min_pnl: .2f}  ({min_date}) \n \n")
    