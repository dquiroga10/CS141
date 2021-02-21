
# coding: utf-8

# In[6]:

MPG = float(input("How many miles per gallon? "))
KM_per_Mi = 1.60934
Gal_per_Litre = .264172
litre_per_100km = 100 / (MPG * KM_per_Mi * Gal_per_Litre) #equation used to convert to litres per 100km
print(MPG , "MPG is equivalent to " , litre_per_100km , "litres per 100km.")
