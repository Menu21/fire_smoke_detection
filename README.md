
# Fire and Smoke Detection Model using Deep Learning

Deep learning-based fire detection system designed to identify fire and smoke from images captured by surveillance systems or other resources. This project leverages Convolutional Neural Networks (CNNs) to detect visual characteristics of fires, such as brightness, color, and texture, and compares the results with transfer learning using VGG16. The project also includes a web application (app.py) that allows users to run the model on a local server for real-time detection.

# Problem Statement

Fire outbreaks are a growing concern due to the significant damage they cause to both nature and human interests. Traditional fire detection systems, which rely on temperature or smoke sensors, often suffer from slow response times and inefficiency, especially when the fire is distant from the detectors. Moreover, these systems can be expensive.

As an alternative, this project explores the use of computer vision and deep learning techniques for fire detection. By analyzing images for specific visual features associated with fires, this approach aims to provide a faster, more cost-effective solution that can be integrated with existing surveillance systems.

# Objectives

### The main objectives of this project are:

- To develop a fire detection model using CNNs that can accurately identify fires from images.
- To compare the performance of the CNN-based model with a transfer learning approach using VGG16.
- To build a web application that allows users to run the fire detection model on a local server.

# Folder Details

- **notebooks/:** Contains Jupyter notebooks for data exploration, model training, and transfer learning.
- **data/:** Includes raw and processed datasets used for training and testing the models.
- **models/:** Stores the trained CNN and VGG16 models.
- **visuals/:** Contains visualizations of the data and results from the model evaluations.
- **app.py:** The Flask-based web application that allows users to run the fire detection model locally.
- **requirements.txt:** Lists all the dependencies needed to run the project.




## How to Run the Project

### Prerequisites
- Python 3.10 or higher
- pip (Python package installer)

Clone the project

```bash
  git clone https://github.com/Menu21/fire_smoke_detection.git
```

Go to the project directory

```bash
  conda create -n fire python=3.10 -y
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Run the Web Application

```bash
  python app.py

```
### View Results
The application will start on **http://127.0.0.1:5000/.** You can upload images and see the fire detection results in real time.

# Technology Benefits

## Compared to Traditional Approaches

### Traditional Fire Detection Systems:

- **Sensors:** Rely on temperature or smoke detectors.
- **Response Time:** Slower, especially if the fire is far from the sensors.
- **Cost:** Expensive, as they require specialized hardware.
- **Scalability:** Limited to physical installation of sensors.

# Fire_and_smoke_detection(Deep Learning-Based):

- **Vision-Based Detection:** Uses images from existing surveillance cameras, eliminating the need for additional hardware.
- **Response Time:** Faster detection as it identifies visual cues directly from images.
- **Cost-Effective:** Lowers costs by utilizing existing infrastructure.
- **Scalable:** Can be easily integrated into any system with camera surveillance, making it highly scalable.

This technology provides a practical, scalable, and cost-effective solution to fire detection, with the potential to save lives and reduce damage by enabling faster response times.

# Future Work

- **Data Augmentation:** Enhance the dataset with more diverse fire scenarios to improve model robustness.
- **Real-Time Video Analysis:** Extend the model to process real-time video feeds.
- **Cloud Deployment:** Deploy the model on cloud platforms for wider accessibility and scalability.

# Conclusion

Fire_and_smoke_detection using CNN is a powerful deep learning solution that offers a modern alternative to traditional fire detection methods. With its ability to detect fires using visual cues, this model can be seamlessly integrated into existing surveillance systems, providing faster and more accurate fire detection capabilities.




