from opensearchpy import OpenSearch
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
                    'refresh_interval': -1,
                    'translog.flush_threshold_size': '10gb',
                    'number_of_replicas': 0
                },
            },
            'mappings': {
                'properties': {
                    'fvec': {
                        'type': 'knn_vector',
                        'dimension': 1280
                    },
                    'url': {
                        'type': 'keyword'
                    }
                }
            }
        }


    def create_index(self): 
        res = self.client.indices.create(self.index_name, body=self.index_body)
        print(res)

    def delete_index(self):
        res = self.client.indices.delete(self.index_name)
        print(res) 


    def bulk(self, vectors):
        print(2)

    
    def query(self, vector):
        print(3)   




