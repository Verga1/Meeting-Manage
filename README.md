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

Here are the designs I made for the site [1](/static/images/meeting_manager_wf1.png), [2](/static/images/meeting_manager_wf2.png), [3](/static/images/meeting_manager_wf3.png), [4](/static/images/meeting_manager_wf4.png) and [5](/static/images/meeting_manager_wf5.png).

### **Design**

#### Colour Scheme
    -   The two main colours used are purple and white.
#### Typography
    -   Roboto 2.0 is the standard font used by the Materialize framework, which is utilised by this app.

## FEATURES

### *Visible to all users*

1. **Index page**
    - Upon entering the site you are greeted with a card panel indicating that you need to register or Login to gain access to the site.

2. **Login / Register**
    - The option to Login or Register is visible to all users from the menu tab in the navigation bar. However, only those registered can use the login feature.
    - Both Username and password require a minimum length of 5 characters. If this is not completed the colour scheme of the line will turn red, (green indicates you have 5 or more characters).

#### *Visible to registered users*

1. **New Meeting**
    - Registered users can create a new meeting through a form.
    - There are six inputs to complete of which only four are required to actually create the meeting.
    - The required inputs text line will turn red if not completed (1 dropdown selection, 2 text inputs minimum 5 characters and a date picker).
    - The other inputs required will more likely be completed after the meeting takes place.

2. **Home**
    - This is where the details of all meetings are held. They are visible to all users.
    - The meeting name and date are displayed for users to see and the details of the meeting are shown in a collapsible body once meeting is clicked.
    - The options to edit or delete the meeting are available in this body to the user who created the meeting or the admin.
    - When a user chooses to delete a meeting a modal will pop up first to prompt the user to confirm they do want to delete the meeting.
    - When a user chooses to edit the meeting they will be taken to the edit meeting page which has the same functionality as the add meeting page except the buttons (edit meeting and cancel).
    - There is a search functionalty which allows you to search by meeting name. Enter a meeting name and click the search button. Click the reset button to show all meetings again.
    - There is a defensive program should anyone try to copy and paste the URL of this page (and the edit page). If a user does not have login access they will be shown an error page.

3. **Profile**
    - The Profile page lets users know what access/capabilities they have on the site.

4. **Logout**

    - Both logged in Users and Admin can log out by clicking the Log Out menu item from the navigation bar. 
    - They will be redirected to the Login page

#### *Visible to admin user*

1. **Manage Groups**
    - Full CRUD funtionality for groups
        - Create Group
        - Read Group
        - Edit Group
        - Delete Group
    - Groups are included in the dropdown selection input on the add meeting page.
    - When the *admin* chooses to delete a group a modal will pop up first to prompt the user to confirm they do want to delete the meeting.
    - There is a defensive program should anyone try to copy and paste the URL of this page. If a user does not have access they will be shown an error page.


    - To view please use the following login details: 
        - *Username*: admin
        - *Password*:adminpassword


 ### Features Left to Impliment

Future features may include but not limted to: 
1. **Profile** 
    - Password update feature
    - Profiles by group selection
2. **Home Page** -  meetings only visible by group profile
3. **New Meeting** - ability to upload external files
4. **Admin User** - at present admin is identified with just username == admin I would like the ability to have multiple admins


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
-   [Balsamiq](https://balsamiq.com/)
    - Balsamiq was used to complete the wireframes,
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

 ### **Feature Testing**

#### First Time User Story - Non Session User

Possible Actions
- View Index Page
- View Login Page
- View Registration Page

##### *View Index Page*
- Launch Site via URL - https://flask-meeting-manager-project.herokuapp.com/
- **Expected Result:** Directed to site index page which directs user to login or register

##### *Register*
Launch Site via URL - https://flask-meeting-manager-project.herokuapp.com/
- Try to find the Registration page
    - **Nav bar** - From the navigation menu click *Register*
- **Expected Result:** 
    - Directed to Register Page

- Fill in username and password 
- **Expected Result:** 
    - Directed to profile page
    - Success flash message to appear with welcome message to user - "*Welcome 'username'*"

<br>

#### Returning/Frequent User Story - Session User

Possible Actions
- Login
- View Home Page 
- View Profile Page
- Logout
- Create a new Meeting
- Edit/Update own Meeting
- Delete own Meeting

##### *Login*
Launch Site via URL - https://flask-meeting-manager-project.herokuapp.com/
- Try to find the Login page
    - From the navigation menu click *Login*
- **Expected Result:** 
    - Directed to Login Page

- Fill in username and password 
- **Expected Result:** 
    - Directed to profile page
    - Success flash message to appear with welcome message to user - "*Welcome 'username'*"
- **Defensive Design:** 
    - Enter a wrong username --> warning flash message returned - "*Incorrect Username and/or Password*"
    - Enter a wrong password --> warning flash message returned - "*Incorrect Username and/or Password*"


##### *Logout*
- From the navigation menu click *Logout* 
- **Expected Result:** 
    - Directed to Login page
    - Success flash message confirming you have logged out --> "*You have been successfully logged out*"

##### *Meetings (CRUD)*
##### *Meeting Create*
- From the navigation menu click *New Meetings*
- Fill out form all fields required 
- Click the "*Add Meeting*" button

- **Expected Result:** 
    - Directed to Home page and will see new meeting live on the page
    - Success flash message to appear --> "*Meeting Successfully Added*"
- **Defensive Design:** 
    - User will be prompted to fill out required fields and won't be able to submit untill populated

##### *Meetings Read*
- Meeting available to read on Home page

##### *Meetings Edit/Update*
- Meeting creator will have the abilty to edit a meeting
- Navigate to the home page
    - From the navigation menu select *Home* then select the meeting to edit 
    - From the meeting detail in collapsible body select the edit button on the card
- **Expected Result:** 
    - Directed to Edit Meeting page
 
- User can edit details and click the *Edit* button
    - **Expected Result:** 
        - Success Flash message --> "*Meeting Successfully Updated*"
- User can cancel changes and click the *cancel* button
    - **Expected Result:** 
        - Directed back to the home page to review

- **Defensive Design:** 
    - To protect the integrity of all meetings a registered user is only able to edit a meeting they created


##### *Meeting Delete*
User can delete a meeting by clicking the *Delete* button
- **Expected Result:** 
    - Pop-up mondal to ask user to confirm deletion
    - Meeting deleted from list
    - User directed back to Home page
    - Success Flash message --> "*Meeting Successfully Deleted*"

- **Defensive Design:** 
    - To protect the integrity of all meetings a registered user is only able to delete a meeting they created
<br>

#### Admin User Story

Possible Actions: 
- Access to all registered user features
- Added feature of group category management 


##### *Login*
- To test admin feature please use the following login details: 
    - *Username*: admin
    - *Password*:adminpassword

##### *Category (CRUD)*
##### *Manage Groups*

- Log in with username == admin
- Select *Manage Groups* from the navigation menu
- **Expected Result:** 
    - Directed to Manage Groups list page 

**Defensive Design:** 
- Only admin can view the groups to protect integrity
 

##### Meeting-Group Create
- On manage groups  page click "*Add Group*" button
- Directed to Add Group page
- Enter new group name and click the "*Add Group*" button

- **Expected Result:** 
    - Directed to Manage Groups page 
    - Success Flash message --> "*New Group Added*"
    - New Group card appears on list page


##### *Project-Category Edit/Update*
- On manage groups page click "*Edit*" button on the group card you'd like to edit
- **Expected Result:** - Directed to Edit Group page
- Make edit to group or cancel changes
- **Expected Result:**
    - Directed back to manage group page
    - If changes made flash message --> "*Group Successfully Updated*"

##### *Project-Category Delete*
- On manage groups page click "*Delete*" button on the group card you'd like to remove
- **Expected Result:** 
    - Pop-up modal to ask user to confirm deletion
    - Category deleted from groups
    - User directed back to manage groups page
    - Success Flash message --> "*Group Successfully Deleted*"


### Defensive Design Testing

- As detailed above all features have been designed with the consideration to the session user to manage the user actions and visibility
- Navigation menu items have been restricted based on session user

### **Code Validators**

To ensure all code was clean, bug free and most importantly for python PEP8 compliant the following validators were used on the site: 

- [W3C HTML validator](https://validator.w3.org/) to validate CSS code
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) to validate CSS code
- [JSlint](https://jslint.com) to validate jQuery Code
- Pylint in the DOM to validate Python code

### **Site UI/UX & Browser Compatibility Testing**

- Manual testing was carried out on this site by the developers family members to review the UX and site responsivness
- Chrome dev tools were used to review responsivness on multiple device sizes
- Cross browser testing was also attempted on Chrome, Firefox and Safari

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
        3. The 'Edit Meeting' form contains the same ability.

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


To deploy this page to GitHub Pages from its GitHub repository, the following steps were taken:

1. Log into GitHub.
2. In the list of repositories on the screen, select Meeting Manager.
3. In the menu items near the top of the page, select Settings.
4. Scroll down to the GitHub Pages section.
5. Under Source select the drop-down menu labelled None and select Master Branch and hit save
6. The Master Branch automatically refreshes the page, the website has now been deployed.
7. Scroll down to the GitHub Pages section in order to retrieve the link to the deployed website.



### Run the project locally

Clone this project from GitHub:

1. Click for the [GitHub repository](https://github.com/Verga1/Meeting-Manager).
2. Near the top of the page, click the green button "Code".
3. In the Clone with HTTPs section, copy the clone URL for the repository.
4. Open your preferred IDE.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type git clone, and then paste the URL you copied in Step 3.
7. Press Enter. Your local clone will be created.

Further details on cloning a repository can be found on [GitHub](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

## CREDITS

### Tutorial
-   This app was built in conjunction with The Code Institute 'Data Centric Development' module.

### Acknowledgements

I would like to extend a special thanks to my Code Institute Mentor Rohit Sharma for kind support and time throughout this project.
Thank you also to the tutors for their support throughout this project.


#### Disclaimer
The content of this website is for educational purposes only.
 
