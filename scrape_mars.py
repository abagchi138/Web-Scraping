#!/usr/bin/env python
# coding: utf-8

# In[1]:


from splinter import Browser
import pandas as pd
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


mars= {}
url= "https://redplanetscience.com/"
browser.visit(url)


# In[4]:


html= browser.html
soup= bs(html, 'html.parser')
element= soup.select_one('div.list_text')
title= element.find('div', class_= 'content_title').text
title
paragraph= element.find('div', class_= 'article_teaser_body').text
paragraph


# In[5]:


mars["news_title"]= title
mars["news_paragraph"]= paragraph


# In[6]:


url2= "https://spaceimages-mars.com/"
browser.visit(url2)


# In[7]:



element= browser.find_by_tag('button')[1]
element.click()


# In[8]:


html= browser.html
soup= bs(html, 'html.parser')
image_url= soup.find('img', class_= 'fancybox-image')['src']
image_url


# In[9]:


fullurl= url2+image_url
fullurl


# In[10]:


mars['feature_image_url']= fullurl


# In[11]:


url4= "https://marshemispheres.com/"
browser.visit(url4)


# In[12]:


hemisphere_image_url= []
imagelink= browser.find_by_css('a.product-item img')
for link in range(len(imagelink)):
    hemisphere={}
    browser.find_by_css('a.product-item img')[link].click()
    element= browser.find_by_text('Sample')['href']
    hemisphere['image_url']= element
    hemisphere['title']= browser.find_by_css('h2.title').text
    hemisphere_image_url.append(hemisphere)
    browser.back()
    
    
hemisphere_image_url    

mars["hemispheres"]= hemisphere_image_url


# In[13]:


mars


# In[23]:


url3= "https://galaxyfacts-mars.com"
df_facts= pd.read_html(url3)[0]
df_facts


# In[24]:


df_facts.columns= ["description", "mars", "earth"]
df_facts


# In[25]:


df_facts.set_index("description", inplace= True)
df_facts


# In[26]:


mars["facts"]= df_facts.to_html(classes= "table table-striped")
mars


# In[ ]:




