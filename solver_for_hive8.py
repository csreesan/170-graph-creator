from solver_specific import solver


#file_list = ['551', '555', '558', '561', '562', '563', '564', '573', '574', '575', '576', '582', '583', '595', '609', '610', '614', '628', '629', '636', '637']

#file_list = [691, 562, 563, 574]
#file_list = ['573', '574', '610', '629']
#'471' '472'
file_list = [ '492', '493', '494', '699']
solver("./curr_hive8.txt", "./iter_hive8.txt", "./beaten_hive8.txt", "./outputs/", False, file_list)
