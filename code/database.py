print('''
=======================================

Creater: 
\t1) Sarvesh Dakhore

=======================================

''')
import uuid
mac_ad="a"+str((hex(uuid.getnode())))
import platform
import os
try:
    import mysql.connector
except:
    os.system("pip install mysql-connector-python")
    import mysql.connector
from mysql.connector import Error

if platform.system()=="Windows":
    apps_list_win=[[""],["MsEdge", "Microsoft Edge","edge","edge browser","micrisoft browser"],["chrome","Google chrome","browser","net surfing in google ","net surfing"],["Excel","Microsoft Excel","excel","microsoft excel","data entry"],["onenote","Microsoft OneNote","one note","office","ms office"],["powerpnt","Power Point","powerpoint","power point","Presentation","ppt presentation"],["winword","MS Word","word","writing pad"]]
else:
    apps_list_win=[[""],["System Preferences","System Preferences","setting","settings"],["Photos","Photos","photos","photo"],["Preview","Preview","preview"],["Music","Music","music","musics"],["Podcasts","Podcasts","podcasts"],["iMovie","iMovie","imovie","video editing"],["KeyNote","KeyNote","keynote","presentation"],["Stocks","Stocks","stocks","stock"],["Xcode","Xcode","xcode"]]
while True:
    pas=str(input("enter password of mysql localhost server: "))
    try:
        mydb = mysql.connector.connect(host="localhost",user="root",passwd=pas,charset = 'utf8')
        pop=0
    except Error:
        print("wrong password... Try again \n --------------------------------------")
        pop=1
    if pop==0:
        break
    
#-------------------------------------------------------------------------
def lts(lst):
    return (str('0'.join(lst)))

def stl(string):
    return (list(string.split('0')))
#------------------------------------------------------------------------

cursor=mydb.cursor()
cursor.execute("CREATE DATABASE if not exists usr_data_137642387sqlalchemy")
cursor.execute("USE usr_data_137642387sqlalchemy")
cursor.execute("show tables")
x=cursor.fetchall()
tb_l=[]
for i in x:
    tb_l.append(i[0])
if mac_ad in tb_l:
    pass
else:
    t_s="create table if not exists "+ mac_ad +" (app_data text)"
    cursor.execute(t_s)
    for i in range(1,len(apps_list_win)):
        cursor.execute("insert into " + mac_ad + " values('"+  lts(apps_list_win[i])  +"')")
        mydb.commit()

def retrive_app_data():
    cursor.execute("select * from "+mac_ad)
    app_d=list(cursor.fetchall())
    app_list_win=[[""]]
    for i in range(0,len(app_d)):
        app_list_win.append(stl(app_d[i][0]))
    return (app_list_win)

def close_s():
    if mydb.is_connected():
        cursor.close()
        mydb.close()
        print("MySQL connection is closed")

def remove_app_sql(s_no):
    apps_list_win=retrive_app_data()
    cursor.execute("delete from "+ mac_ad +" where app_data='"+ lts(apps_list_win[s_no]) +"'")
    mydb.commit()

def add_app_sql(tmp_sql_list):
    cursor.execute("insert into " + mac_ad + " values('"+  lts(tmp_sql_list) +"')")
    mydb.commit()


