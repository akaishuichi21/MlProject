import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass




@dataclass
class DataConfig:
    trainPath: str
    testPath: str
    dataPath: str


class DataIngestion:
    def __init__(self):
        self.config = DataConfig(
            os.path.join("artifacts", "train.csv"),
            os.path.join("artifacts", "test.csv"),
            os.path.join("artifacts", "data.csv"))
        
    

    def initiateDataIngestion(self):
        logging.info("Data ingestion is being initiated")

        try:
            data = pd.read_csv("./data/stud.csv")
            print(data.head())
            logging.info("data has been loaded into a dataframe")
            os.makedirs(os.path.dirname(self.config.dataPath), exist_ok=True)
            data.to_csv(self.config.dataPath, index=False, header=True)
            
            trainData, testData = train_test_split(data, test_size=0.25)

            trainData.to_csv(self.config.trainPath, index=False, header=True)
            testData.to_csv(self.config.testPath, index=False, header=True)

            logging.info("data has been split and saved into their respective places")

            return(self.config.trainPath, self.config.testPath)


        except Exception as e:
            raise CustomException(e, sys)



if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiateDataIngestion()