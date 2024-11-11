from fastapi import APIRouter

import os 
import sys 

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Services'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Models'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from fastapi import Depends

from auth import User,get_current_user
from Models.Financial_s_Classification_base import Financial_s_Classification_base

from Services.Service_Regression import Service
import numpy as np

router=APIRouter(prefix='/Financial_s',
                 tags=['addiction'])


model_name="Financial_s_Classification_models/Financial_s_Classification_model.joblib"
scaler_name="Financial_s_Classification_models/Financial_s_Classification_scaler.joblib"

model_name_database="Financial_s_Classification_model"
scaler_name_database="Financial_s_Classification_scaler"




# Call Service
Service_rating=Service(model_name,scaler_name,model_name_database,scaler_name_database)







@router.post('/Financial_s_Classification/predict')

def predict_rating(data:Financial_s_Classification_base,curent_user: User = Depends(get_current_user)):
    data = data.dict()
    
    prediction=Service_rating.predict(data)
    return {
        'prediction': int(prediction[0])
    } 
   