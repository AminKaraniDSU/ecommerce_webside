import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("/home/khizer/Downloads/shootings.csv")
print(df['manner_of_death'].unique())
df_groupby = df.groupby(by='manner_of_death')
print(df['race'].unique())

asian = []
white = []
hispanic =[]
black =[]
other = []
native = []

for key, value in df_groupby:
    print(key)
    count = value.race.value_counts()
    print(count)
    asian.append(count.Asian)
    white.append(count.White)
    hispanic.append(count.Hispanic)
    black.append(count.Black)
    other.append(count.Other)
    native.append(count.Native)

n_groups = 2
# means_frank = (party_seat.Party)
# means_guido = party_seat.Part
# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.097
opacity = 0.8
rects1 = plt.bar(index - bar_width*2, asian, bar_width,alpha=opacity,color='b',label='Asia')
rects2 = plt.bar(index - bar_width*1, white, bar_width,alpha=opacity,color='g',label='White')
rects3 = plt.bar(index + bar_width*0, hispanic, bar_width,alpha=opacity,color='r',label='Hispanic')
rects4 = plt.bar(index + bar_width*1, black, bar_width,alpha=opacity,color='black',label='Black')
rects5 = plt.bar(index + bar_width*2, other, bar_width,alpha=opacity,color='y',label='Other')
rects6 = plt.bar(index + bar_width*3, native, bar_width,alpha=opacity,color='pink',label='Native')
plt.xlabel('Manner of death')
plt.ylabel('Race')
plt.title('shootings')

# label = frequency_2.tolist()
for i in range(2):
    plt.text(x = (i - bar_width*2)-.02 , y = asian[i]+1, s = asian[i], size = 6)
    plt.text(x = (i - bar_width*1)-.02 , y = white[i]+1, s = white[i], size = 6)
    plt.text(x = (i - bar_width*0)-.02 , y = hispanic[i]+1, s = white[i], size = 6)
    plt.text(x = (i + bar_width*1)-.02 , y = black[i]+1, s = white[i], size = 6)
    plt.text(x = (i + bar_width*2)-.02 , y = other[i]+1, s = white[i], size = 6)
    plt.text(x = (i + bar_width*3)-.02 , y = native[i]+1, s = white[i], size = 6)
tic = df['manner_of_death'].unique()
plt.xticks(index + bar_width, tic)
plt.legend()
plt.tight_layout()
plt.show()