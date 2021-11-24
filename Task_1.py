#!/usr/bin/env python
# coding: utf-8

# ## Вычисления с помощью Numpy

# ### Задание 1

# In[8]:


import numpy as np

a = np.array([[1, 2, 3, 3, 1],
            [6, 8, 11, 10, 7]]).transpose()

mean_a = np.mean(a, axis = 0)

print(mean_a)


# ### Задание 2

# In[9]:


a_centered = a - mean_a

print(a_centered)


# ### Задание 3

# In[12]:


a_centered_sp = a_centered.T[0] @ a_centered.T[1]

print(a_centered_sp)


# In[13]:


a_centered_sp / (a_centered.shape[0] - 1)


# ## Работа с данными в Pandas

# ### Задание 1

# In[5]:


import pandas as pd

authors = pd.DataFrame({'author_id':[1, 2, 3], 
                        'author_name':['Тургенев', 'Чехов', 'Островский']}, 
                         columns=['author_id', 'author_name'])

print(authors)


# In[6]:


books = pd.DataFrame({'author_id':[1, 1, 1, 2, 2, 3, 3], 
                      'book_title':['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
                      'price':[450, 300, 350, 500, 450, 370, 290]}, 
                       columns=['author_id', 'book_title', 'price'])

print(books)


# ### Задание 2

# In[9]:


authors_price = pd.merge(authors, books, on='author_id', how='left')

print(authors_price)


# ### Задание 3

# In[15]:


top5 = authors_price.nlargest(5, 'price')

print(top5)


# ### Задание 4

# In[17]:


authors_stat = authors_price['author_name'].copy()

print(authors_stat)


# In[23]:


authors_stat = authors_price.groupby('author_name').agg({'price':['min', 'max', 'mean']})

authors_stat = authors_stat.rename(columns={'min':'min_price', 'max':'max_price', 'mean':'mean_price'})

print(authors_stat)


# In[ ]:




