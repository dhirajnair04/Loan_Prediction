import flask
import pickle
import pandas as pd
import os
import sklearn

my_model=pickle.load(open('full_pipeline1','rb'))

# Initialise the Flask app
app = flask.Flask(__name__, template_folder='templates')

# Set up the main route
@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        # Just render the initial form, to get input
        return(flask.render_template('main_v2.html'))
    
    if flask.request.method == 'POST':
        # Extract the input
        Married = flask.request.form['Married']
        Education = flask.request.form['Education']
        ApplicantIncome = flask.request.form['ApplicantIncome']
        LoanAmount = flask.request.form['LoanAmount']
        Credit_History = flask.request.form['Credit_History']

        # Make DataFrame for model
        test = pd.DataFrame([[Married,Education,ApplicantIncome,LoanAmount,Credit_History]],
                                       columns=['Married','Education','ApplicantIncome','LoanAmount','Credit_History'],
                                       index=['input'])

        # Get the model's prediction

        prediction=my_model.predict(test)[0]
        
        
        #prediction = model.predict(input_variables)[0]
    
        # Render the form again, but add in the prediction and remind user
        # of the values they input before
        return flask.render_template('main_v2.html',
                                     original_input={'Married':Married,
                                                     'Education':Education,
                                                     'ApplicantIncome':ApplicantIncome,
                                                     'LoanAmount':LoanAmount,
                                                     'Credit_History':Credit_History},
                                     result=prediction,
                                     )

# if __name__ == '__main__':
#     app.run()

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000)) #Define port so we can map container port to localhost
    app.run(host='0.0.0.0', port=port)  #Define 0.0.0.0 for Docker