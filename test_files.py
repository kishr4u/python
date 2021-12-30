from files import *
import unittest

class FileTest(unittest.TestCase):
    
    def test_files_count(self):
        filenam1 = ('first.py','second.py','third.py')
       
        self.assertEqual(count_words(filenam1[0]),84)
        self.assertEqual(count_words(filenam1[1]),189)
        self.assertEqual(count_words(filenam1[2]),13, "file names dont match")

if __name__=='__main__':
    unittest.main()
            
