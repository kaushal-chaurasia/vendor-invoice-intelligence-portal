import joblib
import pandas as pd

MODEL_PATH = "freight_cost_prediction/models/predict_freight_model.pkl"

def load_model(model_path=MODEL_PATH):
    """
    Load trained freight cost prediction model.
    """
    with open(model_path, 'rb') as f:
        model = joblib.load(f)
    return model


def predict_freight_cost(input_data):
    """
    Predict freight cost for new vendor invoices.

    Parameters
    ----------
    input_data : dict

    Returns
    -------
    pd.DataFrame with predicted freight cost
    """
    model = load_model()

    input_df = pd.DataFrame([input_data])

    # 🔥 AUTO MATCH FEATURES (BEST FIX)
    input_df = input_df[model.feature_names_in_]

    input_df['Predicted_Freight'] = model.predict(input_df).round(2)

    return input_df


if __name__ == "__main__":
    # ✅ Correct sample input (ALL REQUIRED FEATURES)
    sample_data = {
        "Quantity": 10,
        "Dollars": 500
    }

    predictions = predict_freight_cost(sample_data)
    print(predictions)