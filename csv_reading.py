import json
import pandas as pd

class DataStructure:
    def __init__(self):
        self.data={}
    
    def add_entry(self, id,key, value):
        if id not in self.data:
            self.data[id]={}
        if key not in self.data[id]:
            self.data[id][key]=value
        
    def to_json(self):
        return json.dumps(self.data,indent=4)
    
    def write_to_file_json(self,filename):
        with open(filename,'w') as file:
            file.write(self.to_json())
    
    def write_to_file_csv(self,filename):
        self.to_table().to_csv(filename)
            
    def to_table(self):
        table_data=[]
        for id, values in self.data.items():
            row={'ID': id}
            row.update(values)
            table_data.append(row)
        return pd.DataFrame(table_data)
    
data_structure=DataStructure()

read_file_path = "/home/yuvalyh@mta.ac.il/biobank/ukb673316.csv"
read_file_path2 = "/home/yuvalyh@mta.ac.il/biobank/ukb672220.csv"
read_file_path3 = "/home/yuvalyh@mta.ac.il/biobank/ukb673540.csv"
first_file_starting_index_41270=1102
first_file_ending_index_41270=1361
second_file_starting_index_41270=13619
second_file_ending_index_41270=13877
third_file_starting_index_41270=None
third_file_ending_index_41270= None
first_file_starting_index_40008=753
first_file_ending_index_40008=775
second_file_starting_index_40008=12442
second_file_ending_index_40008=12464
first_file_starting_index_40006=731
first_file_ending_index_40006=753
second_file_starting_index_40006=12418
second_file_ending_index_40006=12440
second_file_starting_index_31=22
second_file_ending_index_31=23
second_file_starting_index_26424=11474
second_file_ending_index_26424=11475
second_file_starting_index_40007=12440
second_file_ending_index_40007=12441
second_file_starting_index_26410=11460
second_file_ending_index_26410=11461
#returns an enumerable object, with each item being a part of a dataframe filtered by the IDs with T860 in their table under the 41270 series of indices. 
def get_filtered_data_frame(filename, starting_index_41270, ending_index_41270):
    chunk_size=1000
    for chunk in pd.read_csv(filename, chunksize=chunk_size):
        filtered_df=((chunk[chunk.iloc[:, starting_index_41270:ending_index_41270].eq("T860").any(axis=1)]))
        yield filtered_df
                
with open("/home/yuvalyh@mta.ac.il/results_json.json", 'r') as file:
    data_structure.data=json.load(file)
    
    
#first file, 41270 T860- DONE
# for filtered_chunk in get_filtered_data_frame(read_file_path, first_file_starting_index_41270, first_file_ending_index_41270):
#     for index, row in filtered_chunk.iterrows():
#         values_to_print=row.iloc[first_file_starting_index_41270:first_file_ending_index_41270]
#         column_names=filtered_chunk.columns[first_file_starting_index_41270:first_file_ending_index_41270]
#         first_column_values=row.iloc[0] #brings the ids
        
#         #if you want to limit, use "columns names, values to print". (for stuff other than T860)
#         #if you want to check all of them, use "filtered_chunk.columns, row". (for T860)
#         for col_name, value in zip(filtered_chunk.columns, row):
#             if(pd.isnull(value) is not True and value=="T860"): #to check if a value is not null, pd.isnull(value) is not True
#                 #print(f"{first_column_name} {col_name}\n{first_column_values} {value}")
#                 data_structure.add_entry(str(first_column_values), col_name,value)
#                 #print(data_structure.to_json())
#                 print("just added ", col_name, value, " for ",str(first_column_values))
                
                
#first file, 40008 --DONE
# for filtered_chunk in get_filtered_data_frame(read_file_path, first_file_starting_index_41270, first_file_ending_index_41270):
#     for index, row in filtered_chunk.iterrows():
#         values_to_print=row.iloc[first_file_starting_index_40008:first_file_ending_index_40008]
#         column_names=filtered_chunk.columns[first_file_starting_index_40008:first_file_ending_index_40008]
#         first_column_values=row.iloc[0] #brings the ids
        
#         #if you want to limit, use "columns names, values to print". (for stuff other than T860)
#         #if you want to check all of them, use "filtered_chunk.columns, row". (for T860)
#         for col_name, value in zip(column_names, values_to_print):
#             if(pd.isnull(value) is not True): #to check if a value is not null, pd.isnull(value) is not True
#                 #print(f"{first_column_name} {col_name}\n{first_column_values} {value}")
#                 data_structure.add_entry(str(first_column_values), col_name,value)
#                 #print(data_structure.to_json())
#                 print("just added ", col_name, value, " for ",str(first_column_values))
           
# #first file, 40006--DONE
# for filtered_chunk in get_filtered_data_frame(read_file_path, first_file_starting_index_41270, first_file_ending_index_41270):
#     for index, row in filtered_chunk.iterrows():
#         values_to_print=row.iloc[first_file_starting_index_40006:first_file_ending_index_40006]
#         column_names=filtered_chunk.columns[first_file_starting_index_40006:first_file_ending_index_40006]
#         first_column_values=row.iloc[0] #brings the ids
      
#         #if you want to limit, use "columns names, values to print". (for stuff other than T860)
#         #if you want to check all of them, use "filtered_chunk.columns, row". (for T860)
#         for col_name, value in zip(column_names, values_to_print):
#             if(pd.isnull(value) is not True): #to check if a value is not null, pd.isnull(value) is not True
#                 #print(f"{first_column_name} {col_name}\n{first_column_values} {value}")
#                 data_structure.add_entry(str(first_column_values), col_name,value)
#                 #print(data_structure.to_json())
#                 print("just added ", col_name, value, " for ",str(first_column_values))
          
#second file, 41270 T860 -- DONE
# for filtered_chunk in get_filtered_data_frame(read_file_path2, second_file_starting_index_41270, second_file_ending_index_41270):
#     for index, row in filtered_chunk.iterrows():
#         values_to_print=row.iloc[second_file_starting_index_41270:second_file_ending_index_41270]
#         column_names=filtered_chunk.columns[second_file_starting_index_41270:second_file_ending_index_41270]
#         first_column_values=row.iloc[0] #brings the ids
        
#         #if you want to limit, use "columns names, values to print". (for stuff other than T860)
#         #if you want to check all of them, use "filtered_chunk.columns, row". (for T860) and add a condition inside the 'if' to check if the value is t860
#         for col_name, value in zip(filtered_chunk.columns, row):
#             if(pd.isnull(value) is not True and value=="T860"): #to check if a value is not null, pd.isnull(value) is not True
#                 #print(f"{first_column_name} {col_name}\n{first_column_values} {value}")
#                 data_structure.add_entry(first_column_values, col_name,value)
#                 print("just added ", col_name, value, " for ",first_column_values)
#                 #print(data_structure.to_json())

# #second file, 40008 --DONE
# for filtered_chunk in get_filtered_data_frame(read_file_path2, second_file_starting_index_41270, second_file_ending_index_41270):
#       for index, row in filtered_chunk.iterrows():
#           values_to_print=row.iloc[second_file_starting_index_40008:second_file_ending_index_40008]
#           column_names=filtered_chunk.columns[second_file_starting_index_40008:second_file_ending_index_40008]
#           first_column_values=row.iloc[0] #brings the ids
      
#           #if you want to limit, use "columns names, values to print". (for stuff other than T860)
#           #if you want to check all of them, use "filtered_chunk.columns, row". (for T860)
#           for col_name, value in zip(column_names, values_to_print):
#               if(pd.isnull(value) is not True): #to check if a value is not null, pd.isnull(value) is not True
#                   #print(f"{first_column_name} {col_name}\n{first_column_values} {value}")
#                   data_structure.add_entry(str(first_column_values), col_name,value)
#                   print("just added ", col_name, value, " for ",str(first_column_values))
#                   #print(data_structure.to_json())

# # #second file, 40006- DONE
# for filtered_chunk in get_filtered_data_frame(read_file_path2, second_file_starting_index_41270, second_file_ending_index_41270):
#     for index, row in filtered_chunk.iterrows():
#         values_to_print=row.iloc[second_file_starting_index_40006:second_file_ending_index_40006]
#         column_names=filtered_chunk.columns[second_file_starting_index_40006:second_file_ending_index_40006]
#         first_column_values=row.iloc[0] #brings the ids
       
#         #if you want to limit, use "columns names, values to print". (for stuff other than T860)
#         #if you want to check all of them, use "filtered_chunk.columns, row". (for T860)
#         for col_name, value in zip(column_names, values_to_print):
#             if(pd.isnull(value) is not True): #to check if a value is not null, pd.isnull(value) is not True
#                 #print(f"{first_column_name} {col_name}\n{first_column_values} {value}")
#                 data_structure.add_entry(str(first_column_values), col_name,value)
#                 print("just added ", col_name, value, " for ",str(first_column_values))
#                 #print(data_structure.to_json())
                
 #second file, 31-DONE
# for filtered_chunk in get_filtered_data_frame(read_file_path2, second_file_starting_index_41270, second_file_ending_index_41270):
#     for index, row in filtered_chunk.iterrows():
#         values_to_print=row.iloc[second_file_starting_index_31:second_file_ending_index_31]
#         column_names=filtered_chunk.columns[second_file_starting_index_31:second_file_ending_index_31]
#         first_column_values=row.iloc[0] #brings the ids
       
#         #if you want to limit, use "columns names, values to print". (for stuff other than T860)
#         #if you want to check all of them, use "filtered_chunk.columns, row". (for T860)
#         for col_name, value in zip(column_names, values_to_print):
#             if(pd.isnull(value) is not True): #to check if a value is not null, pd.isnull(value) is not True
#                 #print(f"{first_column_name} {col_name}\n{first_column_values} {value}")
#                 data_structure.add_entry(str(first_column_values), col_name,value)
#                 print("just added ", col_name, value, " for ",str(first_column_values))
#                 #print(data_structure.to_json())
                
#second file, 26424 --DONE
# for filtered_chunk in get_filtered_data_frame(read_file_path2, second_file_starting_index_41270, second_file_ending_index_41270):
#     for index, row in filtered_chunk.iterrows():
#         values_to_print=row.iloc[second_file_starting_index_26424:second_file_ending_index_26424]
#         column_names=filtered_chunk.columns[second_file_starting_index_26424:second_file_ending_index_26424]
#         first_column_values=row.iloc[0] #brings the ids
        
#         #if you want to limit, use "columns names, values to print". (for stuff other than T860)
#         #if you want to check all of them, use "filtered_chunk.columns, row". (for T860)
#         for col_name, value in zip(column_names, values_to_print):
#             if(pd.isnull(value) is not True): #to check if a value is not null, pd.isnull(value) is not True
#                 #print(f"{first_column_name} {col_name}\n{first_column_values} {value}")
#                 data_structure.add_entry(str(first_column_values), col_name,value)
#                 print("just added ", col_name, value, " for ",str(first_column_values))
#                 #print(data_structure.to_json())


#second file, 26410--DONE 
# for filtered_chunk in get_filtered_data_frame(read_file_path2, second_file_starting_index_41270, second_file_ending_index_41270):
#     for index, row in filtered_chunk.iterrows():
#         values_to_print=row.iloc[second_file_starting_index_26410:second_file_ending_index_26410]
#         column_names=filtered_chunk.columns[second_file_starting_index_26410:second_file_ending_index_26410]
#         first_column_values=row.iloc[0] #brings the ids
        
#         #if you want to limit, use "columns names, values to print". (for stuff other than T860)
#         #if you want to check all of them, use "filtered_chunk.columns, row". (for T860)
#         for col_name, value in zip(column_names, values_to_print):
#             if(pd.isnull(value) is not True): #to check if a value is not null, pd.isnull(value) is not True
#                 #print(f"{first_column_name} {col_name}\n{first_column_values} {value}")
#                 data_structure.add_entry(str(first_column_values), col_name,value)
#                 print("just added ", col_name, value, " for ",str(first_column_values))
#                 #print(data_structure.to_json())


#second file, 40007--
for filtered_chunk in get_filtered_data_frame(read_file_path2, second_file_starting_index_41270, second_file_ending_index_41270):
    for index, row in filtered_chunk.iterrows():
        values_to_print=row.iloc[second_file_starting_index_40007:second_file_ending_index_40007]
        column_names=filtered_chunk.columns[second_file_starting_index_40007:second_file_ending_index_40007]
        first_column_values=row.iloc[0] #brings the ids
        
        #if you want to limit, use "columns names, values to print". (for stuff other than T860)
        #if you want to check all of them, use "filtered_chunk.columns, row". (for T860)
        for col_name, value in zip(column_names, values_to_print):
            if(pd.isnull(value) is not True): #to check if a value is not null, pd.isnull(value) is not True
                #print(f"{first_column_name} {col_name}\n{first_column_values} {value}")
                data_structure.add_entry(str(first_column_values), col_name,value)
                print("just added ", col_name, value, " for ",str(first_column_values))
                #print(data_structure.to_json())

print("finished file")
data_structure.write_to_file_json("/home/yuvalyh@mta.ac.il/results_json.json")
data_structure.write_to_file_csv("/home/yuvalyh@mta.ac.il/results_csv.csv")
print(len(data_structure.data))
