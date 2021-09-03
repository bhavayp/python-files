from os import name
import unittest
import MySQLdb
import logging

class Testconnection(unittest.TestCase):
    def dbconn(self):
        try:
            db_connection = MySQLdb.connect(
               Host = 'localhost',
               User = 'root',
               Password = 'bhavyateja',
               database= 'test',
                     
            )
            
        except:
            print("Can't connect to DB")
            return 0
            print('connected')
        
        cursor = db_connection.cursor() 

class EasyTest(unittest.TestCase):
    def test_one(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
        
