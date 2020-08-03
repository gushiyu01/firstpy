# # 导入pymysql模块
# import pymysql
# # 连接database
# conn = pymysql.connect(host="47.104.168.202", user="root",password="root",database="python_db",charset="utf8mb4")
# # 得到一个可以执行SQL语句的光标对象
# cursor = conn.cursor()
# # 定义要执行的SQL
# sql = 'insert into pytable(id, ttt) values (%s, %s);'
# # 执行SQL语句
# s = cursor.execute(sql, ('aaa', 'bbb'))
#
# # 关闭光标对象
# cursor.close()
# # 关闭数据库连接
# conn.close()
