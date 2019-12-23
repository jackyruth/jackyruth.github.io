# Template HTML Code
Due to the bootstrap dependencies and the ever present navigation bar, every html file has the same start and end code. This template code can be seen in *template_code.html* inside the **design** folder

## The Maintenance Problem
Since every index, about, posts, projects and contact all contains their own version of the template code, if I want to change something about the nav bar, than I need to manually replace the start of every HTML file with the updated nav bar code. This makes the website unmaintainable as the number of html files grow, so does the time it takes to update each file (it is O(n^2) complexity). 

### Plausible solution
If I can somehow factor the start and end of every html file and put them in a *begin.html* and *end.html* file respectively. When I compile the website, if I can make it compile *begin.html* + *content.html* + *end.html* as if it was one HTML file, then I only need to maintain two files, *begin.html* and *end.html*. Here are a few different ways of doing this

1. Change the *.html* file extension to *.php* and use the *include* option [StackOverflow](https://stackoverflow.com/questions/33551409/what-is-the-best-way-to-separate-a-large-html-file-into-three-smaller-html-files)

2. Use jquery javascript and keep the *.html* extension [StackOverflow](https://stackoverflow.com/questions/34238131/how-to-separate-html-text-file-into-multiple-files)

3. Makefiles and Python Scripts to automate the manual labour of changing every html file. This is messy and prone to error so no thanks