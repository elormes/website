# Code for my website

Hey! Here lies the source for my personal website. The site design was inspired by my love of Japanese ink wash paintings. They rock!

The site pages are authored in markdown and converted into static html pages by a custom python script. I wrote the script over a night, so there is a lot of weird stuff like hardcoded directory paths, etc in it. I would be cleaning up the script and adding features as time goes on. However, I would always prioritize creating site content over improving the script.

## Requirements
* Python
* Linux (I haven't tried building on Windows but it should work)

## How to build
Run the commands below on the command line. Remember not to include the dollar signs :) 

* First check out the repo using
 `$ git clone https://github.com/elormes/website.git`

* You might want to create a [virtual environment](https://realpython.com/python-virtual-environments-a-primer/) before running the next step.
  `$ pip install -r requirements.txt`

* Then
  `$ make`

You can access all the raw html files in the folder named "build" that would appear in the root directory. To get rid of the "build" folder, run `$ make clean`

## License
The content of this site is licensed under the Creative Commons license CC BY 4.0. All illustrations found on the site were taken from [pixabay](https://pixabay.com/) and are licensed under the Creative Commons license. All software in this project is licensed under the MIT license. 
