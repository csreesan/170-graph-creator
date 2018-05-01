from solver_specific import solver

#file_list = ['60', '61', '62', '74', '75', '79', '94', '97', '99', '122', '127', '130', '154', '156', '157', '158', '159', '160', '161', '162', '163']
#file_list = [146, 180, 181]


#file_list = ['99', '127', '157', '181']  
file_list = ['164', '169', '198', '235', '236']
solver("./curr_hive2.txt", "./iter_hive2.txt", "./beaten_hive2.txt", "./outputs/", False, file_list)
