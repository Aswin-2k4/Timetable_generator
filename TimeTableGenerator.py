#Variables used
# slots -> a list to store timings selected by the user
# class_total -> list to store classes for a week
# class_number -> get number of classes for per subject per week
# slots_per_day -> filtered out temparory storage for class for a day



import pandas as pd     #importing required libs
import random
import streamlit as st

st.title("TIME TABLE GENERATOR")            #Setting title and a small intro
st.write("Create time table of your choice")

slots=st.multiselect("Pick your slots :",['9-10','10-11','11-12','2-3','3-4','4-5'])

subjects=st.text_input("Enter the subjects (separate it with commas) ")
subjects=subjects.split(",")                                             

    
max_slots=len(slots)*5   #calculating maximum no: of slots available
class_total=[]           #An array to store total classes in a week


for sub in subjects:
    class_number=int(st.number_input(f"Enter classes required {sub} per week :",key=f"in_{sub}",step=1)) #unique key to distinguishing
                                                                                                         #(for each user action streamlit reruns)
    for i in range(class_number):
      class_total.append(sub)
      
if st.button("Generate"):
    for i in range(len(class_total),max_slots):
        class_total.append('-')
        
    if len(class_total)>max_slots:
        st.write("Your required number of slots exceeds maximum available slots")
    else:
       
        random.shuffle(class_total)
        slots_per_day=[class_total[i:i+len(slots)] for i in range(0,len(class_total),len(slots))] #filtering classes for a day
        time_table=pd.DataFrame(slots_per_day,columns=slots)
        time_table.index=['MON','TUE','WED','THU','FRI']
        st.table(time_table)


