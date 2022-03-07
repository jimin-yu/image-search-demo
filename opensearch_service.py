import json
from opensearchpy import OpenSearch, helpers
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

class OpensearchService:
    __instance = None

    @classmethod
    def instance(cls):
        if(cls.__instance is None):
            cls.__instance = cls()

        return cls.__instance        

    def __init__(self):
        # By default connect to localhost:9200
        self.client = OpenSearch(
            hosts=[{'host': 'localhost', 'port': 9200}],
            http_auth=('admin', 'admin'),
            use_ssl = True,
            ca_certs = os.path.join(ROOT_DIR, 'security/root-ca.pem'),
            http_compress=True,
            client_cert = os.path.join(ROOT_DIR, 'security/esnode.pem'),
            client_key = os.path.join(ROOT_DIR, 'security/esnode-key.pem'),
            verify_certs = True,
            ssl_assert_hostname = False,
            ssl_show_warn = False)
        self.index_name = 'img_search'
        self.index_body = {
            'settings' : {
                'index' : {
                    'knn': True,
                    'knn.algo_param' : {
                        'ef_search' : 256,
                        'ef_construction' : 128,
                        'm' : 48
                    },
                },
            },
            'mappings': {
                'properties': {
                    'img_vector': {
                        'type': 'knn_vector',
                        'dimension': 1280,
                        'method':{
                            'name': 'hnsw',
                            'space_type': 'l2',
                            'engine': 'nmslib'
                        }
                    },
                    'url': {
                        'type': 'keyword'
                    }
                }
            }
        }

    def create_index(self): 
        if(self.client.indices.exists(index='img_search')):
            self.delete_index()
            
        res = self.client.indices.create(self.index_name, body=self.index_body)
        print(res)


    def delete_index(self):
        res = self.client.indices.delete(self.index_name)
        print(res) 


    def create_doc(self, doc):
        res = self.client.index(index = self.index_name, body = doc) 
        print(res)   


    def delete_doc(self, id):
        res = self.client.delete(index = self.index_name, id = id)
        print(res)


    def bulk(self, doc_array):
        rows = [{'_index': self.index_name, '_source': doc} for doc in doc_array]
        helpers.bulk(self.client, rows)


    def query(self, vector):
        # The plugin returns k amount of results for each shard (and each segment) 
        # and size amount of results for the entire query.
        body = {
            "size": 2,
            "query": {
                "knn": {
                    "img_vector": {
                        "vector": vector,
                        "k": 2
                    }
                }
            },
            "_source": {
                "exclude": ["img_vector"]
            }
        }
        res = self.client.search(request_timeout=30, index=self.index_name, body=body)
        urls = [ (x['_source']['url'], x['_score']) for x in res['hits']['hits']]
        print(urls)




