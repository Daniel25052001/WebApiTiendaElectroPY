



import uvicorn 

def start():
    uvicorn.run( "application.webapitiendaelectroPY:app",
        host="127.0.0.1",
        port=7000,
        reload=True
    )


if __name__ == "__main__":
    start()
    