from hdfs.ext.kerberos import KerberosClient
from  hdfs.ext.dataframe import write_dataframe
import pandas as pd

#TODO

df = pd.read_csv ('dataset.csv')
client = KerberosClient('http://hdfs-nn-1.au.adaltas.cloud:50070')
hdfs_path = '/education/cs_2022_spring_1/s.adda-cs/PFR/'
client.upload(hdfs_path, 
            '/Users/sio/Documents/TD/hadoop_file_rouge/', 
            n_threads=1, 
            temp_dir=None, 
            overwrite = True,
            chunk_size=65536, 
            progress=None, 
            cleanup=True)
