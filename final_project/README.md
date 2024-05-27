# DRF Project

This project is built using Django Rest Framework (DRF) and includes the following features:
1. 6 Models
2. 4 Relationships
3. 1 Template
4. 2 Filters for templates
5. Authorization
6. DRF serializers for all models
7. Viewsets for all models
8. 2 DRF Actions
9. Background Tasks using Dramatiq or Celery

## Models

The project includes the following six models:
1. **User**: Custom user model for authentication.
2. **Category**: Model for categorizing links.
3. **Tag**: Model for tagging links.
4. **Link**: Model for storing information about links.
5. **Click**: Model for tracking clicks on links.
6. **LinkUsage**: Model for storing usage statistics for links.

## Relationships

The models are related as follows:
- **Link** to **Category**: ForeignKey
- **Link** to **Tag**: ManyToManyField
- **Link** to **User**: ForeignKey
- **Click** to **Link**: ForeignKey

## Template

One Django template is included for the user interface:
- **User Page**: Displays a list of links that users can view and click.

## Filters for Templates

Two filters are provided for the templates:
1. Filter links by category.
2. Filter links by tags.

## Authorization

JWT authentication is implemented using `djangorestframework-simplejwt`. Only admin users can add, delete, and update links. Regular users can only view and click on links.

## DRF Serializers

Serializers are provided for all models:
- `UserSerializer`
- `CategorySerializer`
- `TagSerializer`
- `LinkSerializer`
- `ClickSerializer`
- `LinkUsageSerializer`

## Viewsets

Viewsets are implemented for all models:
- `UserViewSet`
- `CategoryViewSet`
- `TagViewSet`
- `LinkViewSet`
- `ClickViewSet`
- `LinkUsageViewSet`

## DRF Actions

Two custom actions are implemented in the `LinkViewSet`:
1. `click`: Tracks a click on a link.
2. `top_links`: Retrieves the top links based on click count.

## Background Tasks

Background tasks are implemented using Celery. An example task is provided to update link usage statistics.

## Installation and Setup

### Prerequisites

- Python 3.8+
- Django 3.2+
- Django Rest Framework
- djangorestframework-simplejwt
- Celery
- Redis (for Celery)

### Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
2. **Create and activate a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate
3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
4. **Apply migrations**:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
5. **Create a superuser**:
    ```sh
    python manage.py createsuperuser
6. **Run the development server**:
    ```sh
    python manage.py runserver
7. **Run Celery worker**:
    ```sh
    celery -A your_project_name worker --loglevel=info

### Endpoints:
- Register: /api/register/ (POST)
- Login: /api/login/ (POST)
- Refresh Token: /api/token/refresh/ (POST)
- User ViewSet: /api/users/
- Category ViewSet: /api/categories/
- Tag ViewSet: /api/tags/
- Link ViewSet: /api/links/
- Click ViewSet: /api/clicks/
- Link Usage ViewSet: /api/linkusages/