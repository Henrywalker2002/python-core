import unittest
from dataclasses import dataclass, FrozenInstanceError

class DictManagement:
    @staticmethod
    def add_to_dic(dic, key, value):
        dic[key] = value 
        return dic 
    
    @staticmethod
    def remove_key_from_dic(dic, key):
        dic.pop(key)
        return dic
    
    @staticmethod 
    def get_value_by_key(dic, key):
        return dic[key]

class TestData(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.dic = {}
    
    def test_function_add_to_dic(self):
        self.dic = DictManagement.add_to_dic(self.dic, 'key', 'value')
        self.assertEqual(self.dic['key'], 'value')
        
    def test_function_remove_from_dic(self):
        self.dic['key'] = 'value'
        self.dic = DictManagement.remove_key_from_dic(self.dic,'key')
        self.assertRaises(KeyError, DictManagement.get_value_by_key, self.dic, 'key')
        
    def tearDown(self):
        self.dic = {}
        
@dataclass(frozen= True)
class Imutetable(object):
    val : any
    
    def get(self):
        return self.val
    
    def set_val(self, val):
        self.val = val 
    
class TestImmutable(unittest.TestCase):        
    def setUp(self):
        self.o = Imutetable(5)
        
    def test_get_val(self):
        self.assertEqual(self.o.get(), 5)
    
    def test_set_val(self):
        self.assertRaises(FrozenInstanceError, self.o.set_val, 3)
    
    def tearDown(self):
        self.o = None 
        
unittest.main()