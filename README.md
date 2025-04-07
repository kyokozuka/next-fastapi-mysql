# Overview
This is a full-stack boilerplate project designed for rapid development using Next.js, FastAPI, and MySQL. It provides a clean and scalable architecture to help you get started quickly with modern web application development.
This template includes a basic example of a CRUD (Create, Read, Update, Delete) system for managing posts. You can use it as a reference to build your own system or customize it freely to suit your specific needs.

# Stack
### Frontend
- NextJS
- NodeJS: 23.10
### Backend
- FastAPI
- Python: 3.13
### Database
- Mysql: 9.2

# How to Run
1. Run the follow command on Terminal
```
docker compose up -d
```
2. Open browser and access to http://127.0.0.1:3041
# How to develop
## Development Environment with DevContainer (VS Code)

This project uses DevContainer to provide a consistent development environment using Visual Studio Code.

### Prerequisites
- Docker installed and running
- Visual Studio Code
- Dev Containers extension

### Getting Started
1. Clone the repository:
```.bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```
2. Open the project in Visual Studio Code.
3. When prompted, click “Reopen in Container”.
Alternatively, open the command palette (Cmd+Shift+P or Ctrl+Shift+P), then select:
```
Dev Containers: Reopen in Container
```
4. VS Code will build the dev container and set up the environment automatically.
5. Once the container is ready, you can start coding!