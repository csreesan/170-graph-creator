from solver_specific import solver

#file_list = ['488', '490', '492', '493', '494', '497', '502', '507', '509', '510', '511', '512', '523', '525', '526', '527', '531', '538', '547', '549', '550']

#file_list =[690, 550, 561]
#file_list = ['509', '561', '562', '563'] 
file_list = ['438', '439', '460', '462']
solver("./curr_hive7.txt", "./iter_hive7.txt", "./beaten_hive7.txt", "./outputs/", False, file_list)