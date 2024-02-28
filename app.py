from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/app', methods=['POST'])
def compare_files():
    try:
        # Get user-uploaded files
        all_users_file = request.files['all_users']
        submitted_users_file = request.files['submitted_users']

        # Read the Excel files into DataFrames
        all_users_df = pd.read_excel(all_users_file)
        submitted_users_df = pd.read_excel(submitted_users_file)

        # Compare files to get users who did not submit
        not_submitted_df = all_users_df[~all_users_df['UserID'].isin(submitted_users_df['UserID'])]

        # Create a new Excel file with users who did not submit
        not_submitted_file = 'not_submitted_users.xlsx'
        not_submitted_df.to_excel(not_submitted_file, index=False)

        return f'Success! File "{not_submitted_file}" created with users who did not submit.'
    except Exception as e:
        return f'Error: {str(e)}'

if __name__ == '__main__':
    app.run(debug=True)
