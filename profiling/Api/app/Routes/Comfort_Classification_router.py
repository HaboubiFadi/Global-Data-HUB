from fastapi import APIRouter

import os 
import sys 

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Services'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Models'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from auth import User,get_current_user
from fastapi import Depends



from Models.Comfort_Classification_base import Comfort_Classification_base

from Services.Service_Regression import Service
import numpy as np




router=APIRouter(prefix='/Comfort',
                 tags=['addiction']
               )


model_name="Comfort_Classification_models/Comfort_Classification_model.joblib"
scaler_name="Comfort_Classification_models/Comfort_Classification_scaler.joblib"

model_name_database="Comfort_Classification_model"
scaler_name_database="Comfort_Classification_scaler"


Service_rating=Service(model_name,scaler_name,model_name_database,scaler_name_database)





@router.post('/Comfort_Classification/predict')
def predict_rating(data:Comfort_Classification_base,curent_user: User = Depends(get_current_user)):
    print(data)

    data = data.dict()
    prediction=Service_rating.predict(data)
    return {
        'prediction': int(prediction[0])
    } 
   