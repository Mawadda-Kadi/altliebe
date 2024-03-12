
# AltLiebe
- AltLiebe is an online marketplace for vintage and second-hand goods where users can buy and sell items. The project aims to provide a sustainable shopping option by facilitating the reuse of goods.
- "AltLiebe": Meaning "old love" in German, this name evokes the notion of finding new affection for previously owned items.
- This name is designed to be catchy, meaningful, and reflective of the app's purpose and values, specifically tailored to a German-speaking audience interested in sustainability, recycling, and handmade goods.
- "Where Memories Find New Homes." Slogan: Evokes a sense of nostalgia and the continuation of stories associated with the items.

## User Experience (UX)
- **Strategy**: The goal is to create an intuitive platform for users looking to purchase or sell second-hand items, promoting sustainability.
- **Scope**: Functional requirements include product listings, search functionality, user authentication, and participating in conversations.
- **Structure**: Organized around a user-friendly navigation system to easily browse, add, edit, and manage products.
- **Skeleton**: Wireframes and flowcharts were used to design the interface focusing on simplicity and usability.


## User Stories
1. USER STORY: Search by Product title, Seller, description, status,  or Location

As a **site user**,

I can **search for products by their name, seller's username, description, status,  or Location **,

so that I **can find the specific items or sellers I'm interested in more easily **.



### Acceptance Criteria

When a user enters a search query, the app filters products  based on the input.

The search results page displays relevant product titles, images, and locations.

- The search functionality is accessible from all pages of the site.

2. USER STORY: View List of Products

As a **site visitor**,

I can **view a list of products with their titles, images,  price, creation date, and location**,

so that I **can quickly browse through what's available**.



### Acceptance Criteria

The main page and category pages display products with the mentioned details.

Products are sorted by the most recently added by default.

- Users can navigate through different categories to filter products.

3. USER STORY: View a Single Product and Its Details

As **a site user**,

I can **click on a product to view its detailed information**,

so that I **can learn more about the item before deciding to start a conversation with the seller.**



### Acceptance Criteria

Clicking on a product in the list opens a detailed view page.

The detailed view includes all product details, including images, price, description, seller and conversation section.

- the product's availability and status are displayed.

4. USER STORY: Login Ability

As **a new user**,

I can **sign up and log in using my username, and an email address**,

so that I can **participate in selling or starting a conversation with other users**.



### Acceptance Criteria

New users can register with the required information.

Returning users can log in with their username and password.

- Errors are clearly communicated for invalid login attempts or registration issues.

5. USER STORY: Logging Out Ability

As a **logged-in user**,

I can **log out of the app**,

so that I **can ensure my account is secure when I'm done using the app**.



### Acceptance Criteria

A log out option is accessible from main navigation.

Clicking the log out option securely logs the user out.



6. USER STORY: Editing a Personal Profile

As a **registered user**,

I can **edit my personal profile information**,

so that I **can keep my information up to date**.



### Acceptance Criteria

Users can access their profile edit page from their profile.

Users can update their email, location, about_me and profile photo.

- Changes are saved and immediately reflected in the user's profile upon submission.

7. USER STORY: Add Products to Sell

As a **signed-up user**,

I can **add my products to sell them on the app**,

so that **other users can view and start a conversation with me about their interest**.



### Acceptance Criteria

A "Sell" or "Add Product" option is clearly visible on  main navigation for logged-in users.

Users can enter product details such as title, description, images, price, and status.

- Once added, the product is immediately listed and visible to other users.

8. USER STORY: Update or Delete Products

As a **seller**,

I can **update my product's details or delete my product**,

so that **my product listings remain accurate and up to date**.



### Acceptance Criteria

Sellers can access an edit option on their product detail page.

Sellers can update any product information or delete the products entirely.

- Changes are immediately reflected, and deleted products are removed from the site.

9. USER STORY: Initiate and View Conversations
As a **registered user**,

I can **initiate a conversation related to a product**,

so that I **can discuss details with the seller or interested buyers and track all my conversation threads**.

### Acceptance Criteria

- The conversation feature is accessible only to logged-in users to ensure privacy and security.
- The conversation section should list all messages in the conversation, sorted by date.
- Users can post new messages within the conversation thread.
- An appropriate error message is displayed if the user tries to send an empty message.

10. USER STORY: Order Items by Preference

As a **site user**,

I can **order the list of items by date, and price**,

so that I **can easily find items that match my preference**.



### Acceptance Criteria

Sort options are clearly displayed on product listing pages.

Selecting a sort option immediately reorders the listings according to the selected criterion.

- The currently selected sort option is highlighted or indicated to the user.

11. USER STORY: Pagination of Product Listings

As a **site user**,

I can **navigate through lists of products using next/previous buttons**,

so that I **can easily browse through large numbers of listings without overwhelming load times**.



### Acceptance Criteria

Product listings are divided into pages with a set number of items per page.

Pagination controls allow users to go to the next or previous page and jump to first or last pages.

- The current page is highlighted, and unavailable navigation options are disabled or hidden.

12. USER STORY: Favorite/Wishlist Feature

As a **signed-up user**,

I can **click on an “add to wishlist” button of a product to save it to my wishlist in my profile**,

so that I **can keep track of items I'm interested in buying later**.



### Acceptance Criteria

Each product listing has an"Add to Wishlist" button.

Favorited items are accessible through a wishlist section in the user's profile.

Users can remove items from their wishlist .

Agile Methodology
Data Model
## Testing
view: TESTING.md

## Security Features and Defensive Design
- Input validation and sanitization
- Authentication and authorization
- Data encryption and secure storage
- Error handling and logging
Features
Deployment - Heroku
To deploy this page to Heroku from its GitHub repository, the following steps were taken:

Create the Heroku App:
Log in to Heroku or create an account.
On the main page click the button labelled New in the top right corner and from the drop-down menu select "Create New App".
Enter a unique and meaningful app name.
Next select your region.
Click on the Create App button.
Attach the Postgres database:
In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.
Copy the DATABASE_URL located in Config Vars in the Settings Tab.
Prepare the environment and settings.py file:
In your GitPod workspace, create an env.py file in the main directory.
Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
Update the settings.py file to import the env.py file and add the SECRETKEY and DATABASE_URL file paths.
Comment out the default database configuration.
Save files and make migrations.
Add Cloudinary URL to env.py
Add the cloudinary libraries to the list of installed apps.
Add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.
Link the file to the templates directory in Heroku.
Change the templates directory to TEMPLATES_DIR
Add Heroku to the ALLOWED_HOSTS list the format ['app_name.heroku.com', 'localhost']
Create files / directories
Create requirements.txt file
Create three directories in the main directory; media, storage and templates.
Create a file named "Procfile" in the main directory and add the following: web: gunicorn project-name.wsgi
Update Heroku Config Vars
Add the following Config Vars in Heroku:

SECRET_KEY value
CLOUDINARY_URL
PORT = 8000
DISABLE_COLLECTSTATIC = 1
Deploy
NB: Ensure in Django settings, DEBUG is False
Go to the deploy tab on Heroku and connect to GitHub, then to the required repository.
Scroll to the bottom of the deploy page and either click Enable Automatic Deploys for automatic deploys or Deploy Branch to deploy manually. Manually deployed branches will need re-deploying each time the repo is updated.
Click View to view the deployed site.
The site is now live and operational.

Forking this repository
Locate the repository at this link The Easy Eater.
At the top of the repository, on the right side of the page, select "Fork" from the buttons available.
A copy of the repository is now created.
Cloning this repository
To clone this repository follow the below steps:

Locate the repository at this link The Easy Eater.
Under 'Code', see the different cloning options, HTTPS, SSH, and GitHub CLI. Click the prefered cloning option, and then copy the link provided.
Open Terminal.
In Terminal, change the current working directory to the desired location of the cloned directory.
Type 'git clone', and then paste the URL copied from GitHub earlier.
Type 'Enter' to create the local clone.
Languages
Python
HTML
CSS
Javascript


Credits
- code institute walkthrow model
- stack overflow for trobleshooting
- chat GPT for trobleshooting
- sign up/ login template https://colorlib.com/wp/free-bootstrap-registration-forms/
- Carousel for images https://www.sliderrevolution.com/resources/css-slideshow/
