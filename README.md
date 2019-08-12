# Python and Pandas Workshop

### Schedule

###### Session 1
Aug. 12–16, 6-9 p.m.

###### Session 2
Aug. 19–23, 6-9 p.m.


### Day 1: Install party!

#### iTerm2: Your Terminal
Download from here: https://www.iterm2.com/.

Use this instead of your default terminal. 

###### Some basic terminal commands

1. cd (change directory)
	How it works: ``` cd <directory-name>```
	
	Example: ```cd ~``` (change directory home)
	
	Example: ``` cd ..``` (change directory parent)

2. ls (list)

	How it works: ```ls```

	Example: ```ls -a``` (list hidden files and directories, prefixed with .)

3. touch
	
	How it works: ```touch <filename>```

	Example: ```touch helloworld```

4. cp (copy)
	
	How it works: ```cp <filename> <new-filename>```

	Example: ```cp helloworld helloworld2```

5. rm (remove)
	
	How it works: ```rm <filename>```

	Example: ```rm helloworld2```

6. mkdir (make directory)

	How it works: ```mkdir <directory-name>```

	Example: ```mkdir my-directory```

7. mv

	How it works: ```mv <filename> <directory-name>```

	Example: ```mv helloworld my-directory```

#### Xcode
Run ```xcode-select --install```

#### Homebrew

Run ```/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"```

#### Git and Github

Run ```brew install git```

Check that it's installed using ```git --version```

Then make an account on ```github.com``` if you don't already have one.

##### Setting up Github ssh keys

You want to set up an ssh key so you don't have to type in your username and password when you use it.

https://help.github.com/en/articles/connecting-to-github-with-ssh

#### Zsh
First check if you have Zsh installed. 

```zsh --version```

If you don't run

```brew install zsh zsh-completions```

Then make zsh your default shell

```chsh -s /bin/zsh```

Install Oh My Zsh

```sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"```


#### Sublime

Sublime is a text editor, where you can write your code. Download it from here: https://www.sublimetext.com/3.

Run ```ln -s "/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl" /usr/local/bin/sublime``` to launch Sublime from the command line

Try ```sublime helloworld```. It should open up sublime with your empty file. You can also open an entire directory using this command.


###### Some basic git commands

1. git init
	
2. git add -A

3. git commit -m "your message"

4. git push

5. git clone

#### Installing Python

[Python Wrangler](http://littlecolumns.com/tools/python-wrangler/) might help you if you have previous versions of Python installed and clean them up.

Please use this Python installation [guide](https://docs.google.com/document/d/1cYmpfZEZ8r-09Q6Go917cKVcQk_d0P61gm0q8DAdIdg/edit)

#### Python Part 1
Download this [notebook](https://github.com/lamthuyvo/python-data-nicar2019/blob/master/python1/Python%20intro.ipynb)

Create a directory called ```python-part1```

```cd``` into the directory

Run ```pipenv shell```

```pipenv install jupyter```

```jupyter notebook```

## Some other helpful resources

[How to set up your mac like an interactive news developer](https://open.nytimes.com/set-up-your-mac-like-an-interactive-news-developer-bb8d2c4097e5)


