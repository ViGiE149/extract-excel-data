# User Submission Discrepancy Analyzer

## Introduction

Welcome to the User Submission Discrepancy Analyzer! This Python Flask-based web application simplifies the process of identifying users who haven't submitted necessary information. By leveraging the Pandas library for Excel file manipulation, this tool offers an intuitive solution for organizations managing user data.

## Live Demo

You can access the live version of the User Submission Discrepancy Analyzer at [mutinnovationlab.pythonanywhere.com](http://mutinnovationlab.pythonanywhere.com).

## Author

- **Name:** Vusumuzi Gwala
- **Alias:** Vigie
- **Email:** vgwala149@gmail.com

## How to Use

1. **File Upload:**
   - Start by uploading two Excel files: one containing comprehensive user data and another with details exclusively for users who have submitted information.

2. **Column Selection:**
   - Dynamically select the column names from each file that uniquely identify users using the presented dropdown menus.

3. **Initiate Comparison:**
   - Click the "Compare Files" button to trigger the application to use Pandas for a meticulous comparison between the two files, focusing on the selected identification columns.

4. **Identify Non-Submitters:**
   - The tool will identify users present in the primary file but absent in the submission file, effectively extracting those who have not submitted required information.

5. **Export Results:**
   - Download the newly generated Excel file, which consolidates information about users who have not submitted. This facilitates follow-up communication or targeted outreach.

## Contact

For any inquiries or feedback, please feel free to reach out to the author:

- **Email:** vgwala149@gmail.com

Thank you for using the User Submission Discrepancy Analyzer!
