# Recipe Haven

![mock-up images](docs/readme/responsive.PNG "Website preview at different resolutions")

[View The Live Project Here](#) <!-- Add link to live site here -->

## Purpose of the Project
Recipe Haven is a community-driven platform for home-cooked meal recipes. This project provides users with a space to discover delicious recipes, share their own, and engage in discussions with fellow food enthusiasts.

When users visit Recipe Haven, they are welcomed with a homepage that encourages them to explore popular recipes. Registered users can access additional features, such as sharing their own recipes and participating in the comments section.

## Table Of Contents
1. [Introduction](#Introduction)
    1. [Scenario](#Scenario)
2. [UX](#UX)
    1. [User Stories](#User-Stories)
    2. [Design Thinking](#Design-Thinking)
3. [Features](#Features)
    1. [Design Features](#Design-Features)
    2. [Existing Features](#Existing-Features)
    3. [Future Adaptations](#Future-Adaptations)
4. [Issues and Bugs](#Issues-and-Bugs)
5. [Technologies Used](#Technologies-Used)
    1. [Main Languages Used](#Main-Languages-Used)
    2. [Frameworks, Libraries & Programs Used](#Frameworks,-Libraries-&-Programs-Used)
6. [Testing](#Testing)
7. [Deployment](#Deployment)
8. [Credits](#Credits)
9. [Acknowledgements](#Acknowledgements)

---

## Introduction
Recipe Haven

Welcome to Recipe Haven! A community platform where users can discover, share, and explore delicious home-cooked recipes.

### Scenario

In today’s digital age, the joy of cooking and sharing recipes is more accessible than ever. Recipe enthusiasts no longer have to rely solely on printed cookbooks or traditional word-of-mouth sharing. Platforms like Recipe Haven allow users to connect over their love of food, explore new cuisines, and contribute their own culinary creations to a growing collection of recipes.

Consider Recipe Haven as the perfect digital space for home cooks who want to share their favorite family dishes, create new recipes, or simply find inspiration for their next meal. While many may enjoy browsing recipes online, some want to go a step further by contributing their own creations to a community of like-minded food lovers.

Recipe Haven’s user-friendly interface allows individuals to create an account, upload their recipes, and comment on others’ posts, fostering a sense of connection and collaboration in the kitchen. Additionally, the platform caters to both novice and experienced cooks, giving everyone a chance to engage, learn, and share in a space that celebrates all things food.

In a world where time is precious and convenience is key, Recipe Haven gives users the ability to browse and share recipes at any time, from any place. Whether it's a quick dinner idea or a complex holiday meal, the platform offers a wealth of options for any occasion. With these capabilities, Recipe Haven enhances the traditional experience of sharing recipes, bringing it into the modern age of connectivity and digital interaction.

With the above in mind, let's explore Recipe Haven together!

## UX
### User Stories
- As a user, I want to register and log in to share my recipes.
- As a user, I want to edit and delete the recipes I have posted.
- As a user, I want to comment on recipes shared by others and engage with the community.
- As a user, I want to see the most popular or highly-rated recipes.

### Design Thinking
The platform is designed to offer a user-friendly and visually appealing experience. Its simple navigation, clean design, and responsive layout ensure users can easily explore and share recipes.

## Features
### Design Features
- A modern, responsive design that adapts to various screen sizes.
- Flexbox-based layout for recipe cards ensuring consistent alignment.
- Interactive navigation, including a dropdown menu for FAQ and About sections.

### Existing Features
- User registration, login, and profile management.
- Recipe sharing functionality with fields for title, ingredients, methods, and images.
- Commenting and interaction on shared recipes.
- Pagination for browsing recipes.

### Future Adaptations
- Integration of a rating system for recipes.
- Social media sharing buttons to extend the recipe audience.
- Implementation of a search function to filter recipes by ingredients or cuisine types.

## Issues and Bugs
- Resolved issues with recipe form submission.
- Adjusted layout for consistent display of recipe cards.
- Ongoing improvements for mobile responsiveness.

## Technologies Used
### Main Languages Used
- HTML, CSS, JavaScript for frontend development.
- Python (Django) for backend logic.
- SQL (PostgreSQL/MySQL) for database management.

### Frameworks, Libraries & Programs Used
- Django for backend web development.
- Bootstrap for responsive design and layout.
- Cloudinary for image storage.

## Testing
Manual testing was conducted for all key features, including recipe submission, profile management, and commenting functionality. Testing ensures that all components work smoothly on various devices and browsers.

## Deployment
- The application was deployed using Heroku, and the database was configured with PostgreSQL.
- Cloudinary was integrated to manage image uploads for recipes.

## Credits
### Content
- Recipe content was provided by the community and contributors.
  
### People
- Project development and design by [Your Name].

## Acknowledgements
Special thanks to the Recipe Haven community for their contributions and feedback.






##############################################################################################################
#############################################################################################################

[#19](https://github.com/Tenda-M/recipe-haven/issues/19)
[#19](https://github.com/Tenda-M/recipe-haven/issues/19)
![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome Tatenda Mudehwe,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **June 18, 2024**

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py` if your Python file is named `app.py`, of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

By Default, Gitpod gives you superuser security privileges. Therefore, you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you, so do not share it. If you accidentally make it public, you can create a new one with _Regenerate API Key_.

### Connecting your Mongo database

- **Connect to Mongo CLI on a IDE**
- navigate to your MongoDB Clusters Sandbox
- click **"Connect"** button
- select **"Connect with the MongoDB shell"**
- select **"I have the mongo shell installed"**
- choose **mongosh (2.0 or later)** for : **"Select your mongo shell version"**
- choose option: **"Run your connection string in your command line"**
- in the terminal, paste the copied code `mongo "mongodb+srv://<CLUSTER-NAME>.mongodb.net/<DBname>" --apiVersion 1 --username <USERNAME>`
  - replace all `<angle-bracket>` keys with your own data
- enter password _(will not echo **\*\*\*\*** on screen)_

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**June 18, 2024,** Add Mongo back into template

**June 14, 2024,** Temporarily remove Mongo until the key issue is resolved

**May 28 2024:** Fix Mongo and Links installs

**April 26 2024:** Update node version to 16

**September 20 2023:** Update Python version to 3.9.17.

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!

