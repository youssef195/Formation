#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


data_users=pd.read_excel(r'C:\Users\9820937G\OneDrive - SNCF\Bureau\data_users.xlsx')


# In[3]:


data_users.head(10)


# In[4]:


data_users.dtypes
data_users['money_spent']=data_users['money_spent'].astype('int32')
data_users.dtypes
data_users.head(10)


# In[5]:



data_users.loc[data_users['money_spent']<=0,'has_ordered']=0
data_users.loc[data_users['money_spent']>0,'has_ordered']=1
data_users['has_ordered']=data_users['has_ordered'].astype('int32')
data_users.head(10)


# In[11]:


gender=data_users.groupby(['gender']).size().reset_index(name='count')
gender
y=gender['count']
fig1, ax1 = plt.subplots()
ax1.pie(y, labels=gender['gender'], autopct='%1.0f%%',
        shadow=True, startangle=90)
ax1.axis('equal') 
plt.legend(title = "gender")
plt.title('répartitions des genres')
plt.show()


# In[12]:


spend=data_users.groupby(['account_id']).sum()
spend
x = data_users['money_spent']
bins=range(10,100,10)
plt.hist(x,bins=bins)
plt.title('histogramme du total dargent dépensé pour TOUS les comptes')
plt.xlabel('argents dépensé')
plt.ylabel('account_id')
plt.show() 


# In[13]:



argent=data_users[data_users['has_ordered']==1]
argent
x = argent['money_spent']
bins=range(10,100,10)
plt.hist(x,bins=bins)
plt.title('histogramme du total dargent dépensé UNIQUEMENT pour les comptes ayant dépensé de largent')
plt.xlabel('argents dépensé')
plt.ylabel('has_ordered')
plt.show() 


# In[14]:




data_clients=data_users[data_users['has_ordered']==1]
data_clients=data_clients[data_clients['last_connection_since']>30]
data_clients


# In[16]:


data_clients.loc[(data_clients['money_spent'] >0) & (data_clients['money_spent'] <=50),'reduc']=10
data_clients.loc[(data_clients['money_spent'] >50),'reduc']=20


# In[17]:


def mail(d):
    idc = data_clients.loc[data_users['account_id'] == d]
    Reduction = '10' if idc['money_spent'].values <= 50 else '20'
    return "Bonjour utilisateur " + str(account_id) + " ! Pour récompenser votre fidélité, nous vous offrons " + Reduction + " euros de réductions sur votre prochaine commande." 


# In[18]:


print(mail(30052))
print(mail(92449))
print(mail(70231))


# In[35]:


paris= {'arrondissement':['Paris 1er Arrondissement',
'Paris 2e Arrondissement',
'Paris 3e Arrondissement',
'Paris 4e Arrondissement',
'Paris 5e Arrondissement',
'Paris 6e Arrondissement',
'Paris 7e Arrondissement',
'Paris 8e Arrondissement',
'Paris 9e Arrondissement',
'Paris 10e Arrondissement',
'Paris 11e Arrondissement',
'Paris 12e Arrondissement',
'Paris 13e Arrondissement',
'Paris 14e Arrondissement',
'Paris 15e Arrondissement',
'Paris 16e Arrondissement',
'Paris 17e Arrondissement',
'Paris 18e Arrondissement',
'Paris 19e Arrondissement',
'Paris 20e Arrondissement'],
        'num_aron':[1,
2,
3,
4,
5,
6,
7,
8,
9,
10,
11,
12,
13,
14,
15,
16,
17,
18,
19,
20],
        'm2':[13810,
12350,
12870,
13710,
13000,
15010,
14600,
12620,
11550,
10610,
10980,
10280,
9650,
10750,
10750,
11440,
11220,
10300,
9310,
9640]}

df['m2']=df['m2'].astype('int32')
df.dtypes


# In[36]:


x = df['m2']
y=df['arrondissement']

y_pos = np.arange(len(y))

bars=plt.barh(y_pos, x)
 

plt.yticks(y_pos, y)
 
for  bar in bars:
    width = bar.get_width()
    label_y = bar.get_y() + bar.get_height() / 2
    plt.text(width, label_y, s=f'{width}')
plt.title('prix m2 par arrondisssement')
plt.xlabel('prix moyen aux m2')
plt.ylabel('arrondissement')
plt.show()


# In[37]:


paris.loc[paris['num_aron'] == 3]


# In[18]:


arrondissement = 4
prix_moyen=paris['m2']


def moyen(arrondissement):
    prix_moyen= paris.loc[paris['num_aron'] == arrondissement ,'m2'].iloc[0]
    print("Le prix moyen d'un logement du m2 dans le",arrondissement,"eme arrondissement de Paris est de",prix_moyen,"€.")
    
moyen(arrondissement)


# In[39]:


def marche(surface, prix, arrondissement):
    market_price = get_prix(arrondissement,surface)
    percentage = ((market_price - prix) * 100) / prix
    if percentage > 5:
        return "Ce bien est en dessous du prix du marché"
    elif percentage < -5:
        return "Attention cet appartement parait cher"
    else:
        return "Cet appartement est dans les prix"
marche(100,100,3)


# In[33]:


def arrondissement(budget, surface):
    list_arr = []
    for i, row in paris.iterrows():
        if get_price(row['num_aron'], surface) < budget:
            list_arr.append(row["arrondissement"])
    return list_arr


# In[73]:


uni=pd.read_csv(r'C:\Users\9820937G\OneDrive - SNCF\Bureau\unicorns (2).csv')


# In[74]:


uni.dtypes


# In[76]:


uni.head(10)


# In[77]:


uni['Company'].describe()


# In[88]:


uni2=uni.groupby(['Industry','Country','Company']).mean()
uni2


# In[93]:


fin=uni[uni['Industry']=='Fintech']
fin


# In[97]:


nbcompa=fin['Company'].value_counts()
nbcompa


# In[99]:


fint=fin.groupby(['Country']).size().reset_index(name='count')
fint
y=fint['count']
fig1, ax1 = plt.subplots()
ax1.pie(y, labels=fint['Country'], autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal') 
plt.legend(title = "contry")
plt.show()


# In[ ]:




