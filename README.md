
# AltLiebe
![feat6](https://github.com/Mawadda-Kadi/altliebe/assets/151715427/21501f0d-5685-41d5-aea9-296877e1dea1)
- AltLiebe is an online marketplace for vintage and second-hand goods where users can buy and sell items. The project aims to provide a sustainable shopping option by facilitating the reuse of goods.
- "AltLiebe": Meaning "old love" in German, this name evokes the notion of finding new affection for previously owned items.
- This name is designed to be catchy, meaningful, and reflective of the app's purpose and values, specifically tailored to a German-speaking audience interested in sustainability, recycling, and handmade goods.
- "Where Memories Find New Homes." Slogan: Evokes a sense of nostalgia and the continuation of stories associated with the items.
- Here is the Live Site [AltLiebe](https://altliebe-e30d7366fcef.herokuapp.com/)


## User Experience (UX)
- **Strategy**: The goal is to create an intuitive platform for users looking to purchase or sell second-hand items, promoting sustainability.
- **Scope**: Functional requirements include product listings, search functionality, user authentication, and participating in conversations.
- **Structure**: Organized around a user-friendly navigation system to easily browse, add, edit, and manage products.


## User Stories
1. USER STORY: Search by Product title, Seller, description, status,  or Location
As a **site user**,
I can **search for products by their name, seller's username, description, status,  or Location **,
so that I **can find the specific items or sellers I'm interested in more easily **.
### Acceptance Criteria
- When a user enters a search query, the app filters products  based on the input.
- The search results page displays relevant product titles, images, and locations.
- The search functionality is accessible from all pages of the site.

2. USER STORY: View List of Products
As a **site visitor**,
I can **view a list of products with their titles, images,  price, creation date, and location**,
so that I **can quickly browse through what's available**.
### Acceptance Criteria
- The main page and category pages display products with the mentioned details.
- Products are sorted by the most recently added by default.
- Users can navigate through different categories to filter products.

3. USER STORY: View a Single Product and Its Details
As **a site user**,
I can **click on a product to view its detailed information**,
so that I **can learn more about the item before deciding to start a conversation with the seller.**
### Acceptance Criteria
- Clicking on a product in the list opens a detailed view page.
- The detailed view includes all product details, including images, price, description, seller and conversation section.
- the product's availability and status are displayed.

4. USER STORY: Login Ability
As **a new user**,
I can **sign up and log in using my username, and an email address**,
so that I can **participate in selling or starting a conversation with other users**.
### Acceptance Criteria
- New users can register with the required information.
- Returning users can log in with their username and password.
- Errors are clearly communicated for invalid login attempts or registration issues.

5. USER STORY: Logging Out Ability
As a **logged-in user**,
I can **log out of the app**,
so that I **can ensure my account is secure when I'm done using the app**.
### Acceptance Criteria
- A log out option is accessible from main navigation.
- Clicking the log out option securely logs the user out.

6. USER STORY: Editing a Personal Profile
As a **registered user**,
I can **edit my personal profile information**,
so that I **can keep my information up to date**.
### Acceptance Criteria
- Users can access their profile edit page from their profile.
- Users can update their email, location, about_me and profile photo.
- Changes are saved and immediately reflected in the user's profile upon submission.

7. USER STORY: Add Products to Sell
As a **signed-up user**,
I can **add my products to sell them on the app**,
so that **other users can view and start a conversation with me about their interest**.
### Acceptance Criteria
- A "Sell" or "Add Product" option is clearly visible on  main navigation for logged-in users.
- Users can enter product details such as title, description, images, price, and status.
- Once added, the product is immediately listed and visible to other users.

8. USER STORY: Update or Delete Products
As a **seller**,
I can **update my product's details or delete my product**,
so that **my product listings remain accurate and up to date**.
### Acceptance Criteria
- Sellers can access an edit option on their product detail page.
- Sellers can update any product information or delete the products entirely.
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
- Sort options are clearly displayed on product listing pages.
- Selecting a sort option immediately reorders the listings according to the selected criterion.
- The currently selected sort option is highlighted or indicated to the user.

11. USER STORY: Pagination of Product Listings
As a **site user**,
I can **navigate through lists of products using next/previous buttons**,
so that I **can easily browse through large numbers of listings without overwhelming load times**.
### Acceptance Criteria
- Product listings are divided into pages with a set number of items per page.
- Pagination controls allow users to go to the next or previous page and jump to first or last pages.
- The current page is highlighted, and unavailable navigation options are disabled or hidden.

12. USER STORY: Favorite/Wishlist Feature
As a **signed-up user**,
I can **click on an “add to wishlist” button of a product to save it to my wishlist in my profile**,
so that I **can keep track of items I'm interested in buying later**.
### Acceptance Criteria
- Each product listing has an"Add to Wishlist" button.
- Favorited items are accessible through a wishlist section in the user's profile.
- Users can remove items from their wishlist .


## Agile Methodology
- In the development of this project, Agile Methodology was followed, incorporating various practices such as User Story Board in GitHub, manual and automated testing, and Iterative Development.


## Testing
view: TESTING.md
/workspace/altliebe/TESTING.md


## Security Features and Defensive Design
- Input validation and sanitization
- Authentication and authorization
- Data encryption and secure storage
- Error handling and logging


## Features
Here's a brief overview of the main featuers of AltLiebe:

### User Authentication and Authorization:
![feat-1](https://github.com/Mawadda-Kadi/altliebe/assets/151715427/c4921626-cd39-4a43-8a2a-e6effa509d59)
- Users can register for an account, providing a username, email, and password.
- Authentication is implemented for users to securely log in and log out of their accounts.
- Logged-in users have access to additional features such as adding products and initiating conversations.

### Product Management:
![feat2](https://github.com/Mawadda-Kadi/altliebe/assets/151715427/b5d06ef0-3918-47d2-bb25-a7b22db74f20)
- Registered users can add new products to the platform for sale, including details such as title, description,  price, category, and status.
- Additionally, registered users can upload up to six images for each product they add to the platform. This includes one main image and up to five additional images. As users upload images, they can preview them before finalizing the product listing, ensuring that they accurately represent the item being sold.
- Sellers can update or delete their product listings as needed to keep information accurate and up-to-date.
- Products are displayed in a list format, with options to view detailed information and initiate conversations related to specific products.

### Product Listings and Search:
![feat3](https://github.com/Mawadda-Kadi/altliebe/assets/151715427/d157ebc5-d55a-4cf8-b293-773f01a5c0fa)
- The Products page displays a list of products with essential details such as title, image, price, and location.
- Users can search for products by title, seller's username, description, status, or location, improving the discoverability of items.

### Conversation Management:
![feat4](https://github.com/Mawadda-Kadi/altliebe/assets/151715427/38a963fd-676e-4b75-874c-ee2f22e9f887)
- Users can initiate conversations related to specific products to discuss details with sellers or interested buyers.
- Conversation threads are displayed with all messages, allowing only authenticated users to track and manage their communications conveniently.

### Profile Management:
![feat5](https://github.com/Mawadda-Kadi/altliebe/assets/151715427/c1554a73-b425-46d2-b100-2ed927924e21)
- Users have personalized profiles where they can view and edit their personal information, including email, location, and profile photo.
- Registered users can access their wishlist, where they can add or remove items they are interested in buying later.

### Sorting and Pagination:
- Users can sort product listings based on criteria such as date and price, providing flexibility in browsing options.
- Pagination controls allow users to navigate through large numbers of product listings efficiently, reducing load times and improving user experience.

### Error Handling and Messaging:
- Comprehensive error handling is implemented throughout the application to provide clear feedback to users in case of invalid inputs or actions.
- Messages are displayed to users to communicate important notifications, such as successful actions, errors, or prompts for further action.

### Security and Data Integrity:
- User authentication and authorization mechanisms ensure that only authorized users can access certain features and data.
- Data integrity is maintained through validation checks and error handling to prevent issues such as duplicate product titles or empty messages in conversations.




## Deployment - Heroku
To deploy this page to Heroku from its GitHub repository, the following steps were taken:
### Create the Heroku App:
1. Log in to Heroku or create an account.
2. On the main page click the button labelled New in the top right corner and from the drop-down menu select "Create New App".
3. Enter a unique and meaningful app name.
4. Next select your region.
5. Click on the Create App button.
### Attach the Postgres database:
1. In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.
2. Copy the DATABASE_URL located in Config Vars in the Settings Tab.
### Prepare the environment and settings.py file:
1. In your GitPod workspace, create an env.py file in the main directory.
2. Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
3. Update the settings.py file to import the env.py file and add the SECRETKEY and DATABASE_URL file paths.
4. Comment out the default database configuration.
5. Save files and make migrations.
6. Add Cloudinary URL to env.py
7. Add the cloudinary libraries to the list of installed apps.
8. Add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.
9. Link the file to the templates directory in Heroku.
10. Change the templates directory to TEMPLATES_DIR
11. Add Heroku to the ALLOWED_HOSTS list the format ['app_name.heroku.com', 'localhost']
12. Create files / directories
13. Create requirements.txt file
14. Create three directories in the main directory; media, storage and templates.
15. Create a file named "Procfile" in the main directory and add the following: web: gunicorn project-name.wsgi
16. Update Heroku Config Vars
### Add the following Config Vars in Heroku:
1. SECRET_KEY value
2. CLOUDINARY_URL
3. PORT = 8000
4. DISABLE_COLLECTSTATIC = 1
### Deploy:
1. Ensure in Django settings, DEBUG is False
2. Go to the deploy tab on Heroku and connect to GitHub, then to the required repository.
3. Scroll to the bottom of the deploy page and either click Enable Automatic Deploys for automatic deploys or Deploy Branch to deploy manually. Manually deployed branches will need re-deploying each time the repo is updated.
4. Click View to view the deployed site.
5. The site is now live and operational.


## Forking this repository
1. Locate the repository at this link The Easy Eater.
2. At the top of the repository, on the right side of the page, select "Fork" from the buttons available.
3. A copy of the repository is now created.
4. Cloning this repository


## To clone this repository follow the below steps:
1. Locate the repository at this link The Easy Eater.
2. Under 'Code', see the different cloning options, HTTPS, SSH, and GitHub CLI. Click the prefered cloning option, and then copy the link provided.
3. Open Terminal.
4. In Terminal, change the current working directory to the desired location of the cloned directory.
5. Type 'git clone', and then paste the URL copied from GitHub earlier.
6. Type 'Enter' to create the local clone.


## Languages
- Python
- HTML
- CSS
- Javascript


## Frameworks, Libraries, and Programs Used
- Django: Web framework for rapid development and clean, pragmatic design.
- Bootstrap: For responsive design and layout.
- PostgreSQL: As the database backend.
- Cloudinary: For storage of static and media files.
- Chat GPT: For trobleshooting.
- Herokuapp: For deployment.
- GitHub
- Gitpod



## Educational Resources
- Code institute walkthrow model.
- Stack overflow for trobleshooting.


## Credits
- sign up/ login template from [colorlib](https://colorlib.com/wp/free-bootstrap-registration-forms/)
- Carousel for images from [sliderrevolution](https://www.sliderrevolution.com/resources/css-slideshow/)


## Acknowledgements
- I would like to express my sincere gratitude to Anto Rodriguez for his invaluable guidance and support throughout this project.
- I would also like to extend my thanks to Alan from tutoring support for their assistance in resolving an issue during the deployment phase.
