from solver_specific import solver

#file_list = ['164', '165', '168', '169', '175', '178', '180', '181', '182', '198', '201', '202', '203', '215', '220', '230', '234', '235', '236', '238', '239']
#file_list = [587, 220, 239]
#file_list = ['230', '298', '381', '382']
file_list = ['420', '239', '248', '268', '297', '306', '322']
solver("./curr_hive3.txt", "./iter_hive3.txt", "./beaten_hive3.txt", "./outputs/", False, file_list)