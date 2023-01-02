#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Exo : 1 
# Importation des données

# In[2]:


data_users=pd.read_excel(r'C:\Users\9820937G\OneDrive - SNCF\Bureau\data_users.xlsx')


# In[3]:


data_users.head(10)


# Exercice 1, question 2

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


# Exercice 1, question 3A
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


#Exercice1, question 3b
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


# Exercice 1, question 3c
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


#Exercice 1, question 4A
# In[14]:




data_clients=data_users[data_users['has_ordered']==1]
data_clients=data_clients[data_clients['last_connection_since']>30]
data_clients

# Test pour question 4B
# In[16]:


data_clients.loc[(data_clients['money_spent'] >0) & (data_clients['money_spent'] <=50),'reduc']=10
data_clients.loc[(data_clients['money_spent'] >50),'reduc']=20


# Exercice 1, question 4B
# In[17]:


def mail(d):
    idc = data_clients.loc[data_users['account_id'] == d]
    Reduction = '10' if idc['money_spent'].values <= 50 else '20'
    return "Bonjour utilisateur " + str(account_id) + " ! Pour récompenser votre fidélité, nous vous offrons " + Reduction + " euros de réductions sur votre prochaine commande." 


# Exercice 1, question 4C
# In[18]:


print(mail(30052))
print(mail(92449))
print(mail(70231))



















# Mise en place des données
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


# Exerice 2, question 1
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

#Exercice 2, question 2   


# In[100]:

arrondissement_paris = 2
surface_aum2 = 100
arron_n = arrondissement_paris -1

def moyen(arrondissement_paris, surface_aum2):
    prix_moyen = surface_aum2 * arrondissement_paris
    print("Le prix moyen d'un logement de",surface_aum2,"m2 dans le",arrondissement_paris,"eme arrondissement de Paris est de",prix_moyen,"€.")
    
moyen(arrondissement_paris, surface_aum2)
    



# EXO 2, question 3 --- On a fait le choix d''utiliser des dictionnaires pluôt que des data frame pour la 3 & 4

def notif(sur,prix,arr):
    x = sur * paris[arr]
    Y = (prix-x)/x
    if Y <= -0.05:
        print ('au dessous...')
    elif y <0.05:
        print('dans prix')
    else :
        print('attention')

# EXO 2, question 4


def ref(budget, surf):
    l=[]
    x = budget/surf
    for cle,valeur in paris.items():
        if x >= valeur:
            l=l + [cle]
    return l

















#Exercice 3 (6.5pt)
# 
# 1) Importer la base de données 'unicorns.csv' donnant la liste des licornes, leur valorisation, leur secteur et leur pays. Afficher les premières lignes et le nombre de licornes dans la base (1pt)

uni=pd.read_excel(r'C:\Users\9820937G\OneDrive - SNCF\Bureau\unicorns (2).xlsx')
uni
uni.dtypes
uni.head(10)
uni['Company'].describe()


# 2) Trouver quel pays a le plus de licornes dans le domaine de la FinTech (en détaillant la méthode) (1.5pt)
fin=uni[uni['Industry']=='Fintech']
fin

nbcompa=fin['Country'].value_counts()
nbcompa.head(10)

fint=fin.groupby(['Country']).size().reset_index(name='count')
fint
y=fint['count']
fig1, ax1 = plt.subplots()
ax1.pie(y, labels=fint['Country'], autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal') 
plt.legend(title = "contry")
plt.show()

# 3) Créer un dataFrame avec les licornes françaises et l'afficher (1pt)
france=uni[uni['Country']=='France']
france.head(10)

# 4) Ecrire une fonction telle qu'on passe un pays en entrée et qui affiche la valorisation moyenne de ses licornes (1pt)
def pays(pays):
    Country_Licorne = uni[uni.Country == pays]
    return Country_Licorne['Valuation ($B)'].mean()
pays('France')
