import unittest
from data_clean import clean_nodes

class TestDict(unittest.TestCase):
    def test_original(self):
        _dict = {'name':{'first':'Robert','middle':'','last':'Smith'},'age':25,'DOB':'-','hobbies':['running','coding','-'],'education':{'highschool':'N/A','college':'Yale'}}
        _clean = {'name': {'first': 'Robert', 'last': 'Smith'},'age': 25, 'hobbies': ['running', 'coding'], 'education': {'college': 'Yale'}}
        self.assertEqual(clean_nodes(_dict), _clean)

    def test_deep_4(self):
        _dict = {'name':{'first':'Robert','middle':'','last':'Smith'},'age':25,'DOB':'-','hobbies':['running','coding','-', 'N/A'],'education':{'highschool':{'country': 'USA', 'course': {'first': 'N/A', 'second': 'yes', 'third': {'another': 'yes', 'this_no': ''}}},'college':'Yale'}}
        _clean = {'name': {'first': 'Robert', 'last': 'Smith'}, 'age': 25, 'hobbies': ['running', 'coding', 'N/A'], 'education': {'highschool': {'country': 'USA', 'course': {'second': 'yes', 'third': {'another': 'yes'}}}, 'college': 'Yale'}}
        self.assertEqual(clean_nodes(_dict), _clean)

if __name__ == '__main__':
    unittest.main()