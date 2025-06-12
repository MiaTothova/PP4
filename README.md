Introduction---------(overview)

am i responsive image -------


[Link to the live site.](https://pp4-2025-20f4ea33eee5.herokuapp.com/)

# Design & Planning:

## User Stories
1. As a guest, I want to browse the website easily through navbar options. So that I can see the menu and decide if I want to register.
2. As a user, I want to register an account so I can make a restaurant booking
3. As a logged in user, I want to be able to make a booking at the restaurant.
4. As a user, I want login and logout successfully when I need to so that I can manage my bookings.
5. As an admin, I want to view all customer bookings, so that I can manage reservations effectively.
6. As an admin, I want to manage user accounts and have all their information visible to me so that I can contact them if necessary.
7. As a user, I want to see an easy-to-understand website so that I can make conscious selections.
8. As a logged-in user, I want to see all my upcoming reservations.
9. As a logged-in user, I want to cancel any of my upcoming bookings if my plans change.
10. As an admin, I want to see all booking reservations in my admin panel to manage them accordingly.
11. As a user/regular customer I want to be able to make/ access my booking through my phone or tablet for convenience.

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

### UX 
#### Design
#### color

### Features
### Future Features





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


User stories testing -------

### Bugs



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






### Credits

### Acknowledgements