from src.components.data_ingestion import DataIngestion
from src.entity.config_entity import DataIngestionConfig
from src.exception.exception import NetworkSecurityException
from src.entity.config_entity import TrainingPipelineConfig
from src.logging.logger import logging
import sys


if __name__=='__main__':
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        dataingestion = DataIngestion(dataingestionconfig)

        logging.info("Initiate data ingestion")

        dataingestionartifact = dataingestion.initiate_data_ingestion()
        print(dataingestionartifact)
        
    except Exception as e:
        raise NetworkSecurityException(e, sys)