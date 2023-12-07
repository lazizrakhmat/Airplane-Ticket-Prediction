from joblib import dump, load

def get_pipeline(model_path):
    pipeline = load(model_path)
    return pipeline

def predict_price(pipeline, data):
    predicted_price = pipeline.predict(data)
    return predicted_price[0]