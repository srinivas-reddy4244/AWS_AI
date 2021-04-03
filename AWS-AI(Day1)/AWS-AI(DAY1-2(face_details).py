#!/usr/bin/env python
# coding: utf-8

# In[1]:


#webcam 
#pip install opencv-python
import cv2


# In[2]:


#for main cam like webcam i.e 0 and for external cam keep 1
cap = cv2.VideoCapture(0)


# In[3]:


#clicking my pic
myphoto = "srinu.jpg"
ret, photo =cap.read()


# In[4]:


ret


# In[5]:


#to save the image & storing in harddisk
cv2.imwrite(myphoto, photo )
#step1 is done...


# In[6]:


#to release the camera/turning off camera
cap.release()


# In[7]:


#step2


# In[8]:


#pip install boto3
#boto is SDK using SDK we can connect to AWS
#pip install aws //provides aws command to configure.
import boto3


# In[9]:


#boto go and connect to s3 service
s3 = boto3.resource('s3')


# In[10]:


s3.Bucket('awsaiday1thirdapril').upload_file(myphoto, "srinu.jpg")


# In[11]:


region='ap-south-1'


# In[12]:


#connect to rek
rek=boto3.client('rekognition', region)


# In[13]:


facedetail=rek.detect_faces(
Image={
         
          'S3Object': {
              'Bucket': 'awsaiday1thirdapril',
              'Name': 'srinu.jpg',
              
          }
      },
      Attributes=['ALL']
      
)


# In[14]:


facedetail['FaceDetails'][0]['Emotions'][2]


# In[ ]:




