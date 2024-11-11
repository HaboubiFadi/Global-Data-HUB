from fastapi import APIRouter

import os 
import sys 

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Services'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Models'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Models.recommendation_Classification_base import recommendation_Classification_base

from Services.Service_Regression import Service
import numpy as np
from fastapi import Depends

from auth import User,get_current_user


router=APIRouter(prefix='/Recommendation',
                 tags=['addiction'])


model_name="Recommendation_Classification_models/Recommendation_Classification_model.joblib"
scaler_name="Recommendation_Classification_models/Recommendation_Classification_scaler.joblib"

model_name_database="Recommendation_Classification_model"
scaler_name_database="Recommendation_Classification_scaler"




# Call Service
Service_rating=Service(model_name,scaler_name,model_name_database,scaler_name_database)



@router.post('/Recommendation_Classification/predict')

def predict_rating(data:recommendation_Classification_base,curent_user: User = Depends(get_current_user)
):
    data = data.dict()
    
    prediction=Service_rating.predict(data)
    return {
        'prediction': int(prediction[0])
    } 
   