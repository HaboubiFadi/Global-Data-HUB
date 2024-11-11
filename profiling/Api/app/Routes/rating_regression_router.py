from fastapi import APIRouter

import os 
import sys 

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Services'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Models'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Models.rating_base import Rating_Base

from Services.Service_Regression import Service
import numpy as np

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from fastapi import Depends

from auth import User,get_current_user

router=APIRouter(prefix='/Rating_regression',
                 tags=['addiction'])


model_name="Rating_regression_models/Rating_regression_model.pkl"
scaler_name="Rating_regression_models/Rating_regression_scaler.joblib"

model_name_database="Rating_regression_model"
scaler_name_database="Rating_regression_scaler"




# Call Service
Service_rating=Service(model_name,scaler_name,model_name_database,scaler_name_database)


@router.post('/rating/predict')

def predict_rating(data:Rating_Base,curent_user: User = Depends(get_current_user)
):
    data = data.dict()
    
    prediction=Service_rating.predict(data)
    return {
        'prediction': prediction[0]
    } 
   