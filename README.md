# VIKOR Method Flask Implementation

This project implements the VIKOR (VIseKriterijumska Optimizacija I Kompromisno Resenje) method using Flask framework. VIKOR is a multi-criteria decision making (MCDM) method that focuses on ranking and selecting from a set of alternatives with conflicting criteria.

## Prerequisites

Before running this project, make sure you have the following installed on your system:

- Python 3.7 or higher
- pip (Python package installer)

## Installation Steps

1. Clone the repository

```bash
git clone https://github.com/BagasBerlian/VIKOR-Method-Flask.git
cd VIKOR-Method-Flask
```

2. Install the Library Requirements

```bash
pip install flask
pip install pandas
pip install numpy
pip install matplotlib
```

## Project Structure

```
VikorProject/
│
├── templates/          # HTML templates directory
│   ├── index.html     # Main input page
│   └── result.html    # Results display page
│
├── static/            # Static files directory
│   └── css/          # CSS styles directory
│       └── style.css # Main stylesheet
│
├── database/         # Database related files
│   └── db.py        # Database configuration and operations
│
└── app.py           # Main Flask application file
```

## Application Components

1. **app.py**

   - Main Flask application file
   - Contains routing and VIKOR calculation logic
   - Handles form submissions and displays results

2. **templates/**

   - **index.html**: Main page where users input their decision matrix and criteria
   - **result.html**: Displays the VIKOR calculation results and rankings

3. **static/css/**

   - **style.css**: Contains all styling for the application

4. **database/**
   - **db.py**: Handles all database operations and configurations

## Running the Application

1. After installing all dependencies, run the Flask application:

```bash
python app.py
```

2. Open your web browser and navigate to:

```
http://localhost:5000
```

## Usage

1. Once the application is running, you can:

   - Navigate to the main page (index.html)
   - Input your decision matrix
   - Set criteria weights
   - Define whether each criterion is beneficial or non-beneficial
   - Submit the form to see results

2. The system will calculate and display on result.html:
   - Normalized decision matrix
   - Weighted normalized matrix
   - VIKOR index values
   - Final rankings

## Contact

- Author: Bagas Berlian
- GitHub: [@BagasBerlian](https://github.com/BagasBerlian)
