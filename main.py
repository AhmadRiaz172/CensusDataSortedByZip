#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from pyzipcode import ZipCodeDatabase
zcdb=ZipCodeDatabase()
import csv
from uszipcode import SearchEngine
zcdb=ZipCodeDatabase()
search = SearchEngine(simple_zipcode=False)
print ("running")
with open('innovators.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Zip code", "Home value", "House hold income","Pcic another form of income","Family","Homeowner","Marries","College"])
    num=0
    for i in zcdb:
        check=0
        num+=1
#        print(i)
        example = search.by_zipcode(i)
        s = 0
            
        if type(None)==type(example.average_household_income_over_time):
            check = 1
        if example.average_household_income_over_time is None:
            check = 1
        if example.source_of_earnings is None:     
            check = 1
        if example.families_vs_singles is None:     
            check = 1
        if type(None)==type(example.housing_units):
            check=1
        if example.owner_occupied_home_values is None: 
            check = 1
        if example.families_vs_singles is None:
            check = 1
        if example.educational_attainment_for_population_25_and_over is None:
            check = 1
            
        if check==0:
            s = 0
            for i in example.owner_occupied_home_values[0]['values']:
                s += i['y']
        
            writer.writerow([example.zipcode,
                 example.housing_units,
                 example.average_household_income_over_time[0]['values'][0]['y'],
                 example.source_of_earnings[0]['values'][1]['y'] ,
                 example.families_vs_singles[0]['values'][0]['y'] ,
                 s,
                 example.families_vs_singles[0]['values'][0]['y']/example.population * 100,
                 (example.educational_attainment_for_population_25_and_over[0]['values'][1]['y']/example.population)*100
                 ])
                      
        
print("completed")
            
        #if example.families_vs_singles is not None: 
         #   print(example.families_vs_singles[0]['values'][0]['y'],"\n" )


# In[ ]:





# In[ ]:





# In[ ]:




