# Testing for Recipe Haven   
  
## Testing Contents  
  
1. [Validation](#validation)
2. [Browser Testing](#browser-testing)
3. [Manual Testing](#manual-testing)
4. [Bugs](#bugs)  
  
  -----
## Validation  
The code was validated using the [Code Institute's](https://pep8ci.herokuapp.com/#) during its development. No errors were found in the final testing, as shown below:
![Pep8 Linter Validation](/documentation/readme/pep8validation.png)


## User Input Validation for Recipe Haven

In Recipe Haven, strong input validation mechanisms are in place to ensure the integrity of user data and deliver a seamless experience. Below are the key validation strategies employed across the application:

### File Size Validation:

    For recipe images uploaded by users, Recipe Haven checks that the file size does not exceed the limit of 10MB. If the image exceeds this limit, users are informed and prompted to upload a smaller file.

### Forms
    
    In Recipe Haven, several input fields are marked as required to ensure that users provide essential information when submitting recipes, comments, or other forms. Below are the key required fields across various forms:
    
#### Recipe Submission Form:

- **Title:** Users must provide a clear and descriptive recipe title. This helps ensure the recipe can be easily identified by others.
- **Image:** A recipe image is required to visually represent the dish. The system prompts users to upload an image that meets the specified file size and format requirements.

#### Comment Submission Form:

- **Body:** Users must provide content when submitting a comment. Empty comments are not allowed, ensuring meaningful engagement on the platform.

#### User Registration Form:

- **Username:** A unique username is required for every user to identify themselves within the Recipe Haven community.
- **Email:** A valid email address is required for user communication and account management.
- **Password:** Users must create a strong password to secure their account. The system enforces password validation to ensure security.

## Browser Testing 
Baker's Heart was tested on the Heroku app website across multiple browsers, including Google Chrome, Mozilla Firefox, and Safari, without encountering any issues.

    