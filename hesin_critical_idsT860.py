import csv
file_path1 = "/home/yuvalyh@mta.ac.il/ids_T860.txt"
file_path2 = "/home/yuvalyh@mta.ac.il/biobank/hesin_critical.txt"
file_path3 = "/home/yuvalyh@mta.ac.il/biobank/hesin_delivery.txt"
file_path4 = "/home/yuvalyh@mta.ac.il/biobank/hesin_diag.txt"
file_path5 = "/home/yuvalyh@mta.ac.il/biobank/hesin_maternity.txt"
file_path6 = "/home/yuvalyh@mta.ac.il/biobank/hesin_oper.txt"
file_path7 = "/home/yuvalyh@mta.ac.il/biobank/hesin_psych.txt"
file_path8 = "/home/yuvalyh@mta.ac.il/biobank/hesin.txt"
file_path9 = "/home/yuvalyh@mta.ac.il/biobank/death.txt"


#with open('/home/yuvalyh@mta.ac.il/hesin_critical_T860.txt', 'w') as hesin_critical_T860:
    #with open(file_path1, 'r') as ids:
        #with open(file_path2, 'r') as hesin_critical_inf:
         #   for row1 in ids:
          #      #print("checking row: " +row1)
           #     for row2 in hesin_critical_inf:
                    #print("Comparing between "+row1+" and "+ str(row2.split()[0]))
            #        if (row1.strip() == str(row2.split()[0]).strip()):
             #           hesin_critical_T860.write(str(row2))
              #  hesin_critical_inf.seek(0)
           
def write_hesin(file_path1, file_path2, str1):
    isFirst = True
    with open('/home/yuvalyh@mta.ac.il/' +str1, 'w') as hesin_T860:
        with open(file_path1, 'r') as ids:
            with open(file_path2, 'r') as hesin_inf:
                for row1 in ids:
                    for row2 in hesin_inf:
                        if(isFirst):
                            hesin_T860.write(str(row2))
                        isFirst = False
                        if(row1.strip() == str(row2.split()[0]).strip()):
                            #print("yessss")
                            hesin_T860.write(str(row2))
                    hesin_inf.seek(0)
                            
            

#write_hesin(file_path1,file_path2,"hesin_critical_T860.txt")
#write_hesin(file_path1,file_path3,"hesin_delivery_T860.txt")
#write_hesin(file_path1,file_path4,"hesin_diag_T860.txt")
#write_hesin(file_path1,file_path5,"hesin_maternity_T860.txt")
#write_hesin(file_path1,file_path6,"hesin_oper_T860.txt")
#write_hesin(file_path1,file_path7,"hesin_psych_T860.txt")
#write_hesin(file_path1,file_path8,"hesin_T860.txt")
write_hesin(file_path1,file_path9,"death_T860.txt")




