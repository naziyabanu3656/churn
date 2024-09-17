from flask import Flask, render_template,request
import pickle
# render_template is a method called from Flask package

#create object here app is object
app = Flask(__name__)



with open('churn_rfc_model', 'rb')as f:
    model = pickle.load(f)

# creating route to define API / endpoint
@app.route('/')  # by default GET http methods is taken here
def index():
    return render_template('index.html') #specify which page need to be displayed


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/result', methods=['POST','GET'])
def result():
    tenure=request.form.get('tenure')
    monthly_charges=request.form.get('monthly_charges')
    total_charges=request.form.get('total_charges')
    multiple_lines=request.form.get('multiple_lines')
    internet_service=request.form.get('internet_service')
    online_backup=request.form.get('online_backup')
    device_protection=request.form.get('device_protection')
    tech_support=request.form.get('tech_support')
    contract_encoder=request.form.get('contract_encoder')
    payment_method=request.form.get('payment_method')

    input=[tenure,monthly_charges,total_charges,multiple_lines,internet_service,online_backup,device_protection,tech_support,contract_encoder,payment_method]

    predict=model.predict([input])[0]
    print(predict)
    if predict == [0]:
        result="no churn"
    else:
        result="churn"

    return render_template('result.html',res=result)



if __name__ == '__main__':
    app.run(debug=True)
