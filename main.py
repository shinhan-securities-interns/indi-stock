import threading

from fastapi import FastAPI
from controllers.IndiStockController import router as indi_stock_router
from services.IndiStockService import run_indi_app
import sys
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_directory, "controllers"))
sys.path.append(os.path.join(current_directory, "services"))

app = FastAPI()

app.include_router(indi_stock_router, prefix="/indi-stock", tags=["indi-stock"])

def run_fastapi_server():
    import uvicorn
    host = os.getenv("HOST")
    port = int(os.getenv("PORT"))
    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    indi_thread = threading.Thread(target=run_indi_app)
    indi_thread.start()

    server_thread = threading.Thread(target=run_fastapi_server)
    server_thread.start()

