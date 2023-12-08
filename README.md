hi! if you want to run any of these files, you'll need to install reportlab first. i'm pretty sure i just did it globally, but you can create a venv if you want.

the folders are different examples of pdf documents from the videos. the
`main.py` file is mostly an example of moving things around, creating lines and text, etc. it is not necessary to have a `main.py` file, and it was just named that for the first video.

once reportlab is installed, you just need to run the file that contains the actual pdf document you're trying to generate. some of the folders have `temp` files, which are templates. so you want to be in the other file to create the document. you can run it from the terminal, or by hitting the play button in vscode. then, the pdf should appear in your documents folder (as outlined by the my_path variable in those files).

each time you make a change, you need to run the file, then click on the pdf again. a new file isn't created every time; it just refreshes when you click on it.
