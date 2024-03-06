from typing import Dict



class MinhaCollectionRepository:
  def __init__(self, db_connection) -> None:
    self.__collection_name = "users"
    self.__db_connection = db_connection
  
  def insert_document(self, document: Dict) -> Dict:
    collection = self.__db_connection.get_db_connection(self.__collection_name)
    collection.insert_one(document)
    return document
