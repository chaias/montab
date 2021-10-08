#import cx_Oracle
#import os
#import sys

#print(sys.version)
#print(os.environ['ORACLE_HOME'])
#print(os.environ['path'])

#con = cx_Oracle.connect('SCI/SCI@192.9.200.12:1521/orcl.mosi.com.gt ')
#print (con.version)

#con.close()
import cx_Oracle


con = cx_Oracle.connect('SCI/SCI@192.9.200.12:1521/orcl.mosi.com.gt')

cur = con.cursor()
cur.execute("select * from montab order by moncod")
res = cur.fetchall()
for row in res:
    print(row)
