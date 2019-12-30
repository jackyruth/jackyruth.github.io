# Template HTML Code
Due to the bootstrap dependencies and the ever present navigation bar, every html file has the same start and end code. This template code can be seen in *template_code.html* inside the **design** folder

## The Maintenance Problem
Since every index, about, posts, projects and contact all contains their own version of the template code, if I want to change something about the nav bar, than I need to manually replace the start of every HTML file with the updated nav bar code. This makes the website unmaintainable as the number of html files grow, so does the time it takes to update each file (it is O(n^2) complexity). 

### Plausible solution
If I can somehow factor the start and end of every html file and put them in a *begin.html* and *end.html* file respectively. When I compile the website, if I can make it compile *begin.html* + *content.html* + *end.html* as if it was one HTML file, then I only need to maintain two files, *begin.html* and *end.html*. Here are a few different ways of doing this

1. Change the *.html* file extension to *.php* and use the *include* option [StackOverflow](https://stackoverflow.com/questions/33551409/what-is-the-best-way-to-separate-a-large-html-file-into-three-smaller-html-files)

2. Use jquery javascript and keep the *.html* extension [StackOverflow](https://stackoverflow.com/questions/34238131/how-to-separate-html-text-file-into-multiple-files)

3. Makefiles and Python Scripts to automate the manual labour of changing every html file. 

After a hour or two of looking around, there doesn't appear to be an easy way to do this without using server-side logic. Way number 2 only seems to work for dividing up the body and not the header. 

So Python Scripts it is.

#### 'update_template.py' 

In **scripts**, *update_template.py* python script automatically traverses and updates relevant html files with the altered *template_code.html* . It does this by replacing the code of each relevant html file with the altered code in *template_code.html* It uses **<!-- Page Header -->** and **<!-- Footer -->** to let the script know that it should replace the code above and below respectively. 

The downside is that the top and bottom of every html file must be the same. All the relevant html files are listed in the **metadata** folder under *list_of_html.txt*. Another limitation is that all html files must have the *.html* ending.

*contact.html* is the only html file that has a different footer. Instead of accounting for it in the python script, I removed contact.html from the *list_of_html.txt*. It doesn't take too long to manually update just the contact.html.

**TODO:** The script should ignore the *title* at the top, it would be nice to have a custom title for every page. 

