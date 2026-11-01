# AI Usage Disclosure

## 1. AI tool(s) used
Tool: ChatGPT by OpenAI

Model: GPT-6

Usage date: 1 November 2026

Purpose: Project planning, Django code generation, debugging, test-case development, documentation, and troubleshooting.

## 2. Prompts given

### 1. Project Planning and Architecture

"Analyze the requirements for an AI-Assisted Box Selection System and design a complete Django-based web application. Define the project architecture, application structure, database models, business logic, and implementation workflow."

### 2. Django Backend Development

"Develop a functional Django backend for the box selection system. Implement Product, Box, Order, and OrderItem models with appropriate fields, relationships, validations, and database operations using SQLite."

### 3. Box Selection Algorithm

"Implement a box recommendation algorithm that selects the most cost-effective shipping box based on product dimensions, product weight, box internal dimensions, maximum weight capacity, and product rotation. Ensure that multiple products can be packed without overlapping."

### 4. Frontend Development

"Create a responsive and user-friendly HTML, CSS, and Django Templates frontend. Include dashboard, product management, box management, order creation, and box recommendation pages."

### 5. Django Admin Integration

"Configure the Django administration panel to manage products, shipping boxes, orders, and order items. Ensure that administrators can efficiently create, update, view, and manage application records."

### 6. Testing and Validation

"Develop Django automated test cases to validate box selection, dimensional constraints, weight restrictions, product rotation, multiple-product packing, and application functionality. Include appropriate edge-case scenarios."

### 7. Debugging and Troubleshooting

"Analyze the Django database error `OperationalError: no such table: shipping_product`. Identify its root cause and provide the correct steps to resolve the database migration issue."

### 8. Documentation

"Prepare professional project documentation, including a README.md file with project overview, features, technology stack, installation instructions, database setup, execution commands, and testing instructions."

### 9. Verification

"Review the completed Django application and provide a verification checklist covering database migrations, automated tests, admin authentication, product management, box management, order processing, and box recommendations."


## 3. Output accepted
The following AI-generated suggestions and implementations were used:

Django project structure and application configuration.

Product, Box, Order, and OrderItem data models.

HTML, CSS, and Django template-based frontend.

SQLite database integration.

Box selection and packing recommendation algorithm.

Product and box management functionality.

Order creation and box recommendation display.

Automated Django test cases.

## 4. Output rejected or modified
The initial database setup required additional migration commands after encountering the error no such table: shipping_product.

Database tables were created by applying Django migrations.

The generated test output was reviewed against the actual terminal output.

Documentation was adjusted to describe the actual database migration issue and its resolution.

The box-packing algorithm was treated as a heuristic rather than a guaranteed globally optimal packing solution.

## 5. Mistakes found
### Database Migration Error – SQLite

During application execution, Django raised the following error:

`django.db.utils.OperationalError: no such table: shipping_product`

**Cause:** The required database table for the Product model had not been created in the SQLite database because the database migrations had not been applied.

**Solution:** Run the following commands from the project root directory:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

After applying the migrations, Django creates the required database tables and the application can access product records successfully.

## 6. Verification

# 1. Environment versions
Python: 3.13.14
Django: 5.2.18
Database: SQLite

# 2. Commands executed

The following commands were used during project setup and verification:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py test
python manage.py runserver
```

# 3. Automated testing

**Command:**

```bash
python manage.py test
```

**Observed result from terminal screenshot:**

- Tests discovered: 9
- System check: No issues identified
- Tests passed: 9
- Tests failed: 0
- Execution time: 0.070 seconds
- Final status: `OK`

### 4. Manual verification

| Scenario | Actual result |

Django application startup: Successful
Admin login: Successful
Product creation: Successful
Box creation: Successful
Order creation: Successful
Box recommendation: Successful
Database migration: Successful

### 5. Issues encountered

**Issue:** `django.db.utils.OperationalError: no such table: shipping_product`

**Resolution:** Applied Django database migrations using:

```bash
python manage.py makemigrations
python manage.py migrate
```

The database tables were created after applying the migrations.

### What I Learned from This Assignment

During this assignment, I gained practical experience in developing a web application using Python and Django. I learned how to create Django models, manage database relationships using SQLite, and perform CRUD operations. I also understood how to organize a Django project and connect the frontend with the backend.

One of the most interesting parts was working on the box selection algorithm. I learned how product dimensions, weight, rotation, and box capacity affect the selection of a suitable shipping box. I also got a better understanding of the challenges involved in packing multiple products without overlapping.

While developing the project, I faced some issues related to database migrations and application configuration. Troubleshooting these errors helped me understand Django's workflow better. I also learned the importance of writing test cases and checking whether the application works correctly under different conditions.

Overall, this assignment helped me improve my practical Django knowledge, problem-solving skills, and confidence in developing a complete web application.