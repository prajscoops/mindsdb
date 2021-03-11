# @TODO, replace with arrow later: https://mirai-solutions.ch/news/2020/06/11/apache-arrow-flight-tutorial/
import xmlrpc.client
import time

from mindsdb.utilities.config import Config
from mindsdb.utilities.log import log


class ModelInterface():
    def __init__(self):
        self.config = Config()
        for _ in range(30):
            try:
                time.sleep(3)
                self.proxy = xmlrpc.client.ServerProxy("http://localhost:17329/")
                assert self.proxy.ping()
                return
            except:
                log.info('Wating for native RPC server to start')
        raise Exception('Unable to connect to RPC server')


    def create(self, name):
        return self.proxy.create(name)

    def learn(self, name, from_data, to_predict, datasource_id, kwargs={}):
        return self.proxy.learn(name, from_data, to_predict, datasource_id, kwargs)

    def predict(self, name, when_data=None, kwargs={}):
        return self.proxy.predict(name, when_data, kwargs)

    def analyse_dataset(self, ds):
        return self.proxy.analyse_dataset(ds)

    def get_model_data(self, name, db_fix=True):
        return self.proxy.analyse_dataset(name, db_fix)

    def get_models(self):
        return self.proxy.get_models()

    def delete_model(self, name):
        return self.proxy.delete_model(name)
