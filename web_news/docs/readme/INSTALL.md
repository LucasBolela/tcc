
## **Prerequisites**
-  **Python 3.9**
-  **Postman**. Download [HERE](https://www.postman.com/downloads/)
-  **SGBD** _(Optional)_. A database management system for PostgreSQL or SQLite
	- I recommend using [DBeaver](https://en.wikipedia.org/wiki/DBeaver). Download [HERE](https://dbeaver.io).
-  **Docker** _(Optional)_ [DOCKER INSTALLATION GUIDE](../apps/INSTALL_DOCKER.md)

-------------------------------------------------------------------------------------------------------------------------------

### **Configure Project**

This project organizes own configuration in this way:

* Project **credentials** (all sensible info) is stored in `.env` file.

Please copy (do not rename) `.env.credentials` to `.env` file:

```bash
$ cd /path/to/core
$ cp .env_example_ .env
```

## **Installation**
1. **Clone the Repository.**
``` bash
$ cd /path/to/core
$ git clone https://github.com/Soruh-Finance/core.git
```
### **Run with VSCode Remote Container**
Use the following commands to install or reinstall Project.
* [https://code.visualstudio.com/docs/remote/containers](https://code.visualstudio.com/docs/remote/containers)

2. Please install the following VS Code extensions:

* Remote Development
* Python
* Docker
* Django

2. On HOST Terminal, run

```bash
$ cd /path/to/core
$ make install
$ docker compose build
```

3. On command-palette select "**Remote-Containers: Rebuild and Reopen in Container**"

### **Run locally with Docker**
2. Build the Container
``` bash
$ docker-compose build
```

3. Start the Container
``` bash
$ docker-compose up -d
```

### **Run locally without Docker**
2.  Create a virtual environment and activate it:
``` bash
$ python -m venv env
$ source env/bin/activate
```

3. Install the required packages:
```
$ make install
```

4. Change the Environment Variable ``` ENV='dev' ``` in the **.env** file. It will setup **SQLite** as Default DB.
```
ENV='dev'
```

5.  Setup the Application (Run Migrations and Run server):
``` bash
$ make setup
```

## **Test**
### **Testing in VSCode:**

* [https://code.visualstudio.com/docs/python/testing#_enable-a-test-framework](https://code.visualstudio.com/docs/python/testing#_enable-a-test-framework)

1. On command-palette select "**Python: Configure Tests**" .
2. Select framework **Pytest** and base folder "."
3. Click "**Run Tests**"

- You can run the Tests running the following command.
```
    make test
```

## Usage
To start using the project, you can create a superuser by running the following command (**Non-mandatory**):
```
    python3 manage.py createsuperuser
```
You can format your code using the following command. It will run the black hook into the project
```
    make format
```
