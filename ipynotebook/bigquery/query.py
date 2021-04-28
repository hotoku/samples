#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/hotoku/.config/gcloud/legacy_credentials/dtws_yasunori_horikoshi@oaklawn.co.jp/adc.json"


# In[2]:


from google.cloud import bigquery

client = bigquery.Client(
    project="olm-pipeline-dev",
    location="asia-northeast1"
)


# In[3]:


ret = client.query("select 1")


# In[4]:


ret.to_dataframe()


# In[6]:


ret.total_bytes_processed


# In[7]:


ret.total_bytes_billed

