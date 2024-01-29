<img align="center" alt="Coding" width="300" src="./odoo_logo.svg">

## Purchases-Extended  
![GitHub contributors](https://img.shields.io/github/contributors/MartinKalema/Hospital-Management-Odoo?style=for-the-badge&logo=github) ![Static Badge](https://img.shields.io/badge/Odoo_version-v16.0-neon?style=for-the-badge)

Leveraging the power of Odoo, this system offers a modular and customizable approach to meet the unique needs of hospitals, clinics, and medical facilities. From patient management to inventory control, it provides a unified platform for healthcare professionals to enhance patient care and overall efficiency.

The Key features are;
-  Patient Management
-  Appointments and scheduling
-  Electronic Health Records
-  Billing and Invoicing
-  Inventory Management
-  Reporting and Analytics

## Stack
<a href="https://www.postgresql.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original-wordmark.svg" alt="postgresql" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> 

## Structure
```
── controllers
│   ├── __init__.py
│   ├── main.py
│   └── __pycache__
│       ├── __init__.cpython-311.pyc
│       └── main.cpython-311.pyc
├── data
│   └── patient_tag_data.xml
├── __init__.py
├── __manifest__.py
├── models
│   ├── appointment.py
│   ├── __init__.py
│   ├── patient.py
│   ├── patient_tag.py
│   └── __pycache__
│       ├── appointment.cpython-311.pyc
│       ├── __init__.cpython-311.pyc
│       ├── patient.cpython-311.pyc
│       └── patient_tag.cpython-311.pyc
├── odoo_logo.svg
├── __pycache__
│   └── __init__.cpython-311.pyc
├── README.md
├── security
│   └── ir.model.access.csv
├── static
│   └── description
│       └── icon.png
├── views
│   ├── appointment_view.xml
│   ├── female_patient_view.xml
│   ├── menu.xml
│   ├── patient_tag_view.xml
│   ├── patient_view.xml
│   └── website_form.xml
└── wizard
    ├── cancel_appointment.py
    ├── cancel_appointment.xml
    ├── __init__.py
    └── __pycache__
        ├── cancel_appointment.cpython-311.pyc
        └── __init__.cpython-311.pyc


```
## Install this project
Add this to your custom addons folder using this bash command 
  ```bash
  git clone https://github.com/MartinKalema/Hospital-Management-Odoo.git
  ```

