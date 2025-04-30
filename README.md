# Basic-Social-Media-App

This is a Django-based social media application that allows users to create posts, comment on posts, and like posts. The application also includes user authentication (signup, login, and logout) and a user dashboard to manage posts.

## Features

- **User Authentication**: Users can sign up, log in, and log out.
- **Post Management**: Users can create, update, and delete posts.
- **Categories**: Posts can be categorized into predefined categories.
- **Comments**: Users can comment on posts.
- **Likes**: Users can like or unlike posts.
- **Dashboard**: Users can view and manage their posts in a personalized dashboard.

## Project Structure
bsmp/ 
├── auth_system/ │ ├── templates/ │ │ ├── login.html │ │ ├── signup.html │ ├── views.py │ ├── urls.py │ ├── models.py │ ├── admin.py │ ├── apps.py │ ├── tests.py │ ├── migrations/ ├── social_media/ │ ├── templates/ │ │ ├── all_posts.html │ │ ├── create_post.html │ │ ├── single_post.html │ │ ├── update.html │ │ ├── user_dashboard.html │ │ ├── posts_by_category.html │ │ ├── nav.html │ ├── views.py │ ├── urls.py │ ├── models.py │ ├── admin.py │ ├── apps.py │ ├── tests.py │ ├── migrations/ ├── bsmp/ │ ├── settings.py │ ├── urls.py │ ├── wsgi.py │ ├── asgi.py ├── manage.py


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
2.Create a virtual environment and activate it:
- python -m venv venv
- source venv/bin/activate  # On Windows: venv\Scripts\activate
3.Install dependencies:
- pip install django
4.Apply migrations:
- python manage.py migrate
5.Create a superuser:
- python manage.py createsuperuser
6.Run the development server:
- python manage.py runserver
7.Open the application in your browser at "http://127.0.0.1:8000"

## Usage
- Home Page: Displays all posts with their categories, likes, and comments.
- User Dashboard: Accessible after login, allows users to manage their posts.
- Post Details: View a single post, add comments, and like/unlike the post.
- Authentication: Users can sign up, log in, and log out.

## Models
Post
- title: Title of the post.
- content: Content of the post.
- category: Foreign key to the Category model.
- user: Foreign key to the User model.
- total_likes(): Returns the total number of likes for the post.
- total_comments(): Returns the total number of comments for the post.
Comment
- post: Foreign key to the Post model.
- content: Content of the comment.
- user: Foreign key to the User model.
Category
- name: Name of the category (e.g., Lifestyle, Technology, etc.).
Like
- post: Foreign key to the Post model.
- user: Foreign key to the User model.

## Templates
- all_posts.html: Displays all posts.
- create_post.html: Form to create a new post.
- single_post.html: Displays a single post with comments and like functionality.
- update.html: Form to update a post.
- user_dashboard.html: Displays the user's posts.
- nav.html: Navigation bar for the application.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
