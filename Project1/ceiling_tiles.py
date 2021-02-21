
# coding: utf-8

# In[2]:

tile_length = float(input("What is the length of a Tile's side in inches? "))
wall_length = float(input("What is the length of the wall in feet? "))


# In[17]:

length_in_feet = tile_length / 12 #converting inches to feet
tile_number = wall_length // length_in_feet
remainder = (wall_length % length_in_feet) * 12 #converting feet to inches


# In[18]:

print("Each row needs" , tile_number , "tiles , with ", remainder , "inches remaining. ")
