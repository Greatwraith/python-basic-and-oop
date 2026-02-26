


# Iterating through a dictionary
file_counts = {"python":22, "java": 12, "c++": 15}
for file in file_counts:
    print(file) # python, java, c++
    

# 1ST | 
# use 'items()' to get key-values pairs
# to get the key-value pairs of the dictionary, we can use the 'items()' method
for file, amounts in file_counts.items():
    print("files: {}  amounts: {}".format(file, amounts) ) # ('python', 22), ('java', 12), ('c++', 15)
    
    
    
    

# to get the keys of the dictionary, we can use the 'keys()' method
# to get the values of the dictionary, we can use the 'values()' method
hitung_kunci = file_counts.keys() 
hitung_isi =file_counts.values()

print("hitung_kunci:   ", hitung_kunci) # dict_keys(['python', 'java', 'c++'])
print("hitung_isi:   ", hitung_isi) # dict_values([22




# 2ND | 'keys()'
# use 'keys()' to get and iterate the KEYS of the dictionary
# iterating through the keys of the dictionary using the 'keys()' methods
for file in file_counts.keys():
    print(file) # python, java, c++
    


# 3RD | 'values()'
# use 'values()' to get and iterate the VALUES of the dictionary
# iterating through the values of the dictionary using the 'values()' methods
for file in file_counts.values():
    print(file) # 22, 12, 15
    



    
    
