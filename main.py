from fastapi import FastAPI

app = FastAPI()
app.title = "Cool heart predictor to not die"


from routers.request import router as query_router
app.include_router(query_router, prefix="/api")