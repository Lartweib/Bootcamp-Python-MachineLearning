import os
import pandas as pd
import plotnine as gg
import numpy as np
import warnings
import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly.tools as tls
import seaborn as sns

#clean console
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

train = pd.read_csv('~/PycharmProjects/titanic/train.csv')

test = pd.read_csv('~/PycharmProjects/titanic/test.csv')

train.head()

survived_sex = pd.crosstab(index=train["Survived"],
                           columns=train["Sex"])
survived_class = pd.crosstab(index=train["Survived"],
                           columns=train["Pclass"])
survived_age = pd.crosstab(index=train["Survived"],
                           columns=train["Age"])
survived_em = pd.crosstab(index=train["Survived"],
                           columns=train["Embarked"])
survived_sib = pd.crosstab(index=train["Survived"],
                           columns=train["SibSp"])
survived_parch = pd.crosstab(index=train["Survived"],
                           columns=train["Parch"])

survived_class.index= ["died","survived"]
survived_sex.index= ["died","survived"]
survived_age.index= ["died","survived"]
survived_em.index= ["died","survived"]
survived_sib.index= ["died","survived"]
survived_parch.index= ["died","survived"]

survived_class
survived_sex
survived_age
survived_em
survived_sib
survived_parch

survived_age.tail


sns.catplot(y="Age", x="Survived", hue="Pclass", data=train,kind="swarm")
plt.show()

sns.catplot(y="Age", x="Survived", hue="Sex", data=train,kind="swarm")
plt.show()

sns.catplot(y="SibSp", x="Parch", hue="Survived", data=train,kind="swarm",s=2)
plt.show()




survived_age.isnull().describe()

cabin_tab = pd.crosstab(index=train["Cabin"],
                        columns="count")

cabin_tab

def char_rem():
    global train
    train.Cabin.fillna('T', inplace = True)

    train['Cabin'] = train ['Cabin'].map(lambda c: c[0])

    cabin_dummies = pd.get_dummies(train['Cabin'],prefix='Cabin')
    train=pd.concat([train,cabin_dummies)], axis=1)

    train.drop('Cabin', axis=1, inplace=True)
    return train


cabin_tab/cabin_tab.sum()


cabin= train[["Cabin"]]

c=cabin.iloc[1]
c[0][0]
c.values[0][0][0]

c2=cabin.iloc[3][0]
c2[0][0]


cabin.charAt(0); // Returns "f"

plt.plot(train[["Survived"]])

plt.show(train[["Survived"]])

plt.plot(train[["Survived"]],train[["Pclass"]])

plt.show()

plt.plot(train[["Survived"]],train[["Age"]])
plt.show()

my_tab = pd.crosstab(index=train["Survived"],
                              columns="n")

my_tab


mpl_fig = plt.figure()
ax = mpl_fig.add_subplot(111)

ax.boxplot(data)

plotly_fig = tls.mpl_to_plotly( mpl_fig )
py.iplot(plotly_fig, filename='mpl-multiple-boxplot')

import re
deck = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "U": 8}
data = [train, test]

for dataset in data:
    dataset['Cabin'] = dataset['Cabin'].fillna("U0")
    dataset['Deck'] = dataset['Cabin'].map(lambda x: re.compile("([a-zA-Z]+)").search(x).group())
    dataset['Deck'] = dataset['Deck'].map(deck)
    dataset['Deck'] = dataset['Deck'].fillna(0)
    dataset['Deck'] = dataset['Deck'].astype(int)
# we can now drop the cabin feature
train_df = train.drop(['Cabin'], axis=1)
test_df = test.drop(['Cabin'], axis=1)

data = [train_df, test_df]

for dataset in data:
    mean = train_df["Age"].mean()
    std = test_df["Age"].std()
    is_null = dataset["Age"].isnull().sum()
    # compute random numbers between the mean, std and is_null
    rand_age = np.random.randint(mean - std, mean + std, size = is_null)
    # fill NaN values in Age column with random values generated
    age_slice = dataset["Age"].copy()
    age_slice[np.isnan(age_slice)] = rand_age
    dataset["Age"] = age_slice
    dataset["Age"] = train_df["Age"].astype(int)
train_df["Age"].isnull().sum()

genders = {"male": 0, "female": 1}
data = [train_df, test_df]

for dataset in data:
    dataset['Sex'] = dataset['Sex'].map(genders)
