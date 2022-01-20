# sm64pclauncher
A launcher for super mario 64 pc port. works on linux apt/pacman based distros and Windows.
![screenshot](https://cdn.discordapp.com/attachments/886701656488697878/919333674229583923/Zrzut_ekranu_z_2021-12-11_22-02-23.png)
## Windows installation
install [python 3](https://www.python.org/downloads/) and [msys2](https://www.msys2.org/), then download the latest release and unpack it, then doubleclick on `installdepends.bat`.
## Usage
### Running on Windows
doubleclick  on `launcher.py`
### Using it
To build sm64, press "Build"  
To play, select existing build and click "Play"  
## How to build
If you are on windows, you should see a window prompting to select the msys2 folder. Basicallly you need to select the folder where you installed msys2. If you are building for the first time or reinstalled msys2, check install msys2 dependencies. (Default Folder: `C:/msys64`)
In the first input box, paste github repository of any sm64pc, and in the box next to the first one type the branch (For Archipelago enter `archipelago`)
In the second box, type any name you want for your repo folder. it will display like that in the launcher build selection.
In the other two boxes you can specify modelpack and texture pack folder. Note: when you browse for the folder, you have to be in this folder to select it.  
Click "Ok". it will freeze for a while this is because it is downloading the repo.  
Click "Browse" and find your Super Mario 64 USA rom. Click "Ok"  
Specify the build flags, you can find which build flags are avaible for your repo by cheking the makefile or checking your repo's wiki if it exists. Remember to add "-jn" where `n` is your amount of cores for faster building speed.  
Click "Build". Now wait patiently for the build to finish. The Program may apper to have crashed, but don't close it, it's probably working.
After it's finished, the program will close. Start the launcher again, select the build and set the launch options. Then you can press play to start
