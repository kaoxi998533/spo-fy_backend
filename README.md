<p align="center">
  <a href="" rel="noopener">
</p>

<h3 align="center">Spo+fy Backend</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kaoxi998533/spo-fy_backend/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kaoxi998533/spo-fy_backend/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> The backend for the project spo++fy
    <br> 
</p>

## 📝 Table of Contents

- [📝 Table of Contents](#-table-of-contents)
- [🧐 About ](#-about-)
- [🏁 Getting Started ](#-getting-started-)
  - [Prerequisites](#prerequisites)
  - [Installing](#installing)
- [🎈 Usage ](#-usage-)
- [🚀 Deployment ](#-deployment-)
- [⛏️ Built Using ](#️-built-using-)
- [✍️ Authors ](#️-authors-)
- [🎉 Acknowledgements ](#-acknowledgements-)

## 🧐 About <a name = "about"></a>

The project contains the backend code for Spo++fy software, including functions like splitting song tracks and loading album images. It is made by Django framework. 

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

You are using a Linux system machine or virtual machine that can act as a server. You have `pip` installed on your machine


### Installing

A step by step series of examples that tell you how to get a development env running.


Step 1: Clone the repository
```
git clone https://github.com/kaoxi998533/spo-fy_backend
```

Step 2: Active a new virtual environment and install the required dependencies at the project root directory

```
python -m venv .env && source .env/bin/activate && pip install -r requirements.txt
```
Step 3: In myproject/settings.py, check if your ip address for the machine as host is included, do include it if it is not

Step 4: Run the project
```
python manage.py runserver 0.0.0.0:8000 # runserver and the server should be accessible from any IP address (0.0.0.0) on port 8000.

```


## 🎈 Usage <a name="usage"></a>

This backend should be used together with the frontend app at https://github.com/dingf3ng/spoplusplusfy

## 🚀 Deployment <a name = "deployment"></a>

With the server running, it is already considered to be deployed. The frontend app will then function normally. 

## ⛏️ Built Using <a name = "built_using"></a>

- [Django](https://www.djangoproject.com/) - Backend Framework
- [Sqlite](https://sqlite.org/) - Database
- [nginx](https://nginx.org/) - Web Server

## ✍️ Authors <a name = "authors"></a>

- [@eddy](https://github.com/kaoxi998533) - Designer for models and views
- [@Feng](https://github.com/dingf3ng) - Data organizer for database


## 🎉 Acknowledgements <a name = "acknowledgement"></a>

This project includes code of [Demucs](https://github.com/adefossez/demucs), [Allauth](https://github.com/pennersr/django-allauth) under MIT license.