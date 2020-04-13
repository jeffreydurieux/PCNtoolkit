# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 14:34:06 2017

@author: andmar
"""
#import nispat
import os
import time
from nispat.normative_parallel import execute_nm, collect_nm, delete_nm

data_dir = '/home/preclineu/andmar/py.sandbox/normative_oslo/'
respfile = os.path.join(data_dir, 'ICA100_oslo15_v2_spaces.txt')
covfile = os.path.join(data_dir, 'cov_oslo15_spaces.txt')

cvfolds = 2

python_path = '/.../.conda/envs/python3/bin/python'
normative_path = '/.../nispat/nispat/normative.py'
processing_dir= '/.../'
job_name = 'nmp_test'
batch_size = 10
memory = '4gb'
duration = '01:00:00'
cluster = 'torque'

execute_nm(processing_dir, python_path, normative_path, job_name, covfile,  respfile,
           batch_size, memory, duration, cluster_spec=cluster, 
           cv_folds=cvfolds, log_path=processing_dir)#, alg='rfa')#, configparam=4)

print("waiting for jobs to finish ...")
time.sleep(60)

collect_nm(processing_dir, job_name, collect=True)
#delete_nm(procedssing_dir)

