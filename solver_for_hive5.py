from solver_specific import solver

file_list = ['323', '325', '345', '348', '350', '370', '371', '379', '381', '382', '383', '387', '388', '390', '395', '398', '405', '411', '412', '413', '420']

solver("./curr_hive5.txt", "./iter_hive5.txt", "./beaten_hive5.txt", "./outputs/", False, file_list)