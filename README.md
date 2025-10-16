# Django-Realtime-code-editor


# Real-Time Code Editor    

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Django](https://img.shields.io/badge/Django-v4.2+-green.svg)
![WebSocket](https://img.shields.io/badge/WebSocket-Enabled-orange.svg)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)

A real-time collaborative code editor built with Django and WebSockets, enabling multiple developers to code together seamlessly with live syntax highlighting, auto-completion, and integrated communication features.

## Features

- **Real-Time Collaboration** - Multiple users can edit code simultaneously with live cursor tracking
- **Syntax Highlighting** - Support for 20+ programming languages with intelligent code highlighting
- **Live Code Execution** - Run and test code directly in the browser with instant results
- **Room Management** - Create private or public coding rooms with access controls
- **Modern UI** - Editor has a very good looking modern UI experience for user
- **Live user cursor** - Live cursor to notify which user is collaborating
- **Plugin Support** - Extensible architecture for custom plugins and integrations

## 🛠 Tech Stack

**Backend:**
- Django 4.2+
- Django Channels 4.0+ (WebSocket support)
- SQL (Database)
- Monaco Editor

**Frontend:**
- HTML5, CSS3, JavaScript (ES6+)
- CodeMirror 6 (Code editor)
- Socket.IO Client (Real-time communication)
- Tailwind CSS

**DevOps & Infrastructure:**
- Docker
- Cloud

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8+
- Django Installed
- Docker (optional, for containerized setup)

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### How to Run the Project

1. **Clone the repository**
   ```bash
   git clone https://github.com/SagarBawanthade/Django-Realtime-code-editor.git
   cd Django-Realtime-code-editor
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   - Open your browser and go to: `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

### 👤 Creating an Admin User

To access the Django admin panel, you need to create a superuser account:

1. **Make sure your virtual environment is activated and the server is stopped**
   ```bash
   # Stop the server if running (Ctrl+C)
   # Ensure venv is activated
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

3. **Follow the prompts:**
   - Enter a username (e.g., `admin`)
   - Enter email address (optional, can be left blank)
   - Enter password (you'll need to type it twice)

4. **Login to admin panel**
   - Start the server: `python manage.py runserver`
   - Go to: `http://127.0.0.1:8000/admin/`
   - Use the username and password you just created

### ⚠️ Current Status
**Note**: This project is currently in development. The repository contains a basic Django setup with the following structure:
- Django project configuration ✅
- Basic app structure ✅ 
- Real-time code editor UI ⚠️ (Not implemented yet)
- WebSocket functionality ⚠️ (Not implemented yet)
- Collaborative features ⚠️ (Not implemented yet)

The actual real-time code editor features described in this README are still under development.


## Contributing🤝 

1. Fork the repository
2. Create feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push branch: `git push origin feature/amazing-feature`
5. Open Pull Request

### Development Guidelines

- Update documentation
- Use meaningful commit messages

## Support📨

- **Email**: sagar.bawanthade2004@gmail.com
- **Email**: krishdsoni019@gmail.com
- **Email**: varadjadhav1864@gmail.com




