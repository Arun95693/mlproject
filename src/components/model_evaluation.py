import sys
import pandas as pd
from src.entity.config_entity import ModelEvaluationConfig
from src.entity.artifact_entity import DataIngestionArtifact, DataTransformationArtifact, ModelTrainerArtifact, ModelEvaluationArtifact
from sklearn.metrics import f1_score
from src.exception import CustomerException
from src.logger import logging

class ModelEvaluation:
    def __init__(
        self,
        model_trainer_artifact: ModelTrainerArtifact,
        model_evaluation_config: ModelEvaluationConfig
    ):
        self.model_trainer_artifact = model_trainer_artifact
        self.model_evaluation_config = model_evaluation_config

    def initiate_model_evaluation(self) -> ModelEvaluationArtifact:
        logging.info("Entered model evaluation.")
        try:
            # Only local model comparison
            test_data = pd.read_csv(self.model_evaluation_config.test_data_path, header=0)
            y_true = test_data[self.model_evaluation_config.target_column]
            
            # Load trained model and make predictions (example, adapt to your loading logic)
            from src.utils.main_utils import load_model  # Make sure this exists in your utils
            model = load_model(self.model_trainer_artifact.trained_model_file_path)
            y_pred = model.predict(test_data.drop(self.model_evaluation_config.target_column, axis=1))
            
            f1 = f1_score(y_true, y_pred)
            logging.info(f"F1 score: {f1}")

            artifact = ModelEvaluationArtifact(f1_score=f1)
            return artifact
        except Exception as e:
            raise CustomerException(e, sys)
