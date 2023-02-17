import numpy as np
def predict_h(predict_list, model):
    try:
        reshaped = np.array(predict_list).reshape(1, -1)
    except ValueError:
        return "Invalid input. Please enter valid values"

    try:
        result = model.predict(reshaped)
    except Exception as e:
        return f"Error occurred during prediction: {str(e)}"

    if result[0] == 0:
        text = 'The person is not Having Heart Disease'
    else:
        text = 'The person is Having Heart Disease'
    return text
