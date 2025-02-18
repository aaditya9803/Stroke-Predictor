
# Stroke Predictor

https://github.com/aaditya9803/Stroke-Predictor

https://github.com/aaditya9803/Stroke-Predictor/-/wikis/home


![](/static/image.png)


# Project Description

Stroke Predictor is a web app that helps users predict their risk of having a stroke. Users can learn about strokes through visualizations. Developers can explore how the data was processed and trained for Stroke Predictor.

# Installation


Versions:

- Python 3.10.16
- streamlit 1.41.1   
- rasa 3.6.20

## How to start

Start rasa actions: `rasa run actions -p 8080`

Start rasa server: `rasa run --enable-api -p 8000`

Start the web app service: `streamlit run main.py`

Open the app in the browser with URL: `http://localhost:8501`

# Data

The Stroke Prediction Dataset was accessed from following source:

https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset

Further details about the data are also described in the Wiki.


# Basic Usage

After downloading the project files in a project folder, do the following steps:

1. Download Anaconda Navigator
    https://www.anaconda.com/download/success
2. Launch Anaconda Prompt
3. Create Conda Environment
    `conda create --name stroke-predictor python==3.10.16`
4. Activate Conda Environment
    `conda activate stroke-predictor`
5. Go to the Project folder
    `cd project-folder`
6. Install all the required packages in requirements.txt
    `pip install -r requirements.txt`
7. Train the Rasa model
    `rasa train`
8. Start Rasa action server
    `rasa run actions -p 8080`
9. Start Rasa server
    `rasa run --enable-api -p 8000`
10. Start Streamlit Server
    `streamlit run main.py`


Then call the streamlit URL 'localhost:8051', in the browser.


# Work done

All work by Aaditya Neupane.
