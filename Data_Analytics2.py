#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df=pd.read_csv('adult.csv')
df


# In[3]:


df.info()


# In[4]:


#Checking the duplicate rows
duplicate_rows=df[df.duplicated()].count()
duplicate_rows


# In[5]:


#Lets drop duplicate rows
df=df[~df.duplicated()]
df


# In[6]:


#Read the data of df after the removing duplicate data
df.info()


# In[7]:


#Lets check the data
df.describe(include='all')


# In[8]:


df.boxplot(figsize=(20,20))


# In[9]:


#it seems that at final weight lots of outliers found


# # Data cleaning

# In[10]:


#WE can see lots of nan values lets do some of the operation


# In[11]:


from numpy import nan
df = df.replace('?',nan)
df.head()


# In[12]:


df['income'].value_counts()#it seems that less than 50k most of the salary is


# In[13]:


df['income']=df['income'].map({'<=50K': 0, '>50K': 1, '<=50K.': 0, '>50K.': 1})
df.head()


# In[14]:


null_values = df.isnull().sum()
null_values


# In[15]:


null_values = df.isnull().sum()
null_values = pd.DataFrame(null_values,columns=['null'])
j=1
sum_total=len(df)
null_values['percentage'] = null_values['null']/sum_total
round(null_values*100,3).sort_values('percentage',ascending=False)


# From the observation it seems that on occupation,workclass,native-country has null values

# In[16]:


print('workclass',df.workclass.unique())
print('education',df.education.unique())
print('marital-status',df['marital-status'].unique())
print('occupation',df.occupation.unique())
print('relationship',df.relationship.unique())
print('race',df.race.unique())
print('gender',df.gender.unique())
print('native-country',df['native-country'].unique())


# Lets do some operation to the null values present on the 3 columns

# In[17]:


df['native-country'].fillna(df['native-country'].mode()[0],inplace = True)
df['workclass'].fillna(df['workclass'].mode()[0],inplace = True)
df['occupation'].fillna(df['occupation'].mode()[0],inplace = True)


# In[18]:


df.isnull().sum()


# #no null values present operating null values with all the mode in respective columns

# # Univariate and bivariate analysis

# In[19]:


sns.pairplot(df)


# # Age distribution

# In[20]:


df['age'].hist(figsize = (6,6))
plt.show


# By observation age attribute is right-skewed and not symetric. min and max age in btw 17 to 90.

# # Final-Weight distribution

# In[21]:


df['fnlwgt'].hist(figsize = (5,5))
plt.show()


# It seems like Right skewed.

# # Capital gain distribution

# In[22]:


df['capital-gain'].hist(figsize=(5,5))
plt.show()


# Capital-gain shows that either a person has no gain or has gain in a very large amount

# # Capital-loss distribution

# In[23]:


df['capital-loss'].hist(figsize=(5,5))
plt.show()


# most of the capital observed that it stands on 0

# # Relationship between capital-gain and capital-loss

# In[24]:


sns.relplot('capital-gain','capital-loss',data= df)
plt.xlabel('capital-gain')
plt.ylabel('capital-loss')
plt.show()


# 1.both capital-gain and capital-loss can be zero
# 2.if capital-gain is Zero then capital-loss being high or above zero. 
# 3.if capital-loss is Zero then capital-gain being high or above zero.

# # Hours per week distribution

# In[25]:


df['hours-per-week'].hist(figsize=(5,5))
plt.show()


# In this data the hours per week atrribute varies within the range of 1 to 99. By observayion,30-40 hrs people work per week,around 27000 people. There are also few people who works 80-100 hours per week and some less than 20 which is unusual.

# # Workclass distribution

# In[26]:


plt.figure(figsize=(20,10))
sns.countplot(x='workclass',data=df)
plt.show()


# In observation it seems that most of them working Private sector

# # Educational distribution

# In[27]:


plt.figure(figsize=(20,5))
a= sns.countplot(x='education',data=df)
plt.show()


# HS-grade has the highest and pre school has the min

# # Occupational distribution

# In[28]:


plt.figure(figsize=(20,8))
ax = sns.countplot(x="occupation", data=df)
plt.show()


# Prof-specialty has the maximum count. Armed-Forces has minimum samples in the occupation attribute.

# # Income distribution

# In[29]:


plt.figure(figsize=(5,5))
ax = sns.countplot(x="income", data=df)
plt.show()


# Most of them are getting income less than 50k from the observation

# # Age Relationship with Income

# In[30]:


fig = plt.figure(figsize=(5,5))
sns.boxplot(x='income',y='age',data=df).set_title('Box plot of INCOME and AGE')
plt.show()


# Income less than 50k from the median by using boxplot it seems that at the age of 34 and Income greater than 50k from the medain by using boxplot it seems that at the age of 42

# # Workclass  Relationship with Income

# In[31]:


fig = plt.figure(figsize=(10,5))
sns.countplot(x='workclass',hue ='income',data=df).set_title("workclass vs count")
plt.show()


# #a person having income more than 50k and less than 50k are working in private sector only

# # relationship Relationship with income

# In[32]:


plt.figure(figsize=(10,7))
sns.countplot(x="relationship", hue="income",data=df)
plt.show()


# In[33]:


#husband is working more 


# # Relationship between gender and income

# In[34]:


plt.figure(figsize=(20,10))
sns.countplot(x="occupation", hue="gender",data=df)
plt.show()


# In[35]:


#as in craft sector,trnasport female worker is so less than male
#and in armed forces no female worker is been seen


# # race Relationship with income

# In[36]:


plt.figure(figsize=(20,5))
sns.catplot(y="race", hue="income", kind="count",col="gender", data=df)
plt.show()


# In[37]:


sns.heatmap(df.corr())

