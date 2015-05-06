import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

loansData.dropna(inplace=True)

#This boxplot tells us that amount requested is very similar to amount
#funded, but the request of funds over USD 30.000 is higher than actual.
loansData.boxplot(column='Amount.Requested') #boxplot

#By looking at the histogram, we see that investors mostly fund between
#USD 5.000 and USD 10.000, the fund request is similar except the investors
#tend to invest lower, although close to requested.
loansData.hist(column='Amount.Requested') #histogram

#QQ plot tells us that the funds have mostly been on the left side 
#of a histogram, meaning that the funds were made less as the fund
#value grows. The difference between funded and requested graphs are
#too similar that not much could be interpreted. 
plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.show()