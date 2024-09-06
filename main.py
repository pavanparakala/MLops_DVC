from src.CnnClassifier.utils import logger
from src.CnnClassifier.pipeline.stage_01_data_ingestion import (
    DataIngestionTrainingPipeline,
)
from src.CnnClassifier.pipeline.stage_02_prepare_base_model import (
    PrepareBaseModelTrainingPipline,
)

STAGE_NAME = "Data Ingestion Stage"


try:
    logger.info(f">>>> stage {STAGE_NAME} <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<<<\n\nx==============x")
except Exception as e:
    logger.info(e)
    raise e

STAGE_NAME = " Prepare base model"
try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started<<<<<<<<")
    obj = PrepareBaseModelTrainingPipline()
    obj.main()
    logger.info(f">>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx==========x")
except Exception as e:
    raise e
