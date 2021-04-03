#!/usr/bin/env python
# coding: utf-8

# In[2]:


#connect to webcam and click the photograph
#upload pics--->object storage(S3)
#connect/contack to rekcognition from s3 and analysis it as my requirements(particular method..e.g(recognition,comparision...etc)
#output/responce e.g smiling,car,male...etc


# In[76]:


#webcam 
#pip install opencv-python
import cv2


# In[77]:


#for main cam like webcam i.e 0 and for external cam keep 1
cap = cv2.VideoCapture(0)


# In[78]:


#clicking my pic
myphoto = "srinu.jpg"
ret, photo =cap.read()


# In[79]:


ret


# In[80]:


#to save the image & storing in harddisk
cv2.imwrite(myphoto, photo )
#step1 is done...


# In[81]:


#to release the camera/turning off camera
cap.release()


# In[69]:


#step2


# In[70]:


#pip install boto3
#boto is SDK using SDK we can connect to AWS
#pip install aws //provides aws command to configure.
import boto3


# In[82]:


#boto go and connect to s3 service
s3 = boto3.resource('s3')


# In[83]:


s3.Bucket('awsaiday1thirdapril').upload_file(myphoto, "srinu.jpg")


# In[84]:


region='ap-south-1'


# In[85]:


#connect to rek
rek=boto3.client('rekognition', region)


# In[44]:


rek


# In[51]:


responce=rek.detect_labels(
 Image={
         
          'S3Object': {
              'Bucket': 'awsaiday1thirdapril',
              'Name': 'srinu.jpg',

          }
      },
      MaxLabels=2,
      MinConfidence=90
  )


# In[52]:


responce


# In[55]:


responce['Labels'][1]['Name']


# In[57]:


for i in range(2):
    print( responce['Labels'][i]['Name'])


# In[87]:





# In[98]:





# In[ ]:




