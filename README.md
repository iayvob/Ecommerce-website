# Django Full Stack E-Commerce Application

This project is a comprehensive solution for building and managing a robust e-commerce platform using Python, Django, JavaScript, jQuery, and SQLite.

## Overview⚡️

This project aims to provide a solid foundation to create a feature-rich and scalable e-commerce website. Leveraging the power of Django, a high-level web framework written in Python, and integrating dynamic front-end interactions with JavaScript and jQuery, our application delivers a seamless and responsive user experience.

## Tech Stack🚀

- Backend: Python, Django
- Frontend: JavaScript, jQuery
- Database: SQLite

## Features📚

- User Authentication
- User Profile
- Shopping Cart
- Wishlist
- Product Discount
- Products / Vendors Page
- Product detail / Vendor detail Page
- Tags for Product and Blog
- Category list Page
- Improved Admin Panel
- Product Reviews
- Blog post Comments
- Products Filter
- Search Functionality
- Related Products
- Related Blog posts

## Installation Guide📚
1. Create and activate a virtual environment:

Unix based systems:
```
virtualenv env
source env/bin/activate
```

Windows:
```
python -m venv env
source env/Scripts/activate
```

2. Install Python requirements:

```
pip install -r requirements.txt
```

3. Create a SECRET_KEY and copy:

```
python secret_key.py
```

4. Create a `.env` file and add a SECRET_KEY value to `.env`:

```
SECRET_KEY=generated-secret-key
```

5. Migrate DB:

```
python manage.py migrate
```

6. To create superuser:

```
python manage.py createsuperuser
```

7. Run application:

```
python manage.py
```