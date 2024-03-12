# Automated TEST:

The automated testing suite for the Django web application methodically verifies user registration, profile editing, product management, and messaging functionalities, ensuring a seamless and reliable user experience. These tests validate the core features of the application, from account creation and profile customization to product listings and user communication, highlighting the system's robustness and functionality.


## Profile View Test

- **Test Function**: `test_view_own_profile`
- **Objective**: Ensure that logged-in users can access their own profile page.
- **Method**: Calls the `profile_view` function with the username of the logged-in user.
- **Assertions**:
  - Checks if the HTTP response status is 200.
  - Confirms the `own_profile` context variable is `True`.

- **Test Function**: `test_view_other_profile`
- **Objective**: Verify that a user can view another user's profile correctly.
- **Method**: Fetches the profile of a different user created during the test setup.
- **Assertions**:
  - Ensures the HTTP response status is 200.
  - Validates that the `own_profile` context variable is `False`.

- **Test Function**: `test_profile_not_found`
- **Objective**: Ensure the system correctly handles requests for profiles that do not exist.
- **Method**: Attempts to access a profile page using a username that does not exist.
- **Assertions**:
  - Checks if the HTTP response status is 404.


## Product Creation Test

- **Test Function**: `test_product_create_view`
- **Objective**: Test the creation of a new product and associated images through the `ProductCreate` view.
- **Method**:
  - Submits a POST request to the product creation URL with form data for a product and an image.
- **Assertions**:
  - Confirms that the response is a redirect (typically to the product list page, indicating success).
  - Validates that the product was created in the database and is associated with the logged-in user.


## ProductSearchFormTest

- **Test Function**: `test_form_empty`
  - **Objective**: Verify that the search form is valid even with no data input.
  - **Method**: Submits an empty form to evaluate its validity.
  - **Assertions**:
    - Asserts that the form is valid when empty, accommodating a broad search scenario where no specific query is provided.

- **Test Function**: `test_form_with_query`
  - **Objective**: Ensure that the form correctly handles and validates a provided search query.
  - **Method**: Submits the form with a specific search term ('test') and checks the processed data.
  - **Assertions**:
    - Asserts that the form is valid with a non-empty search term.
    - Confirms that the `cleaned_data` contains the exact search term ('test') inputted by the user.

- **Test Function**: `test_form_with_whitespace_query`
  - **Objective**: Test the form's handling of search queries made up of only whitespace.
  - **Method**: Submits the form with a query string that contains only whitespace characters to observe how it is processed.
  - **Assertions**:
    - Asserts that the form is valid, ensuring it can handle and process whitespace-only queries.
    - Checks that the `cleaned_data['query']` is an empty string, indicating whitespace is appropriately stripped from the query.


## `ConversationListViewTest`

- **Setup**:
  - Creates two users (`self.user1` and `self.user2`) and one `seller`.
  - Creates a product associated with the `seller`.
  - Initiates two conversations, each linked to one of the users.


## `ConversationDetailViewTest`

- **Setup**:
  - Creates a `seller` and a regular `user`.
  - Creates a product associated with the `seller`.
  - Initiates a conversation related to the product and adds the regular `user` as a participant.

- **Test Function**: `test_conversation_detail_view`
- **Objective**: Ensure the conversation detail view displays the correct conversation for the logged-in user.
- **Method**:
  - Logs in as `user`.
  - Fetches the conversation detail view for `self.conversation`.
- **Assertions**:
  - Checks that the HTTP response status is 200.
  - Asserts the conversation in the context is the expected one.

- **Test Function**: `test_post_message_in_conversation`
- **Objective**: Verify that a user can post a message in a conversation.
- **Method**:
  - Logs in as `user`.
  - Posts a message to the conversation detail view.
- **Assertions**:
  - Checks that the response status is 302 (indicating a redirect, typically after a successful POST request).
  - Asserts the conversation contains exactly one message, and its text matches the posted message.


# User Story Testing

### User Story: Search by Product Title, Seller, Description, Status, or Location

- **Test Steps**:
  1. Navigate to the search bar accessible from any page.
  2. Enter a search term related to a product's title, seller's username, description, status, or location.
  3. Submit the search query.

- **Expected Results**:
  - The search results page should display products that match the search criteria.
  - Each result should include the product's title, image, and location.

### User Story: View List of Products

- **Test Steps**:
  1. Visit the products or any category page.

- **Expected Results**:
  - The page should list products with titles, images, prices, seller, status, availability, creation dates, and locations.
  - Products should be sorted by the most recent addition.

### User Story: View a Single Product and Its Details

- **Test Steps**:
  1. Click on a product listing to view its details.

- **Expected Results**:
  - The detailed view page should display all product details including images, price, description, seller username, and conversation section.

### User Story: Login Ability

- **Test Steps**:
  1. Navigate to the login/sign-up page.
  2. Enter registration details for a new user or login credentials for an existing user.

- **Expected Results**:
  - New users should be able to register.
  - Existing users should be able to log in.
  - Any errors should be clearly communicated.

### User Story: Logging Out Ability

- **Test Steps**:
  1. Click on the logout option in the main navigation.

- **Expected Results**:
  - The user should be securely logged out of the application.

### User Story: Editing a Personal Profile

- **Test Steps**:
  1. Navigate to the profile edit page.
  2. Update personal information like email, location, about_me, and profile photo.

- **Expected Results**:
  - Changes should be saved and reflected in the user's profile.

### User Story: Add Products to Sell

- **Test Steps**:
  1. Click on the "Add Product" option.
  2. Enter product details and submit the form.

- **Expected Results**:
  - The new product should be listed and visible on the site.

### User Story: Update or Delete Products

- **Test Steps**:
  1. Go to the product detail page and click on the edit or delete button.
  2. Update or delete the product and confirm the action.

- **Expected Results**:
  - Updated product details should be reflected on the site.
  - Deleted products should be removed from listings.

### User Story: Order Items by Preference

- **Test Steps**:
  1. Navigate to the product listing page.
  2. Select a sorting option like date or price.

- **Expected Results**:
  - Listings should be reordered based on the selected sort criterion.

### User Story: Pagination of Product Listings

- **Test Steps**:
  1. View a product listing page with multiple pages of items.
  2. Use pagination controls to navigate through pages.

- **Expected Results**:
  - Users should be able to browse through products on different pages.

### User Story: Favorite/Wishlist Feature

- **Test Steps**:
  1. Click the “add to wishlist” button on a product.
  2. Access the wishlist from the user's profile.

- **Expected Results**:
  - The product should be added to the wishlist.
  - Users should be able to remove items from their wishlist.

### USER STORY: Initiate and View Conversations

- **Objective**: Ensure that registered users can initiate and view conversations related to products, interact within these conversations, and see all messages sorted by date.

#### Pre-conditions
- The tester must have at least two registered user accounts and one product listed on the platform.

#### Test Steps

1. **Initiate Conversation**:
   - Log in as a registered user (User A).
   - Navigate to the product detail page of a product listed by another user (User B).
   - Locate the conversation section that allows initiating a conversation.
   - Start a conversation by entering a message and submitting the form.

2. **View Conversation**:
   - Ensure the conversation thread appears with the sent message.
   - Log out from User A's account and log in as User B.
   - Navigate to the same product's detail page or to a dedicated conversation section in the user profile.
   - Open the conversation initiated by User A and verify that the message is visible.

3. **Post New Message**:
   - As User B, respond to the conversation with a new message.
   - Submit the message and verify it appears in the conversation thread above the initial message.

4. **Check Empty Message Validation**:
   - Try to send an empty message or one consisting of only whitespace.
   - Confirm that the message is not sent and an appropriate error message is displayed.

#### Expected Results
- Conversations can be initiated from product detail pages by logged-in users, linking directly to the product in question.
- All messages within a conversation are displayed in a chronological order, making it easy to follow the dialogue.
- Users can successfully add new messages to an existing conversation.
- Sending an empty message should result in an error, preventing the form submission and informing the user of the mistake.

# Validator Testing

## HTML:
All HTML pages were run through the W3C HTML Validator. See results in below table.

## CSS
No errors were found when passing my CSS file through the official W3C CSS Validator

## JavaScript
No errors were found when passing my javascript through Jshint

## Python
All Python files were run through Pep8 with no errors found.

## Lighthouse
Lighthouse validation was run on all pages (both mobile and desktop) in order to check accessibility and performance.

## Browser Testing
The Website was tested on Google Chrome, Firefox, Safari browsers with no issues noted.

## Device Testing
The website was viewed on a variety of devices such as Desktop, Laptop, iPhone 8, iPhoneXR and iPad to ensure responsiveness on various screen sizes in both portrait and landscape mode. The website performed as intended. The responsive design was also checked using Chrome developer tools across multiple devices with structural integrity holding for the various sizes.

# Mannual Testing:

## Site Navigation
| Element                | Action   | Expected Result               | Pass/Fail |
|------------------------|----------|-------------------------------|-----------|
| Site Name (logo area)  | Click    | Redirect to home              |    Pass   |
| Home Link              | Click    | Redirect to home              |    Pass   |
| Products Link          | Click    | Open Products Page            |    Pass   |
| Login Link             | Click    | Open Login Form               |    Pass   |
| Signup Link            | Click    | Open to Signup Form           |    Pass   |
| Username Link          | Click    | Redirect to Profile Page      |    Pass   |
| Logout Link            | Click    | Redirect to Logout Confirmation|   Pass   |
| Search Bar             | Input    | Display search results        |    Pass   |
|Social Media Links      | Click    | Open links in new Tabs        |    Pass   |
---------------------------------------------------------------------------------

## Home Page
| Element            | Action   | Expected Result                 | Pass/Fail   |
|--------------------|----------|-------------------------------- |-------------|
| Sort Option        | Select   | Sort products based on selection|    Pass     |
---------------------------------------------------------------------------------

## Products Page
| Element            | Action   | Expected Result                |  Pass/Fail   |
|--------------------|----------|--------------------------------|--------      |
| Product Item       | Click    | Redirect to Product Detail     |     Pass     |
| Sort Option        | Select   | Sort products based on selection|  Pass       |
| Seller Link        | Click    | Redirect to seller' profile    |     Pass     |
| Pagination Options | Click    | Navigate to the selected Page  |   Pass       |
---------------------------------------------------------------------------------

## Product Detail Page
| Element                | Action                         | Expected Result                                 | Pass/Fail |
|------------------------|--------------------------------|-------------------------------------------------|-----------|
| Image Fields           | View Images                    | Up to 6 product images are uploaded and shown   |    Pass   |
| Edit Product Link      | Click                          | Navigate to Product Edit Form                   |    Pass   |
| Delete Product Button  | Click and confirm              | Product is deleted and removed from listings    |    Pass   |
| Add to Wishlist Button | Click                          | Product is added to the user's wishlist         |    Pass   |
| Participate in Conversation | Enter Message/Submit      | User can send messages in product conversation  |    Pass   |
| Product Information    | View                           | Detailed view                                   |    Pass   |
| Contact Seller         | Click                          | Open message form to contact seller             |    Pass   |
| Write Review Link      | Click                          | Navigate to review section/form                 |    Pass   |
-------------------------------------------------------------------------------------------------------------------------


## Signup Page
| Element                 | Action                | Expected Result                                    | Pass/Fail |
|-------------------------|-----------------------|----------------------------------------------------|-----------|
| Signup Form             | Fill and submit       | New user account is created                        |    Pass   |
| Username Field          | Input                 | Accepts new username                               |    Pass   |
| Email Field             | Input                 | Accepts valid email address                        |    Pass   |
| Password Field          | Input                 | Accepts password according to policy               |    Pass   |
| Password Confirmation Field | Input             | Accepts password, must match with Password Field   |    Pass   |
| Submit Button           | Click                 | Form is submitted, user is redirected to profile   |    Pass   |
| Error Messages          | Display after submit  | Shows appropriate error messages for invalid inputs|    Pass   |
--------------------------------------------------------------------------------------------------------------------

## Login Page
| Element                 | Action                | Expected Result                                    | Pass/Fail |
|-------------------------|-----------------------|----------------------------------------------------|-----------|
| Login Form              | Fill and submit       | User is logged in                                  |    Pass   |
| Username Field          | Input                 | Accepts existing username                          |    Pass   |
| Password Field          | Input                 | Accepts correct password                           |    Pass   |
| Submit Button           | Click                 | Form is submitted, user is redirected to Profile   |    Pass   |
| Error Messages          | Display after submit  | Shows appropriate error messages for invalid inputs|    Pass   |
--------------------------------------------------------------------------------------------------------------------

## Profile View Page
| Element                 | Action                | Expected Result                                     | Pass/Fail |
|-------------------------|-----------------------|-----------------------------------------------------|-----------|
| Profile Information     | View                  | Display the current user's profile information      | Pass      |
| Edit Profile Button     | Click                 | Navigate to the profile edit form                   | Pass      |
| Logout Profile Button   | Click                 | Navigate to the profile edit form                   | Pass      |
| Delete Account Button   | Click and Submit      | Account is deleted                                  | Pass      |
| Profile Picture         | View                  | Display the current profile picture                 | Pass      |
| Update Information Form | Submit                | Update and reflect the new information on the profile| Pass     |
| Wishlist and Added products| View               | Display Wishlist and added products                 | Pass      |
| Empty Wishlist Message  | View                  | Display a message if the wishlist is empty          | Pass      |
| Empty Products Message  | View                  | Display a message if the My Products is empty       | Pass      |
---------------------------------------------------------------------------------------------------------------------


## WishList Page
| Element                 | Action                | Expected Result                                     | Pass/Fail |
|-------------------------|-----------------------|-----------------------------------------------------|-----------|
| Wishlist Items          | View                  | List all products added to the user's wishlist      | Pass      |
| Remove Item Button      | Click                 | Remove the item from the wishlist                   | Pass      |
| Product Link            | Click                 | Navigate to the product's detail page               | Pass      |
| Empty Wishlist Message  | View                  | Display a message if the wishlist is empty          | Pass      |
---------------------------------------------------------------------------------------------------------------------


## Edit Profile Page
| Element                 | Action                | Expected Result                                     | Pass/Fail |
|-------------------------|-----------------------|-----------------------------------------------------|-----------|
| Email Field             | Edit and submit       | Updated email is saved and displayed                | Pass      |
| About Me Field          | Edit and submit       | Updated about me is saved and displayed             | Pass      |
| Profile Picture Upload  | Upload and submit     | Updated profile picture is saved and displayed      | Pass      |
| Save Changes Button     | Click                 | Changes are saved and user receives confirmation    | Pass      |
---------------------------------------------------------------------------------------------------------------------


## Add Product Page
| Element                          | Action                | Expected Result                                      | Pass/Fail |
|----------------------------------|-----------------------|------------------------------------------------------|-----------|
| Title Field                      | Input                 | Accepts product title                                | Pass      |
| Description Field                | Input                 | Accepts product description                          | Pass      |
| Price Field                      | Input                 | Accepts product price                                | Pass      |
| Main Image Field with Thumbnail  | Upload                | Uploads and displays a thumbnail of the main image   | Pass      |
| Additional Image Fields with Thumbnails | Upload         | Uploads and displays thumbnails of additional images | Pass      |
| Status Selection                 | Select                | Allows selection of product status                   | Pass      |
| Availability Selection           | Select                | Allows selection of product availability             | Pass      |
| Submit Button                    | Click                 | Form is submitted and product is added to listings   | Pass      |
-------------------------------------------------------------------------------------------------------------------------------

## Edit Product Page
| Element                          | Action                | Expected Result                                      | Pass/Fail |
|----------------------------------|-----------------------|------------------------------------------------------|-----------|
| Title Field                      | Edit                  | Updates product title                                | Pass      |
| Description Field                | Edit                  | Updates product description                          | Pass      |
| Price Field                      | Edit                  | Updates product price                                | Pass      |
| Main Image Field with Thumbnail  | Change/Upload         | Updates and displays a new thumbnail of the main image | Pass    |
| Additional Image Fields with Thumbnails | Change/Upload  |Updates and displays new thumbnails for additional images | Pass  |
| Category Selection               | Change                | Updates the prcodut category                         | Pass      |
| Status Selection                 | Change                | Updates the product status                           | Pass      |
| Availability Selection           | Change                | Updates the product availability                     | Pass      |
| Save Changes Button              | Click                 | Form is submitted and product updates are saved      | Pass      |
-------------------------------------------------------------------------------------------------------------------------------

## Delete Product Page
| Element                           | Action                      | Expected Result                                            | Pass/Fail |
|-----------------------------------|-----------------------------|------------------------------------------------------------|-----------|
| Delete Button                     | Click and confirm           | User account is permanently deleted from the system        | Pass      |
--------------------------------------------------------------------------------------------------------------------------------------------

## Logut Page
| Element                           | Action                      | Expected Result                                            | Pass/Fail |
|-----------------------------------|-----------------------------|------------------------------------------------------------|-----------|
| Logout Option                     | Click                       | User is logged out                                         | Pass      |
--------------------------------------------------------------------------------------------------------------------------------------------

## Delete Account Page
| Element                           | Action                      | Expected Result                                            | Pass/Fail |
|-----------------------------------|-----------------------------|------------------------------------------------------------|-----------|
| Delete Account Button             | Click and confirm           | User account is permanently deleted from the system        | Pass      |
--------------------------------------------------------------------------------------------------------------------------------------------

# Bugs

## Fixed Bugs


## Unfixed bugs

