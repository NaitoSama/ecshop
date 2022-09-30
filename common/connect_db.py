'''
连接数据库
'''

import pymysql

class ConnectDB:
    def __init__(self):
        self.db = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='',
            db='ecshop',
            charset='utf8'
        )
        self.cursor = self.db.cursor()

    def execute_sql(self,sql):
        self.cursor.execute(sql)
        if sql.startswith('select'):
            return self.cursor.fetchall()
        else:
            self.db.commit()

    def close_db(self):
        self.cursor.close()
        self.db.close()


if __name__ == '__main__':
    db = ConnectDB()
    sql = 'insert into ecs_users(user_id,email,user_name) values(2,"dfnwionwa@odf.com","www")'
    db.execute_sql(sql)
    sql = 'select * from ecs_users'
    print(db.execute_sql(sql))
    db.close_db()

