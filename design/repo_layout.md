# Repo Tree Structure

## Location and purpose of all files
### Template files
These files are required to render to the template. They are all in the root directory

**FOLDERS**
1. css folder: contains the css template file
2. img folder: contains the major background images of the website
3. js  folder: contains js files for interactive elements and contact form
4. mail folder: contains php file for the contact page
5. node_modules folder: a bunch of files
6. scss folder: a bunch of files
7. vender folder: contains bootstrap, jquery and fontawesome-free

**FILES**
Most of the files in the root directory originate from the template, although the code within may have been modified. We will only talk of the important files here

1. index.html: handles the *HOME* page. 
	* This file must stay in the root directory and must be named *index.html* as that is what the web server will display
2. about.html: handles the *ABOUT* page. 
	* This file is in the **about** folder
3. projects.html: handles the *PROJECT* page
	* This file is in the **projects** folder
4. posts.html: handles the *POSTS* page 
	* This file is in the **posts** folder
5. contact.html: handles the *CONTACT* page
	* This file shall remain in the root directory due to its extra dependencies and the fact that it will not be regularly changed
6. a_post.html: template code that handles regular blog post pages
	* This file is in the **posts** folder
7. a_project.html: template code that handles regular project pages
	* This file is in the **projects** folder

### The Pathing Problem
I would like to move all the *.html* files above into their own seperate folders under the common folder *content*. However the relative path references used for the bootstrap and the nav bar makes changing the pathing non-trivial

**Solution**: Super simple solution that hits all the boxes is to use the root relative path "/". All the 'main' html files such as the *projects.html* shall use this root relative path. All sub html files such as *my_project_1.html* shall be in the **projects** folder and it shall use relative pathing (not root relative).
