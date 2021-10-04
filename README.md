# Django-React-Boilerplate

## Prerequisites

-   `Git` [Guide to Git](https://git-scm.com/doc) [Installing Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)
-   `Python 3.6 or higher (Python 3.7 preferred)` [Python Software Foundation](https://www.python.org/)
-   `NodeJs` [Download nodejs](https://nodejs.org/en/download/)
-   `Npm` [NpmJs](https://www.npmjs.com/get-npm)

## Setting up the development environment on OSX

#### HomeBrew

Install homebrew

    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

#### Direnv

Install direnv on your local machine, and set it up so it works
in your shell. These are the instructions for the (default) bash shell. If
you're using a different shell, you probably know where to configure it for
yours or the check the [direnv setup page](https://direnv.net/docs/hook.html) for your shell:

    brew install direnv   # for Macs

Then, add the following line to the end of your shell configuration file as follows:

For BASH, add below to `~/.bash_profile` or `~/.profile`

    eval "$(direnv hook bash)"

For ZSH, add below to `~/.zshrc`

    eval "$(direnv hook zsh)"
    
## Setting up the development Environment on Linux
**_NOTE_**:

Currently the environment does not run well on Windows Bash / WSL ( Windows Subsystem for Linux ).
There are too many issues with line terminators and other environment inconsistencies.

The best option is to run "bare metal" Linux or dual boot. You can run Linux in a VM, but performance will suffer, buyer beware.

#### Direnv

Install direnv on your local machine, and set it up so it works
in your shell. These are the instructions for the (default) bash shell. If
you're using a different shell, you probably know where to configure it for
yours or the check the [direnv setup page](https://direnv.net/docs/hook.html) for your shell:

    sudo apt install direnv   # for Linux

Then, add the following line to the end of your shell configuration file as follows:

For BASH, add below to `.bashrc`

    eval "$(direnv hook bash)"

For ZSH, add below to `.zshrc`

    eval "$(direnv hook zsh)" 
 
    
## Running the Stack
**_NOTE_**:

This is continuation to `MacOS` and `linux` setup above. **Not applicable to `Windows` setup**.

#### Repo setup

Clone the repo

    git clone https://github.com/ja-odur/django-react-boilerplate.git

`cd` into the cloned `django-react-boilerplate` folder

#### Create the `.envrc` and `.env` files

In the `.envrc` file add the following code

    layout python python3.7
    PATH_add node_modules/.bin
    dotenv

In summary, this ensures a python virtual environment is created each time you cd into this directory.
The `PATH` variable is updated with the `node_modules` path and `.env` loaded.

Populate the `.env` file with the following keys and their respective values

    WEB_STATIC_HOST
    SECRET_KEY

Allow `direnv` to load the new changes

    direnv allow .

#### Install both `Python` and `node` requirements

Python requirements

    pip install -r requirements.txt

Node requirements

    npm install

#### Running the website app

Once properly setup, run the following in two separate terminals:

    # Terminal 1
    inv run-web

    # Terminal 2
    inv webpack-server

At this point you should be able to navigate to the local instance at http://localhost:8000/

## Development Invoke Commands

#### Running servers

Running django server

    inv run-web

Running webpack dev-server

    inv webpack-server

#### Lint checks and auto fixing

Running `JS` lint checks

    inv lint-js

Auto fixing `JS` lint issues

    inv prettier-js

#### Static builds

Running `Webpack` build (production)

    inv run-build
