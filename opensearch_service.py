from elasticsearch import Elasticsearch

class OpensearchService:
    def __init__(self):
        # By default connect to localhost:9200
        self.es = Elasticsearch()
        self.mapping = {
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
                        'dimension': dim
                    }
                }
            }
        }


    def create_index(self):
        print(1)


    def bulk(self, vectors):
        print(2)

    
    def query(self, vector):
        print(3)            



