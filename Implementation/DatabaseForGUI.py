import sqlite3

class Database:
  def __init__(self, db_name):
    self._db_name = db_name
    self.CreateTables()
    
  def ExecuteSql(self, sql):
    with sqlite3.connect(self._db_name) as db:
      cursor = db.cursor()
      cursor.execute(sql)
    
  def CreateTables(self):
    sql = """create table if not exists Teacher
            (TeacherID integer,
            Name text,
            primary key(TeacherID))"""
    self.ExecuteSql(sql)
    
  def AddNewTeacher(self, name):
    sql = """insert into Teacher values
            ((SELECT max(TeacherID) FROM Teacher)+1,
            '{0}')""".format(name)
    self.ExecuteSql(sql)
    
  def GetAllTeachers(self):
    with sqlite3.connect(self._db_name) as db:
      cursor = db.cursor()
      cursor.execute("select * from Teacher")
      teachers = cursor.fetchall()
      return teachers
      
