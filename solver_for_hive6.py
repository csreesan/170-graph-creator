from solver_specific import solver


file_list = ['430', '431', '433', '437', '438', '439', '440', '454', '459', '460', '462', '463', '471', '472', '473', '475', '477', '479', '481', '486', '487']

solver("./curr_hive6.txt", "./iter_hive6.txt", "./beaten_hive6.txt", "./outputs/", False, file_list)