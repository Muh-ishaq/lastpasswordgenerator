## Docker Image

The first command i had used for Docker is docker image creation

>docker build –t lastpassword .

I.	Base Command to build image.

II.	-t is used to name tags .

III.	Image isTagged lastpassword.

IV.	. means to look for docker file in current directory.

#This command will built an image having name lastpassword using docker file from current Directory.

### NEXT COMMAND RUNNING CONTAINER

To run container the following command is used
>docker run -d -p 8000:8000 --name lastpasswordapp lastpassword

I.	base command to run container.
II.	-d says to run container in detachhed form.
III.	specify the port.
IV.	--name is used to name the container.
V.	Lastpassowrd is image name

### Verification of the image creation can be done by running command 
>docker images
## OUTPUT
lastpassword:latest   d653546bb716        215MB         52.8MB    U

###  TAG THE IMAGE

> docker tag lastpassword:latest ishaq0925/lastpassword:1.0

### PUSH THE IMAGE ON DOCKERK.IO 
To push the image on the docker hub use the following command
> docker push ishaq0925/lastpassword:1.0

### PULL THE IMAGE

now we can pull the image anywhere we want by the command
> docker pull ishaq0925/lastpassword:1.0

#### GIT COMMANDS
>git init
this command is used to initialize a directory as a local git repository
>git status
to show the status of the directory, either the modification made, in stagging stage
>
