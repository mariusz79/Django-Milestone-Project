##### Django Milestone Project
# IssueTracker website

Django milestone project for Code Insitute.

[![Build Status](https://travis-ci.org/mariusz79/Django-Milestone-Project.svg?branch=master)](https://travis-ci.org/mariusz79/Django-Milestone-Project)

> The purpose of the project is to build a full-stack site based around business logic used to control a centrally-owned dataset. The website should have an authentication mechanism and provide paid access to the site's data and/or other activities based on the dataset, such as the purchase of a product/service.
> By authenticating on the site and paying for some of its services, users can advance their own goals. Before authenticating, the site makes it clear how those goals would be furthered by the site.
> The site owner is able to make money by providing this set of services to the users. There is no way for a regular user to bypass the site's mechanisms and derive all of the value available to paid users without paying.


## Table of Contents
1. [Ux](#ux)
   1. [Users stories](#users-stories)
   1. [Wireframes](#wireframes)
1. [Features](#features)
1. [Technologies used](#technologies-used)
1. [Project difficulties](#project-challenges)
1. [Testing](#testing)
   1. [User stories](#user-stories)
   1. [Different browsers, mobile, desktop](#different-browsers-mobile-desktop)
1. [Deployment](#deployment)
1. [Content](#content)
1. [Acknowledgements](#acknowledgements)

## UX
The website is made to be as responsive as possible. HTML, CSS, and JavaScript are used to enhance the look and feel of the project. The site also makes use of CSS framework named Bootstrap.

Target audience of the website are people who want to create tickets for bugs they found in the application or ask for adding new features to the app. This site offers the service and bug fixes for free, but ask for money from users to develop additional features.

#### Users Stories:
1. As a user who is visiting the website I want to be able:
    - to see images and slogans explaining the website's content, 
    - to register, to get access to registered users features,
    - to see info about services provided by the website,
    - to see testimonials,
    - to see info about people working here,
    - to see latest blog posts:
        - each post should show miniature image, title, and date of adding,
    - to search for posts, bugs and features in database by typing a phrase in a searchbar:
        - search in posts
        - search in bugs
        - search in features
    - to see statistics of issues in website's database,
    - to see all bugs:
        - sorted by name(ascending and descending) or date(ascending and descending) or number of likes.
    - to see all features:
        - sorted by name(ascending and descending) or date(ascending and descending) or number of likes.
    - to see all posts:
        - sorted by name(ascending and descending) or date(ascending and descending) or number of likes.
    - in case when posts are searched or browsed each post should show:
        - miniature image,
        - title,
        - author's name,
        - date of adding,
        - number of views, likes and comments
     - in case when bugs and features are searched or browsed each bug and feature should show:
        - title,
        - author's name,
        - date of adding,
        - number of views, likes and comments
    - to see all info about a single post displayed on single page by clicking on the post:
        - title
        - full image,
        - author's name and avatar, date of adding,
        - content
        - views, likes, comments,
        - comments leaved by users.
    - to see all info about a single bug or feature displayed on single page by clicking on the bug or feature:
        - title
        - full image,
        - author's name and avatar, date of adding,
        - description,
        - views, likes, comments,
        - comments leaved by users.
    - to contact website's owners, by filling in and submitting contact form,
    - to see links to social media,
    - to see info about ways of contacting website owners.
    
2. As a registered user I want to be able:
    - to log in,
    - to reset my password,
    - to add new bug,
    - to access my profile:
        - update my profile avatar,
        - if profile's avatar wasn't delivered deafault avatar for a profile shoud by displayed
        - check bugs and features added by me,
    - to edit, delete bugs added by me,
    - comment bugs and blog posts,
    - like bugs and blog posts,
    - to log out,
    - to make donation.

3. As a registered user who donated money I want to be able:
    - to add new features with description,
    - to edit features added by me,
    - to upvote features existed in the database,
    - to comment features,
    - to stand out from the other users on the website.
    


#### Wireframes
- [Wireframes link](https://issuetracker-django.s3-eu-west-1.amazonaws.com/media/IssutrackerWireframes.png)


## Features
- __Register__
    - user can register by providing email address, username and password in register form. Password needs to be confirmed in extra field. If user tries to register username or email address that already exists in the database an error is displayed. After successful registering user is redirected to the home page.
- __Log in, log out__
    - registered user can log in by filling in login form. If user was redirected to login page from a page which functionality required user to be authenticated, after successful logging in user will be redirected back to that page. Otherwise user is redirected to the profile page. If user provides wrong username and/or wrong password an error is displayed.
- __Add bugs and features__
    - user can add bugs and features to database by filling in a form. The form contains following fields:
        - title 
        - description
    - all fields are required
    - if user leaves any field empty an error is displayed
    - after filling in all fields user can post bug/feature to the database by clicking on 'Create Bug/Feature' button
    - only registered users can add bugs
    - only registered users who donated money can add features
- __Edit bug/feature__
    - user can update bug/feature by changing data in add bug/fature form. Characteristic of 'Create bug/fature' feature from above is in use
- __Donate__
    - user can donate money to be able to add new feature
    - minimum amount of donation is 50 euro
- __Search__
    - user can search for bugs, features and posts by typing a phrase in a search-bar and pressing  search button or enter on the keyboard,
    - a phrase needs to be at least 2 characters long, otherwise a warning will be displayed;
    - user can choose where to look for his search: in bugs, features or posts,
    - pagination is in use
- __View all bugs, posts or features__
    - user has access to all bugs, posts and features sorted by name(ascending and descending) or date(ascending and descending) or number of likes(ascending and descending)
    - pagination is in use
- __Contact__
    - user can send message to website's owners by filling in contact form's fields:
        - email address, subject and message
        - each field is required
    - in case of errors an error is diplayed
    - user can post message by clicking on 'Send message' button
    - if success, success message is displayed
    - user can be redirect to the home page without sending message by clicking on 'Back to the home page' link
- __Statistics__
    - displays charts for all bugs and features
- __Latest posts__
    - displays most recently added posts on the front page
- __View single bug, feature or post__
    - displays all information about the bug, feature or post on a single page
- __Like single bug, feature or post__
    - user is able to like single bug, feature or post by clicking on 'Like' button on a single view page
    - only registered users can like bugs, features or posts
- __Comment bug, feature or post__
    - user is able to post comment(s) for single bug, feature or post by filling in comment's form and clicking on 'Add comment' button on a single view page
- __Add/update user's avatar__
    - user can upload pictures for his profile
    - on upload page user has to choose file to upload
- __Navbar__
    - contains logo and other links, fully responsive
- __Footer__
    - contains linked social icons, contact form and contact details; fully responsive


## Technologies Used
- [Django](https://www.djangoproject.com/)
    - to build web application
- [Python 3.7.3](https://www.python.org/)
    - to write logic
- [PostgreSQL](https://www.postgresql.org/)
    - for store and retrieve data
- [HTML5](https://www.w3.org/TR/html52/)
    - to create website
- [CSS3](https://www.w3.org/Style/CSS/Overview.en.html)
    - to style all elements of the website
- [Bootstrap v4](https://getbootstrap.com/)
    - used for responsiveness and styling
- [jQuery](https://jquery.com/) v3.3.1
    - used for DOM manipulation
- [Charts.js](https://www.chartjs.org/)
    - used for creation charts
- [Aos.js](https://michalsnik.github.io/aos/)
    - used for animate web elements on scroll
- [Font Awesome](https://fontawesome.com/) v5.5.0
    - for all icons used on website
- [Google fonts](https://fonts.google.com/)
    - for extra fonts used on website
- [Gimp](https://www.gimp.org/)
    - for changing resolution and cutting images
- [Chrome developer tools](https://developers.google.com/web/tools/chrome-devtools/)
    - for editing page on-the-fly, diagnosing problems
- [Visual Studio Code](https://code.visualstudio.com/)
    - code editor
- [Git & GitHub](https://github.com/)
    - for project's version control
- [Heroku](https://www.heroku.com/)
    - for app deployment
- [Amazon Web Services](https://aws.amazon.com/)
    - for hosting files
- [Stripe](https://stripe.com/)
    - payment platform
- [tinypng.com](https://tinypng.com/) 
    - for images compression
- [Pencil v3.0.4](https://pencil.evolus.vn)
    - for wireframes
- [The W3C Markup Validation Service](https://validator.w3.org/nu/)
    - to check for syntax errors in HTML code
- [The W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
    - to check for errors in CSS code

## Project challenges.
This project was very challenging yet rewarding.
I learned important things from this project.
First, I learned how to use Python as a Server Side Language.
Second, I learned about PostgreSQL and how to use it with Django.
Third, I learned about Hosting Services(AWS). 
I also learned about Stripe payments,  pagination, uploading files, registering, logging, sending emails. I find the time I spend working on the project very beneficial.

## Testing
#### User stories
User stories from the UX section were tested to ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

1. As a user who is visiting the website I want:
    - to see images and slogans explaining the website's content, 
    > - Banner with image is presented on the each page. The banner contains standing out slogan, informing about website content.
    - to register, to get access to registered users features,
    > - Click on User link situated in navbar and then Register link or 'Free account' button on the home page. For browser's width less than 992px click menu('hamburger' icon) and then click 'User' and 'Register'.
    - to see info about services provided by the website,
    > - Services are explained on two panels containing icons and text on the front page.
    - to see testimonials,
    > - Carousel with testimonials is situated in 'Happy users' section on the front page. Each testimony has picture and quoted text.
    - to see info about people working here,
    > - Staff section is situated at the bottom of the front page. Each staff's profile has picture, name, position and linked social icons
    - to see latest blog posts:
        - each post should show miniature image, title, and date of adding,
    > - Three latest added posts are presented in section 'Our Blog' on the front page. Each post shows title, miniature image, date of adding and link to the full post.
    - to search for posts, bugs and features in database by typing a phrase in a searchbar:
        - search in posts
        - search in bugs
        - search in features
    > - A searchbar is provided. User can use it by clicking Search link in the navbar. For browser's width less than 992px click menu('hamburger' icon) and then click 'Search'. 
    - to see statistics of issues in website's database,
        - divided by cousine, difficulty, preparation time and number of servings.
    > - Click on Community link situated in navbar and then on Stats link. For browser's width less than 992px click menu('hamburger' icon) and then click 'Community' and 'Stats'. After that user is redirected to 'Stats' page, where two kinds of charts are displayed.
    - to see all bugs:
        - sorted by name(ascending and descending) or date(ascending and descending) or number of likes.
    > - Click on Bugs link situated in navbar. For browser's width less than 992px click menu('hamburger' icon) and then click 'Bugs'. After that user is redirected to 'Bugs' page, where pagination is in use and 5 bugs are displayed at once. To see more bugs and travel between user has to use pagination links at the bottom of the page. User can choose how bugs have to be sorted. The options are: date ascending and descending, name ascending and descending, upvotes ascending and descending.
    - to see all features:
        - sorted by name(ascending and descending) or date(ascending and descending) or number of likes.
    > - Click on Features link situated in navbar. For browser's width less than 992px click menu('hamburger' icon) and then click 'Features'. After that user is redirected to 'Features' page, where pagination is in use and 5 features are displayed at once. To see more features and travel between user has to use pagination links at the bottom of the page. User can choose how Features have to be sorted. The options are: date ascending and descending, name ascending and descending, upvotes ascending and descending.
    - to see all posts:
        - sorted by name(ascending and descending) or date(ascending and descending) or number of likes..
    > - Click on Community link situated in navbar and then click on Bugs link. For browser's width less than 992px click menu('hamburger' icon) and then click 'Community' and 'All Recipes'. After that user is redirected to 'Posts' page, where pagination is in use and 5 posts are displayed at once. To see more posts and travel between user has to use paginattion links at the bottom of the page. User can choose how posts have to be sorted. The options are: date ascending and descending, name ascending and descending, upvotes ascending and descending.
   - in case when posts are searched or browsed each post should show:
        - miniature image,
        - title,
        - author's name,
        - date of adding,
        - number of views, likes and comments
     - in case when bugs and features are searched or browsed each bug and feature should show:
        - title,
        - author's name,
        - date of adding,
        - number of views, likes and comments
    - to see all info about a single post displayed on single page by clicking on the post:
        - title
        - full image,
        - author's name and avatar, date of adding,
        - content
        - views, likes, comments,
        - comments leaved by users.
    - to see all info about a single bug or feature displayed on single page by clicking on the bug or feature:
        - title
        - full image,
        - author's name and avatar, date of adding,
        - description,
        - views, likes, comments,
        - comments leaved by users.
    - > - Click on the title of the bug/feature/recipe.
    - to contact website's owners, by filling in and submitting contact form
    > - Click on Contact Us link situated in footer. User will be redirected to Contact page and has to fill in contact form. From there user can send message by clicking 'Send message' button or go the front page without sending message by clicking on 'Back to the home page' link.
    - to see links to social media,
    > - Links to social media are displayed in footer. 
    - to see info about ways of contacting website owners.
    > - Phone number, address and email address are displayed in footer. 

2. As a registered user I want to:
    - to log in,
    > - Click on User link situated in navbar and then click on Login link. For browser's width less than 992px click menu('hamburger' icon) and then click 'User' and 'Login'.
    - to reset my password,
    > - Click on User link situated in navbar and then click on Login link. After that click 'Forgot password?' link at the bottom of the login from to get further instructions.  
    - to add new bug,,
    > - Click on User link situated in navbar and then click on Profile link. On Profile page click 'Add Bug' button.
    - to access my profile:
    > - Click on User link situated in navbar and then click on Profile link. For browser's width less than 992px click menu('hamburger' icon) and then Click on 'User' and 'Profile'.
     - to access my profile:
        - update my profile avatar,
        - if profile's avatar wasn't delivered deafault avatar for a profile shoud by displayed
    > - When on Profile page click 'Update profile' button.
        - check bugs and features added by me,
    > - Bugs and features are displayed on Profile page.
    - to edit, delete bugs added by me,
    > - When on single bug page, click 'Edit' button.  
    - comment bugs and blog posts,
    > - When on single bug or post page, type comment in the comment form and click 'Post comment' button.
    - like bugs and blog posts,
     > - When on single bug or post page, click 'Like' button.
    - to log out.
    > - Click on User link situated in navbar and then click 'Logout'. For browser's width less than 992px click menu('hamburger' icon) and then click 'User' and 'Logout'.
    - to make donation.
    > - Click on Donate link situated in navbar. For browser's width less than 992px click menu('hamburger' icon) and then click 'Donate'. When on 'Donate' page, choose amount in donation form and click 'Pay' button.

3. As a registered user who donated money I want to be able:
    - to add new features with description,
    > - Click on User link situated in navbar and then click on Profile link. On Profile page click 'Add Feature' button.
    - to edit features added by me,
    > - When on single feature page, click 'Edit' button.
    - to upvote features existed in the database,
      > - When on single feature page, click 'I want this too' button.
    - to comment features,
    > - When on single feature page, type comment in the comment form and click 'Post comment' button.
    - to stand out from the other users on the website.
    > - Users who donated money have displayed bold, bright label 'SPONSOR' next to their username on the website.


#### Different browsers, mobile, desktop.
According to https://www.w3schools.com/browsers/ statistics, the most popular browsers are:
- Chrome;
- Edge/IE,
- Firefox,
- Opera.

This project website was tested on mentioned above web browsers, desktop/mobile, Android and iOS.
The project looks and works properly on different browsers and screen sizes. 

#### Code validation
HTML and Css code for this website were validated using W3C Validation Service. No errros were found in the code.

## Deployment
#### To push this app to GitHub repository, the following actions were taken:
1. Installing git and creating a GitHub account.
2. Initializing a git repository in the root of the app folder, by running the git init command.
3. Creating a new repository on GitHub:
    - logging in and going to the GitHub home page. Clicking '+ New repository' button,
    - typing name of the repo and providing a brief description,
    - pressing the 'Create repository' button to make new repo,
    - following the '....or push an existing repository from the command line' section.
4. Adding, committing and pushing changes to GitHub repository.

#### Deploying to heroku took following steps:
1. Developing app and pushing it to GitHub.
2. Installing gunicorn, a package for django, used to run app on the server.
```
pip install gunicorn  
```
3. Installing psycopg2, to run PostgreSQL, because is easy to setup on Heroku, instead of MySql or Sqlite.
```
pip install psycopg2  
```
4. Installing dj_database_url, a package used to add database to django.
```
pip install dj_database_url  
```
5. Creating a requirements.txt file. That file contains all required packages to run the application.
```
pip freeze > requirements.txt
```
6. Creating a Procfile. Procfile is a mechanism for declaring what commands are run by application’s dynos on the Heroku platform.
Procfile contains:
```
echo web: gunicorn issuetracker.wsgi:application > Procfile
```
7. Pushing changes on Github.
8. Creating an App on Heroku(before creating an app make sure your GitHub account is connected with Heroku Account):
    - click on Create new app an Heroku website
    - type app name and choose region
    - click create app button.
9. Adding PostgreSQL database.
```
heroku addons:create heroku-postgresql:hobby-dev
```
10. Creating config variables:
    - on Heroku app go to settings
    - click Reveal Vars
    - set EMAIL_PASSWORD, EMAIL_ADRESS, SECRET_KEY, STRIPE_PUBLISHABLE_KEY, STRIPE_SECRET_KEY, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY and HOSTNAME.
11. Deploying the app on Heroku:
    -  open your Heroku app and go to deploy option 
    -  select the deployment method as  Github,
    -  search your repository with a name and click connect 
    -  app started to deploy on Heroku,  wait for some time 
    -  after the successful message popup, app can be view using URL delivered by Heroku. 
Live version of this app can be found [here](https://issuetracker-django.herokuapp.com/).

#### To clone this repository and run the app locally following steps are needed:
1. On GitHub, navigate to the main page of the repository.
2. Under the repository name, click Clone or download.
3. In the Clone with HTTPs section, click an copy icon to copy the clone URL for the repository.
4. Open Git Bash and change the current working directory to the location where you want the cloned directory to be made.
5. Type git clone, and then paste the URL you copied in Step 2.
    ```
    $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
    ```
6. Press Enter. Your local clone will be created.  
7. Install requirements
```
pip install -r requirements.txt
```
8. Set the environmental variables:
 - create file env.py in the main folder of the app
 - set variables for  EMAIL_PASSWORD, EMAIL_ADRESS, SECRET_KEY, STRIPE_PUBLISHABLE_KEY, STRIPE_SECRET_KEY, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY and HOSTNAME
9. Start the app 
```
python manage.py runserver
```
and go to http://127.0.0.1:8000/

## Content
#### Images 
All images used in the project were downloaded from [pixabay](https://pixabay.com/).

## Acknowledgements
I received inspiration for this project from [Code Institute](https://www.codeinstitute.net/).