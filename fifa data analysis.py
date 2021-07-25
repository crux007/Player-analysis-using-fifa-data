#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib as plt
import seaborn as sns
import pandas as pd


# In[2]:


sns.set_style('darkgrid')


# In[3]:


plt.rc('axes', titlesize=18)
plt.rc('axes', labelsize=14)
plt.rc('xtick', labelsize=13)
plt.rc('ytick', labelsize=13)
plt.rc('legend', fontsize=13)
plt.rc('font', size=13)


# In[4]:


sns.color_palette('deep')[0]


# In[9]:


from matplotlib import figure


# In[10]:


f = figure.Figure(figsize=(9,5), tight_layout=True)


# In[12]:


from matplotlib import *


# In[14]:


import matplotlib.pyplot as plt


# In[21]:


plt.hist(..., color=sns.color_palette('Set2')[2], linewidth=2)


# In[19]:


fig, ax = plt.subplots(nrows=1,ncols=2, figsize=(12,5), tight_layout=True)


# In[22]:


plt.xlabel('Nationality')
plt.ylabel('Average Rating')
plt.title('Barplot')


# In[27]:


df_fifa21 = pd.read_csv('players_20.csv')
country = ['United States', 'Canada', 'England', 'Brazil', 'Argentina']
df_country = df_fifa21[df_fifa21['nationality'].isin(country)]


# In[28]:


barplot = df_country.groupby(['nationality'], as_index=False).mean()[['nationality', 'overall']]


# In[29]:


plt.figure(figsize=(9,5), tight_layout=True)
colors = sns.color_palette('pastel')

plt.bar(barplot['nationality'], barplot['overall'], color=colors[:5])

plt.xlabel('Nationality')
plt.ylabel('Average Rating')
plt.title('Barplot')
plt.show()


# In[35]:


new_df = pd.concat(
    [df_country[df_country['nationality']=='Argentina'][:20],
     df_country[df_country['nationality']=='Brazil'][:20],
     df_country[df_country['nationality']=='England'][:20],
     df_country[df_country['nationality']=='Canada'][:20],
     df_country[df_country['nationality']=='United States'][:20]]
     )
barplot = new_df.groupby(['nationality'], as_index=False).mean() [['nationality', 'overall']]


# In[37]:


plt.figure(figsize=(9,5), tight_layout=True)
ax = sns.barplot(x=barplot['nationality'], y=barplot['overall'], palette='pastel', ci=None)
ax.set(title='Barplot', xlabel='Nationality', ylabel='Average Rating')
plt.show()


# In[38]:


barplot = df_country[df_country['league_name'].isin(['Spain Primera Division', 'Italian Serie A', 'German 1. Bundesliga'])]
barplot = barplot.groupby(['nationality', 'league_name'], as_index=False).count()


# In[39]:


plt.figure(figsize=(14,7), tight_layout=True)
ax = sns.barplot(x=barplot['nationality'], y=barplot['sofifa_id'], hue=barplot['league_name'], palette='pastel')
ax.set(title='No of Players outside of domestic league',xlabel='Country',ylabel='Count')
ax.legend(title='League', title_fontsize='13', loc='upper right')
plt.show()


# In[40]:


plt.figure(figsize=(12,6), tight_layout=True)
bins = [160, 165, 170, 175, 180, 185, 190, 195, 200]

plt.hist(df_country['height_cm'], bins=bins, color=sns.color_palette('Set2')[2], linewidth=2)
plt.title('Histogram')
plt.xlabel('Height (cm)')
plt.ylabel('Count')


# In[42]:


plt.figure(figsize=(12,6), tight_layout=True)
bins = [160, 165, 170, 175, 180, 185, 190, 195, 200]

ax = sns.histplot(data=df_country, x='height_cm', bins=bins, color=sns.color_palette('Set2')[2], linewidth=2)
ax.set(title='Histogram', xlabel='Height', ylabel='Count')
plt.show()


# In[43]:


#distribution of height in players from different nations
plt.figure(figsize=(12,6), tight_layout=True)
ax = sns.boxplot(data=df_country, x='nationality', y='height_cm', palette='Set2', linewidth=2.5)
ax.set(title='Boxplot', xlabel='', ylabel='Height (cm)')
plt.show()


# In[44]:


#relationship between height and weight of players
plt.figure(figsize=(10,6), tight_layout=True)
ax = sns.scatterplot(data=df_country, x='height_cm', y='weight_kg', hue='nationality', palette='Set2', s=60)
ax.set(xlabel='Height (cm)',ylabel='Weight (kg)')
ax.legend(title='Country', title_fontsize=12)
plt.show()


# In[45]:


# value of players
piechart = df_fifa21[df_fifa21['club_name']=='Chelsea']
piechart = piechart.sort_values('value_eur', ascending=False)
[['short_name', 'value_eur']]
piechart = piechart[:11]


# In[46]:


color = sns.color_palette('pastel')
plt.figure(figsize=(8,7), tight_layout=True)
explode_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.2]
plt.pie(piechart['value_eur'], labels=piechart['short_name'],autopct='%.0f %%', explode=explode_list, pctdistance=.7, colors=colors, shadow=True)
plt.title('Chelsea', weight='bold')
plt.show()


# In[47]:


# impact of player in his club and national team
fig, ax = plt.subplots(1,2,figsize=(13,6), tight_layout=True)

piechart2 = df_fifa21[df_fifa21['nationality']=='United States']
piechart2 = piechart2[:10].sort_values('value_eur')[['short_name', 'value_eur']]


# In[50]:


colors = sns.color_palette('pastel')
explode_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.2]
ax[0].pie(piechart['value_eur'], labels=piechart['short_name'],autopct='%.0f %%', explode=explode_list, pctdistance=.7, colors=colors, shadow=True)
ax[0].set_title('Chelsea', weight='bold')

explode_list = [0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ax[1].pie(piechart2['value_eur'], labels=piechart2['short_name'], autopct='%.0f %%', explode=explode_list, pctdistance=.7,  colors=colors, shadow=True)
ax[1].set_title('USA', weight='bold')
plt.show()


# In[52]:


#rating
df_fifa21 = pd.read_csv('players_21.csv')
df_fifa20 = pd.read_csv('players_20.csv')
df_fifa19 = pd.read_csv('players_19.csv')
df_fifa18 = pd.read_csv('players_18.csv')
df_fifa17 = pd.read_csv('players_17.csv')
frames = [df_fifa17, df_fifa18, df_fifa19, df_fifa20, df_fifa21]
for i, frame in enumerate(frames):
    frame['year'] = 2017 + i
    
lineplot = pd.concat(frames)[['short_name', 'overall', 'year']]
list_players = ['L. Messi', 'Cristiano Ronaldo', 'K. De Bruyne', 'K. Mbappé', 'V. van Dijk']
lineplot = lineplot[lineplot['short_name'].isin(list_players)]
lineplot = lineplot.pivot(index='short_name', columns='year' ,values='overall').T
lineplot.reset_index(inplace=True)
lineplot = lineplot.set_index('year')


# In[53]:


plt.figure(figsize=(10,6), tight_layout=True)

plt.plot(lineplot, 'o-', linewidth=2)

plt.xticks([2017, 2018, 2019, 2020, 2021])
plt.xlabel('Years')
plt.ylabel('Ratings')
plt.title('Rating troughtout the years')
plt.legend(title='Players', title_fontsize = 13, labels=['L. Messi', 'Cristiano Ronaldo', 'K. De Bruyne', 'V. van Dijk', 'K. Mbappé'])
plt.show()


# In[ ]:




