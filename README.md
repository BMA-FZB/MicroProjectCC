
# Project Title
## Table of Contents
- [Introduction](#introduction)
- [How to Clone Project](#how-to-clone-project)
- [Testing Endpoints](#testing-endpoints)
  - [Using Global Host (Heroku)](#using-global-host-heroku)
  - [Using Local Host](#using-local-host)
    - [Docker](#docker)
    - [Host Machine](#host-machine)

## Introduction
[Go to GitHub repository from here](https://github.com/BMA-FZB/MicroProjectCC.git)

## How to Clone Project
To clone the project repository, run:
```bash
git clone https://github.com/BMA-FZB/MicroProjectCC.git
```

 ## How to Clone Project
 To clone the project repository, run:\n```bash
 git clone https://github.com/BMA-FZB/MicroProjectCC.git```

  ## Testing Endpoints

 ### Using Global Host (Heroku)
 1. Test endpoints:
    - Navigate to the pdfs directory:
      ```bash
      cd MicroProjectCC/pdfs
      ```
    - Create Embedded PDF:
      ```bash
      curl -X POST "https://microproject-d9656eae8280.herokuapp.com/create_embedded_pdf" -F "pdf_Base_file=@file1.pdf" -F "pdf_files=@file2.pdf" --output embedded_file.pdf
      ```
    - Extract Embedded PDF: 
      ```bash
      curl -X POST "https://microproject-d9656eae8280.herokuapp.com/extract_embedded_pdf" -F "embedded_file=@embedded_file.pdf" --output files.zip
      ```

 ### Using Local Host

 #### Docker
 1. Build Docker image:
 ```bash
 docker build -t my-flask-app .
 ```
 2. Run Docker container:
 ```bash
 docker run -p 5000:5000 my-flask-app
 ```
 3. Test endpoints:
    - Navigate to the pdfs directory:
      ```bash
      cd MicroProjectCC/pdfs
      ```
    - Create Embedded PDF:
      ```bash
      curl -X POST "http://localhost:5000/create_embedded_pdf" -F "pdf_Base_file=@file1.pdf" -F "pdf_files=@file2.pdf" --output embedded_file.pdf
      ```
    - Extract Embedded PDF:
      ```bash
      curl -X POST "http://localhost:5000/extract_embedded_pdf" -F "embedded_file=@embedded_file.pdf" --output files.zip"
      ```

 #### Host Machine
 1. Install requirements:
 ```bash
 pip install -r requirements.txt
 ```
 2. Run the application:
 ```bash
 python run.py
 ```
 3. Test endpoints:
    - Navigate to the pdfs directory:
      ```bash
      cd MicroProjectCC/pdfs
      ```
    - Create Embedded PDF:
      ```bash
      curl -X POST "http://localhost:5000/create_embedded_pdf" -F "pdf_Base_file=@file1.pdf" -F "pdf_files=@file2.pdf" --output embedded_file.pdf
      ```
    - Extract Embedded PDF:
      ```bash
      curl -X POST "http://localhost:5000/extract_embedded_pdf" -F "embedded_file=@embedded_file.pdf" --output files.zip
      ```
