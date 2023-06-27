import unittest
from unittest.mock import MagicMock
class Hello:
    """
    Hello class
    """
    
    @staticmethod
    def hello(s:str) -> str:
        """" return decorated hello """
        
        if s == 'Exception':
            raise Exception
        
        return f'hello {s}'

    # @staticmethod
    def mock():
        """
        a mock example
        """
        m = MagicMock('value')
        m.return_value('hello USA')
        
        return m()

class HelloTest(unittest.TestCase):
    
    def test1_valid(tst):
        tst.assertEqual('hello world', Hello().hello('world'))
        
    def test2_exception(tst):
        tst.assertRaises(Exception, Hello.hello, 'Exception')
        
        
    def test_mock(tst):
        tst.assertTrue('hello USA', Hello.mock())

if __name__ == '__main__':
    unittest.main()