from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.endpoints.users import router
from src.models.conection_options.conection import DBConnectionHandler


app = FastAPI(
    title='cookbook',
    version='0.1.0',
    description='Um APP para Adicionar as suas receitas favoritas, e ter sempre em mãos.'
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(router, prefix='/api')

db_handle = DBConnectionHandler()
db_handle.connect_to_db()
db_connection = db_handle.get_db_connection()

 


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host="0.0.0.0", reload=True, log_level='info')
