# Meeting Manager

[View the live app here.](http://flask-meeting-manager-project.herokuapp.com/)

![home](/static/images/screenshot_1.png)

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


 ### Features Left to Implement

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
![index page](/static/images/screenshot_12.png)


##### *Register*
Launch Site via URL - https://flask-meeting-manager-project.herokuapp.com/
- Try to find the Registration page
    - **Nav bar** - From the navigation menu click *Register*
![nav bar](/static/images/screenshot_11.png)

- **Expected Result:** 
    - Directed to Register Page
![register](/static/images/screenshot_13.png)

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

- To view please use the following login details: 
    - *Username*: testuser
    - *Password*: testpassword

##### *Login*
Launch Site via URL - https://flask-meeting-manager-project.herokuapp.com/
- Try to find the Login page
    - From the navigation menu click *Login*
![nav bar](/static/images/screenshot_11.png)    
- **Expected Result:** 
    - Directed to Login Page
![login](/static/images/screenshot_14.png) 

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
![logout](/static/images/screenshot_15.png) 

##### *Meetings (CRUD)*
##### *Meeting Create*
- From the navigation menu click *New Meetings*
- Fill out form all fields required 
- Click the "*Add Meeting*" button
![add meeting](/static/images/screenshot_5.png) 

- **Expected Result:** 
    - Directed to Home page and will see new meeting live on the page
    - Success flash message to appear --> "*Meeting Successfully Added*"
- **Defensive Design:** 
    - User will be prompted to fill out required fields and won't be able to submit untill populated

##### *Meetings Read*
- Meeting available to read on Home page
![home](/static/images/screenshot_1.png)

##### *Meetings Edit/Update*
- Meeting creator will have the abilty to edit a meeting
- Navigate to the home page
    - From the navigation menu select *Home* then select the meeting to edit 
    - From the meeting detail in collapsible body select the edit button on the card
- **Expected Result:** 
    - Directed to Edit Meeting page
![edit meeting](/static/images/screenshot_6.png)
 
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
![delete meeting](/static/images/screenshot_2.png)
![delete button](/static/images/screenshot_7.png)

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
![admin nav bar](/static/images/screenshot_8.png)
![manage groups](/static/images/screenshot_9.png)

**Defensive Design:** 
- Only admin can view the groups to protect integrity
 

##### Meeting-Group Create
- On manage groups  page click "*Add Group*" button
- Directed to Add Group page
- Enter new group name and click the "*Add Group*" button

- **Expected Result:** 
    - Directed to Manage Groups page 
    - Success Flash message --> "*New Group Added*"
    - New Group card appears on manage groups page
![add groups](/static/images/screenshot_16.png)

##### *Project-Category Edit/Update*
- On manage groups page click "*Edit*" button on the group card you'd like to edit
- **Expected Result:** - Directed to Edit Group page
- Make edit to group or cancel changes
- **Expected Result:**
    - Directed back to manage group page
    - If changes made flash message --> "*Group Successfully Updated*"
![edit groups](/static/images/screenshot_10.png)

##### *Project-Category Delete*
- On manage groups page click "*Delete*" button on the group card you'd like to remove
- **Expected Result:** 
    - Pop-up modal to ask user to confirm deletion
    - Category deleted from groups
    - User directed back to manage groups page
    - Success Flash message --> "*Group Successfully Deleted*"
![manage groups](/static/images/screenshot_9.png)
![delete button](/static/images/screenshot_7.png)


### Defensive Design Testing

- As detailed above all features have been designed with the consideration to the session user to manage the user actions and visibility
- Navigation menu items have been restricted based on session user

### **Code Validators**

To ensure all code was clean, bug free and most importantly for python PEP8 compliant the following validators were used on the site: 

- [W3C HTML validator](https://validator.w3.org/) to validate CSS code
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) to validate CSS code
- [JSlint](https://jslint.com) to validate jQuery Code
- Pylint to validate Python code

### **Site UI/UX & Browser Compatibility Testing**

- Manual testing was carried out on this site by the developers family members to review the UX and site responsivness
- Chrome dev tools were used to review responsivness on multiple devices:
    - Moto G4
    - Galaxy S5
    - Pixel 2/2 XL
    - iPhone 5/5E/6/7/8/8+/X
    - iPad/Pro
    - Surface Duo
    - Galaxy Fold
- Cross browser testing was also attempted on Chrome, Firefox and Safari
- Chrome Lighthouse report shows site is highly responsive:
![lighthouse](/static/images/screenshot_17.png)

### Fixed Bugs

- Despite requesting that a user registers and logs in, any page was visible in the browser by copying and pasting the full web address.
- Fixed issue by implementing function which required the correct user or admin to have access to certain urls. This directs the incorrect user to an error page.


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
* The site is now successfully deployed.

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

### Code & Content
- [Materialize](https://materializecss.com/) - Used throughout the project mainly for responsive navigation and the collapsible list components.

### Acknowledgements

I would like to extend a special thanks to my Code Institute Mentor Rohit Sharma for kind support and time throughout this project.
Thank you also to the tutors for their support throughout this project.


#### Disclaimer
The content of this website is for educational purposes only.
 
