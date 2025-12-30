from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.components.data_transformation import DataTransformation
from src.entity.config_entity import DataIngestionConfig
from src.entity.config_entity import DataValidationConfig
from src.entity.config_entity import DataTransformationConfig
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
        logging.info("Data ingestion completed")

        datavalidationconfig = DataValidationConfig(trainingpipelineconfig)
        datavalidation = DataValidation(dataingestionartifact,datavalidationconfig)

        logging.info("Initiate data validation")

        datavalidationartifact = datavalidation.initiate_data_validation()
        print(datavalidationartifact)

        logging.info("data validation is completed")

        datatransformationconfig = DataTransformationConfig(trainingpipelineconfig)
        datatransformation = DataTransformation(data_transformation_config=datatransformationconfig, data_validation_artifact=datavalidationartifact)

        datatransformation.initiate_data_transformation()
        logging.info("Data Transformation is completed")

    except Exception as e:
        raise NetworkSecurityException(e, sys)