import pandas as pd
from scipy import stats

data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''

#First, split them into list of lines.
data = data.splitlines()
#Then split them by commas.
data = [i.split(',') for i in data]
#Convert them into pandas.
column_names = data[0] #First line to be the names.
data_rows = data[1::] #All the other lines, one by one.
df = pd.DataFrame(data_rows, columns = column_names)

print df
'''
#Calculate the mean, median, mode, range, variance and standard deviation.
#First turn them into floats.
df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

#Now calculate.
mean_A = df['Alcohol'].mean()
median_A = df['Alcohol'].median()
mode_A = stats.mode(df['Alcohol'])
range_A = max(df['Alcohol']) - min(df['Alcohol'])
std_A = df('Alcohol').std()
var_A = df('Alcohol').var()

mean_T = df['Tobacco'].mean()
median_T = df['Tobacco'].median()
mode_T = stats.mode(df['Tobacco'])
range_T = max(df['Tobacco']) - min(df['Tobacco'])
std_T = df('Tobacco').std()
var_T = df('Tobacco').var()

for i in Alcohol:
	print i

print "The mean for the Alcohol and Tobacco dataset is %s for Alcohol, and %s for Tobacco." %(mean_A, mean_T)
print "The mode for the Alcohol and Tobacco dataset is %s for Alcohol, and %s for Tobacco." %(mode_A, mode_T)
print "The median for the Alcohol and Tobacco dataset is %s for Alcohol, and %s for Tobacco." %(median_A, median_T)
print "The range for the Alcohol and Tobacco dataset is %s for Alcohol, and %s for Tobacco." %(range_A, range_T)
print "The variance for the Alcohol and Tobacco dataset is %s for Alcohol, and %s for Tobacco." %(var_A, var_T)
print "The standard deviation for the Alcohol and Tobacco dataset is %s for Alcohol, and %s for Tobacco." %(std_A, std_T)
'''
