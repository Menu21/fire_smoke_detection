import os
from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

app = Flask(__name__)

# Load your trained model (replace with your actual model path)
model = load_model('Models/fire_smoke_prediction.keras')

# Define the classes
classes = ['smoke', 'fire', 'non fire']

def predict_fire_smoke(img_path):
    test_image = image.load_img(img_path, target_size=(150, 150))
    test_image = image.img_to_array(test_image) / 255.0
    test_image = np.expand_dims(test_image, axis=0)

    result = model.predict(test_image).round(3)
    pred = np.argmax(result)
    return classes[pred]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the file from the form
        file = request.files['file']
        if file:
            # Define the directory to save the file
            save_dir = 'path_to_save/'
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)

            # Define the full file path
            file_path = os.path.join(save_dir, file.filename)
            file.save(file_path)

            # Predict
            prediction = predict_fire_smoke(file_path)

            return render_template('result.html', prediction=prediction)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
