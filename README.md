# ILearn - ENV SETUP


## Index

1. [Environment Setup](#1-environment-setup)
2. [Important commands](#2-commands)
3. [Github commands](#3-github-commands)
4. [Todo list](#4-todo-list)

## 1. Environment Setup

This project uses the following tools:
- [Poetry](https://python-poetry.org/docs/) for Python dependency management.
- [Pipx](https://pypa.github.io/pipx/) for installing Python CLI tools.
- [Make](https://www.gnu.org/software/make/) for running commands.
- [Ruff](https://github.com/astral-sh/ruff) for python linting and stiling.
- [Black](https://github.com/psf/black) for python code formatting.
- [Pre-commit](https://pre-commit.com/) for git hooks.


### 1.0 Basic Setup

As the selected IDE we are going to use [VSCode](https://code.visualstudio.com/download)

---

Install [git](https://git-scm.com/download) as a distributed version control system that tracks versions of files. This will allow us to interact with the github repo.

For **Mac** or **Linux** os.
```bash
brew install git
```

For **Windows** os.
```bash
brew install git
```

**If you dont have brew or scoop installed, check out the first step in the section 1.1**

---

Clone the repo or donwload it manually.
```bash
git clone https://github.com/username/repository_name.git
```

### 1.1 Setup (installation)

Install [Homebrew](https://brew.sh/index) if you are using **Mac** or **Linux** os.

```zsh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

If you are using **Windows**, install [Scoop](https://scoop.sh/)
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
```
---

Install [pipx](https://pypa.github.io/pipx/).

**Mac** or **Linux** os:
```zsh
brew install pipx
pipx ensurepath
```

**Windows**:
```bash
scoop install pipx
pipx ensurepath
```

---

Install [Poetry](https://python-poetry.org/docs/):
```zsh
pipx install poetry
```

---
Install [Pre-commit](https://pre-commit.com/)

```bash
pipx install pre-commit
```
---

Install [make](https://www.gnu.org/software/make/) only needed for **Windows**.
```bash
scoop install make
```
Linux and Mac typically include make in the OS.

---

Then we ne to install two extensions for [VSCode](https://code.visualstudio.com/):

1. [Ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff) by Astral Software.
2. [Black Formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter) by Microsoft.

Then add the following into your user settings.json by:

1. Open VSCode
2. Navigate to preferences
    - Mac/Linux: Code > Preferences > Settings
    - Windows: File > Preferences > Settings
3. Open settings.json by clicking on the button in the upper right corner of the settings tab `Open Settings (JSON)` icon. This opens the `settings.json` file where you can manually edit settings.
4. Add the following python configuration while mantaining a valid JSON file.
    ```json
        "[python]": {
            "editor.formatOnSave": true,
            "editor.codeActionsOnSave": {
                "source.fixAll": true,
                "source.organizeImports": true
            },
            "editor.defaultFormatter": "ms-python.black-formatter"
        },
    ```
5. Save the `settings.json` file.

---

Run the project setup, this command creates the environment and installs all the dependencies:
```zsh
make setup
```

Then you can activate the environment anytime:
```zsh
make activate
```

### 1.2 Environment Setup (Initial Creation, DO NOT RUN)
This section details the steps taken to set up the environment for the first time. **Only follow these steps if you intend to create a new environment from scratch.**

1. Install Hombrew
2. Install Pipx
3. Install Poetry
4. Install Make
5. Install pre-commit
6. Install Ruff and Black. Then modify the settings.json
7. Create a makefile with the following commands
    ```text
    setup:
        poetry install
        poetry run pre-commit install
        echo "OPENAI_API_KEY=" > .env

    activate:
        poetry shell
    ```
8. Create the Poetry project by running `poetry init` in the root folder. This will start an interactive prompt to set up the project. You can just press `Enter` to accept the default values or fill them out as needed. I recommend you to input the desired python version in this process, the dependencies can be added later. Also you would need to add the rules for the formatter at the end of the file:
    ```text
    [tool.ruff.lint]
    select = ["E4", "E7", "E9", "F", "N801", "N802", "N804", "N805"]
    ignore = ['E501', 'N803']
    ```
9. Add dependencies to the project. For example the package `<package_name>`:
    - For important dependencies use `Poetry add <package_name>`
    - For dependencies only use in development (research, code formatting, etc.) use `Poetry add --group dev <package_name>`
10. Create `.pre-commit-config.yaml` with the following content:
    ```yaml
    repos:
    -   repo: https://github.com/pre-commit/pre-commit-hooks
        rev: v4.5.0
        hooks:
        -   id: check-yaml
        -   id: check-json
        -   id: check-toml
        -
            id: end-of-file-fixer
            exclude: '.vscode/.*'
        -   id: trailing-whitespace
        -   id: detect-private-key
        -   id: requirements-txt-fixer
    - repo: https://github.com/astral-sh/ruff-pre-commit
    # Ruff version.
    rev: v0.4.5
    hooks:
        # Run the linter.
        - id: ruff
        types_or: [ python, pyi, jupyter ]
        args: [ --fix ]
        # Run the formatter.
        - id: ruff-format
        types_or: [ python, pyi, jupyter ]
    ```
11. Run `make setup`

## 2. Commands

This section explains all the important commands that can be run in this proyect. At the moment we are only using makefile so can find all the explanations to all the actions in the makefile. In the future we could add `dvc` to define several pipelines, in that case we would update this section.

1. Run the project setup, this command creates the environment and installs all the dependencies. Ideally this only needs to be executed the first time:
    ```zsh
    make setup
    ```
2. Activate the environment:
    ```zsh
    make activate
    ```
3. To add a new dependency to the project use:
For dependencies only use in development (research, code formatting, etc.):
    ```zsh
    poetry add --group dev <package_name>
    ```

    For important packages that will be needed in production:
    ```zsh
    poetry add <package_name>
    ```
    For example, a dev dependency could be the `notebook` package. A prod dependency could be the `pandas` package.

4. After any modification to `pyproject.toml` run the following command:
    ```zsh
    poetry install
    ```
## 3. GitHub Commands

GitHub commands revolve around the `git` version control system, which allows you to manage changes to your project over time. Below are some basic `git` commands you'll frequently use when working with GitHub.

A more in-deepth guide (revert local commit, manage branches, etc.) can be found in the file [git_guide.md](/git_guide.md).

You can use tools like [lazygit](https://github.com/jesseduffield/lazygit) or the [VScode git source control](https://code.visualstudio.com/docs/sourcecontrol/overview) as an alternative.

To install lazygit in Linux/Mac OS use:
```bash
brew install lazygit
```
For Windows:
```bash
# Add the extras bucket
scoop bucket add extras

# Install lazygit
scoop install lazygit
```

### 3.1 Usual workflow

1. **Check Repository Status (VERY USEFUL, EXECUTE IT BEFORE ANY OTHER ACTION)**
    To see the status of your repository, including changes that have been staged, changes that haven’t been staged, and files that aren’t being tracked by Git:

    ```bash
    git status
    ```
    By running this command before a pull or push operation we can be notified of any other changed in the repo that would cause collisions or other problems.

2. **Pull Changes from GitHub (Also very important, use before any change)**
   To pull the latest changes from a remote repository:
   ```bash
   git pull
   ```
   This command updates your local repository with changes from the remote `<branch-name>`.
   ```bash
   git pull origin <branch-name>
   ```

3. **Add Changes to the Staging Area**
   To add changes to the staging area so they can be committed, use:

   ```bash
   git add <file>
   ```
   Do not add multiple files (e.g. all the files in a folder) at once, this can lead to problems.

4. **Commit Changes**
   To save your staged changes to the repository’s history:

   ```bash
   git commit -m "Your commit message here"
   ```

5. **Push Changes to GitHub**
   To push your committed changes to a remote repository like GitHub:
   ```bash
   git push
   ```
   This command pushes changes to the specified `<branch-name>` of the remote repository named `origin`.
   ```bash
   git push origin <branch-name>
   ```


---

### 4. TODO List

#### **Project Setup**
- [x] Install necessary software and tools (Python, Git, brew/scoop, etc.).
- [x] Define environment (Poetry, pix, code formatter, make, etc).
- [ ] Consider using DVC.
- [ ] Set up remote storage for DVC (e.g., AWS S3).

#### **Development**
- [ ] Scrapper.
- [ ] Create accurate tender data model.
- [ ] DB.
- [ ] Extract info with function calling.
- [ ] Tender chat.

#### **Documentation and Reporting**
- [x] Write comprehensive project installation guide.

#### **Miscellaneous**










# TTS MODEL SELECTION
Thhe main options were the following:
    - ElevenLabs (LIMITED CREDITS) (TOO EXPENSIVE)
    - Coqui [SELECTED] (CLOSED)
    - Deepgram's Aura (good for real-time)
    - WellSaid Labs (good for voice personalization)
    - OpenAI's tts (limited input)
