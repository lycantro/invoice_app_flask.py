from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__, template_folder='C:\\Users\\leona\\invoice_app_flask.py\\templates')
app.secret_key = "supersecretkey"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Capture user input
        data = {
            'name': request.form.get('name'),
            'bank_name': request.form.get('bank_name'),
            'bsb': request.form.get('bsb'),
            'account_number': request.form.get('account_number'),
            'company_name': request.form.get('company_name'),
            'hourly_rate': float(request.form.get('hourly_rate')),
            'dates_locations_hours': [
                (request.form.get(f'date_{i}'),
                 request.form.get(f'location_{i}'),
                 float(request.form.get(f'hours_{i}')))
                for i in range(1, 8)
                if request.form.get(f'date_{i}') and request.form.get(f'hours_{i}')
            ],
        }
        total_hours = sum(hours for _, _, hours in data['dates_locations_hours'])
        data['total'] = data['hourly_rate'] * total_hours
        return render_template('invoice.html', data=data)
    return render_template('input_form.html')

if __name__ == "__main__":
    app.run(debug=True)
import os
print(os.path.abspath(__file__))
