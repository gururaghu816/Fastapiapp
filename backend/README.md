# Fastapiapp

## creating fastapi application


## crud operations
-create
-read
-update
-delete


## Rest API

-Get
-Post
-Put
-Del


## Architecture of FastAPI application
--Model  
--Router  
--Controller  
--Service  
--Repositor  
--Middleware  
--Schem  

## models
alembic ---- database migration



# concepts
# Concepts:

pip install alembic

alembic init alembic

alembic -> env.py -> from imported model -> metadata data

alembic.ini -> sqlalchemy.url = postgres url
--> postgresql://user:password@host:port/database_name

alembic revision --autogenerate -m "initial migration"

alembic upgrade head


npm install axios
 
 UI -- axios -- localhost:8000 (app call)-- fastapi(python) -- db -- useeffect -- setsstate -- rerender -- UI


 useEffect -- Which is used call the Api or which is used to fetch the data from the api automatically when the page is loaded  

useState- which is used to store the data in the component and which
will update the component when the data is updated or changed
