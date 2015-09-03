"""set working directory"""
import os
path  = "C:/Users/rahul.sharma/Desktop/training"
os.chdir(path)


"""Import required libraries"""
import pandas as pd
import string
from nltk.corpus import stopwords

Stop_Words = stopwords.words("english")

"""import and append data files"""
customer_data = pd.read_csv("Customer_input.csv")["Detailed Item Description"]
grainger_data = pd.read_csv("Grainger_input.csv")["Description"]

"""Remove punctuations and stop words"""
i=0
for line in customer_data:
    line1 = ''.join(word for word in line if word not in string.punctuation)
    line1 = line1.replace("\\","")
    line1 = line1.replace("/","")
    line1 = ' '.join(word for word in line1.split() if word not in Stop_Words)
    customer_data[i]=line1
    i=i+1

i=0
for line in grainger_data:
    line1 = ''.join(word for word in line if word not in string.punctuation)
    line1 = line1.replace("\\","")
    line1 = line1.replace("/","")
    line1 = ' '.join(word for word in line1.split() if word not in Stop_Words)
    grainger_data[i]=line1
    i=i+1

"""append data"""
complete_data = customer_data.append(grainger_data)

"""Create hash table"""
master_set = set()
for line in complete_data:
    temp_set=set(line.split())
    master_set = master_set.union(temp_set)
i=1  
hash_table ={}
for element in master_set:
    hash_table[element]=i
    i=i+1

data_frame=pd.DataFrame(hash_table.items(), columns=['Word','Key'])
data_frame.to_csv("hash_table.csv")

"""Create Document Term Matrix for Customer Data"""
file_count = ""
for line in customer_data:
    temp_set = set(line.split())
    document_count = ""
    for element in temp_set:
        word_count = repr(hash_table[element]) + "-" + repr(line.count(element))
        document_count = document_count + word_count + " "
    file_count = file_count + document_count + "\n"
    
customer_file = open("customer_dtm.txt", "w")
customer_file.write(file_count)
customer_file.close()

"""Create Document Term Matrix for Grainger Data"""
file_count = ""
for line in grainger_data:
    temp_set = set(line.split())
    document_count = ""
    for element in temp_set:
        word_count = repr(hash_table[element]) + "-" + repr(line.count(element))
        document_count = document_count + word_count + " "
    file_count = file_count + document_count + "\n"

customer_file = open("grainger_dtm.txt", "w")
customer_file.write(file_count)
customer_file.close()

