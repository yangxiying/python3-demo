#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymssql

server = "127.0.0.1"    # 连接服务器地址
user = "sa"             # 连接帐号
password = "Sa123!"     # 连接密码
dbname = "hzmd-demo"    #默认连接的数据库名

#连接sqlserver语法
# db=pymssql.connect(server,user,password,dbname)
# cur=db.cursor()
# cur.execute('select * from fc_bond_info')
# n=1
# for i in cur.fetchall():
#     if n>100:
#         break
#     else:
#         print(i)
#         n+=1
# db.close()



# 使用另一种语法：with 来避免手动关闭cursors和connection连接

# with pymssql.connect(server, user, password, dbname) as conn:
#     with conn.cursor(as_dict=True) as cursor:   # 数据存放到字典中
#         cursor.execute('SELECT * FROM persons WHERE salesrep=%s', 'John Doe')
#         for row in cursor:
#             print("ID=%d, Name=%s" % (row['id'], row['name']))


# 调用存储过程：
# with pymssql.connect(server, user, password, "tempdb") as conn:
#     with conn.cursor(as_dict=True) as cursor:
#         cursor.execute("""
#         CREATE PROCEDURE FindPerson
#             @name VARCHAR(100)
#         AS BEGIN
#             SELECT * FROM persons WHERE name = @name
#         END
#         """)
#         cursor.callproc('FindPerson', ('Jane Doe',))
#         for row in cursor:
#             print("ID=%d, Name=%s" % (row['id'], row['name']))


with pymssql.connect(server, user, password, dbname) as conn:
    with conn.cursor(as_dict=True) as cursor:   # 数据存放到字典中 指定了as_dict为True，则返回结果变为字典类型，这样就能通过列名来访问结果
        cursor.execute('select b.[库存单位] as dw,b.[原煤库存库容量] as ykr ,b.[原煤库存量] as ykc' +
            ',b.[精煤库存库容量] as jkr ,b.[精煤库存量小计] as jkc ,b.[副产品库存库容量] as fkr,b.[副产品总库存量] as fkc'+
            ',b.[煤泥库容量] as nkr,b.[煤泥库存量] as nkc'+
            ' from [dbo].[霍州煤电集团公司库存情况日报表_明细] B ' + 
            ' where B.RCId = %s', 'RC19120700085')
        c2_list = cursor.fetchall()
        # for row in cursor:
        #     print("库存单位=%s, 原煤库容=%s, 原煤库存=%s, 精煤库容=%s, 精煤库存=%s, 副产品库容=%s, 副产品库存=%s, 煤泥库容=%s, 煤泥库存=%s" % (row['dw'], row['ykr'], row['ykc'], row['jkr'], row['jkc'], row['fkr'], row['fkr'], row['nkr'], row['nkr']))

print("=====================================")
for row in c2_list:
    print("库存单位=%s, 原煤库容=%s, 原煤库存=%s, 精煤库容=%s, 精煤库存=%s, 副产品库容=%s, 副产品库存=%s, 煤泥库容=%s, 煤泥库存=%s" % 
    (row['dw'], row['ykr'], row['ykc'], row['jkr'], row['jkc'], row['fkr'], row['fkr'], row['nkr'], row['nkr']))
