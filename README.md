# Meeting Manager

[View the live app here.](http://flask-meeting-manager-project.herokuapp.com/)

## UX

### **Goals:**

The goal of the app is to provide a service to small businesses and non-profits which will enable them to plan, document and create actionable items from their board or staff meetings. 
It provides them with a set structure to enable the creation and storage of material such as agendas, meeting minutes, and action plans. The app requests that all users register 
and login to view the 'Meeting Manager' associated with their particular group. Once logged in the user can then create, read, update and delete their 'Meetings'. The app is optimized for use on phones and tablets.

### **User Stories**
#### First Time User Goals
    1. As a first time user, I want to see that the app meets my needs or those of my organisation.
    2. As a first time user, I want to easily navigate throughout the app to find content.
    3. As a first time user, I want to see that I can quickly and easily input relevant information.
#### Returning User Goals
    1. As a returning user, I want to create and read Meetings.
    2. As a returning user, I want to share my Meetings with other members of my team.
    3. As a returning user, I want to review meeting details and actions when required.
#### Frequent User Goals
    1. As a frequent user, I want to update and delete Meetings.
    2. As a frequent user, I want to create and manage Meeting Groups.
    3. As a frequent user, I want to view and manage the Meetings.
#### Owner Goals
    1. As the app owner, I want to provide a clean and easy-to-use app that appeals to a certain market.
    2. As the app owner, I want to ensure the app provides industry-standard functionality.
    3. As the app owner, I want to sell other apps to users.


### **Wireframes**

Here are the designs I made for the site [1](/static/images/meeting_manager_wf1.png), [2](/static/images/meeting_manager_wf2.png), [3](/static/images/meeting_manager_wf3.png).

The wireframes were made using [Balsamiq](https://balsamiq.com/)

### **Design**

#### Colour Scheme
    -   The two main colours used are purple and white.
#### Typography
    -   Roboto 2.0 is the standard font used by the Materialize framework, which is utilised by this app.

## FEATURES

-   Responsive on all device sizes.
-   User registration, login & logout.
-   Create, read, update and delete functionality.
-   Search functionality.
-   Confirm delete functionality.
-   Materialize Collapsible Meeting Manager.
-   Mobile collapse nav bar.
-   Different user permissions (Admin/User)


 ### Features Left to Impliment


 ## TECHNOLOGIES USED

### Languages

-   [HTML](https://www.w3schools.com/html/)
-   [CSS](https://www.w3schools.com/css/)
-   [JavaScript](https://www.javascript.com/)
-   [Python](https://www.python.org/)

### Frameworks, Libraries & Programs

-   [Flask](https://flask.palletsprojects.com/)
    - Flask was used to develop the app.
-   [Materialize](https://materializecss.com/)
    - Materialize was used to assist with the responsiveness and styling of the website.
-   [jQuery](https://jquery.com/)
    - jQuery was used in conjunction with Materialize to initialise components.
-   [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub & Heroku.
-   [GitHub](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
-   [MongoDB](https://www.mongodb.com/)
    - MongoDB was the database chosen for use with this app.
-   [Werkzeug](https://werkzeug.palletsprojects.com/)
    - Werkzeug was used for its generate and check password hash functionality.


 ## TESTING

### Testing User Stories from User Experience (UX) Section

#### First Time Visitor Goals

    1. As a first time user, I want to see that the app meets my needs or those of my organisation.

        1. The full workings of the app are apparent from first time use.
        2. The minimalist design allows users to quickly 'Register'/'Login' and see what the 'Meeting Manager' contains and how to edit or add to it.
        3. The 'Profile' page gives information on user permissions with regards to create, read, update and delete rights. (to test this, login as 'testuser' with password 'testpassword')

    2. As a first time user, I want to easily navigate throughout the app to find content.

        1. The app has been designed to be minimalist, with concise information and as few links as possible. 
        2. The 'Meeting Manager' itself appears as a collapsible list as each 'Meeting' contains a lot of information.
        3. The user permissions are slightly different for 'admin' as compared to a regular user and with this in mind, to add or edit a 'Group' don't appear for regular users. (to test this, login as 'admin' with password 'adminpassword')

    3. As a first time user, I want to see that I can quickly and easily input relevant information.
        1. The 'Login' and 'Register' pages only contain 2 input fields.
        2. The 'Add Meeting' link is in the main menu.
        3. The 'Add Group' link is in the main menu for admin. (to test this, login as 'admin' with password 'adminpassword')

#### Returning Visitor Goals

    1. As a returning user, I want to create and view Meetings.

        1. The 'Add Meeting' link is in the main menu for all users.
        2. The 'Meetings/Home' link is in the main menu for all users.
        3. The 'All Meetings' is a collapsible list, all information on a 'Meeting' can be viewed by clicking the 'Meeting' title.

    2. As a returning user, I want to share my 'Meeting' with other members of my team.

        1. There is no limit to how many users can register, login and view the 'Meeting Platform'.
        2. All 'Meetings' are visible the whole team.
        3. 'Meetings' can only be edited or deleted by the user who created them, or by admin.

    3. As a returning user, I want to update action items.
        1. Each 'Meeting' has an ability to edit the meeting details.
        2. The 'Add Meeting' form contains a switch to verify when meeting actions are completed.
        3. The 'Edit Risk' form contains the same ability.

#### Frequent User Goals

    1. As a frequent user, I want to update and delete Meetings.

        1. The 'Edit' and 'Delete' button links are visible within each 'Meeting'. 
        2. 'Meetings' can only be edited or deleted by the user who created them, or by admin.
        3. To delete a 'Meeting' the user will be prompted to confirm they wish to do so.

    2. As a frequent user, I want to create and manage Meeting Groups.

        1. The 'Groups' link is only visible to admin.
        2. The 'Add Group', 'Delete Group' & 'Edit Group' button links are only visible to admin. 
        3. To delete a 'Group' the user will be prompted to confirm they wish to do so.

    3. As a frequent user, I want to view and manage the action items.

        1. 'Meeting Actions' can be changed from within the 'Edit Meeting' form, and has a Materialize switch to show completion.
        2. 'Meeting Actions' are quickly visible in the collapsible body of each Meeting on the Home page.
        3. The Actions Status are tool-tipped to state if the 'Status' is in progress or completed.

#### Owner Goals

    1. As the app owner, I want to provide a clean and easy-to-use app that appeals to a certain market.
        -   The app has been designed to be minimalist, with concise information and as few links as possible.
    2. As the app owner, I want to ensure the app provides industry-standard functionality.
        -   The 'Meeting Manager' contains industry-standard fields and information.
    3. As the app owner, I want to sell other apps to users.
        -   The footer contains a link which can be used to take the user to advertisements for other apps that they might be interested in.

### Further testing
* Tested this website on laptop and mobile.
* Tested this website on Google Chrome, Firefox and Safari browsers.
* I've asked colleagues and friends to give feedback.
* During testing I used "inspect" function on different OS, devices and browsers.


### Bugs


 ## DEPLOYMENT

This project was created using Github, from there I used Gitpod to write my code.
Then I used commits to git followed by pushes to my GitHub repository.
I've deployed this project to Heroku and used automated pushes to make sure my pushes to GitHub were also made to Heroku.
For deployment on Heroku I've used the following steps:
* Using the terminal command pip freeze > requirements.txt I have created a requirements.txt file.
* Using the terminal command echo web: python app.py > Procfile I have created a procfile.
* I've used git add, git commit and git push to push the requirements and procfile to GitHub.
* I've created a new app on the Heroku website by using the "new" button on my dashboard.
* I gave the app a name of flask-meeting-manager-project and set the region to Europe.
* From the Heroku dashboard I've clicked "Deploy" > "Deployment method" and selected GitHub.
* Confirm the linking of the Heroku app to the correct GitHub repository.
* In the Heroku dashboard I've clicked "Settings" > "Reveal Config Vars".
* I've added the config vars for my IP, PORT, MONGO_URI and SECRET_KEY.
* In the "Manual Deployment" section of this page I've made sure the master branch is selected and I've clicked "Deploy Branch".
* The site was now successfully deployed.

## CREDITS

### Tutorial
-   This app was built in conjunction with The Code Institute 'Data Centric Development' module.

### Content

 
 ### Media


## Acknowledgements
 
