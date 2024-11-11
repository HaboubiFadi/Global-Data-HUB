import sys
import os 
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Models'))
import joblib
import numpy as np
import psycopg2
import pickle
class Service():
    def __init__(self,model_name,scaler_name,model_name_database,scaler_name_database):
        
        database=True 
        db_config = {
        'dbname': 'postgres',
        'user': 'admin',
        'password': 'admin',
        'host': 'postgres',  # Or your database host
        'port': '5432'  # Default PostgreSQL port
        }
        try:
            # Connect to PostgreSQL
            conn = psycopg2.connect(**db_config)
            cursor = conn.cursor()

            # Fetch the model from the table
            fetch_model_query = """
            SELECT model_data FROM model_storage
            WHERE model_name = %s;
            """
            cursor.execute(fetch_model_query, (model_name_database,))
            model_blob = cursor.fetchone()[0]

            # Deserialize the model
            model = pickle.loads(model_blob)
            self.Model=joblib.load(model)

            print("Model loaded from PostgreSQL successfully!")

            conn = psycopg2.connect(**db_config)
            cursor = conn.cursor()

            # Fetch the model from the table
            fetch_scaler_query = """
            SELECT scaler_data FROM scalers_storage
            WHERE scaler_name = %s;
            """
            cursor.execute(fetch_scaler_query, (scaler_name_database,))
            scaler_blob = cursor.fetchone()[0]

            # Deserialize the model
            scaler = pickle.loads(scaler_blob)
            self.Scaler=joblib.load(scaler)
            
            print("Scaler loaded from PostgreSQL successfully!")
            if cursor:
                cursor.close()
            if conn:
                conn.close()  

        except Exception as e:
            database=False
            pass
        
        
        if database==False:
            current_dir = os.getcwd()

                

            joblib_in = open(current_dir+"/Resources/"+model_name,"rb")
            
            
            
            
            
            
            self.Model=joblib.load(joblib_in)
            
            
            
            
            
            joblib_in = open(current_dir+"/Resources/"+scaler_name,"rb")
        
        
        
        
            self.Scaler=joblib.load(joblib_in)
    def predict(self,data):
        matrix=np.array(list(data.values())).reshape((1,-1))
        scaled_data=self.Scaler.transform(matrix)  
        print('/////////////////',scaled_data)
        prediction = self.Model.predict(scaled_data)
        print(prediction)
        return prediction
  