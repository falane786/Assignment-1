#!/usr/bin/env python
# coding: utf-8

# # 1. Write a python program to display IMDB’s Top rated 100 Indian movies’ data https://www.imdb.com/list/ls056092300/ (i.e. name, rating, year ofrelease) and make data frame. 

# In[1]:


get_ipython().system('pip  install bs4')


# In[2]:


from bs4 import BeautifulSoup
import requests


# In[3]:


page = requests.get('https://www.imdb.com/list/ls056092300/')
page


# In[4]:


soup = BeautifulSoup(page.content)
soup


# In[5]:


Name = []

for i in soup.find_all('h3',class_="lister-item-header"):
    Name.append(i.text)
    
Name


# In[6]:


Date_of_Release = []

for i in soup.find_all('span',class_="lister-item-year text-muted unbold"):
    Date_of_Release.append(i.text)
    
Date_of_Release


# In[8]:


Rating = []

for i in soup.find_all('div',class_="ipl-rating-star small"):
    Rating.append(i.text)
    
Rating


# In[18]:


print(len(Name),len(Rating))


# In[19]:


import pandas as pd
df = pd.DataFrame({'Name':Name,'Rating':Rating})
df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # 2. Write a python program to scrape product name, price and discounts from https://peachmode.com/search?q=bags 

# In[20]:


from bs4 import BeautifulSoup
import requests


# In[21]:


page = requests.get('https://peachmode.com/search?q=bags')
page


# In[22]:


soup = BeautifulSoup(page.content)
soup


# In[31]:


Product_name = []

for i in soup.find_all('div',class_="filter-item"):
    Product_name.append(i.text)
    
    
Product_name


# In[35]:


Price = []


for i in soup.find_all('span',class_="filter-label"):
    Price.append(i.text)
    
Price


# In[37]:


Discount = []

for i in soup.find_all('div',class_="filter-item"):
    Discount.append(i.text)
    
Discount


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # 3. Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape: 
# # a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating. 
# # b) Top 10 ODI Batsmen along with the records of their team and rating. 
# # c) Top 10 ODI bowlers along with the records of their team and rating. 

# In[86]:


from bs4 import BeautifulSoup
import requests


# In[87]:


page = requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/test')
page


# In[88]:


soup = BeautifulSoup(page.content)
soup


# In[89]:


import pandas as pd
table = []

for i in soup.find_all("table", class_="si-table-body"):
    table.append(i.text)
    
table


# In[ ]:





# In[ ]:





# In[ ]:





# In[96]:


Batsman = []

for i in soup.find_all('div',class_="si-table-row"):
    Batsman.append(i.text)
    
Batsman


# In[ ]:





# In[ ]:





# In[ ]:





# In[97]:


Bowlers = []

for i in soup.find_all('h3',class_="si-team-name"):
    Bowlers.append(i.text)
    
Bowlers


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # 4.Write a python program to scrape details of all the posts from https://www.patreon.com/coreyms .Scrape the heading, date, content and the likes for the video from the link for the youtube video from the post.

# In[54]:


page = requests.get('https://www.patreon.com/coreyms')
page


# In[55]:


soup = BeautifulSoup(page.content)
soup


# In[57]:


Heading = []

for i in soup.find_all('span',data_tag_="post-title"):
    Heading.append (i.text)
    
Heading


# In[61]:





# In[ ]:





# In[ ]:





# In[62]:


date = []

for i in soup.find_all('span'):
    date.append(i.text)
    
date


# In[ ]:





# In[ ]:





# In[ ]:





# In[16]:


likes = []

for i in soup.find_all('div'):
    likes.append(i.text)
    
likes


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # 5. Write a python program to scrape house details from mentioned URL. It should include house title, location, area, EMI and price from https://www.nobroker.in/ .Enter three localities which are Indira Nagar, Jayanagar, Rajaji Nagar. 

# In[63]:


page = requests.get('https://www.nobroker.in/')
page


# In[64]:


soup = BeautifulSoup(page.content)
soup


# In[75]:


Title = []

for i in soup.find_all('h1', title_="1 BHK Flat In Jai Model House Chs For Sale  In Grant Road"):
    Title.append(i.text)
    
Title


# In[ ]:





# In[ ]:





# In[ ]:





# In[77]:


location = []

for i in soup.find_all('div',class_="flex"):
    location.append(i.text)
    
location


# In[ ]:





# In[ ]:





# In[74]:


area = []

for i in soup.find_all('span'):
    area.append(i.text)
    
    
area


# In[ ]:





# In[ ]:





# In[78]:


EMI = []


for i in soup.find_all('div',class_="nb__2WUQp"):
    EMI.append(i.text)
    

EMI


# In[ ]:





# In[ ]:





# In[ ]:





# In[79]:


Price = []

for i in soup.find_all('div',class_="nb__qetBg"):
    Price.append(i.text)
    
Price


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # 6. Write a python program to scrape first 10 product details which include product name , price , Image URL from https://www.bewakoof.com/bestseller?sort=popular . 

# In[80]:


page = requests.get('https://www.bewakoof.com/bestseller?sort=popular')
page


# In[81]:


soup = BeautifulSoup(page.content)
soup


# In[82]:


product = []

for i in soup.find_all('h2'):
    product.append(i.text)
    
product


# In[ ]:





# In[ ]:





# In[84]:


price  = []


for i in soup.find_all('div',class_="productPriceBox d-flex align-items-end  false"):
    price.append(i.text)
    
price


# In[ ]:





# In[ ]:





# In[34]:


image = []


for i in soup.find_all('img',class_="productImgTag"):
    image.append(i['data-src'])
    
image


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # 7.  Please visit https://www.cnbc.com/world/?region=world and scrap- 
# # a) headings 
# # b) date 
# # c) News link

# In[42]:


from bs4 import BeautifulSoup
import requests


# In[43]:


page = requests.get('https://www.cnbc.com/world/?region=world')
page


# In[44]:


soup = BeautifulSoup(page.content)
soup


# In[45]:


headings = []


for i in soup.find_all('h1',class_="ArticleHeader-headline"):
    headings.append(i.text)
    
headings


# In[ ]:





# In[ ]:





# In[85]:


date = []

for i in soup.find_all('time',data_testid_="published-timestamp"):
    date.append(i.text)

date


# In[ ]:





# In[ ]:





# In[49]:


News link = soup.find('a',href_="https://www.cnbc.com/2024/03/27/in-baltimore-bridge-crisis-shippers-left-on-hook-for-cargo-pickup.html")
News link


# In[ ]:





# In[ ]:





# # 8. Please visit https://www.keaipublishing.com/en/journals/artificial-intelligence-in-agriculture/most-downloaded- articles/ and scrap- 
# # a) Paper title 
# # b) date 
# # c) Author

# In[24]:


from bs4 import BeautifulSoup
import requests


# In[25]:


page = requests.get('https://www.keaipublishing.com/en/journals/artificial-intelligence-in-agriculture/most-downloaded-')
page


# In[26]:


soup = Beautifulsoup(page.content)
soup


# In[ ]:





# In[ ]:





# In[ ]:




