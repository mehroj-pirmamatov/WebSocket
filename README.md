WebSocket Chat

A simple real-time chat application built with Django Channels and WebSockets. Users in the same chat room can exchange messages instantly without refreshing the page.

Features

•
Real-time messaging with WebSockets

•
Separate chat rooms

•
Message validation and error handling

•
Secure ws:// and wss:// connection support

•
Redis support for production deployments

•
In-memory channel layer for local development

•
Automated WebSocket tests

Technologies

•
Python

•
Django

•
Django Channels

•
Daphne

•
Redis

•
SQLite

Installation

Clone the repository and open the project directory:

Bash


git clone https://github.com/USERNAME/REPOSITORY.git
cd REPOSITORY



Create and activate a virtual environment:

Bash


python -m venv .venv
source .venv/bin/activate       # Windows: .venv\\Scripts\\activate



Install the dependencies:

Bash


pip install -r requirements.txt



Apply the database migrations and start the development server:

Bash


python manage.py migrate
python manage.py runserver



Open the chat application at:

Plain Text


http://127.0.0.1:8000/chat/



Open the same room in two browser windows to test real-time messaging.

Production configuration

For production, set the following environment variables:

Bash


DJANGO_SECRET_KEY=change-this-to-a-long-random-secret
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=example.com
REDIS_URL=redis://127.0.0.1:6379/0



Redis is recommended for production deployments, especially when running multiple workers. If REDIS_URL is not provided, the application uses an in-memory channel layer for local development.

Running tests

Bash


python manage.py test



Project structure

Plain Text


app/       Chat application, consumers, routes, views and templates
config/    Django project and ASGI configuration
manage.py  Django command-line utility






