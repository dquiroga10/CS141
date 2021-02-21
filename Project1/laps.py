
# coding: utf-8

# In[1]:

miles_goal = float(input("How many miles would you like to run in miles? "))
track_distance = float(input("How long is the track in miles? "))


# In[13]:

laps_lower = miles_goal // track_distance #this is the lower number in the range

upper_num_of_laps = laps_lower + 1 #this is the higher number in the range


# In[15]:

print("You must run between ", laps_lower , "and" , upper_num_of_laps, "laps. ")
