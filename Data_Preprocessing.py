#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 14:26:31 2023

@author: madelinefrank
"""

import os
import pandas as pd
import numpy as np
import pdb
import glob

#%%
datadir='/Users/madelinefrank/Documents/KSU/Course_Work/5_Summer2023/CS_7265/Project/data'
yrs=['2015','2016','2017','2018']
mos=['01','02','03','04','05','06','07','08','09','10','11','12']
fn_fmt='T_ONTIME_REPORTING_{yr}{mo}.csv'
cols=['YEAR','MONTH','DAY_OF_MONTH','DAY_OF_WEEK','FL_DATE','OP_UNIQUE_CARRIER',
      'ORIGIN','ORIGIN_STATE_ABR',
      'DEST',    'DEST_STATE_ABR',
      'CRS_DEP_TIME','DEP_TIME','DEP_DELAY','DEP_DELAY_NEW','DEP_DEL15','DEP_DELAY_GROUP',
      'CRS_ARR_TIME','ARR_TIME','ARR_DELAY','ARR_DELAY_NEW','ARR_DEL15','ARR_DELAY_GROUP',
      'CANCELLED','DIVERTED','CRS_ELAPSED_TIME','ACTUAL_ELAPSED_TIME',
      'DISTANCE','DISTANCE_GROUP',
      'CARRIER_DELAY', 'WEATHER_DELAY','NAS_DELAY','SECURITY_DELAY','LATE_AIRCRAFT_DELAY']
rencols = {'YEAR':'YR','MONTH':'MON','DAY_OF_MONTH':'DAYOFMONTH','DAY_OF_WEEK':'DAYOFWEEK',
           'OP_UNIQUE_CARRIER':'CARRIER',
           'ORIGIN':'ORIG','ORIGIN_STATE_ABR':'ORIG_ST','DEST_STATE_ABR':'DEST_ST',
           'CRS_DEP_TIME':'CRS_T_DEP','DEP_TIME':'ACT_T_DEP',
           'CRS_ARR_TIME':'CRS_T_ARR','ARR_TIME':'ACT_T_ARR',
           'DEP_DELAY_NEW':'DEP_DELAY0','DEP_DEL15':'DEP_DEL15_TF','DEP_DELAY_GROUP':'DEP_DEL_GRP',
           'ARR_DELAY_NEW':'ARR_DELAY0','ARR_DEL15':'ARR_DEL15_TF','ARR_DELAY_GROUP':'ARR_DEL_GRP',
           'CRS_ELAPSED_TIME':'CRS_T_ELAPSED','ACTUAL_ELAPSED_TIME':'ACT_T_ELAPSED',
           'DISTANCE':'DIST','DISTANCE_GROUP':'DIST_GRP',
           'WEATHER_DELAY':'WX_DELAY','SECURITY_DELAY':'SEC_DELAY'}
airports=['ATL', 'ORD', 'DEN', 'LAX', 'DFW', 'PHX', 'SFO', 'LAS', 'SEA', 'MSP',
          'MCO', 'DTW', 'BOS', 'SLC', 'CLT', 'BWI', 'EWR', 'JFK', 'FLL', 'MDW',
          'IAH', 'SAN', 'LGA', 'PHL', 'TPA', 'DCA', 'MIA', 'DAL', 'PDX', 'BNA',
          'STL', 'HOU', 'AUS', 'OAK', 'SJC', 'MSY', 'SMF', 'MCI', 'SNA', 'IAD',
          'RDU', 'SAT', 'RSW', 'MKE', 'PIT', 'CLE', 'IND', 'BUR', 'PBI', 'SJU',
          'CMH', 'BDL', 'ONT', 'ABQ', 'CVG', 'OMA', 'ANC', 'JAX', 'BUF', 'LGB',
          'BOI', 'RNO', 'TUS', 'OKC', 'HNL', 'MEM', 'PVD', 'CHS', 'GEG', 'TUL',
          'RIC', 'ELP', 'ORF', 'ALB', 'GRR', 'COS', 'SDF', 'PSP', 'OGG', 'BHM',
          'FAT', 'MSN', 'DSM', 'ICT', 'ROC', 'MYR', 'SAV', 'LIT', 'SYR', 'MHT',
          'ISP', 'SBA', 'DAY', 'ASE', 'CID', 'GSP']
oconus=['BET','BRW','CDV','DLG','ADQ','FAI','GST','JNU','AKN','KTN','ANC','OME','OTZ','PSG','SCC','SIT','WRG','YAK','ADK','PPG','GUM','KOA','LIH','HNL','OGG','ITO']
airlines=['AA','B6','DL','F9','NK','UA','WN']


#%%
blah=os.path.join(datadir,str(yrs[-1])+'.csv')












