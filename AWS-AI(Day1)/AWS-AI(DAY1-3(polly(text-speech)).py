#!/usr/bin/env python
# coding: utf-8

# In[30]:


import boto3


# In[31]:


po = boto3.client('polly')


# In[55]:


res=po.synthesize_speech(Text="this is srinivas,completing AWS workshop",OutputFormat='mp3',VoiceId='Russell')


# In[56]:


res


# In[57]:


#res['AudioStream'].read()


# In[58]:


file=open('myaudio.mp3','wb')


# In[59]:


file.write(res['AudioStream'].read())


# In[60]:


file.close()


# In[61]:


import IPython


# In[62]:


IPython.display.Audio("myaudio.mp3")


# In[ ]:




