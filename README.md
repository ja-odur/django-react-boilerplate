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