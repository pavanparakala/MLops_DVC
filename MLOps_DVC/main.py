from src.CnnClassifier.utils import logger
from src.CnnClassifier.pipeline.stage_01_data_ingestion import (
    DataIngestionTrainingPipeline,
)
from src.CnnClassifier.pipeline.stage_02_prepare_base_model import (
    PrepareBaseModelTrainingPipline,
)
from src.CnnClassifier.pipeline.stage_03_training import (
    ModelTrainingPipeline,
)
from src.CnnClassifier.pipeline.stage_04_evaluation import EvaluationPipeline

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


STAGE_NAME = "Training"
try:
    logger.info(f"***********")
    logger.info(f">>>>>>>>>stage {STAGE_NAME} staterd <<<<<<<<<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(
        f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx================x"
    )
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Evaluation stage"
try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_evalution = EvaluationPipeline()
    model_evalution.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
    logger.exception(e)
    raise e
