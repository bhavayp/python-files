import unittest
import MySQLdb

class TestConnection(unittest.TestCase):
      def test_connection(self):
          self.db_connection=MySQLdb.connect(
               host = "localhost",
               user = "root",
               password = "bhavyateja",
          )
          self.assertTrue("connection is established")
if __name__ == "__main__":
    unittest.main()