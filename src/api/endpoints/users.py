from fastapi import APIRouter
from src.models.conection_options.conection import DBConnectionHandler
from src.models.repository.minha_collection_repository import MinhaCollectionRepository


router = APIRouter()

collection = MinhaCollectionRepository(db_connection=DBConnectionHandler)

@router.get('/users')
async def get_users():
  documento = { "nome": "Arnaldo", "idade": 30 }
  collection.insert_document(documento)
  return 'oi'