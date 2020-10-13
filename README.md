## Predicting Health Lifestyle

*Web-App Link:* <https://health-lifestyle-prediction.herokuapp.com/>

*Jupyter Notebook Link:* <https://nbviewer.jupyter.org/github/harshulvarma/health_lifestyle_app/blob/master/health_lifestyle_prediction_app.ipynb>

*GitHub Repository Link:* <https://github.com/harshulvarma/health_lifestyle_app>


### Overview

The goal of this project was to make a machine learning web-app for gyms to use where they can input new client's information such as resting heartrate, BMI, Vo2 etc. to get their lifestyle (sedentiary, cardio trainer or weight trainer) for catered fitness programmes.

To achieve this I built a machine learning model to classify users in their lifestyles and deployed it as an web app. The following methods were performed:
- **Pre-processing data**: Joining datasets, grouping for each unique user and retrieving useful features
- **Exploratory Data Analysis**:
  - Checking for imbalanced dataset
  - Visualising correlation through pairplots and distributions for each categories
  - Computing pearson correlation features for removing multicollinear features
  - Visualising the data in 2-D space after dimensionality reduction to find linearly separable data
  
  <img src="health2.png?raw=true"/>
  *Fig: distribution for each category*
  <img src="health4.png?raw=true"/>
  *Fig: correlation between features* 
  <img src="health3.png?raw=true"/>
  *Fig: TSNE plot*
  
- **Model Building**:
  - Baseline Models: Building Logistic Regression and Random Forest Classifier to achieve 0.98 F1 score
  - Feature Engineering: Selecting important features that made the most sense from a business point of view and finally used only two features - resting heartrate and BMI. Although the F1 score reduced to 0.95, but made the user inputs simpler and readily available as heartrate can be measured and BMI can be calculated based on user height and weight
  - Hyperparameter tuning: Conducting hyperparameter tuning for Random Forest model such as max depth, max features, min sample leaf, number of estimators etc. to achieve 0.96 F1 Score, improvement from last model iteration
  
- **Model Deployment**:
  - Saving final model weights in pickle format
  - Building inference pipeline using Streamlit for frontend and backend of the machine learning app connecting to the model weights
  - Final deployment using Heroku
  
  <img src="health.PNG?raw=true"/>
  *Fig: Health App Prediction Interface*
  
For future changes, I plan to let user input their heights and weights as inputs in place of BMI, so that BMI can be computed in the script and make it even readily available inputs for the users.

### Tools Utilised:
- pandas
- seaborn
- matplotlib
- scikit-learn
- pickle
- Streamlit
- Heroku
