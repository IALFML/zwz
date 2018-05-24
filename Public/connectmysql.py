import pymysql


mysqlconfig = {
    'host': '192.168.1.200',
    'port': 3306,
    'user': 'root',
    'password': 'root123456',
    'db': 'pmbox0828'
}



# # 连接资产端数据库
# def conncet_xybaep_mysql():
#     host = "192.168.1.222"
#     user = "aep"
#     password = "aep#123456"
#     db = "xybaep0828"
#     port = 13306
#     xybaep_db = pymysql.connect(host=host, user=user, password=password, db=db, port=port)
#     return xybaep_db
#
# # 连接猪猪数据库
# def conncet_pmbox_mysql():
#     host = "192.168.1.200"
#     user = "root"
#     password = "root123456"
#     db = "pmbox0828"
#     port = 3306
#     pmbox_db = pymysql.connect(host=host, user=user, password=password, db=db, port=port)
#     return pmbox_db


#连接数据库返回一个游标对象
def connect_mysql(**mysqlconfig):
    mysql_db=pymysql.connect(**mysqlconfig)
    return mysql_db


#查询sql
def select_sql(sql):
    mysql_db=connect_mysql(**mysqlconfig)
    mysql_cur = mysql_db.cursor()
    try:
        mysql_cur_sql= mysql_cur.execute(sql)
        results = mysql_cur.fetchall()
        return results
        # for row in results:
        #     # dreamid = row[0]
    except Exception as e:
        print(e)
    finally:
        mysql_db.close()
        mysql_cur.close()


#新增sql
def insert_sql(sql):
    mysql_db=connect_mysql(**mysqlconfig)
    mysql_cur = mysql_db.cursor()
    try:
        mysql_cur_sql= mysql_cur.execute(sql)
        mysql_db.commit()
    except Exception as e:
        mysql_db.rollback()
        print(e)
    finally:
        mysql_db.close()
        mysql_cur.close()


#更新sql
def update_sql(sql):
    mysql_db=connect_mysql(**mysqlconfig)
    mysql_cur = mysql_db.cursor()
    try:
        mysql_cur_sql= mysql_cur.execute(sql)
        mysql_db.commit()
    except Exception as e:
        mysql_db.rollback()
        print(e)
    finally:
        mysql_db.close()
        mysql_cur.close()


#删除sql
def delete_sql(sql):
    mysql_db=connect_mysql(**mysqlconfig)
    mysql_cur = mysql_db.cursor()
    try:
        mysql_cur_sql= mysql_cur.execute(sql)
        mysql_db.commit()
    except Exception as e:
        mysql_db.rollback()
        print(e)
    finally:
        mysql_db.close()
        mysql_cur.close()


if __name__=="__main__":

    # pmbox_db=conncet_pmbox_mysql()
    # pmbox_cur=pmbox_db.cursor()
    # sql = "SELECT id FROM tr_dream t WHERE t.`userId`="+"81380"+" ORDER BY id DESC LIMIT 1;"
    # pmbox_cur_sql= pmbox_cur.execute(sql)
    # results = pmbox_cur.fetchall()
    # for row in results:
    #     dreamid = row[0]
    #     print(dreamid)

    # pmbox_db=connect_mysql(**mysqlconfig)
    # pmbox_cur=pmbox_db.cursor()
    # pmbox_cur=connect_mysql(**mysqlconfig)
    # sql = "SELECT id FROM tr_dream t WHERE t.`userId`="+"81380"+" ORDER BY id DESC LIMIT 1;"
    # pmbox_cur_sql= pmbox_cur.execute(sql)
    # results = pmbox_cur.fetchall()
    # for row in results:
    #     dreamid = row[0]
    #     print(dreamid)

    # sql = "SELECT id FROM tr_dream t WHERE t.`userId`=" + "81380" + " ORDER BY id DESC LIMIT 1;"
    # select_sql(sql)

    # sql = "insert into zhuzhu_0830_usableamt(id,cusId,amount) values(100,100,100);"
    # insert_sql(sql)

    # sql = "update zhuzhu_0830_usableamt set amount=200 where id=100;"
    # update_sql(sql)

    # sql = "delete from zhuzhu_0830_usableamt where id=100;"
    # delete_sql(sql)


    sql = "SELECT id,userid FROM tr_dream t WHERE t.`userId`=" + "81380" + " ;"
    x=select_sql(sql)
    print(x)
    for row in x:
        print(row)