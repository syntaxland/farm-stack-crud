
# 🚀 FARM (FastAPI + React + MongoDB)

### AWS Lambda–Ready Fullstack Deployment

A modern fullstack application built with:

* ⚡ **FastAPI** (Backend API)
* ⚛️ **ReactJS** (Frontend)
* 🍃 **MongoDB** (Database)
* ☁️ **AWS Lambda** (Serverless deployment)

---

## 🏗 Project Structure

```
farm-app/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── ...
│
├── frontend/
│   ├── package.json
│   └── ...
│
└── README.md
```

---

# 🔧 Backend Setup (FastAPI)

## 1️⃣ Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

---

## 2️⃣ Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Verify installation:

```bash
pip show fastapi uvicorn
```

---

## 3️⃣ Run Development Server

From the `backend` directory:

```bash
cd backend
uvicorn main:app --reload
```

Default:

```
http://127.0.0.1:8000
```

---

## 📘 API Documentation (Swagger)

FastAPI auto-generates interactive API docs:

* Swagger UI → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

Use this to test CRUD endpoints.

---

# 🗄 MongoDB Configuration

Make sure MongoDB is running locally or use MongoDB Atlas.

### Local MongoDB

```
mongodb://localhost:27017
```

### Environment Variable Example

Create `.env` file inside `backend/`:

```
MONGO_URI=mongodb://localhost:27017
DATABASE_NAME=farm_db
```

Install dotenv if needed:

```bash
pip install python-dotenv
```

---

# ⚛️ Frontend Setup (React)

```bash
cd frontend
npm install
npm start
```

Default:

```
http://localhost:3000
```

Make sure your backend CORS settings allow frontend origin.

Example in FastAPI:

```python
from fastapi.middleware.cors import CORSMiddleware
```

---

# ☁️ AWS Lambda Deployment (Serverless)

## Option 1: Using Mangum (Recommended)

Install:

```bash
pip install mangum
```

Modify `main.py`:

```python
from mangum import Mangum
handler = Mangum(app)
```

<!-- Clean Build Script -->
rm -rf package aws_lambda_artifact.zip
mkdir package
pip install -r requirements.txt -t package
cp main.py package/
cd package
zip -r ../aws_lambda_artifact.zip .
cd ..
echo "Build complete 🚀"

<!-- run -->
chmod +x build.sh
./build.sh


Deploy using:

* AWS SAM
* Serverless Framework
* AWS API Gateway + Lambda

---

## 🐳 Optional: Docker Setup (Production-Ready)

Example `Dockerfile` (Backend):

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Build:

```bash
docker build -t farm-backend .
docker run -p 8000:8000 farm-backend
```

---

# 🧪 Running Tests

If using pytest:

```bash
pytest
```

---

# 🔐 Environment Variables

Use `.env` and never commit secrets.

Recommended:

```
MONGO_URI=
DATABASE_NAME=
JWT_SECRET=
AWS_REGION=
```

Add to `.gitignore`:

```
.env
venv/
node_modules/
```

---

# 📦 Requirements Example

```
fastapi
uvicorn
motor
pydantic
python-dotenv
mangum
```

---

# ⚡ Production Notes

* Use MongoDB Atlas for cloud deployment
* Use API Gateway in front of Lambda
* Enable CORS properly
* Add logging
* Add rate limiting
* Secure endpoints with JWT
* Configure proper IAM roles

---

# 🧠 Tech Stack Summary

| Layer      | Technology               |
| ---------- | ------------------------ |
| Backend    | FastAPI                  |
| Frontend   | ReactJS                  |
| Database   | MongoDB                  |
| Deployment | AWS Lambda + API Gateway |

---