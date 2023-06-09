#!/usr/bin/env python
# coding: utf-8

# # NECCESSORY LIBRARIES

# In[1]:


import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# ### IMPORTDATA

# In[2]:


raw_data = pd.read_csv("mail_data.csv")


# In[3]:


raw_data.head


# ### REPLACE NULL VALUES WITH NULL STRINGS

# In[4]:


mail_data = raw_data.where((pd.notnull(raw_data)),'')


# In[5]:


mail_data.shape


# ### LABLE ENCODING

# ### SPAM = 0 & HAM = 1

# In[6]:


mail_data.loc[mail_data['Category'] == 'spam', 'Category',] = 0
mail_data.loc[mail_data['Category'] == 'ham', 'Category',] = 1


# In[7]:


mail_data.head


# ### SEPARATING THE DATA AS TEXT & LABELS

# In[8]:


x = mail_data["Message"]
y = mail_data["Category"]


# In[9]:


print(x)


# In[10]:


print(y)


# ### SPLITING THE DATA

# In[11]:


x_train, x_test, y_train, y_test= train_test_split(x, y, test_size =0.2, random_state =3)


# In[12]:


print(x_train.shape)
print(x_test.shape)


# ### FEATURE EXTRACTION

# #### TRANASFORM THE TEXT DATA INTO FEATURE VECTOR

# In[13]:


feature_extraction = TfidfVectorizer(min_df = 1, stop_words = "english", lowercase= 'True')
x_train_features =  feature_extraction.fit_transform(x_train)
x_test_features =  feature_extraction.transform(x_test)


# #### CONVERT Y_TEST & Y_TRAIN VALUES IN INTEGERS

# In[14]:


y_train = y_train.astype('int')
y_test = y_test.astype('int')


# ## TRAINIG THE MODEL

# In[15]:


model = LogisticRegression()


# ### TRAINING THE MODEL WITH TRAIRNING DATA

# In[16]:


model.fit(x_train_features, y_train)


# ### EVALUATING THE TRAINIG MODEL

# #### PREDICTION ON TRAINING DATA

# In[17]:


prediction_on_training_data = model.predict(x_train_features)
accuracy_on_training_data = accuracy_score(y_train, prediction_on_training_data)


# In[18]:


print("Accuracy on training data : ", accuracy_on_training_data)


# #### PREDICTION ON TRAINING DATA

# In[19]:


prediction_on_test_data = model.predict(x_test_features)
accuracy_on_test_data = accuracy_score(y_test, prediction_on_test_data)
 


# In[20]:


print("Accuracy on test data : ", accuracy_on_test_data)


# # BUILDING THE PREDICTIVE SYSYTEM
# 

# In[21]:


input_mail = [""]


# #### CONVERT THE TEXT TO FEACTURE VECTORE

# In[22]:


input_data_feature = feature_extraction.transform(input_mail)


# #### MAKING PREDICTION

# In[23]:


prediction = model.predict(input_data_feature)
print(prediction)


# In[24]:


if (prediction[0]==1):
    print("Ham mail")

else:
    print("Spam mail")


# In[ ]:




