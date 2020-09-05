#!/usr/bin/env python
# coding: utf-8

# # __Hacker News Analysis__
# 
# In this project, I'll be evaluating a dataset from the website Hacker News.  The site functions somewhat like Reddit, in that individuals may post questions, projects, products, or other interesting information.  Other users may then comment on the content, and up/down vote eachothers' comments.
# 
# I'm interested in the following questions:
# * Do Ask HN or Show HN receive more comments on average?
# * Do posts created at a certain time receive more comments on average?

# In[1]:


#Import needed libraries
from csv import reader

#Import the csv file containing our data
opened_file = open('hacker_news.csv')
read_file = reader(opened_file)
hn = list(read_file)

#Print first five lines of hn
print(hn[:5])


# In[2]:


#Remove the first row (column headers) from the list and save it in a new list
headers = hn[:1]
hn = hn[1:]

#Verify that I've split the headers from the dataset
print(headers, ',\n')
print(hn[:5])


# In[3]:


#Separate out posts beginning with 'Ask HN' and 'Show HN' 9with case variations)
ask_posts = []
show_posts = []
other_posts = []

for row in hn:
    title = str(row[1])
    if title.lower().startswith('ask hn'):
        ask_posts.append(row)
    elif title.lower().startswith('show hn'):
        show_posts.append(row)
    else:
        other_posts.append(row)
        
print("There are {} ask-posts".format(len(ask_posts)))
print("There are {} show-posts".format(len(show_posts)))
print("There are {} other-posts".format(len(other_posts)))


# In[4]:


#Determine if ask posts or show posts receive more comments on average
#Determine average number of comments per ask post
total_ask_comments = 0
for post in ask_posts:
    num_ask_comments = post[4]
    num_ask_comments = int(num_ask_comments)
    total_ask_comments += num_ask_comments
    
avg_ask_comments = total_ask_comments/len(ask_posts)
print("Average number of comments per ask post: ", avg_ask_comments)

#Determine average number of comments per show post
total_show_comments = 0
for post in show_posts:
    num_show_comments = int(post[4])
    total_show_comments += num_show_comments
    
avg_show_comments = total_show_comments/len(show_posts)
print("Average number of comments per show post: ", avg_show_comments)


# As we can see in the previous cell, on average, ask posts receive roughly 4 more comments than show posts!
# 
# Because ask posts are more likely to receive comments, we'll focus the rest of our analysis on ask posts only.
# 
# Next, we'll determine if ask posts created at a certain time are more likely to attract comments.

# In[5]:


import datetime as dt
result_list = []

for post in ask_posts:
    created_at = post[6]
    num_ask_comments = int(post[4])
    result_list.append([created_at, num_ask_comments])
counts_by_hour = {}
comments_by_hour = {}

for row in result_list:
    hour = row[0]
    comment = row[1]
    time = dt.datetime.strptime(hour, '%m/%d/%Y %H:%M').strftime("%H")
    if time not in counts_by_hour:
        counts_by_hour[time] = 1
        comments_by_hour[time] = comment
    else:
        counts_by_hour[time] += 1
        comments_by_hour[time] += comment

comments_by_hour, counts_by_hour


# I'll now use the dictionaries created in the previous cell to calculate the average number of comments for posts created during each hour of the day.

# In[6]:


#Initialize a new list for the results of the calculation
avg_by_hour = []

#Calculate
for key in comments_by_hour:
    avg_by_hour.append([key, comments_by_hour[key]/counts_by_hour[key]]) 

avg_by_hour


# In[15]:


#Swap the two rows in the avg_by_hour list and assign it to the new list (swap_avg_by_hour)
swap_avg_by_hour = []

for row in avg_by_hour:
    swap_avg_by_hour.append([row[1], row[0]])
# print(swap_avg_by_hour)

#Sort the new list (swap_avg_by_hour) in descending order
sorted_swap = sorted(swap_avg_by_hour, reverse=True)
# sorted_swap
print('\n', "Top 5 Hours for Ask Posts Comments")

for row in sorted_swap[:5]:
    average = float(row[0])
    hour = row[1]
    print('\n' "{} : {:.2f} average comments per post".format(hour, average))


# # __Results__
# As we can see in the previous cell, 3pm is clearly the time in which ask posts receive the most comments.

# # __Further Study__
# 
# * Determine if show or ask posts receive more points on average.
# * Determine if posts created at a certain time are more likely to receive more points.
# * Compare your results to the average number of comments and points other posts receive.
# * Use Dataquest's data science project style guide to format your project.
# 

# In[ ]:




