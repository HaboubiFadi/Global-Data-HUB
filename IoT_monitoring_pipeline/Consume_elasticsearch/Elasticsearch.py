from elasticsearch import Elasticsearch


import pandas as pd



class Elasticsearch_instance():
    def __init__(self,server):
        self.es=Elasticsearch(server)
        print(self.es.info().body)
        

    

    def create_index(self,index_name,mapping):
        res= self.es.indices.create(index=index_name,mappings=mapping)
        print(res)

    def add_data(self,single_data_doc,index_name):
        print(self.es.cat.count(index=index_name, format="json"))
        self.es.index(index=index_name,document=single_data_doc) 
        self.es.indices.refresh(index=index_name)
        print(self.es.cat.count(index=index_name, format="json"))



    def search_data_with_filter(self,es,index_name,filter_query):
        try :
            resp=self.es.search(index=index_name,query=filter_query)
            print(resp)
            return resp
        except Exception as e:
            print('Exeption show Error',e)

    def delete_doc_with_id(self,index_name,data_id):
        try:
            return self.es.delete(index=index_name,id=data_id)
        except:
            print('Problem in Deleting')   

    def delete_index(self,index_name):
        try:
            return self.es.indices.delete(index=index_name)
        except:
            print('Problem in Deleting') 

    def search_data_with_id(self,index_name,id):
        res = self.es.get(index=index_name, id=id)
        return res['_source'] if res['found'] else None


    def update_index_data(self,index_name,id, updated_data):
        try:
            self.es.update(index=index_name,id=id, doc=updated_data)
        except Exception as e:
            print('Error',e)





"""

if __name__=='__main__':
    es_instance=Elasticsearch_instance(server)
    #es_instance.connect_elasticsearch(server=server)#Connect
    mapping=mappings = {
        "properties": {
            "title": {"type": "text", "analyzer": "english"},
            
            "year": {"type": "integer"},
            "wiki_page": {"type": "keyword"}
    }
}
    #create_index(es,'test1',mapping=mapping)#Add ind0ex
    data={"title":"to be or not to be" ,"year":1952,"wiki_page":'leonardo@10'}
    #add_data(es,data,'test1')        #Add dato index
    query={
            "bool": {
                "must": {
                    "match_phrase": {
                        "wiki_page": "leonardo@10",
                    }
                }
            },
        }            
    #search_data_with_filter(es,'test1',query)    #search_with_filter
    #update_index_data(es,'test1','S5LxlI0BQpwrUYMobqbY',data) #update data in an index
    #delete_doc_with_id(es,'test1','TZLylI0BQpwrUYMoM6ax')    # Delete data in an index 
    #print(delete_index(es,'movies'))# Delete index

    
"""




