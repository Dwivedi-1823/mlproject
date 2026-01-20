import os, sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation, DataTransformationConfig
from src.components.model_trainer import ModelTrainer, ModelTrainerConfig

@dataclass
class DataIngestionCongig:
    #Creating raw, train, and test files under artifacts folder
    raw_data_path: str = os.path.join('artifacts','data.csv')
    train_data_path: str = os.path.join('artifacts','train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionCongig()

    def initiate_data_ingestion(self):
        logging.info("Entered data ingestion method or component")
        try:
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info("Read the csv data as df")

            #Getting the folder to store raw, train, and test files
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok = True)
            logging.info("parent folder for raw, train and test fetched")

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header= True)

            logging.info("Splitting into train and test and saving as csv")
            train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)

            train_data.to_csv(self.ingestion_config.train_data_path, index=False, header= True)
            test_data.to_csv(self.ingestion_config.test_data_path, index=False, header= True)

            logging.info("Inmgestion of the data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException(e, sys)
        
if __name__=="__main__":
    logging.info("Data ingestion is about to start!!")
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    logging.info("Data transformation on the way...")
    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))
