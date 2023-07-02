from flask import Flask,request,render_template,jsonify
from src.pipelines.prediction_pipeline import CustomData,PredictPipeline
from src.logger import logging

application=Flask(__name__)

app=application

@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/predict',methods=['GET','POST'])

def predict_datapoint():
    if request.method=='GET':
        return render_template('form.html')
    
    else:
        data=CustomData(
            mean_texture = float(request.form.get('mean_texture')),
            mean_smoothness = float(request.form.get('mean_smoothness')),
            mean_symmetry = float(request.form.get('mean_symmetry')),
            area_error = float(request.form.get('area_error')),
            concavity_error = float(request.form.get('concavity_error')),
            concave_points_error = float(request.form.get('concave_points_error')),
            worst_symmetry = float(request.form.get('worst_symmetry')),
            worst_fractal_dimension = float(request.form.get('worst_fractal_dimension'))
        )

        final_new_data = data.get_data_as_dataframe()
        predict_pipeline=PredictPipeline()

        pred=predict_pipeline.predict(final_new_data)

        results = pred[0]

        return render_template('form.html',final_result=results)
    

if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True)