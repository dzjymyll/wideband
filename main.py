# -*- coding: utf-8 -*-

#%% Set setup PSO and start optimization
import time
import os
import shutil
from HFSS import HFSS
start_time = time.time()
named_tuple = time.localtime()  # get struct_time
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
time_string_file_name = time.strftime("%m_%d_%Y__%H_%M_%S", named_tuple)
print(f'This program started at: {time_string}')

# Set setup PSO and start optimization
from PSO import PSO

optimization_target='''***************************************************************\n
the target : Design a triple-band antenna\n 
***************************************************************\n'''

Optimization_variables='slot_x', 'slot_y', 'feedline_x'
_base_path = os.getcwd()

hfss_Optimization_record_dir = os.path.join(_base_path,'tripleband')
if not os.path.exists(hfss_Optimization_record_dir):
    os.mkdir(hfss_Optimization_record_dir)
hfss_Optimization_record_file_name = f'Record for simulations {time_string_file_name}.txt'
pso = PSO(Optimization_variables=Optimization_variables, n_dim=3, pop=10, max_iter=20,
          lb=[1,1,1], ub=[38,29,19], w=0.8, c1=0.5, c2=0.5,
          optimization_target=optimization_target,hfss_Optimization_record_dir=hfss_Optimization_record_dir, hfss_Optimization_record_file_name=hfss_Optimization_record_file_name)
pso.run()




# Optimization over and close the software
#h.closeProject()
elapsed_time = time.time() - start_time
print(f'Overall time for this script is: {elapsed_time:.3f}s')
print('Finished all!')

# #print("Files are: %s" %os.listdir(hfss_file_dir))
# #os.removedirs(Hfss_file_path)

# ##Clean temp folder
#shutil.rmtree(hfss_file_dir)
# #os.mkdir(hfss_file_dir)

# ##Clean hfss file result folder
#shutil.rmtree(hfss_result_file_path)
# #os.mkdir(hfss_result_file_path)
