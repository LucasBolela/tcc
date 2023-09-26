# Install Docker
### **Installing Docker - Windows**

- On Windows, first install **WSL2**:
[https://docs.microsoft.com/pt-br/windows/wsl/install-win10](https://docs.microsoft.com/pt-br/windows/wsl/install-win10)
- Then install **Docker Desktop for Windows** using this link:
[https://docs.docker.com/docker-for-windows/install/](https://docs.docker.com/docker-for-windows/install/)
- DO NOT INSTALL docker inside WSL - the Docker Desktop for Windows will
do that.
- Optionally you can install **Windows Terminal** too:
[https://docs.microsoft.com/pt-br/windows/terminal/get-started](https://docs.microsoft.com/pt-br/windows/terminal/get-started)

-------------------------------------------------------------------------------------------------------------------------------
### **Installing Docker - Ubuntu**
#### **Clean install:**

```shell
# New installation
$ curl -fsSL https://get.docker.com -o get-docker.sh
$ sudo sh get-docker.sh
$ sudo usermod -aG docker $USER # then restart bash
$ sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
$ sudo chmod +x /usr/local/bin/docker-compose
```

Do not upgrade an existing docker version, instead remove current docker
installation using this doc:
[https://docs.docker.com/engine/install/ubuntu/](https://docs.docker.com/engine/install/ubuntu/)
and then make a clean install. Make sure you have the latest version
installed.

-------------------------------------------------------------------------------------------------------------------------------
### **Installing Docker - MacOS**
- Go to the Docker website and download the Docker Desktop for Mac: https://www.docker.com/products/docker-desktop
- Once the download is complete, double-click the Docker.dmg file to open it.
- Drag the Docker icon to the Applications folder to install it.
- Open Docker by double-clicking on the Docker icon in the Applications folder.
- You will be prompted to provide your system password to start Docker. Enter your password and click "OK".
- After Docker starts, you will see the Docker whale icon in the menu bar. Click on the icon and select "Preferences" to configure Docker settings.
- From the preferences window, you can configure settings such as the amount of memory and CPU Docker can use, as well as network and other advanced options.
-------------------------------------------------------------------------------------------------------------------------------
