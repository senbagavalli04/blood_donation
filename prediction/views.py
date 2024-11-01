from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PredictionSerializer
import pickle
import numpy as np

# Load the model and scaler
with open('random_forest_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# View to render the prediction page and handle predictions
def prediction_page(request):
    prediction_result = None
    confidence = None

    if request.method == 'POST':
        # Get data from the form
        recency = request.POST.get('recency')
        frequency = request.POST.get('frequency')
        monetary = request.POST.get('monetary')
        time = request.POST.get('time')

        try:
            # Prepare input data for prediction
            input_data = np.array([[float(recency), float(frequency), float(monetary), float(time)]])
            input_data_scaled = scaler.transform(input_data)

            # Make prediction
            prediction_proba = model.predict_proba(input_data_scaled)[0][1]
            threshold = 0.5
            prediction_result = 'will donate blood' if prediction_proba > threshold else 'will not donate blood'
            
            # Convert confidence to percentage
            confidence = prediction_proba * 100  # Multiply by 100 to convert to percentage
        except ValueError:
            prediction_result = "Invalid input. Please enter numeric values."
    
    return render(request, 'predict.html', {
        'prediction_result': prediction_result,
        'confidence': confidence
    })
