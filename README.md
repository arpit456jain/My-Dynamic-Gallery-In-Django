# My-Dynamic-Gallery-In-Django


## 🚀 Quick Start :

#### Step 1: Forking the repository :

To work on an open-source project, you will first need to make your copy of the repository. To do this, you should fork the repository and then clone it so that you have a local working copy.

Get your own Fork/Copy of repository by clicking `Fork` button right upper corner.<br><br>

#### Step 2: Clone the Forked Repository

After the repository is forked, you can now clone it so that you have a local working copy of the codebase.

To make your local copy of the repository follow the steps:
- Open the Command Prompt
- Type this command:
  
```bash
$ git clone https://github.com/<your-github-username>/pixelvibe
```


#### Step 3: Creating a new branch (IMP)
This is one of the very important step that you should follow to contribute in Open Source. A branch helps to manage the workflow, isolate your code and does not creates a mess. To create a new branch:
  
```bash
$ git branch <name_of_branch>
$ git checkout -b <name_of_branch>
```

Keep your cloned repo upto date by pulling from upstream (this will also avoid any merge conflicts while committing new changes)
```bash
git pull origin main
```

#### Step 4: Setting up Project

##### For Django:
**1. Create a Virtual Environment**

- *On macOS and Linux:*
  ```bash
    python3 -m venv env
  ```
- *Windows*
  ```bash
    py -m venv env
  ````

**2. Activate the Virtual Environment**
  - *On Windows*
    ```bash
    .\env\Scripts\activate
    ```
  - *On macOS and Linux:*
    ```bash
    source env/bin/activate
    ```

**3. Install dependencies using**
```bash
pip install -r requirements.txt
```

**4. Make Migrations**

```bash
  python manage.py makemigrations
  python manage.py migrate
```
**5. Run Server**

```bash
  python manage.py runserver
```
**6. Create admin**

```bash
  python manage.py createsuperuser
```

**5.** Go to ` http://127.0.0.1:8000/` and enjoy the application.
 
**To Run application using Docker**
First of all we will create a image using this command
```bash
docker build -t mydyanmic .
```
here mydyanmic is image name you can type any other name too
so Your image is build now you have to run it using this command.
```bash
docker run -d -p 8000:8000  mydyanmic 
```
Here also mydyanmic is the name of image we build earlier.
 
Now you will be able to access it on localhost:8000
Also to view all the running processes in your system you can do.
```bash
docker ps -a
```

**Using docker-compose to run this**
To run this application in dockerized environment run this command
```zsh
docker-compose up  --> to run
docker-compose down --> to stop
```
Now after running this application with docker-compose up
you can visit localhost:8000 and access this application on your browser.


