from fastapi import FastAPI

app = FastAPI(title="MoneyTracker")


@app.get("/")
async def root():
    return {"message": "Welcome to MoneyTracker API"}


@app.get("/health")
async def health_check():
    return {"status": "ok"}
