import configparser

#Sample to load config details
class SmartConfig(object):
    'Convenience class to load system configuration'

    def __init__(self, config_file_name=None):

        #set defaults on incoming argumenst
        if(config_file_name==None):
            config_file_name="config.ini"

        self.config = configparser.ConfigParser()
        self.config.read(config_file_name)
        print(self.config.sections())

    def __str__(self):
        return "host:"+self.getHost()+"port "+self.getPort()+" user:"+self.getUser()+" password:"+self.getPassword()

    def getConfig(self):
        return self.config

    def getHost(self):
        return self.config.get("neo4j","host")

    def getUser(self):
        return self.config.get("neo4j","user")

    def getPassword(self):
        return self.config.get("neo4j","password")

    def getPort(self):
        return self.config.get("neo4j","port")
   

# simple code to run / test class from command line
if __name__ == '__main__':
    config = SmartConfig("config.ini").config
    print(config.sections())
    print(config.get("neo4j","uri"))
