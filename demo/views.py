from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
import pandas as pd
import pickle
import os

def homePageView(request):
    return render(request, 'home.html')


def predictPageView(request):
    return render(request, 'predict.html')


def predictPost(request):
    try:
        # Extract values from request object by control name.
        time = int(request.POST['time'])
        age = int(request.POST['age'])
        serum_creatinine = float(request.POST['serum_creatinine'])
        serum_sodium = int(request.POST['serum_sodium'])
        ejection_fraction = int(request.POST['ejection_fraction'])

    # Enters 'except' block if integer cannot be created.
    except:
        return render(request, 'predict.html', {
            'errorMessage': 'Error: The data submitted is invalid. Please try again.'})
    else:
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(
            reverse('results', kwargs={'time': time, 'age': age, 'serum_creatinine': serum_creatinine,
                                       'serum_sodium': serum_sodium, 'ejection_fraction': ejection_fraction}, ))


def results(request, time, age, serum_creatinine, serum_sodium, ejection_fraction):
    serum_creatinine = float(serum_creatinine)
    print("*** Inside results()")
    # load saved model
    model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'model.pkl')
    with open(model_path, 'rb') as f:
        loadedModel = pickle.load(f)

    # Create a single prediction.
    predictDf = pd.DataFrame(columns=['time', 'age', 'serum_creatinine', 'serum_sodium', 'ejection_fraction'])
    predictDf.loc[0] = [time, age, serum_creatinine, serum_sodium, ejection_fraction]
    predict_int = loadedModel.predict(predictDf)[0]
    predict_proba_list = loadedModel.predict_proba(predictDf)[0].tolist()
    if predict_int < 1:
        confidence = predict_proba_list[0]
        prediction = "NO"
    else:
        confidence = predict_proba_list[1]
        prediction = "YES"
    confidence = '{:.2%}'.format(confidence)
    return render(request, 'results.html', {'time': time, 'age': age, 'serum_creatinine': serum_creatinine,
                                            'serum_sodium': serum_sodium, 'ejection_fraction': ejection_fraction,
                                            'prediction': prediction, 'confidence': confidence})
