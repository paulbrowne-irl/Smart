import unittest
import scripts.ConfigLoader

class Test_ConfigLoader (unittest.TestCase):
 
    def setUp(self):
        self.loader = scripts.ConfigLoader.ConfigLoader("config.ini")
        

    def test_load_config(self):

        myConfig = self.loader.getConfig()
        self.assertIsNotNone((myConfig.sections()))
        self.assertIsNotNone((myConfig.get("neo4j","uri")))

    def test_readNeo4JValues(self):
    
       # self.assertEqual(self.loader.getConfig().get("neo4j","uri"),self.loader.getUri())

        #Test we are getting values back (differetn, not null)
        self.assertNotEqual(self.loader.getUri(),self.loader.getUser())
        self.assertNotEqual(self.loader.getUri(),self.loader.getPassword())
        self.assertNotEqual(self.loader.getPassword(),self.loader.getUser())

if __name__ == '__main__':
    unittest.main()