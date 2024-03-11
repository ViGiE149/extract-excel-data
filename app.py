from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_cors import CORS
from networkx import dfs_edges
import pandas as pd
from urllib.parse import quote

app = Flask(__name__)
CORS(app)
app.secret_key = 'your_secret_key'  # Set a secret key for flash messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/app', methods=['POST'])
def compare_files():
    try:
        # Get user-uploaded files and form data
        all_users_file = request.files['all_users']
        submitted_users_file = request.files['submitted_users']
        all_column_name = request.form['all_column_name'] if 'all_column_name' in request.form else None
        submitted_column_name = request.form['submitted_column_name'] if 'submitted_column_name' in request.form else None

        if not all_users_file or not submitted_users_file or (not all_column_name and not submitted_column_name):
            flash('Error: Both files and at least one column name are required.', 'error')
            return redirect(url_for('index'))

        # Read the Excel files into DataFrames
        all_users_df = pd.read_excel(all_users_file)
        submitted_users_df = pd.read_excel(submitted_users_file)

        # Compare files to get users who did not submit
        not_submitted_df = all_users_df[
            ~all_users_df[all_column_name].str.strip().isin(submitted_users_df[submitted_column_name].str.strip())
        ]
     

        # Create a new Excel file with users who did not submit
        not_submitted_file = 'not_submitted_users.xlsx'
        not_submitted_df.to_excel(not_submitted_file, index=False)

        flash(f'Success! File "{not_submitted_file}" created with users who did not submit.', 'success')
        return redirect(url_for('index'))

    except pd.errors.EmptyDataError:
        flash('Error: At least one of the files is empty.', 'error')
        return redirect(url_for('index'))

    except Exception as e:
        app.logger.error(f'Error processing files: {str(e)}')
        flash(f'Error: {str(e)}', 'error')
        return redirect(url_for('index'))

@app.route('/get_column_names', methods=['POST'])
def get_column_names():
    try:
        uploaded_file = request.files.get('file')

        if not uploaded_file:
            return jsonify({'error': 'No file uploaded'}), 400

        # Read the Excel file into a DataFrame
        df = pd.read_excel(uploaded_file)

        # Replace spaces with underscores in column names
        #df.columns = df.columns.str.replace(' ', '_')
        

        # URL encode column names to handle special characters
        # Inside the get_column_names route
       # encoded_column_names = [quote(column.lower()) for column in df.columns.tolist()]
        encoded_column_names = [quote(column) for column in df.columns.tolist()]

   
        #encoded_column_names = [quote(column) for column in df.columns.tolist()]

        return jsonify(encoded_column_names)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
