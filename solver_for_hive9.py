from solver_specific import solver


#file_list =['647', '651', '652', '653', '660', '661', '663', '664', '665', '669', '670', '675', '677', '678', '679', '690', '691', '692', '699', '718', '720', '728', '735', '736', '741', '742']

#file_list = [692, 665, 678]
#file_list = ['636', '663', '664', '670', '699']
file_list = [ '561', '562', '563', '573', '574']
solver("./curr_hive9.txt", "./iter_hive9.txt", "./beaten_hive9.txt", "./outputs/", False, file_list)
