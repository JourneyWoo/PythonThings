#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 18:07:23 2017

@author: wuzhenglin
"""
import sys
sys.path.insert(0, '//Users/wuzhenglin/Python_nice/python100/python001')

import pymysql
import datetime

from python001_net import generate

def mysql(num):
    
    conn = pymysql.connect(host='127.0.0.1', port = 3306, user='root', password='yyyy', db='python_test')
    cur = conn.cursor()
    drop_table = '''DROP TABLE IF EXISTS code'''
    cur.execute(drop_table)
    sql_create_table = '''
        CREATE TABLE code(
        id   INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
        codes VARCHAR(64) NOT  NULL ,
        create_time VARCHAR(64) NOT  NULL );
    '''
    cur.execute(sql_create_table)
    
    for i in range(num):
        create_time = datetime.datetime.now()
        sql_insert_table = '''INSERT INTO code(codes,create_time) VALUES('TestCode','%s')'''%create_time
        cur.execute(sql_insert_table)
        id = conn.insert_id() #conn.insert_id() before conn.commit()，else return 0
        code = generate(1)
        code_ = code[0]
#        print code_
        sql_update_table ='''UPDATE code SET codes = '%s' WHERE id = %s'''%(code_, id)
        cur.execute(sql_update_table)
        
    conn.commit()
    cur.close()
    conn.close()
    
#def create_code(id, length=15):
#    code = hex(int(id))+'L'
#    length_rdm = length - len(code)
#    random_num = ''.join(random.sample(string.letters+string.digits,length_rdm))
#    return code + random_num

if __name__ == '__main__':
    mysql(200)
        
        
        
        
        
        
        
        
        
        
        
        