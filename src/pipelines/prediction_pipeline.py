import sys
import os
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object
import pandas as pd

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            preprocessor_path = 'artifacts/preprocessor.pkl'
            model_path = 'artifacts/model.pkl'

            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)
            
            print(features)

            data_scaled=preprocessor.transform(features)
            logging.info('transformation complete')
            pred=model.predict(data_scaled)
            return pred
            

        except Exception as e:
            logging.info("Exception occured in prediction")
            raise CustomException(e,sys)

class CustomData:
    def __init__(self,
                 mean_texture:float,
                 mean_smoothness:float,
                 mean_symmetry:float,
                 area_error:float,
                 concavity_error:float,
                 concave_points_error:float,
                 worst_symmetry:float,
                 worst_fractal_dimension:float,
                 ):
        
        self.mean_texture = mean_texture
        self.mean_smoothness = mean_smoothness
        self.mean_symmetry = mean_symmetry
        self.area_error = area_error
        self.concavity_error = concavity_error
        self.concave_points_error  = concave_points_error
        self.worst_symmetry = worst_symmetry
        self.worst_fractal_dimension = worst_fractal_dimension

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'mean_texture':[self.mean_texture],
                'mean_smoothness':[self.mean_smoothness],
                'mean_symmetry':[self.mean_symmetry],
                'area_error':[self.area_error],
                'concavity_error':[self.concavity_error],
                'concave_points_error':[self.concave_points_error],
                'worst_symmetry':[self.worst_symmetry],
                'worst_fractal_dimension':[self.worst_fractal_dimension]
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df
        
        except Exception as e:
            logging.info('Exception Occured in prediction pipeline, getdataasdataframe function')
            raise CustomException(e,sys)


