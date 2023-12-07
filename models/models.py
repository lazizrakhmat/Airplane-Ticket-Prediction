import os

script_path = os.path.abspath(__file__)
script_directory = os.path.dirname(script_path)
run_script_directory = os.path.dirname(script_path)[:-6]

# airplane_prediction_model_path = script_directory.replace("\\", "/") + "/prediction_model.joblib"
airplane_prediction_model_path = script_directory.replace("\\", "/") + "/prediction_model.joblib"