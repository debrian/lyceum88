# -*- coding: utf-8 -*-
import subprocess
import string
import os
import pymysql
import pymysql.cursors
f=open('C:\\Python27\\users.txt','r')
new=open('C:\\Python27\\new.cmd','w')
sqlf=open('C:\\Python27\\sql.txt','w')
sqlf2=open('C:\\Python27\\sql2.txt','w')
new.writelines ('chcp 1251 \n')


for line in f:
   
    line=line.split()
    print(line)
    #line=line[:-1]
    if len(line)==1:
            line.append('123456') 
    if line[1]=='-':
        new.writelines('net user ' + line[0] + ' /delete' + '\n')
        new.writelines('rmdir /s /q C:\\share\\home\\' + line[0] + '\n')
        sqlf.writelines("DELETE FROM `lyceum88`.`users2` WHERE `user_name`='"+line[0]+"';\n")
    else:
        new.writelines ('mkdir C:\\share\\home\\' + line[0] + '\n')
        new.writelines ('net user ' + line[0] + ' ' + line[1] + ' /add \n')
        new.writelines ('net user ' + line[0] + ' ' + line[1] + '\n')
        new.writelines ("CACLS C:\\share\\home\\" + line[0] + " /E /R Все" + '\n')
        new.writelines ('CACLS C:\\share\home\\' + line[0] + " /E /G " + line[0] + ":F" + '\n')
        sqlf.writelines ("INSERT INTO `lyceum88`.`users2` (`user_name`, `hash_method`, `password`) VALUES ("+"'"+line[0]+"'"+", 'NONE', '"+line[1]+"');"+"\n")
        sqlf2.writelines ("UPDATE `lyceum88`.`users2` SET `password`='"+line[1]+"' WHERE `user_name`='"+line[0]+"';\n")
    #conn=pymysql.connect(host='192.168.88.100',user='admin',password='AdMiN', db='lyceum88',charset='utf8')
    #a=conn.cursor()
    #sql="INSERT INTO `lyceum88`.`users` (`user_name`, `hash_method`, `password`) VALUES ("+"'"+line+"'"+", 'NONE', '123456');"
    #sqlf.writelines ("INSERT INTO `lyceum88`.`users` (`user_name`, `hash_method`, `password`) VALUES ("+"'"+line[0]+"'"+", 'NONE', '"+line[1]+"');"+"\n")
    #a.execute(sql)
    #a.close()
    #conn.close()
   
new.close()
f.close()
sqlf.close()
sqlf2.close()
#proc = subprocess.Popen("ping -c2 %s" % ip, shell=True, stdout=subprocess.PIPE)
