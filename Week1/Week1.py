import pandas as pd

## Read one Column
def test_run():
    df = pd.read_csv("G:\Other computers\My Computer\QU91\Study\School Docu\GaTech\CS7646\Data\AAPL.csv")
    print (df['Close'])

if __name__ == '__main__':
    test_run()

## Compute Max Closing Price
def get_max_close(stock1):
    df = pd.read_csv("G:\Other computers\My Computer\QU91\Study\School Docu\GaTech\CS7646\Data\{}.csv".format(stock1))
    return(df['Close'].max())

for stock1 in ['AAPL','IBM']:
    print (stock1, get_max_close(stock1))


## Compute Mean Volume
def get_mean_volume(stock2):
    df = pd.read_csv("G:\Other computers\My Computer\QU91\Study\School Docu\GaTech\CS7646\Data\{}.csv".format(stock2))
    return(df['Volume'].mean())

for stock2 in ['AAPL','IBM']:
    print (stock1, get_mean_volume(stock2))

## Plot 
df = pd.read_csv("G:\Other computers\My Computer\QU91\Study\School Docu\GaTech\CS7646\Data\AAPL.csv")
import matplotlib.pyplot as plt
#Plot one variable
df['Adj Close'].plot()
plt.show()
#Plot multi variables
df[['Adj Close','High']].plot()
plt.show()

