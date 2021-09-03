import unittest
import mysql.connector
import logging

class Testconnection(unittest.TestCase):
    logging.basicConfig(filename=r"C:\\Users\\nagab\\OneDrive\\Desktop\\example.log', encoding='utf-8', level=logging.INFO")
        
    def test_connection(self): 
        
        try:
            self.db_connection = mysql.connector.connect(
               host = 'localhost',
               user = 'root',
               passwd = 'bhavyateja',
                     
            )
            self.assertTrue(self.db_connection.is_connected())
            
        except:
            logging.error('Not Working!') 
        
        else:
             logging.info('Working!')


if __name__ == '__main__':
    unittest.main()
        
