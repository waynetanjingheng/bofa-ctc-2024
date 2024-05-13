import numpy as np

import pandas as pd

clients= pd.read_csv('input_clients.csv')

orders= pd.read_csv('input_orders.csv')

instruments= pd.read_csv('input_instruments.csv')

initialJoin = pd.merge(clients, orders, how='inner', left_on="ClientID", right_on="Client")

finalJoin = pd.merge( initialJoin, instruments, how='left', left_on="Instrument", right_on="InstrumentID") # keep joins 

finalJoin.drop(columns='Client', inplace=True)  
finalJoin.drop(columns='Instrument', inplace=True)  
failedTrades = pd.DataFrame(columns=['REASON', 'ClientID','Currencies','PositionCheck','Rating','Time','OrderID','Quantity', 'Side', 'InstrumentID', 'Currency', 'LotSize', 'completed_buy'])


passedTrades = pd.DataFrame(columns=['ClientID','Rating','Time','OrderID','Quantity', 'Side', 'InstrumentID', 'Currency', 'LotSize'])
completed_buys ={} # hash map storing (client, stock): quantity




def checking(row): 
    if pd.isna(row['InstrumentID']) : 
        row['REASON'] = "REJECTED-INSTRUMENT NOT FOUND"
        failedTrades.loc[len(failedTrades)] =row
        
     

    currencySet = set(row['Currencies'].split(',')) if isinstance(row['Currencies'], str) else set()
    # Check currency presence
    if row['Currency'] not in currencySet:
        row['REASON'] = "REJECTED-MISMATCH CURRENCY"
        failedTrades.loc[len(failedTrades)] =row
        

    # check lot size 
    if row['Quantity']% row['LotSize'] != 0: 
        row['REASON'] = "REJECTED-INVALID LOT SIZE"
        failedTrades.loc[len(failedTrades)] =row
        

    completedBuys = row["completed_buy"]
    length = len(completedBuys)

    # check posiiton
    if row['PositionCheck']=="Y" and row['Side'] == "Sell": 
        Instrument= row['InstrumentID']    
        Client = row['ClientID']
        sellSize = row['Quantity'] 

        # check hash map
        if (Client,Instrument) in completed_buys: 
            buySize = completed_buys[(Client,Instrument)]
            if sellSize<= buySize:
                pass 

            else: 
                
                row['REASON'] = "REJECTED-POSITION CHECK FAILED"
                failedTrades.loc[len(failedTrades)] =row
                
        else: 
           
            row['REASON'] = "REJECTED-POSITION CHECK FAILED"
            failedTrades.loc[len(failedTrades)] =row
        
        passedTrades.loc[len(passedTrades)] =row
            
        

    
    



        


    






    

    
   


