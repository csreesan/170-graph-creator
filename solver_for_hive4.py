from solver_specific import solver

#file_list = ['242', '244', '248', '252', '253', '256', '257', '258', '260', '266', '267', '268', '269', '289', '294', '297', '298', '306', '307', '309', '322']

#file_list = [662, 370, 439]
#file_list = ['383', '438', '460', '463']
# '230', '235',
file_list = ['430', '487', '244', '253', '267', '652']
solver("./curr_hive4.txt", "./iter_hive4.txt", "./beaten_hive4.txt", "./outputs/", False, file_list)