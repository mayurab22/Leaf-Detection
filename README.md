# 🌿 PlantsUp - A Deep Learning Model to Identify Plants by Photos  

### Ever wondered what the name of that beautiful plant is while exploring nature? 🌱 **PlantsUp** is here to help!  
**PlantsUp** is a Deep Learning-powered solution that can identify the name of a plant or leaf from a photo.  

---

## 🚀 Features  
- **Identify plants and leaves:** Upload a photo of a plant or leaf, and PlantsUp will recognize its name.  
- **Cutting-edge model:** Built on the state-of-the-art **EfficientNet-B3** architecture, ensuring high accuracy and efficiency.  
- **Robust dataset:** Trained on a large collection of **13,000+ images** of plants and leaves.  

---

## 🧠 Model  
PlantsUp uses the **EfficientNet-B3** model, which is:  
- Optimized for high performance and computational efficiency.  
- Ideal for datasets with diverse features like leaf structures and plant textures.  
- Trained end-to-end for precise predictions.  

---

## 📂 Dataset  
The dataset used in this project was sourced from **Kaggle**:  
[Indian Medicinal Leaves Dataset](https://www.kaggle.com/datasets/aryashah2k/indian-medicinal-leaves-dataset)  
- Contains **13,000+ images** categorized into two classes: **Leaf** and **Plant**.  
- For better generalization, these classes were merged into a single **Merged_Dataset** to allow identification from both types of images.  

---

## 🛠️ Workflows  

### 🔧 **Planthub Notebook**  
This notebook:  
- Merges the dataset directories (Leaf and Plant) into one.  
- Cleans up impurities like non-JPG files, duplicate images, and more.  
- Prepares a clean dataset for training.  

### 🧪 **PlantsUp Notebook**  
This notebook demonstrates the complete machine learning workflow:  
1. **Data Preprocessing**: Ensures the dataset is ready for training.  
2. **Model Selection**: Leverages **EfficientNet-B3** for feature learning.  
3. **Model Training**: Trains the model using the merged dataset.  
4. **Model Evaluation**: Validates performance on unseen data.  
5. **Fine-Tuning**: Optimizes model for better accuracy.  
6. **Model Saving**: Stores the trained model for deployment.  
7. **Model Deployment**: Prepares the model for integration into an app.  

---

## 📱 User Interface  
PlantsUp's user interface is built using **KivyMD** and **Kivy**, popular Python frameworks for app development.  
- **Seamless interaction**: Upload a photo and get instant results.  
- **Mobile-friendly**: The app is optimized for smartphone use.  

---

## ⚡ Getting Started

### 1. Python Version
This project is compatible with **Python 3.8 – 3.10**. Using other versions may cause issues with TensorFlow or Kivy dependencies.

### 2. Environment Setup
1. (Recommended) Create a virtual environment:
	```bash
	python -m venv .venv
	# Activate the environment:
	# On Windows:
	.venv\Scripts\activate
	# On macOS/Linux:
	source .venv/bin/activate
	```
2. Install all dependencies:
	```bash
	pip install -r requirements.txt
	```

### 3. Training the Model
To retrain the model on your dataset, run:
```bash
python retrain_and_save_model.py
```
This will automatically detect all classes in the dataset folders and train the model.

### 4. Running the App
To launch the PlantsUp app UI (after training or using a pre-trained model):
```bash
python main.py
```

---

## 📝 Notes
- Ensure your dataset is placed in the correct folder structure as described above.
- If you encounter dependency issues, check your Python version and ensure all packages from requirements.txt are installed.

