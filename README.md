# FastAPI-project

###  How to Run the FastAPI Task Manager Project

1. Clone the repository

```bash
git clone https://github.com/HaidarH726/FastAPI-project.git
```

2. Go into the project folder

```bash
cd FastAPI-project
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Start the FastAPI server

```bash
uvicorn main:app --reload
```

5. Open the API documentation in your browser

```
http://127.0.0.1:8000/docs
```

You should now see the interactive Swagger UI where you can test all endpoints.


## 📌 Detailed Information About This Project

This project is a simple REST API built with **FastAPI** that allows users to manage tasks.
It demonstrates how APIs receive requests, process data, store information, and return responses.

---

## 🚀 Features

* Create tasks
* View all tasks
* View a single task
* Update a task
* Delete a task
* Delete all tasks
* Task statistics endpoint
* File-based storage using JSON lines

---

## 🛠 Programming Languages & Tools Used

* Python
* FastAPI
* Pydantic
* Uvicorn

---

## 📂 How Data Is Stored

Tasks are stored in a file called:

```
tasks.txt
```

Each line in the file represents one task in JSON format.
This simulates database storage for learning purposes and shows how backend systems persist data.
