from fastapi import APIRouter

import os 
import sys 
from fastapi import Depends
    
    


sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Services'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Models'))

from Models.Claim_settlement_time_base import Claim_settlement_time_base


from auth import User,get_current_user

from Services.Service_Regression import Service
import numpy as np

router=APIRouter(prefix='/Claim_settlement_time',
                 tags=['addiction'])

model_name="Claim_Settlement_time_models/Claim_Settlement_time_regression_model.joblib"
scaler_name="Claim_Settlement_time_models/Claim_Settlement_time_regression_scaler.joblib"
model_name_database="Claim_Settlement_time_regression_model"
scaler_name_database="Claim_Settlement_time_regression_scaler"

Service_rating=Service(model_name,scaler_name,model_name_database,scaler_name_database)


@router.post('/Claim_settlement_time/predict')

def predict_rating(data:Claim_settlement_time_base,curent_user: User = Depends(get_current_user)):
    data = data.dict()
    print(curent_user)
    prediction=Service_rating.predict(data)
    return {
        'prediction': prediction[0]
    } 
   