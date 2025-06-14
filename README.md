# Project Overview
The Fork and Knife Steakhouse is a fictional, full-stack web application built for a premium dining experience. Designed with a focus on user convenience and elegant simplicity, the site aims to showcase the restaurant’s brand, enable smooth online reservations, and enhance customer engagement.

[Link to the live site.](https://pp4-2025-20f4ea33eee5.herokuapp.com/)
![](https://github.com/MiaTothova/PP4/blob/main/Readme-documentation/responsive.png)

# UX / Design & Planning :

## Site Goals

* Provide a visually appealing and user-friendly platform for potential customers.
* Allow guests to browse the menu, register an account, and book a table effortlessly.
* Enable authenticated users to view, edit, and cancel their reservations.
* Support restaurant staff with an admin interface to manage bookings and customer interactions.

## Target Users

* New and returning customers looking to reserve a table at the steakhouse.
* Guests browsing the menu before dining in.
* Authenticated users who wish to manage their bookings online.
* Restaurant management accessing the admin dashboard to handle reservations efficiently.

This application is built with a mobile-first, responsive design to ensure a seamless experience across all devices—from smartphones to desktops—making fine dining just a few clicks away.

## User Stories
1. As a guest, I want to browse the website easily through navbar options. So that I can see the menu and decide if I want to register.[#1](https://github.com/users/MiaTothova/projects/5?pane=issue&itemId=98547855&issue=MiaTothova%7CPP4%7C1)
2. As a user, I want to register an account so I can make a restaurant booking.[#2](https://github.com/users/MiaTothova/projects/5/views/1?pane=issue&itemId=98547856&issue=MiaTothova%7CPP4%7C2)
3. As a logged in user, I want to be able to make a booking at the restaurant.[#3](https://github.com/users/MiaTothova/projects/5/views/1?pane=issue&itemId=98547858&issue=MiaTothova%7CPP4%7C3)
4. As a user, I want login and logout successfully when I need to so that I can manage my bookings.[#4](https://github.com/users/MiaTothova/projects/5/views/1?pane=issue&itemId=98547860&issue=MiaTothova%7CPP4%7C4)
5. As an admin, I want to view all customer bookings, so that I can manage reservations effectively.[#5](https://github.com/users/MiaTothova/projects/5/views/1?pane=issue&itemId=98728716&issue=MiaTothova%7CPP4%7C5)
6. As an admin, I want to manage user accounts and have all their information visible to me so that I can contact them if necessary.[#6](https://github.com/users/MiaTothova/projects/5/views/1?pane=issue&itemId=98730100&issue=MiaTothova%7CPP4%7C6)
7. As a user, I want to see an easy-to-understand website so that I can make conscious selections.[#7](https://github.com/users/MiaTothova/projects/5/views/1?pane=issue&itemId=98737167&issue=MiaTothova%7CPP4%7C7)
8. As a logged-in user, I want to see all my upcoming reservations.[#8](https://github.com/users/MiaTothova/projects/5/views/1?pane=issue&itemId=99013887&issue=MiaTothova%7CPP4%7C8)
9. As a logged-in user, I want to cancel any of my upcoming bookings if my plans change.[#9](https://github.com/users/MiaTothova/projects/5/views/1?pane=issue&itemId=99013888&issue=MiaTothova%7CPP4%7C9)
10. As an admin, I want to see all booking reservations in my admin panel to manage them accordingly.[#10](https://github.com/users/MiaTothova/projects/5/views/1?pane=issue&itemId=99013889&issue=MiaTothova%7CPP4%7C10)
11. As a user/regular customer I want to be able to make/ access my booking through my phone or tablet for convenience.[#12](https://github.com/users/MiaTothova/projects/5/views/1?pane=issue&itemId=99013996&issue=MiaTothova%7CPP4%7C12)

### Wireframes
Initial wireframes were sketched by hand using pen and paper. This approach helped me quickly brainstorm ideas, identify key components, and visualize the overall structure of the website. Once I had a clearer direction, I recreated the wireframes in Balsamiq to produce a more refined layout. During the design phase, some elements were modified to enhance usability and improve the overall user experience.

Web View
![](https://github.com/MiaTothova/PP4/blob/main/Readme-documentation/wireframes/web.png)

Tablet View
![](https://github.com/MiaTothova/PP4/blob/main/Readme-documentation/wireframes/tablet.png)

Mobile View
![](https://github.com/MiaTothova/PP4/blob/main/Readme-documentation/wireframes/mobile.png)

## Agile Methodology
The development of The Knife and Fork Steakhouse was managed using the Agile Methodology, with an emphasis on incremental progress and flexible planning. I used GitHub Issues to document all User Stories, each containing clear Acceptance Criteria and a list of tasks to complete.

As I progressed through the project, some of the tasks and acceptance criteria were adjusted to better reflect the technical requirements and the reality of implementation. This was especially important in the early stages, as I was still learning how to approach problems using Django and Agile principles together.

To help prioritize features, I applied the MoSCoW Method:
* Must Have: Core features such as booking creation, user authentication, and viewing bookings.
* Should Have: Useful features like editing and deleting bookings.
* Could Have: Additional improvements such as styling tweaks and user notifications.
* SWon’t Have: Optional features like email confirmations were left in the Backlog for future iterations.

Although I didn’t work in fixed sprints, I used a Kanban-style board to manage my workflow. It was highly motivating to move tasks from "To Do" to "Done", and it helped me keep track of progress throughout the project.

This was my first time applying Agile methodology to a Django project, and I found it incredibly helpful. It provided structure, improved time management, and gave me a clear sense of direction from start to finish.

### Design
The Fork and Knife Steakhouse website is built with a focus on clean design and consistent structure across all pages. It is fully responsive and adjusts seamlessly to screen sizes ranging from 320px (mobile) to 2560px (large desktop).

The navigation bar is accessible on every page and features the restaurant logo along with clearly labeled links to the Homepage, Menu, Bookings, and user authentication options (Register, Login, or Logout). On smaller screens, a hamburger menu appears to ensure a clutter-free layout and ease of use.

The footer is also consistent throughout the site, providing quick access to social media links (which open in new tabs). This ensures that users can easily get in touch or stay connected.

The Home Page acts as the entry point to the site, welcoming users with a large hero section featuring the restaurant’s name and buttons to direct users to the menu or booking pages. An “About” section further introduces the restaurant’s story and values.

The Menu Page categorizes dishes for easy browsing, such as Starters, Mains, Desserts, and Beverages.

User authentication pages (registration and login) are styled to be simple and familiar, ensuring an easy onboarding process. These are accessible via the navbar and behave predictably on all devices.

Finally, the Book Now and My Bookings pages are reserved for logged-in users. These pages provide full CRUD functionality, allowing users to create, view, edit, or cancel their table reservations in a user-friendly environment.

### Typography
The website uses the Poppins font from Google Fonts throughout all pages. It’s a clean, modern sans-serif font that improves readability and gives a stylish and professional look across devices.

### Colour Scheme

| Colour Use            | Hex Code   | Description                                      |
|-----------------------|------------|--------------------------------------------------|
| Primary Accent        | `#8b0000`  | Deep red used for headings, buttons, and highlights |
| Button Gradient       | `#8b0000 → #ff4500` | Gradient for call-to-action buttons    |
| Background            | `#f7d9bf`  | Soft peach for a warm and inviting background    |
| Header/Footer Text    | `#ffffff`  | Clean white used for text contrast               |
| Body Text             | `#333333`  | Dark grey for easy readability                   |
| Hover Highlight       | `#f39c12`  | Orange/yellow used for interactive effects       |

This colour palette was chosen to reflect the warmth and boldness of a steakhouse brand while keeping it elegant and user-friendly.

This colour pallete was used as a inspiration:
![](https://github.com/MiaTothova/PP4/blob/main/Readme-documentation/color.png)


## Features

### Header and Navigation
* A responsive navigation bar is displayed across all pages. It updates dynamically based on user login status, showing options like "Register" and "Login" for guests, and "Book Now", "My Bookings", and "Logout" for authenticated users. On mobile devices, the navigation menu collapses into a hamburger icon for better accessibility.

![](https://github.com/MiaTothova/PP4/blob/main/Readme-documentation/nav.png)

### Home page
The home page serves as the main entry point to the site and clearly communicates the restaurant’s identity and purpose. It features a carousel with three hero image slides, each promoting the atmosphere and offerings of the restaurant. Below the carousel is an About section that shares the story of the restaurant and its values, helping users connect with the brand

![](https://github.com/MiaTothova/PP4/blob/main/Readme-documentation/home.png)

### Footer
Displayed on all pages, the footer contains the restaurant’s social media links that open in new tabs, and a clean layout that ensures consistency across the site.

![](https://github.com/MiaTothova/PP4/blob/main/Readme-documentation/footer.png)

### Menu page
Lists the restaurant’s dishes in categories such as Starters, Mains, Desserts, and Drinks. Each section is styled for readability and consistency.

![](https://github.com/MiaTothova/PP4/blob/main/Readme-documentation/menu.png)

### Register page
Allows new users to sign up using a simple form powered by Django Allauth. The form includes username, email, and password fields, styled to match the overall design of the site.

![](https://github.com/MiaTothova/PP4/blob/main/Readme-documentation/reg.png)

### Login
Provides a secure login form for returning users. Once logged in, users are redirected to the homepage, with their navigation links updated accordingly.

![](https://github.com/MiaTothova/PP4/blob/main/Readme-documentation/signin.png)

#### Logout 
A simple logout confirmation page that signs users out securely and updates the navbar to reflect their logged-out status.

![](https://github.com/MiaTothova/PP4/blob/main/Readme-documentation/logout.png)

### Book Now
Authenticated users can access a booking form to reserve a table. The form includes name, email, date, time, and guest number.

![](https://github.com/MiaTothova/PP4/blob/main/Readme-documentation/book-now.png)

### My Bookings
Authenticated users can view, edit, or cancel their reservations. Each booking is displayed with key details like date, time and guest count. Update and Cancel actions are available per booking.

![](https://github.com/MiaTothova/PP4/blob/main/Readme-documentation/bookings.png)

### Admin Panel
Accessible only by superusers. The admin panel provides full CRUD control over bookings, users, and any registered models. It uses Django’s built-in admin interface and supports filtering, searching, and inline editing.
Admins can:
* Create new bookings or users
* Read booking and user data
* Update any entry
* Delete records as needed
It provides full control over the data and uses built-in Django features like filtering and search.

![](https://github.com/MiaTothova/PP4/blob/main/Readme-documentation/admin.png)

### CRUD Functionality 
The site implements full CRUD operations for the Booking model:
* Create: Users can make new bookings.
* Read: View bookings on the "My Bookings" page.
* Update: Modify existing bookings.
* Delete: Cancel a booking.
All these actions are protected behind user authentication to ensure data privacy and security.



### Future Features
* Email and SMS Booking Confirmations - 
Automatically send booking confirmation and reminders to users after a reservation is made.
* Edit User Profile - 
Enable users to update their personal information (e.g., name, email, password) through a profile page.
* Special Events and Promotions -
A section for the restaurant to post upcoming events, limited-time menus, or discount offers.
* Newsletter Integration - 
Let users subscribe to receive news, offers, and updates via email.


## Testing
### Code Validations :
#### HTML:
HTML code was tested using the [W3C Validator](https://validator.w3.org/) by text input. The HTML code was copied and pasted in from each page's source code from the live website. 
Pages tested:
* Home, Menu, Book Now, My Bookings, Logout, Login, Register and Edit Booking. As the validation results were consistent across all pages, a single representative screenshot is included.
![](https://github.com/MiaTothova/PP4/blob/main/Readme-documentation/validators/html.png)

#### CSS:
CSS code was tested using the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) by text input and by url. Both results were consistent.  
![](https://github.com/MiaTothova/PP4/blob/main/Readme-documentation/validators/css.png)

#### Python:
The Python code was tested using [Code Institute's Python Linter](https://pep8ci.herokuapp.com/) to check for PEP8 compliance. Additionally, Flake8 was run in the terminal throughout development to identify and fix any formatting issues or unused imports. Both tools helped ensure the code followed clean, readable, and consistent Python style guidelines.
![](https://github.com/MiaTothova/PP4/blob/main/Readme-documentation/validators/flake8.png)

#### Java Script:
JavaScript code was tested using [JSHint](https://jshint.com/) to check for syntax errors and adherence to best practices. Minor adjustments, such as setting esversion: 6, were made to accommodate modern JavaScript features like const and let.
![](https://github.com/MiaTothova/PP4/blob/main/Readme-documentation/validators/js.png)

#### Lighthouse:
Lighthouse testing was performed using Chrome DevTools to evaluate performance, accessibility, best practices, and SEO across key pages. Results helped guide improvements to overall user experience and site efficiency.
![](https://github.com/MiaTothova/PP4/blob/main/Readme-documentation/validators/lighthouse.png)

#### responsivness Testing
The website is fully responsive across a wide range of screen sizes, from a minimum width of 320px to a maximum of 2560px. Friends and family tested the site on various devices, including phones and tablets, and reported no issues with layout or usability. Additional manual testing was carried out using [Chrome's DevTools](https://websiteresponsivetest.com/) to simulate different screen resolutions and ensure consistent responsiveness throughout.

#### Browser Compatibility Testing
The website was tested across all major browsers and passed compatibility checks without any issues. The layout, functionality, and responsiveness remained consistent on the following browsers:
* Google Chrome
* Mozilla Firefox
* Microsoft Edge
* Safari
* Opera
All core features, including navigation, form handling, and responsiveness, performed as expected across each browser.

### User stories testing 

1. As a guest, I want to browse the website easily through navbar options. So that I can see the menu and decide if I want to register.[#1](https://github.com/users/MiaTothova/projects/5?pane=issue&itemId=98547855&issue=MiaTothova%7CPP4%7C1)
![](https://github.com/MiaTothova/PP4/blob/main/Readme-documentation/%231.png)
* As shown in the image, the navigation menu is clearly visible, allowing the user to easily identify and choose their desired action.

2. As a user, I want to register an account so I can make a restaurant booking.[#2](https://github.com/users/MiaTothova/projects/5/views/1?pane=issue&itemId=98547856&issue=MiaTothova%7CPP4%7C2)
![](https://github.com/MiaTothova/PP4/blob/main/Readme-documentation/%232.png)
* When users navigate to the registration page, they are presented with a form where they can choose a username, enter their email and password, and click the "Sign Up" button to register.

3. As a logged in user, I want to be able to make a booking at the restaurant.[#3](https://github.com/users/MiaTothova/projects/5/views/1?pane=issue&itemId=98547858&issue=MiaTothova%7CPP4%7C3)
![](https://github.com/MiaTothova/PP4/blob/main/Readme-documentation/%233.png)
* When logged-in users navigate to the Book Now page, they are presented with a booking form. They enter their name, email, date, time, and number of guests, then click the Book Now button to confirm their reservation.

4. As a user, I want login and logout successfully when I need to so that I can manage my bookings.[#4](https://github.com/users/MiaTothova/projects/5/views/1?pane=issue&itemId=98547860&issue=MiaTothova%7CPP4%7C4)
![](https://github.com/MiaTothova/PP4/blob/main/Readme-documentation/%234.png)
![](https://github.com/MiaTothova/PP4/blob/main/Readme-documentation/%234-logout.png)
* When a registered user wants to log in, they are presented with a simple form. They enter their username and password, then click the Sign In button to access their account.
* When the user is finished, they can easily sign out by navigating to the logout page and clicking the Sign Out button.

5. As an admin, I want to view all customer bookings, so that I can manage reservations effectively.[#5](https://github.com/users/MiaTothova/projects/5/views/1?pane=issue&itemId=98728716&issue=MiaTothova%7CPP4%7C5)
![](https://github.com/MiaTothova/PP4/blob/main/Readme-documentation/%235.png)
* When the admin accesses the Bookings section, they are presented with a list of current bookings, allowing them to manage and update each entry as needed.

6. As an admin, I want to manage user accounts and have all their information visible to me so that I can contact them if necessary.[#6](https://github.com/users/MiaTothova/projects/5/views/1?pane=issue&itemId=98730100&issue=MiaTothova%7CPP4%7C6)
![](https://github.com/MiaTothova/PP4/blob/main/Readme-documentation/%236.png)
* When the admin navigates to the Users section, they are presented with a list of all currently registered users and can manage their information as needed.

7. As a user, I want to see an easy-to-understand website so that I can make conscious selections.[#7](https://github.com/users/MiaTothova/projects/5/views/1?pane=issue&itemId=98737167&issue=MiaTothova%7CPP4%7C7)
![](https://github.com/MiaTothova/PP4/blob/main/Readme-documentation/%237.png)
* The layout of the website is simple and intuitive. The logo and restaurant name are prominently displayed, the navigation bar is easy to read, and key sections like the About area and footer are clearly visible. Users can quickly understand where to go based on their needs.

8. As a logged-in user, I want to see all my upcoming reservations.[#8](https://github.com/users/MiaTothova/projects/5/views/1?pane=issue&itemId=99013887&issue=MiaTothova%7CPP4%7C8)
![](https://github.com/MiaTothova/PP4/blob/main/Readme-documentation/%238.png)
* When users navigate to the My Bookings page, they can clearly view all their reservations. From this page, they have the option to edit or cancel any booking as needed.

9. As a logged-in user, I want to cancel any of my upcoming bookings if my plans change.[#9](https://github.com/users/MiaTothova/projects/5/views/1?pane=issue&itemId=99013888&issue=MiaTothova%7CPP4%7C9)
![](https://github.com/MiaTothova/PP4/blob/main/Readme-documentation/%239.png)
* From the My Bookings page, users can select which reservation they wish to cancel. They are then presented with a confirmation prompt asking if they are sure they want to proceed or return to the My Bookings page.
* Upon cancellation, a Bootstrap alert notifies the user that their booking has been successfully cancelled. To improve the user experience, I added a small JavaScript function that automatically dismisses the alert after 3 seconds, eliminating the need for users to manually close it each time—helping to keep interactions smooth and less disruptive.

10. As an admin, I want to see all booking reservations in my admin panel to manage them accordingly.[#10](https://github.com/users/MiaTothova/projects/5/views/1?pane=issue&itemId=99013889&issue=MiaTothova%7CPP4%7C10)
![](https://github.com/MiaTothova/PP4/blob/main/Readme-documentation/%235.png)
* Same as in User story no.5, When the admin accesses the Bookings section, they are presented with a list of current bookings, allowing them to manage and update each entry as needed.

11. As a user/regular customer I want to be able to make/ access my booking through my phone or tablet for convenience.[#12](https://github.com/users/MiaTothova/projects/5/views/1?pane=issue&itemId=99013996&issue=MiaTothova%7CPP4%7C12)
![](https://github.com/MiaTothova/PP4/blob/main/Readme-documentation/%2311-tablet.png)
![](https://github.com/MiaTothova/PP4/blob/main/Readme-documentation/%2311-phone.png)
* I tested the My Bookings page on both mobile and tablet devices, and in each case, the user was able to access and view their bookings without any issues.



### known Bugs and Issues

* Date and Time Validation on Booking Form :
Due to limited time and the need to focus on finalizing the README before resubmission, full validation for the booking date and time has not yet been implemented.
While the form remains functional and allows users to submit bookings, the lack of proper validation can affect the user experience by allowing bookings for past dates or outside intended operating hours. This does not break the application but is something that should be addressed in future development to ensure accurate and user-friendly input handling.

* Bootstrap Alerts Auto-Close:
Bootstrap alerts used to require manual dismissal. This was improved by implementing a JavaScript function that auto-dismisses alerts after 3 seconds for a smoother user experience.

* Minor Mobile Layout Adjustments:
Some UI elements such as forms and text spacing needed extra styling for smaller screens. Media queries were added to resolve layout inconsistencies.

* Heroku 504 Gateway Timeout:
A temporary timeout occurred during login or page load, likely related to Heroku’s connection through CloudFront. No changes were needed in the application code.

* JavaScript Warnings:
JSHint initially reported ES6 syntax and undefined global variables like bootstrap. These were resolved by updating JSHint settings and explicitly declaring global variables where necessary.


## Deployment
For good practice, this project was deployed early to [Heroku](https://www.heroku.com).

After installing Django and the necessary libraries, the base project was set up and the initial database migration was completed.

By default, Django uses [db.sqlite3](https://docs.python.org/3/library/sqlite3.html), which is only available within the local development environment. To make the project work in a live production setting like Heroku, a more robust and accessible database is needed. Instead of using Heroku’s paid Postgres add-on, a free PostgreSQL database was set up using [CI Database](https://dbs.ci-dbs.net/), which works well for deployment purposes.
### First Deployment:

##### Create the Heroku App
1. Login to Heroku and click on the top right button ‘New’ on the dashboard. 
2. Click ‘Create new app’.
3. Give your app a name and select the region closest to you. 
4. Click on the ‘Create app’ button.

#### Create the PostgreSQL Database
1. Login to https://dbs.ci-dbs.net/.
2. step 1: enter your email and submit.  
3. step 2: creates a database.  
4. step 3: receive the database link in your email.

#### Create the env.py file
After setting up the database, you need to connect it to your project. Some variables should be kept private and not uploaded to GitHub

1. To keep sensitive variables hidden, create a file called env.py and add it to your .gitignore so it won’t be uploaded to GitHub.
2. At the top of env.py, write import os, then set the DATABASE_URL variable like this:
`os.environ["DATABASE_URL"] = "your_database_url"`
3. Django also needs a SECRET_KEY variable for security. You can make one up or generate it using [MiniWebTool](https://miniwebtool.com/django-secret-key-generator/). Add it like this:
`os.environ["SECRET_KEY"] = "your_secret_key"`

#### settings.py
To connect your Django project to the new PostgreSQL database and use the variables stored in env.py, follow these steps:
1. In your settings.py file, make Django aware of your environment variables. Use this conditional import to avoid errors if env.py is missing:
```
import os
import dj_database_url

if os.path.isfile(‘env.py’):
    import env
```
2. Replace Django’s default secret key with the one you defined in env.py by referencing the environment variable:
```
SECRET_KEY = os.environ.get(‘SECRET_KEY’)
```
3. Update the database configuration to use the external PostgreSQL database instead of the default sqlite3. Comment out the existing block and replace it with:
```

DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}
```

**NOTE**:  If you started the project using sqlite3, remember to add db.sqlite3 to your .gitignore so it doesn’t get pushed to GitHub.
4. Once everything is set up, apply the database migrations to create the necessary tables:
`python3 manage.py migrate`

#### Link the Database to Heroku
1. Go to the Heroku dashboard, select your app, and navigate to the Settings tab.
2. Under Config Vars, click Reveal Config Vars and add a new variable:
* DATABASE_URL with the value copied from your PostgreSQL database created on CI database.
3. Add another variable:
* SECRET_KEY using the same value set in your env.py file.
4. If you're developing with Gitpod, add an additional variable:
* PORT with the value 8000 (this ensures proper deployment).

#### Add the Heroku Host Name
In your settings.py file, find the ALLOWED_HOSTS list and add your Heroku app’s hostname. This is usually the name you gave the app followed by .herokuapp.com. You should also add 'localhost' so the app can run locally during development:
```
ALLOWED_HOSTS = [‘heroku-app-name.herokuapp.com’, ‘localhost’]
```
#### Set Up Static, Media, and Procfile
1. At the root of your project (next to manage.py), create folders for static, media, and templates.
2. In the same directory, create a new file named Procfile (capital "P", no file extension).
3. Add the following line to tell Heroku how to run your app (replace your_project_name with your actual project folder name):
```
web: gunicorn your_project_name.wsgi
```
* web tells Heroku to handle web traffic.
* gunicorn is the WSGI HTTP server used in production.
* wsgi connects Django to the server.
4. Save all changes and commit them before pushing to GitHub.

### Initial Deployment to Heroku
1. In Heroku, open your app and go to the Deploy tab.
2. Under Deployment method, choose GitHub and connect your GitHub account if needed.
3. Search for your project repository and click Connect.
4. Click Deploy Branch to start the build process.
5. Once complete, click Open App to view the live project. You should see Django’s default success page if everything worked correctly.

### Final Deployment
1. Before deploying the final version, make sure DEBUG is set to False in your settings.py file.
If you used `DEBUG = 'DEVELOPMENT' in os.environ`, you can leave it as is since the env.py file is excluded from version control.
2. Save, commit, and push your latest changes to your GitHub repository.
3. Log in to Heroku, go to your project’s app, and open the Settings tab. Under Config Vars, remove the DISABLE_COLLECTSTATIC variable (if present).
4. Go to the Deploy tab and scroll to the Deploy a GitHub branch section.
5. Select the branch you want to deploy and click Deploy Branch.
Once the deployment is successful, you’ll see a confirmation message in the build log.
6. Click View to open your live site in a new tab, or use the Open App button at the top of the dashboard.


### Technologies Used

#### Languages
* HTML
* CSS
* Python
* Java Script

#### Tools
* [GitHub](https://github.com/) - For repo creation and commiting my changes
* [VSCode](https://code.visualstudio.com/) - Coding enviroment
* [Heroku](https://www.heroku.com) - To host the website
* [Bootstrap 4.6.2](https://getbootstrap.com/docs/4.6/getting-started/introduction/) - Responsive, mobile-fist design
* [W3C Validator](https://validator.w3.org/) - HTML validation
* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) - CSS validation
* [Code Institute's Python Linter](https://pep8ci.herokuapp.com/) - Python validation 
* [Flake 8](https://flake8.pycqa.org/en/latest/) - Python testing in the terminal
* [Chrome DevTools](https://developer.chrome.com/docs/devtools/) - Web Developer Tools
* [TinyPNG](https://tinypng.com/) - Resize images
* [Pexels](https://www.pexels.com/) - Free Images
* [Coolors](https://coolors.co/) - Colour Palette Generator
* [Google Fonts](https://fonts.google.com/) - Fonts
* [Balsamiq](https://balsamiq.com/wireframes/) - Low Fidelity Wireframes
* [ChatGPT](chatgpt.com) Used to generate landing page text and menu 
* [FontAwesome](https://fontawesome.com/) - Navbar icon

#### Libraries & Frameworks

* [Django 3.2.18](https://www.djangoproject.com/) - A high-level, open-source Python web framework that promotes rapid development and clean design.
* [Gunicorn 20.1.0](https://gunicorn.org/) - A Python WSGI HTTP server used to deploy the Django application on Heroku.
* [PostgreSQL 0.5.0](https://www.postgresql.org/) - A robust, open-source object-relational database system used for data storage.
* [Pyscopg2 2.9.5](https://www.psycopg.org/docs/) - A PostgreSQL adapter for Python, allowing communication between Django and the PostgreSQL database.
* [Heroku](https://www.heroku.com) - A cloud platform used for deploying, managing, and scaling the web application.
* [Django Allauth](https://django-allauth.readthedocs.io/en/latest/) -  A Django package that provides a full suite of authentication, registration, and account management features.
* [Bootstrap 4.6.2](https://getbootstrap.com/docs/4.6/getting-started/introduction/) - A front-end framework used for building responsive and mobile-first web pages.
* [whitenoise==5.3.0](https://whitenoise.readthedocs.io/en/latest/) - Used to efficiently serve static files directly from the Django app, especially in production.
* [sqlparse==0.5.0](https://pypi.org/project/sqlparse/) - A Python library for parsing and formatting SQL statements.

### Credits

### Acknowledgements