# Django Gauth without all-auth
Incorporating Google's OAuth system into a Django project can sometimes seem daunting, especially with the myriad of third-party solutions available. This guide will provide a methodical walkthrough to integrate Google OAuth, devoid of the `django-allauth` solution.

# Getting Started

## Prerequisites

Before you start setting up the project, make sure you have the following prerequisites installed on your system:

- Python (>= 3.6)
- Django (>= 4.2)

## Getting Started

Follow these steps to get the project up and running:

1. Clone the repository to your local machine:

   ```
   git clone <repository_url>
   cd blog-project
   ```

2. Create a virtual environment for the project:

   ```
   python -m venv venv
   ```

3. Activate the virtual environment:

   On Windows:

   ```
   venv\Scripts\activate
   ```

   On macOS and Linux:

   ```
   source venv/bin/activate
   ```

4. Install the project dependencies 
    ```
    pip install -r requirements.txt 
    ```

5. Run database migrations:

   ```
   python manage.py migrate
   ```

6. Create a Google OAuth 2.0 client ID and secret by following Google's documentation for setting up OAuth 2.0 authentication. Once you have these credentials, add them to the project's settings as environment variables. **Never share your credentials in public repositories.**


7. Start the development server:

   ```
   python manage.py runserver
   ```
8. Open a web browser and navigate to `http://localhost:8000` (or your domain) to access the blog.



## Contributions and Issues

If you encounter any issues or have suggestions for improvements, please create a new issue on the project's GitHub repository. Contributions are welcome via pull requests.

## License

This project is open-source and available under the [MIT License](LICENSE).
