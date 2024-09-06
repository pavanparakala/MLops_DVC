from src.CnnClassifier.config.configuration import ConfigurationManager
from src.CnnClassifier.components.prepare_base_model import PrepareBaseModel
from src.CnnClassifier.utils import logger


STAGE_NAME = "Prepare base model"


class PrepareBaseModelTrainingPipline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()


if __name__ == "__manin__":
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started<<<<<<<<")
        obj = PrepareBaseModelTrainingPipline()
        obj.main()
        logger.info(
            f">>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx==========x"
        )
    except Exception as e:
        logger.exception(e)
        raise e
