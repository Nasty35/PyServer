import MySQLdb

class Database():
    def __init__(self, host, user, passwd, db):
        try:
            self.sql = MySQLdb.connect(host, user, passwd, db)
        except MySQLdb.DatabaseError, e:
            print e
        finally:
            print 'MySQL iniciado!'
    def readRows(self, data):
        query = self.sql.cursor()
        query.execute(data)
        return query.fetchall()