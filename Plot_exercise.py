import matplotlib.pyplot as plt
import datetime as dt
import random
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def dice_throws(dice_num, throws):
    global dice_list
    dice_list = []
    while True:
        dice_num = random.randint(1, 6)
        dice_list.append(dice_num)
        if len(dice_list) == throws:
            break
    return dice_list

def plot_dices(dices_list, file_name=''):
    dices_list = dice_list
    count_list = Counter(list(dices_list))
    df = pd.DataFrame.from_records(list(dict(count_list).items()), columns=['dices','count'])
    print(df)
    chart = sns.barplot(data=df, x='dices', y='count', color='purple')
    for i in chart.containers:  #to display bar values
        chart.bar_label(i,)
    
    chart.set(xlabel='Dices')
    chart.set(ylabel='Count')
    chart.set(title=f'Total Number of Occurence of Each Dice')
    date = dt.datetime.now()
    plt.suptitle(date, ha='left', va='bottom', size='x-small')
    file_name = plt.savefig("Dices Histogram.jpg")
    return dices_list, plt.show(), file_name


if __name__ == "__main__":
    my_dice_list = dice_throws(6, 1000)
    my_plot = plot_dices(dice_list)
    
    

# plt.figure(figsize=(12,5))
# chart = sns.lineplot(x = 'dices', y = 'count', marker='o', data = df)
# plt.xticks(
#     rotation=90, 
#     horizontalalignment='right',
#     fontweight='light')
# chart.set(xlabel='Dices')
# chart.set(ylabel='Count')
# chart.set(title=f'Total Number of Dices')
# for x, y in zip(df['dices'], df['count']):
#     plt.text(x = x,
#     y = y,
#     s = '{:.0f}'.format(y), # data label, formatted to ignore decimals
#     color = 'purple') 
# plt.show()