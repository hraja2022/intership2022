#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set_style("whitegrid")


# In[2]:


df=pd.read_excel("aspiring_minds_employability_outcomes_2015.xlsx")
df


# In[3]:


#to display all the columns
pd.set_option('display.max_columns',None)


# In[4]:


df


# We can see our dataset consists of
# 1)27 Numerical columns
# 2)9 catogorical columns
# 3)2 datetime

# # Description of dataset

# In[5]:


df.describe()


# In[6]:


#all the datatype in respective column
df.dtypes


# In[7]:


df.isnull().sum()


# In[8]:


#From the dataset no null values found


# # Import the head and shape

# In[9]:


df.head()


# In[10]:


df.shape#as the dataset contains 3998 rows and 39 columns


# # Doing some operation to Missing values

# 1.We can see the DOJ,DOL,DOB are given in timestamp format
# 2.Job city column contains -1 values which are NaN equivalents.
# 3.10 board column contain 0 value which is missing value
# 4.12 board column contain 0 value which is missing value
# 5.college state column contain 'union teritory' which is not a specific state
# 6.Graduation year column contain 0 which is a missing value
# 7.Domain column contain -1 which is a missing value

# In[11]:


import datetime as dt
df["DOJ"]=pd.to_datetime(df["DOJ"]).dt.date
df["DOL"].replace("present",dt.datetime.today(),inplace=True)
df['DOL'] = pd.to_datetime(df['DOL']).dt.date

df['Period'] = pd.to_datetime(df["DOL"]).dt.year - pd.to_datetime(df['DOJ']).dt.year


df['DOB'] = pd.to_datetime(df['DOB']).dt.year
df.head(5)


# In[12]:


#we have worked on the period as how many years the client has worked


# In[13]:


#lets drop 12th grade age column


# In[14]:


df['GraduationYear'].replace(0,df.GraduationYear.mode()[0],inplace=True)
df['GraduationYear']=pd.to_datetime(df['GraduationYear'])
df['gyear']=df['GraduationYear'].dt.year

### New columns which can used to the know 
df['12GradAge']=abs(df['12graduation']-df['DOB'])
df['GradAge']=abs(df['gyear']-df['DOB'])
df.head(5)


# In[15]:


(df==0).astype(int).sum(axis=0)#checking how many 0 values it contains


# In[16]:


df.isin([-1, 'NaN']).sum()


# Designation Column has 'get' value which is a not a desired value.We should clean this and can be imputed with mode of the column.

# In[17]:


df[df["Designation"]=="get"][['Designation','JobCity','Salary','Specialization']]


# from the above observation it seems that (get) contains specialization as 'Mechanical Engineer' as max and "eeg" engineering so lets replace the get value

# In[18]:


mech = df[df['Specialization'].isin(['mechanical engineering','mechanical and automation'])]['Designation'].mode()[0]

eee = df[df['Specialization']==('electronics and electrical engineering')]['Designation'].mode()[0]
print(f'mode for mechanical:  {mech}\nmode for EEE:  {eee}')


# In[19]:


#For mechanical domain
df.loc[df['Specialization'].isin(['mechanical engineering','mechanical and automation']),'Designation'].replace('get',mech,inplace=True)
#for EEE domain,as all previous get's will be replaced,we can replace the remaining directly without conditions
df['Designation'].replace('get',eee,inplace=True)


# In[20]:


#at jobcity it contains the missing values as -1 so lets do operation


# In[21]:


df['JobCity'].replace(-1,'unknown',inplace=True)
df['JobCity'].apply(lambda x:x.title())


# In[22]:


df[df["JobCity"]=='unknown']


# In[23]:


df[df["JobCity"]=="unknown"][["Designation","12GradAge","GradAge","JobCity","Gender","10percentage","10board","12percentage","12board","Degree","Specialization","CollegeState","Specialization"]].mode()


# In[24]:


#lets clean the data
df["JobCity"].replace("Bangalore","Bengaluru",inplace=True)
df["JobCity"].replace("Banaglore","Bengaluru",inplace=True)
df["JobCity"].replace("Chennai, Bangalore","Bengaluru",inplace=True)
df["JobCity"].replace(" Bangalore","Bengaluru",inplace=True)
df["JobCity"].replace("Bangalore ","Bengaluru",inplace=True)
df["JobCity"].replace("Banglore","Bengaluru",inplace=True)
df["JobCity"].replace("Jaipur ","Jaipur",inplace=True)
df["JobCity"].replace("Gandhinagar","Gandhi Nagar",inplace=True)
df["JobCity"].replace("Bangalore ","Bengaluru",inplace=True)
df["JobCity"].replace("Jaipur ","Jaipur",inplace=True)
df["JobCity"].replace("Gandhinagar","Gandhi Nagar",inplace=True)
df["JobCity"].replace("Hyderabad ","Hyderabad",inplace=True)
df["JobCity"].replace("Hyderabad(Bhadurpally)","Hyderabad",inplace=True)
df["JobCity"].replace("Bhubaneswar ","Bhubaneswar",inplace=True)
df["JobCity"].replace("Delhi/Ncr","Delhi",inplace=True)
df["JobCity"].replace("Nagpur ","Nagpur",inplace=True)
df["JobCity"].replace("Pune ","Pune",inplace=True)
df["JobCity"].replace("Trivandrum ","Trivandrum",inplace=True)
df["JobCity"].replace("Thiruvananthapuram","Trivandrum",inplace=True)


# In[25]:


best_mode = []
best_mode.append(df[df["Designation"]=="software engineer"]["JobCity"].mode().to_list()[0])
best_mode.append(df[df["Gender"]=="m"]["JobCity"].mode().to_list()[0])
best_mode.append(df[df["10percentage"]==76]["JobCity"].mode().to_list()[0])
best_mode.append(df[df["10board"]=="cbse"]["JobCity"].mode().to_list()[0])
best_mode.append(df[df["12percentage"]==64]["JobCity"].mode().to_list()[0])
best_mode.append(df[df["12board"]=="cbse"]["JobCity"].mode().to_list()[0])
best_mode.append(df[df["collegeGPA"]==70]["JobCity"].mode().to_list()[0])
best_mode.append(df[df["Salary"]==200000]["JobCity"].mode().to_list()[0])
best_mode.append(df[df["Degree"].str.startswith("B.Tech/")]["JobCity"].mode().to_list()[0])
best_mode.append(df[df["Specialization"].str.startswith("electronics and communication eng")]["JobCity"].mode().to_list()[0])
best_mode.append(df[df["CollegeState"].str.startswith("Uttar Pradesh")]["JobCity"].mode().to_list()[0])
best_mode


# In[26]:


# We can see mode from the best_mode list is 'Bangalore'
df["JobCity"].replace("unknown",'Bengaluru',inplace=True)


# In[27]:


#column having missing values as 0 lets replace with mode values
df[df["10board"]==0][["Designation","12GradAge","GradAge","JobCity","Gender","10percentage","10board","12percentage","12board","Degree","Specialization","CollegeState","Specialization"]].mode()


# In[28]:


### Same process as above written for jobcity
best_value2=[]
best_value2.append(df[df["Designation"]=="software engineer"]["10board"].mode().to_list()[0])
best_value2.append(df[df["Gender"]=="m"]["10board"].mode().to_list()[0])
best_value2.append(df[df["10percentage"]==75]["10board"].mode().to_list()[0])
best_value2.append(df[df["JobCity"]=="Bengaluru"]["10board"].mode().to_list()[0])
best_value2.append(df[df["12percentage"]==65]["10board"].mode().to_list()[0])
best_value2.append(df[df["collegeGPA"]==65]["10board"].mode().to_list()[0])
best_value2.append(df[df["Salary"]==400000]["10board"].mode().to_list()[0])
best_value2.append(df[df["Degree"].str.startswith("B.Tech/")]["10board"].mode().to_list()[0])
best_value2.append(df[df["Specialization"].str.startswith("computer eng")]["10board"].mode().to_list()[0])
best_value2.append(df[df["CollegeState"].str.startswith("Tamil Nadu")]["10board"].mode().to_list()[0])
best_value2


# In[29]:


df['10board'].replace(0,'cbse',inplace=True)


# In[30]:


df['12board'].replace(0,'cbse',inplace=True)


# In[31]:


plt.figure(figsize=(20,10))
sns.boxplot(df['Domain'])
plt.show()


# In[32]:


## As we can see outlier,it is better to use median to replace the missing values.
df['Domain'].replace(-1,df['Domain'].median(),inplace=True)
df.head()


# In[33]:


#replacing the redundant values of the 12board column with 'state','cbse','icse' and 'n/a'
replace_list_state=['board of intermediate education,ap', 'state board',
       'mp board',  'karnataka pre university board', 'up',
       'p u board, karnataka', 'dept of pre-university education', 'bie',
       'kerala state hse board', 'up board', 'bseb', 'chse', 'puc',
       ' upboard',
       'state  board of intermediate education, andhra pradesh',
       'karnataka state board',
       'west bengal state council of technical education', 'wbchse',
       'maharashtra state board', 'ssc',
       'sda matric higher secondary school', 'uttar pradesh board', 'ibe',
       'chsc', 'board of intermediate', 'upboard', 'sbtet',
       'hisher seconadry examination(state board)', 'pre university',
       'borad of intermediate', 'j & k board',
       'intermediate board of andhra pardesh', 'rbse',
       'central board of secondary education', 'jkbose', 'hbse',
       'board of intermediate education', 'state', 'ms board', 'pue',
       'intermediate state board', 'stateboard', 'hsc',
       'electonincs and communication(dote)', 'karnataka pu board',
       'government polytechnic mumbai , mumbai board', 'pu board',
       'baord of intermediate education', 'apbie', 'andhra board',
       'tamilnadu stateboard',
       'west bengal council of higher secondary education',
       'cbse,new delhi', 'u p board', 'intermediate', 'biec,patna',
       'diploma in engg (e &tc) tilak maharashtra vidayapeeth',
       'hsc pune', 'pu board karnataka', 'kerala', 'gsheb',
       'up(allahabad)', 'nagpur', 'st joseph hr sec school',
       'pre university board', 'ipe', 'maharashtra', 'kea', 'apsb',
       'himachal pradesh board of school education', 'staae board',
       'international baccalaureate (ib) diploma', 'nios',
       'karnataka board of university',
       'board of secondary education rajasthan', 'uttarakhand board',
       'ua', 'scte vt orissa', 'matriculation',
       'department of pre-university education', 'wbscte',
        'preuniversity board(karnataka)', 'jharkhand accademic council',
       'bieap', 'msbte (diploma in computer technology)',
       'jharkhand acamedic council (ranchi)',
       'department of pre-university eduction', 'biec',
       'sjrcw', ' board of intermediate', 'msbte',
       'sri sankara vidyalaya', 'chse, odisha', 'bihar board',
       'maharashtra state(latur board)', 'rajasthan board', 'mpboard',
       'state board of technical eduction panchkula', 'upbhsie', 'apbsc',
       'state board of technical education and training',
       'secondary board of rajasthan',
       'tamilnadu higher secondary education board',
       'jharkhand academic council',
       'board of intermediate education,hyderabad', 'up baord', 'pu',
       'dte', 'board of secondary education', 'pre-university',
       'board of intermediate education,andhra pradesh',
       'up board , allahabad', 'srv girls higher sec school,rasipuram',
       'intermediate board of education,andhra pradesh',
       'intermediate board examination',
       'department of pre-university education, bangalore',
       'stmiras college for girls', 'mbose',
       'department of pre-university education(government of karnataka)',
       'dpue', 'msbte pune', 'board of school education harayana',
       'sbte, jharkhand', 'bihar intermediate education council, patna',
       'higher secondary', 's j polytechnic', 'latur',
       'board of secondary education, rajasthan', 'jyoti nivas', 'pseb',
       'biec-patna', 'board of intermediate education,andra pradesh',
       'chse,orissa', 'pre-university board', 'mp', 'intermediate board',
       'govt of karnataka department of pre-university education',
       'karnataka education board',
       'board of secondary school of education', 'pu board ,karnataka',
       'karnataka secondary education board', 'karnataka sslc',
       'board of intermediate ap', 'u p', 'state board of karnataka',
       'directorate of technical education,banglore', 'matric board',
       'andhpradesh board of intermediate education',
       'stjoseph of cluny matrhrsecschool,neyveli,cuddalore district',
       'bte up', 'scte and vt ,orissa', 'hbsc',
       'jawahar higher secondary school', 'nagpur board', 'bsemp',
       'board of intermediate education, andhra pradesh',
       'board of higher secondary orissa',
       'board of secondary education,rajasthan(rbse)',
       'board of intermediate education:ap,hyderabad', 'science college',
       'karnatak pu board', 'aissce', 'pre university board of karnataka',
       'bihar', 'kerala state board', 'uo board', 
       'karnataka board', 'tn state board',
       'kolhapur divisional board, maharashtra',
       'jaycee matriculation school',
       'board of higher secondary examination, kerala',
       'uttaranchal state board', 'intermidiate', 'bciec,patna', 'bice',
       'karnataka state', 'state broad', 'wbbhse', 'gseb',
       'uttar pradesh', 'ghseb', 'board of school education uttarakhand',
       'gseb/technical education board', 'msbshse,pune',
       'tamilnadu state board', 'board of technical education',
       'kerala university', 'uttaranchal shiksha avam pariksha parishad',
       'chse(concil of higher secondary education)',
       'bright way college, (up board)', 'board of intermidiate',
       'higher secondary state certificate', 'karanataka secondary board',
       'maharashtra board', 'cgbse', 'diploma in computers', 'bte,delhi',
       'rajasthan board ajmer', 'mpbse', 'pune board', 
        'state board of technical education', 'gshseb',
       'amravati divisional board', 'dote (diploma - computer engg)',
       'karnataka pre-university board', 'jharkhand board',
       'punjab state board of technical education & industrial training',
       'department of technical education',
       'sri chaitanya junior kalasala', 'state board (jac, ranchi)',
       'aligarh muslim university', 'tamil nadu state board', 'hse',
       'karnataka secondary education', 'state board ',
       'karnataka pre unversity board',
       'ks rangasamy institute of technology',
       'karnataka board secondary education', 'narayana junior college',
       'bteup', 'board of intermediate(bie)', 'hsc maharashtra board',
        'tamil nadu state', 'uttrakhand board', 'psbte',
       'stateboard/tamil nadu', 'intermediate council patna',
       'technical board, punchkula', 'board of intermidiate examination',
       'sri kannika parameswari highier secondary school, udumalpet',
       'ap board', 'nashik board', 'himachal pradesh board',
       'maharashtra satate board',
       'andhra pradesh board of secondary education',
       'tamil nadu polytechnic',
       'maharashtra state board mumbai divisional board',
       'department of pre university education',
       'dav public school,hehal', 'board of intermediate education, ap',
       'rajasthan board of secondary education',
       'department of technical education, bangalore', 'chse,odisha',
        'maharashtra nasik board',
       'west bengal council of higher secondary examination (wbchse)',
       'holy cross matriculation hr sec school', 'cbsc',
       'pu  board karnataka', 'biec patna', 'kolhapur', 'bseb, patna',
       'up board allahabad', 'nagpur board,nagpur', 'diploma(msbte)',
       'dav public school', 'pre university board, karnataka',
       'ssm srsecschool', 'state bord', 'jstb,jharkhand',
       'intermediate board of education', 'mp board bhopal', 'pub',
       'madhya pradesh board', 'bihar intermediate education council',
       'west bengal council of higher secondary eucation',
        'mpc','certificate for higher secondary education (chse)orissa',
       'maharashtra state board for hsc',
       'board of intermeadiate education', 'latur board',
       'andhra pradesh', 'karnataka pre-university',
       'lucknow public college', 'nagpur divisional board',
       'ap intermediate board', 'cgbse raipur', 'uttranchal board',
       'jiec', 
       'bihar school examination board patna',
       'state board of technical education harayana', 'mp-bse',
       'up bourd', 'dav public school sec 14',
       'haryana state board of technical education chandigarh',
       'council for indian school certificate examination',
       'jaswant modern school', 'madhya pradesh open school',
        'aurangabad board', 'j&k state board of school education',
       'diploma ( maharashtra state board of technical education)',
       'board of technicaleducation ,delhi',
       'maharashtra state boar of secondary and higher secondary education',
       'hslc (tamil nadu state board)',
       'karnataka state examination board', 'puboard', 'nasik',
       'west bengal board of higher secondary education',
       'up board,allahabad', 'board of intrmediate education,ap', 
       'karnataka state pre- university board',
       'state board - west bengal council of higher secondary education : wbchse',
       'maharashtra state board of secondary & higher secondary education',
       'biec, patna', 'state syllabus', 'cbse board', 'scte&vt',
       'board of intermediate,ap',
       'secnior secondary education board of rajasthan',
       'maharashtra board, pune', 'rbse (state board)',
       'board of intermidiate education,ap',
       'board of high school and intermediate education uttarpradesh',
       'higher secondary education',
       'board fo intermediate education, ap', 'intermedite',
       'ap board for intermediate education', 'ahsec',
       'punjab state board of technical education & industrial training, chandigarh',
       'state board - tamilnadu', 'jharkhand acedemic council',
       'scte & vt (diploma)', 'karnataka pu',
       'board of intmediate education ap', 'up-board',
       'boardofintermediate','intermideate','up bord','andhra pradesh state board','gujarat board']             


# In[34]:


#replacing the redundant values of the 12board column with 'state','cbse','icse' 
for i in replace_list_state:
    df['12board'].replace(i,'state',inplace=True)

replace_list_cbse=['cbse', 
       'all india board', 
       'central board of secondary education, new delhi', 'cbese']
for i in replace_list_cbse:
    df['12board'].replace(i,'cbse',inplace=True)

replace_list_icse=[ 'isc', 'icse', 'isc board', 'isce', 'cicse',
       'isc board , new delhi']
for i in replace_list_icse:
    df['12board'].replace(i,'icse',inplace=True)

df['12board'].unique()


# In[35]:


specialization_map = {'electronics and communication engineering' : 'EC',
 'computer science & engineering' : 'CS',
 'information technology' : 'CS' ,
 'computer engineering' : 'CS',
 'computer application' : 'CS',
 'mechanical engineering' : 'ME',
 'electronics and electrical engineering' : 'EC',
 'electronics & telecommunications' : 'EC',
 'electrical engineering' : 'EL',
 'electronics & instrumentation eng' : 'EC',
 'civil engineering' : 'CE',
 'electronics and instrumentation engineering' : 'EC',
 'information science engineering' : 'CS',
 'instrumentation and control engineering' : 'EC',
 'electronics engineering' : 'EC',
 'biotechnology' : 'other',
 'other' : 'other',
 'industrial & production engineering' : 'other',
 'chemical engineering' : 'other',
 'applied electronics and instrumentation' : 'EC',
 'computer science and technology' : 'CS',
 'telecommunication engineering' : 'EC',
 'mechanical and automation' : 'ME',
 'automobile/automotive engineering' : 'ME',
 'instrumentation engineering' : 'EC',
 'mechatronics' : 'ME',
 'electronics and computer engineering' : 'CS',
 'aeronautical engineering' : 'ME',
 'computer science' : 'CS',
 'metallurgical engineering' : 'other',
 'biomedical engineering' : 'other',
 'industrial engineering' : 'other',
 'information & communication technology' : 'EC',
 'electrical and power engineering' : 'EL',
 'industrial & management engineering' : 'other',
 'computer networking' : 'CS',
 'embedded systems technology' : 'EC',
 'power systems and automation' : 'EL',
 'computer and communication engineering' : 'CS',
 'information science' : 'CS',
 'internal combustion engine' : 'ME',
 'ceramic engineering' : 'other',
 'mechanical & production engineering' : 'ME',
 'control and instrumentation engineering' : 'EC',
 'polymer technology' : 'other',
 'electronics' : 'EC'}


# In[36]:


df['Specialization'] = df['Specialization'].map(specialization_map)
df['Specialization'].unique()


# # Univariate Analysis at all the numerical values

# In[37]:


df.drop(columns=['CollegeID','CollegeCityID','CollegeCityTier'],axis=1,inplace=True)


# In[38]:


df.loc[df['Salary']<=50000,'Salary']*=12
lst = ['ComputerProgramming','ElectronicsAndSemicon','ComputerScience','MechanicalEngg','ElectricalEngg','TelecomEngg','CivilEngg']
for i in lst:
    df[i].replace(-1,0,inplace=True)


# In[39]:


#filtering out all the num values to find outliers
df_num = df._get_numeric_data()
df_num


# In[40]:


df_num.hist(figsize=(15,20))


# In[81]:


from seaborn import distplot
distplot(df["10percentage"])


# In[82]:


sns.distplot(df["12percentage"],hist=True,color="g")


# In[83]:


sns.distplot(df["collegeGPA"],hist=True,color="y")


# In[41]:


#Salary-from the histogram its been observed that salary having outliers
#English-It is normally distributed column
#Logical-It is normally distributed column
#Quant-It is normally distributed column
#TelecomEngg-Over here ouliers found
#CivilEngg-No outliers found
#Conscientiousness-No outliers found in this column,it is slight left skewness
#Agreeableness-Since no ouliers found 
#Extraversion-It is normally distrbuted data
#Nueroticism-Is normally distributed data,no outliers found
#Openess_to_experience-Outliers are found ,in which some of the ID having less than 0 experience


# # Univariate analysis at the categorical values

# In[42]:


df.groupby(['Designation']).sum()#it is found that 419 unique designation from all the dataset


# In[43]:


freq_table=df.groupby(['Designation']).size().reset_index(name='Count')
freq_table


# Observation:
# 1)It is found that 419 unique designation found from all the dataset.
# 2)Frequency of every Designation is found

# In[44]:


df.groupby(['JobCity']).sum() 


# In[45]:


freq_table=df.groupby(['JobCity']).size().reset_index(name='Count')
freq_table.iloc[1: , :]


# Observations:
# 1)338 unique jobcity found on complete dataset
# 2)Frequency of the complete job city is observed.

# In[46]:


df.groupby(['Gender']).count()#As female count is less than male from the dataset given


# In[47]:


df.groupby(['10board']).sum()#275 unique 10th board found on dataset


# In[48]:


df.groupby(['12board']).sum()#340 unique board found on the 12th borad


# In[49]:


df.boxplot(figsize=(50,40))


# #Observations-
# Since it is seems that in salary there is so much of outliers found

# - Research Questions
# - Times of India article dated Jan 18, 2019 states that “After doing your Computer Science
# Engineering if you take up jobs as a Programming Analyst, Software Engineer,
# Hardware Engineer and Associate Engineer you can earn up to 2.5-3 lakhs as a fresh
# graduate.” Test this claim with the data given to you.

# In[50]:


df['ComputerScience'].hist()


# In[51]:


df.groupby(['ComputerScience','Designation']).sum()


# In[52]:


freq_table=df.groupby(['ComputerScience','Designation']).size().reset_index(name='Count')
freq_table


# In[53]:


freq_table=df.groupby(['ComputerScience','Designation']).size().reset_index(name='Count')
freq_table.max()


# #from the observation it seems that after taking computer Science stream 395 graduates have opted for windows systems administrator
# for the highest number of person has been chosen windows systems administrator

# In[54]:


freq_table=df.groupby(['ComputerScience','Designation']).size().reset_index(name='Count')
sorted=freq_table.sort_values(by='Count')
sorted.iloc[-1]


# #Even it seems that 395 software engineer opted and made a sucessfully transition after taking Computer Science graduates
# in the same way let see 2nd highest and 3rd highest

# In[55]:


freq_table=df.groupby(['ComputerScience','Designation']).size().reset_index(name='Count')
sorted=freq_table.sort_values(by='Count')
sorted.iloc[-2]


# In[56]:


freq_table=df.groupby(['ComputerScience','Designation']).size().reset_index(name='Count')
sorted=freq_table.sort_values(by='Count')
sorted.iloc[-3]


# In[57]:


df.groupby(['Gender','Specialization']).size()


# In[58]:


d=df.groupby(['Gender','Specialization'])
dd=pd.DataFrame(d)


# In[59]:


d=df.groupby(['Gender','Specialization']).size().reset_index(name='Count')
dd=pd.DataFrame(d)
dd


# In[60]:


plt.figure(figsize=(15,5))
colors = sns.color_palette('bright',n_colors=2)
sns.FacetGrid(df, col="Gender", size=5,palette=colors)    .map(sns.distplot, "Salary",bins=50)    .add_legend()
plt.show()
#relationship between salary and gender


# Observations-
# We can observe that the salary data is right skewed.
# We can also see that the distributions are quite similar for male and female in the range below 10lakhs.

# In[61]:


plt.figure(figsize=(10,5))
sns.boxplot(x='Salary',y='Gender',data=df)


# It is noted that there are many outliers in the salary data
# There is not much difference between median salary for both genders.
# We can also observe male have more outliers indicating they are more people getting higher pays in male than female category

# In[62]:


plt.figure(figsize=(15,5))
sns.boxplot(x='Salary',y='Specialization',data=df)
plt.suptitle('Salary levels by specialization')


# Median salary of people from all specializations are nearly similar.
# We can see there are more people getting higher pays who have specialization in CS/EC compared to others.

# In[63]:


### Designation
popular_Designation = df['Designation'].value_counts()[:20].index.tolist()
print(popular_Designation)


# In[64]:


### We want on
top_Designations = df[df['Designation'].isin(popular_Designation)]
print(f"Unique professions : {len(df['Designation'].unique())}")
top_Designations.head()


# In[65]:


plt.figure(figsize=(20,10))
sns.countplot(x='Designation',hue='Gender',data=top_Designations)
plt.xticks(fontsize=30,rotation=90)
plt.yticks(fontsize=30)
plt.show()


# # Relationship between gender and specialization

# 1)All the general professions are more dominated by the males as we can there is considerable difference of frequency for every role.
# 2)Here we took the most common roles taken by the amcat aspirants which are mostly 'IT Roles'.
# 3)from the below plot,we can understand the reason for most 'IT roles' might be because of Specialization.

# In[66]:


sns.countplot(df['Specialization'])


# In[67]:


#as from above observation most of them opted CS


# In[68]:


sns.countplot(df['Degree'])


# In[69]:


#as most of them opted for CS/btech


# In[70]:


plt.figure(figsize=(20,10))
sns.barplot(x='Designation',y='Salary',hue='Gender',data=top_Designations)
plt.xticks(fontsize=30,rotation=90)
plt.yticks(fontsize=30)
plt.show()


# In[71]:


#from the observation it seems that senios software engineer are paid well
#mean salary of top most frequent roles is nearly independent of gender.
#there is some considerable difference in some roles.but we cannot be sure that women is being paid less in that role
#it might be due to experience,specialization etc.


# In[72]:


high = list(df.sort_values("Salary",ascending=False)["Designation"].unique())[:20]
high_pay = df[df['Designation'].isin(high)]
high_pay.head()


# In[73]:


plt.figure(figsize=(20,10))
sns.barplot(x='Designation',y='Salary',hue='Gender',data=high_pay)
plt.xticks(fontsize=30,rotation=90)
plt.yticks(fontsize=30)
plt.show()


# 1)Most of the high paying jobs are from IT domain.
# 2)In 45% of top paying roles,men are generally paid higher compared to women.
# 3)In 20% of top paying roles,women are paid higher than men
# 4)In roles like junior manager,sales account manager,software engineer trainee there are no women working in these fields.
# 5)Junior manager is highest paying for men and field engineer is the highest paying role for women.
# 6)The disperancy between pay based on gender might be because of other features like experience,specialization etc.
# 7)Software Enginner and Software developer are most frequent and highest paying jobs

# Overall conclusion-
# 1.Most of Amcat Aspirants are male working in IT domain with an experience of around 5years with degree in Btech and specialization in Computer Science/Information Technology from tier-2 college in uttarpradesh with an average salary around 300k.
# 2.Highpaying jobs taken up by amcat aspirants are mostly from 'IT' Domain.
# 3.Software Engineer and Software Developer are the most aimed profession for amcat aspirants.
