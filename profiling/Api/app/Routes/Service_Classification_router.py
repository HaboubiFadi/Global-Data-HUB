from fastapi import APIRouter

import os 
import sys 

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Services'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Models'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from fastapi import Depends

from Models.Service_Classification_base import Service_Classification_base

from Services.Service_Regression import Service
import numpy as np
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from auth import User,get_current_user


router=APIRouter(prefix='/Service',
                 tags=['addiction'])


model_name="Service_Classification_models/Service_Classification_model.joblib"
scaler_name="Service_Classification_models/Service_Classification_scaler.joblib"

model_name_database="Service_Classification_model"
scaler_name_database="Service_Classification_scaler"




# Call Service
Service_rating=Service(model_name,scaler_name,model_name_database,scaler_name_database)


@router.post('/Service_Classification/predict')

def predict_rating(data:Service_Classification_base,curent_user: User = Depends(get_current_user)
):
    data = data.dict()
    
    prediction=Service_rating.predict(data)
    return {
        'prediction': int(prediction[0])
    } 
   