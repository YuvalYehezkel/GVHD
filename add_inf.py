import pandas as pd
csv_file = "/home/yuvalyh@mta.ac.il/biobank/ukb673316.csv"
chunksize = 1000
target_row = "1000386"
target_col_name= '41204-0.39'

#found_value = None

#for chunk in pd.read_csv(csv_file, chunksize=chunksize):
   # try:
    #    found_value = chunk.loc[target_row, target_col_name]
   #     print("Found value:", found_value)
  #      break
 #   except KeyError:
#        pass 
        
chunk_size = 10000
for chunk in pd.read_csv(csv_file, chunksize=chunk_size):
  print("read csv")
  filtered_df=((chunk[chunk.iloc[:, 1102:1361].eq("T860").any(axis=1)]))
  print("Made filtered df")
  matching_columns=chunk.columns[chunk.eq("T860").any()]
  print("got matching columns")
  output_data=[]
  for index, row in filtered_df.iterrows():
    matching_columns_names=list(matching_columns[filtered_df.loc[index,matching_columns]=="T860"])
    matching_columns_names_str=", ".join(matching_columns_names)
    output_data.append([row.iloc[0], matching_columns_names_str])
  print("After for loop")
  output_df=pd.DataFrame(output_data, columns=['FirstColumn', 'T860_Columns'])
  output_df.to_csv('/home/yuvalyh@mta.ac.il/csv_pandas_ukb673316.txt', mode='a', header=False, index=False)

