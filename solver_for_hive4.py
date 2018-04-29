from solver_specific import solver

file_list = ['242', '244', '248', '252', '253', '256', '257', '258', '260', '266', '267', '268', '269', '289', '294', '297', '298', '306', '307', '309', '322']

solver("./curr_hive4.txt", "./iter_hive4.txt", "./beaten_hive4.txt", "./outputs/", False, 300, 400)