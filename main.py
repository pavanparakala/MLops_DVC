from src.CnnClassifier.utils import logger
from src.CnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"


try:
    logger.info(f">>>> stage {STAGE_NAME} <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<<<\n\nx==============x")
except Exception as e:
    logger.info(e)
    raise e


