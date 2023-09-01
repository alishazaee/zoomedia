# Zoomedia Project Setup

This repository contains the codebase for Zoomedia, a simplified social network. Follow the steps below to set up the project locally.

## Prerequisites
Make sure you have the following dependencies installed on your machine:
- Python 3.10
- `virtualenv`
- Docker
- Docker Compose

## Installation Steps

1. Clone the Repository and Navigate to Project Directory
```bash
git clone https://github.com/alishb80/zoomedia.git
cd zoomedia
```

2. Create and Activate the Virtual Environment
```bash
virtualenv -p python3.10 venv
source venv/bin/activate
```

3. Install Dependencies
```bash
pip install -r requirements_dev.txt
pip install -r requirements.txt
```

4. Create the Environment File
```bash
cp .env.example .env
```

Make any necessary configurations in the newly created `.env` file.

5. Run Database Migrations
```bash
python manage.py migrate
```

6. Start the Development Server
```bash
docker-compose -f docker-compose.dev.yml up -d
python manage.py runserver
```

7. Running Celery Tasks
You can run Celery tasks to handle asynchronous processing in the background.

```bash
celery -A zoomedia.tasks worker -l info --without-gossip --without-mingle --without-heartbeat
celery -A zoomedia.tasks beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
```

Now, you can access the Zoomedia application by visiting `http://localhost:8000` in your browser.

## Additional Resources

For more information and documentation, refer to the following resources:
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

Feel free to explore and customize the Zoomedia project to fit your needs. Happy coding!
