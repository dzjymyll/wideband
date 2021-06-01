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
the target : Design a wideband antenna\n 
***************************************************************\n'''

Optimization_variables='dra_x', 'dra_y', 'dra_z', 'strip_y', 'strip_z'
_base_path = os.getcwd()

hfss_Optimization_record_dir = os.path.join(_base_path,'DRA Record')
if not os.path.exists(hfss_Optimization_record_dir):
    os.mkdir(hfss_Optimization_record_dir)
hfss_Optimization_record_file_name = f'Record for simulations {time_string_file_name}.txt'
pso = PSO(Optimization_variables=Optimization_variables, n_dim=5, pop=10, max_iter=10,
          lb=[5,5,5,0.5,1], ub=[50,50,50,10,30], w=0.8, c1=0.5, c2=0.5,
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
