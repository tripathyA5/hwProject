import pandas as pd
import csv
import statistics
import plotly.figure_factory as ff 
df=pd.read_csv('HeightWeightData.csv')
fig=ff.create_distplot([df['Weight(Pounds)'].tolist()],['Weight'],show_hist=False)
heightList = df['Height(Inches)'].tolist()
weightList = df['Weight(Pounds)'].tolist()
heightMean = statistics.mean(heightList)
heightMedian = statistics.median(heightList)
heightStd= statistics.stdev(heightList)
heightMode = statistics.mode(heightList)
weightMean = statistics.mean(weightList)
weightMedian = statistics.median(weightList)
weightMode = statistics.mode(weightList)
print(weightMode, weightMedian, weightMean)
print(heightMode, heightMedian, heightMean)
height_first_std_deviation_start, height_first_std_deviation_end = heightMean - heightStd, heightMean + heightStd
height_second_std_deviation_start, height_second_std_deviation_end = heightMean - (2*heightStd), heightMean + (2*heightStd)
height_third_std_deviation_start, height_third_std_deviation_end = heightMean - (3*heightStd), heightMean + (3*heightStd)



height_list_of_data_within_1_std_deviation = [result for result in heightList if result > height_first_std_deviation_start and result < height_first_std_deviation_end]
height_list_of_data_within_2_std_deviation = [result for result in heightList if result > height_second_std_deviation_start and result < height_second_std_deviation_end]
height_list_of_data_within_3_std_deviation = [result for result in heightList if result > height_third_std_deviation_start and result < height_third_std_deviation_end]
heightPercent1Std = len(height_list_of_data_within_1_std_deviation)*100/len(heightList)
heightPercent2Std = len(height_list_of_data_within_2_std_deviation)*100/len(heightList)
heightPercent3Std = len(height_list_of_data_within_3_std_deviation)*100/len(heightList)

print(heightPercent1Std, heightPercent2Std, heightPercent3Std)
