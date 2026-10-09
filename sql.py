import pymysql

conn=pymysql.connect(
    host='localhost',
    user='root',
    password='samuel@123',
    database='aug2026',
)
cursor=conn.cursor()


#sql="insert into employee values(1,'arun',20000,'dev')"
#sql="insert into employee values(2,'sam',25000,'hr')"
#sql="insert into employee values(3,'samuel',26000,'dev')"
#sql="insert into employee values(4,'neymer',27000,'dev')"
#sql="insert into employee values(5,'messi',28000,'it')"
#sql="insert into employee values(6,'ronaldo',29000,'it')"
#sql="create table employee(id int primary key ,name varchar(20),salary int ,dep varchar(20))"
sql="select * from employee"


cursor.execute(sql)

#row=cursor.fetchcall()
#row=cursor.fetchmany(2)

row=cursor.fetchone()
print (row)
#for i in row:
    #print(i[0],i[1],i[2],i[3])



conn.commit()
conn.close()
