from fastapi import FastAPI
from langserve import add_routes
from lcel.server.server import server_chain
#Initialize fast api
app=FastAPI(title="Langchain Server",
            version='0.1',
            description="A simple api server using langchain runnable interface")


#Add chain route

add_routes(
    app,
    server_chain(),
    path="/chain"  
)

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000)
