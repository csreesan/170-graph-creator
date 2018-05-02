from solver_specific import solver

#file_list = ['323', '325', '345', '348', '350', '370', '371', '379', '381', '382', '383', '387', '388', '390', '395', '398', '405', '411', '412', '413', '420']

#file_list = [675, 440, 462]


#file_list = ['471', '472', '492', '493']
file_list = ['433', '678', '268', '298', '381', '663']

solver("./curr_hive5.txt", "./iter_hive5.txt", "./beaten_hive5.txt", "./outputs/", False, file_list)