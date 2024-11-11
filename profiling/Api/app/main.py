import uvicorn
import Routes.rating_regression_router as rating_regression_router
import Routes.Claim_settlement_time_router as Claim_settlement_time_router
import Routes.Comfort_Classification_router as Comfort_Classification_router
import Routes.Financial_d_Classification_router as Financial_d_Classification_router
import Routes.Price_Classification_router as Price_Classification_router
import Routes.Service_Classification_router as Service_Classification_router
import Routes.Financial_s_Classification_router as Financial_s_Classification_router
import Routes.recommendation_Classification_router as recommendation_Classification_router
import auth as auth

from fastapi import FastAPI, Request

from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse


app = FastAPI(title="Insurances Agency APIs",
    description="API with high performance to predict various metrics",
    )


app.include_router(rating_regression_router.router)
app.include_router(Claim_settlement_time_router.router)
app.include_router(Comfort_Classification_router.router)
app.include_router(Financial_d_Classification_router.router)
app.include_router(Price_Classification_router.router)
app.include_router(Service_Classification_router.router)
app.include_router(recommendation_Classification_router.router)
app.include_router(Financial_s_Classification_router.router)
app.include_router(auth.router)


templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    
    return templates.TemplateResponse("index.html", {"request": request})



if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)