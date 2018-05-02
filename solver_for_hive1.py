from solver_specific import solver

#file_list = ['3', '5', '6', '7', '8', '18', '22', '28', '30', '32', '39', '40', '42', '43', '45', '46', '47', '49', '57', '58', '59']
#file_list = [3, 18, 741]


#file_list = ['39', '43', '45', '180'] 
#file_list = ['6', '7'] 
#6, 7 
file_list = ['164', '169', '39', '43', '609']  

   


   
solver("./curr_hive1.txt", "./iter_hive1.txt", "./beaten_hive1.txt", "./outputs/", False, file_list)
