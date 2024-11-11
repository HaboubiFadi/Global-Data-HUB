from fastapi import APIRouter

import os 
import sys 
from fastapi import Depends

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Services'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Models'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Models.Financial_d_Classification_base import Financial_d_Classification_base

from Services.Service_Regression import Service
import numpy as np
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from auth import User,get_current_user
curent_user: User = Depends(get_current_user)
router=APIRouter(prefix='/Financial_d',
                 tags=['addiction'])


model_name="Financial_d_Classification_models/Financial_d_Classification_model.joblib"
scaler_name="Financial_d_Classification_models/Financial_d_Classification_scaler.joblib"

model_name_database="Financial_d_Classification_model"
scaler_name_database="Financial_d_Classification_scaler"




# Call Service
Service_rating=Service(model_name,scaler_name,model_name_database,scaler_name_database)






@router.post('/Financial_d_Classification/predict')

def predict_rating(data:Financial_d_Classification_base):
    data = data.dict()
    
    prediction=Service_rating.predict(data)
    return {
        'prediction': int(prediction[0])
    } 
   