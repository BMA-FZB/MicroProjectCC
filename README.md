# Project Title

## Table of Contents
- [Introduction](#introduction)
- [How to Clone Project](#how-to-clone-project)
- [How to Run the Application](#how-to-run-the-application)
  - [On Host Machine](#on-host-machine)
  - [Using Docker](#using-docker)
  - [On Heroku](#on-heroku)

## Introduction
Provide a brief introduction to your project.

## How to Clone Project
Instructions on how to clone the project repository.

```bash
git clone <repository_url>
```

## How to Run the Application
Instructions on how to run the application using different methods.

### On Host Machine
1. Install requirements:
```bash
pip install -r requirements.txt
```
2. Run the application:
```bash
python run.py
```
3. Usage:
   - Create Embedded PDF:
     ```bash
     curl -X POST -F "files=@/path/to/first_pdf.pdf" -F "files=@/path/to/second_pdf.pdf" http://localhost:5000/create_embedded_pdf -o create_embedded_pdf_output.json
     ```
   - Extract Embedded PDF:
     ```bash
     curl -X POST -F "embedded_json=@/path/to/embedded.json" http://localhost:5000/extract_embedded_pdf -o files.zip
     ```

### Using Docker
1. Build Docker image:
```bash
docker build -t my-flask-app .
```
2. Run Docker container:
```bash
docker run -p 5000:5000 my-flask-app
```
3. Usage (same as host machine).

### On Heroku
1. Open the following URL:
   - [https://microproject-d9656eae8280.herokuapp.com/](https://microproject-d9656eae8280.herokuapp.com/)
2. Usage:
   - Create Embedded PDF:
     ```bash
     curl -X POST -F "files=@/path/to/first_pdf.pdf" -F "files=@/path/to/second_pdf.pdf" https://microproject-d9656eae8280.herokuapp.com/create_embedded_pdf -o create_embedded_pdf_output.json
     ```
   - Extract Embedded PDF:
     ```bash
     curl -X POST -F "embedded_json=@/path/to/embedded.json" https://microproject-d9656eae8280.herokuapp.com/extract_embedded_pdf -o files.zip
     ```

