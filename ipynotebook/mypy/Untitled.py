#!/usr/bin/env python
# coding: utf-8

# In[1]:


x = 1


# In[ ]:


y = 2


# In[4]:


from notebook.config_manager import BaseJSONConfigManager


# In[5]:


cm = BaseJSONConfigManager(parent=None, config_dir="/Users/hotoku/.jupyter")


# In[7]:


dir(cm)


# In[9]:


cm.get()

