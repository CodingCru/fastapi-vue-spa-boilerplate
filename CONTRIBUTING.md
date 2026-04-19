# Contributing

> This file covers contributing to the boilerplate itself. If you've used this as a template for your own project, feel free to replace it with your own contributing guidelines.

Thank you for your interest in contributing. This guide will help you get started quickly.

## Before You Start

1. Browse the [open issues](https://github.com/CodingCru/fastapi-vue-spa-boilerplate/issues) and find one tagged `good first issue`
2. Comment on the issue: "I'd like to work on this" — wait to be assigned before starting
3. Don't open a PR without a linked issue


## ⚙️ Prerequisites

Make sure you have the following installed:

* Python 3.9+
* Node.js 18+
* Git


## ⚙️ Local Setup

Follow the steps below to set up the project locally.

### 1️⃣ Clone the repository

```bash
git clone https://github.com/CodingCru/fastapi-vue-spa-boilerplate.git
cd fastapi-vue-spa-boilerplate
```

### 2️⃣ Bootstrap setup

This script sets up the development environment by:
- Creating a virtual environment
- Installing backend dependencies
- Installing frontend dependencies

```bash 
./bootstrap_local.sh
```

⚠️ Note for Windows users:
Use Git Bash or WSL to run .sh scripts.


## ⚠️ Troubleshooting

If the bootstrap script fails:

- Ensure Python and Node.js are installed correctly
- Try reinstalling dependencies manually in backend and frontend

### 3️⃣ Environment Variables

```bash 
cp .env.example .env
```
Update values inside .env if required.

## 🚀 Running the Project

### 4️⃣ Backend Setup

```bash 
cd backend
source .venv/bin/activate
```
The backend entry point is located at:
backend/app/main.py
Run the server using:

```bash 
uvicorn app.main:app --reload
```

### 5️⃣ Frontend Setup

```bash 
cd frontend
npm install
npm run dev
```

## 🌐 Local URLs

* Frontend → http://localhost:3000
* Backend → http://localhost:8000
* API Docs → http://localhost:8000/docs


## 🌿 Git Workflow

#### 1️⃣ Fork the repository

Click the Fork button on GitHub.

#### 2️⃣ Create a branch

```bash 
git checkout -b feature/your-feature-name
```

#### 3️⃣ Make changes 

* Write clean, readable code
* Follow existing project structure

#### 4️⃣ Commit your changes

```bash
git add .
git commit -m "feat: add meaningful description"
```

## 📝 Commit Message Format

We follow Conventional Commits:

```bash 
<type>: <description>
```

## Common types:

* feat → new feature
* fix → bug fix
* docs → documentation
* refactor → code improvement
* test → testing
* chore → minor changes

## 🔍 Code Quality

We follow strict code quality standards:

- Ruff (linting)

- Black (formatting)

- MyPy (type checking)

Run the following commands before pushing:

```bash
ruff check .
black .
mypy .
```
## ✅ Before Submitting PR

- Ensure backend runs without errors  
- Ensure frontend works correctly  
- Verify your changes locally  

## 🚀 Submitting a Pull Request

1. Push your branch

```bash 
git push origin feature/your-feature-name
```

2. Open a Pull Request on GitHub
3. Link the issue in description:

```bash 
Closes #<issue-number>
```

4. Request review
5. Wait for approval ✅

## ❗ Important Rules

* Do not open PR without an issue
* Keep PRs small and focused
* Follow existing code style
* Do not break existing functionality
* Always run checks before pushing

## 💡 Need Help?

If you’re stuck, feel free to ask questions in the issue discussion.

## ❤️ Final Note

Every contribution matters — even small improvements help the project grow.