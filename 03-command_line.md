# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> >
1. pwd- print working directory
2. mkdir- make directory
3. cd - change directory
4. ls- list contents of directory
5. rmdir- remove directory
6. pushd- push directory to a list and change to a new directory, or change between two directories if no arguments
7. popd- pop first directory from list and change to this directory
8. cp- copy a file or directory
9. mv- move a file or directory
10. less- page through a file
11. cat- print whole file in terminal window
12. grep- find things inside files

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> >
ls: list contents of a file or directory <br />
ls -a: list all files <br />
ls -l: display the long format listing <br />
ls -lh: display the long format listing, with human readable file size <br />
ls -lah: list long format including hidden files, with human readble file size <br />
ls -t: display contents in reverse chronological order <br />
ls -Glp: display contents with directories highlighted in blue and files in black <br />

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > 
1. ls -d: displays only directories <br />
2. ls -R: display subdirectories <br />
3. ls -u: display files by file access time <br />
4. ls -m: display names as a comma-separated list -<br />
5. ls -1: display each entry on a line <br />

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs executes some operation by passing a long list of arguments produced by commands like 'find' or 'grep'. This is useful because many Unix systems don't accept long lists of arguments, and xarg can divide such a list into sublists and allow the terminal to execute such a command. An example of how xargs work is you can use it to search for a specific file of a certain type within a specified directory, e.g. finding one's resume in their documents folder:

> > find ./documents -name "*.docx" | xargs grep "resume"

> > the above code finds all documents of type .docx files in the documents directory and below, and then searches through each of these files for the word "resume".



