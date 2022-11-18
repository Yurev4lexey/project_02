
import sqlite3




def get_connection():
  connection = sqlite3.connect("teatchers_new.db")
  return connection


def close_connection(connection):
  if connection:
    connection.close()

# connection = get_connection()
# cursor = connection.cursor()
# query = """CREATE TABLE Students_base(Student_id INTEGER NOT NULL PRIMARY KEY,Student_name TEXT NOT NULL,
#                     School_id INTEGER NOT NULL,School_name TEXT NOT NULL);"""
# cursor.execute(query)
# query_insert = """INSERT INTO Students_base(Student_id,Student_name,School_id,School_name)
# VALUES('201','Иван','1','Протон'),
# ('202','Петр','2','Перспектива'),
# ('203','Анастасия','3','Спектр'),
# ('204','Игорь','4','Содружество');"""
# cursor.execute(query_insert)
# connection.commit()
# close_connection(connection)


def get_student_detail(Student_id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    select_query = """SELECT * FROM Students_base WHERE Student_Id = ?"""
    cursor.execute(select_query, (Student_id,))
    records = cursor.fetchall()
    print ("Данные по студенту")
    for row in records:
      print ("ID студента:", row[0])
      print ("Имя студента:", row[1])
      print ("ID школы:", row[2])
      print ("Название школы:", row[3])
    close_connection(connection)
  except (Exception, sqlite3.Error) as error:
    print ("Ошибка в получении данных по студенту ", error)

get_student_detail(202)  # номер ID студента
