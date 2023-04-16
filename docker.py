# Docker ia a service for launching application in container!

# single purpose - one purpose ia a one container
# Docker components:
# - client
# - demon (service)
# - host
# - container
# - image
# - repository
# - registry

# if container doesn't have active process docker will close this container  !!!!!!!!!
#
# image consists of layers, basic layer and others.
# Images are read-only
# Images are saved in repository
# in one repository saved only one image with different versions


# ---------------------------         main commands    ------------------
# docker ps -a   show list of all containers
# docker ps -l   show the latest created container (includes all states)
# docker ps -q   show only ids of containers
# docker ps --format=$FORMAT     show containers by format
# docker version   show info about docker client and docker server
# docker run <image>  create container based on current image
# hostname -i   show ip
# ping <site name or ip> v check available connection to internet

# docker search <name of image>       search image in registry with different version

# docker rmi <name or id of image>    will remove image

# docker container prune      will delete all stopped containers  !!!!!!!!

# docker run -d <image name>    flag -d detached , background mode!!

# docker container inspect <id or name of container>

# docker stop <id or name of container>   or    docker kill  <id or name of container>          stop container

# docker exec -it <id or name of container> <name of process for ex bash>    execute process in container

# docker run -d --name <myContainerName> <name of image>     will create container with our name

# docker attach <container name>    will attach to detached container

# ctrl+p or ctrl+q    will jump out from attached container

# ctrl+d   will stop container

# docker run -p 8080:80 nginx       mapping of ports  where -p  publishing port, 8080 outer port, 80 port of container,
# nginx - name of image,  0.0.0.0:8080->80/tcp tell me that I can use any free port including localhost

# docker run -v ${PWD}:/usr/share/nginx/html nginx      -v means volume, ${PWD} -  path to local folder,
# /usr.... - path to folder inside of container    nginx name of image    , mapping of volumes

# docker run --rm -ti --name test1 -v /Users/dmitriyshypilov/docker_test:/inside_container ubuntu:14.04 bash    where
# /inside_container directory inside container which bundled with directory outside container, files shared between two
# directories. !!!!!! files must exists before sharing between containers

# docker run -ti -v /dir_inside_container --name test1_container ubuntu bash        create volume inside container
# docker run -ti --volumes-from test1_container ubuntu bash           share volumes from container test1_container

# docker run -it --rm busybox    --rm automatically remove container after container will be stopped

# docker run --rm -ti  ubuntu bash -c 'sleep 5; echo all done' will remove container after it will be stopped , flag -c
# will execute command in quotes

# docker run -it /
# --rm busybox    carry command on the new line

# docker build . -f <name docker file> -t imageName:version tag   . use in current directory, -f use docker file name,
# if standard  name Dockerfile we don't use flag -f, -t use when we want give name of our image :2.3  version of image

# docker commit <id container>    will create image based on container with id including all files and changes in it!!!

# docker tag <id image>  new_name     will give name to image with pointed id

# docker commit <name of containers>  <name of new image>   will create a new image based on container and give it name

# docker run -p outside port: inside port / protocol type (tcp or udp), docker dynamically determines port
# docker run -ti -p 45111/udp ubuntu:14.04 bash
# nc -ulp 45111      udp listen port 45111
# nc -u localhost <name of port >   on local machine outside of container

# docker run --rm -ti -p 45111:45111 -p 45112:45112 --name testing-port ubuntu:14.04
# nc -lp 45678 | nc -lp 45679      -lp listen port ,  So that means that data will get passed into our system on one
# port and then spit out on another port.
# nc localhost 45678      will expose port 45678 on computer
#  The Netcat utility is a great network debugging program for just moving bits from one place to another. It's super
#  simple and a good way to show off networking without having to get concerned with anything else like starting a web
#  server.
# docker run -ti -p 45111 --name test-container-name ubuntu:14.04 bash    I'm specifying only the port as seen from
# inside the container.

# docker port <test-container-name or id>    to get assigned to the available port

# docker build -t <name of image> .     -t will give name

# -------------------- docker network ----------------
# docker network ls    will show all existing network of docker by default
#  - Bridge is the network used by containers that don't specify a preference to be put into any other network.
#  - Host is when you want a container to not have any network isolation at all. This does have some security concerns.
#  - And none is for when a container should have no networking.
#
#                   example 1
# docker network create <learning >   will create new network with name learning
# docker run --rm -ti --net learning --name catserver ubuntu:14.04 bash      will create container with name catserver
# and connect to network that we have created
# nc -lp 1111
# docker run --rm -ti --net learning --name dogserver ubuntu:14.04 bash
# nc catserver 1111     will communicate with both containers

# docker network connect <name of network> <name of container>

# ----------------    Dockerfile  statements----------------
# FROM  ubuntu as builder    from what image we should start
# ......
# FROM alpine
# COPY --from=builder /google-size  /google-size     Then down here, I'm going to add another from, from alpine. I'm
# going to call copy --from=builder, which is just the name I assigned above, /google-size, and I want to copy it to
# the same path in this new image, google-size, okay? Save, now let's run that again. I'm going to rebuild it. This time
# I'll call it google-size.

# MAINTAINER Firstname Lastname <email@example.com> defines author of this Dockerfile

# RUN apt-get -y update   ,run command and safe result
# RUN apt-get -y install curl   can be few commands RUN
# RUN curl https://google.com | wc -c > google-size     Now we're going to run an example project that just calls curl
# https://google.com and pipe the output to word count, wc. It just counts words. - C to count the number of characters
# and we're going to save that into a build artifact called google-size. So this just pre-calculates at build time how
# big is the Google homepage in characters.

#

# ADD run.sh  /run.sh     adds local file
# ADD project.tar.gz   /install/       adds the contents of tar archive and uncompress
# ADD http://project.exaple.com/download/1.0/project.rpm   /project/   work with URL as well, download in

# ENV DB_HOST=db.production.example.com      The Environment statement sets environment variable both for the duration
# ENV DB_PORT=5432                           of the Dockerfile

# ENTRYPOINT    specifies the start of the command to run, The `ENTRYPOINT` statement is for making your containers look
# like normal programs.

# CMD           specifies the whole command to run
# Shell form looks like this     nano notes.txt
# Exec form looks like this      ["/bin/nano", "notes.txt"]
#
# EXPOSE 8080     maps port into the container

# VOLUME  ["/shared-data", "/host/path/"] defines shared volumes or ephemeral volumes, depending on whether you have one or two arguments.

# WORKDIR /install/         The WORKDIR statement sets the directory both for the remainder of the
# Dockerfile and for the resulting container when you run it. It's like typing CD at the beginning of every run
# expression after that, so it's a useful expression to know about. You say WORKDIR /install, then all the rest of your
# run statements will happen in the install directory.

# USER Dmitriy or 100    sets which user the container will run as

#  ---------------        legacy linking     -------------------
# docker run --rm -ti -e SECRET=secret_word --name catserver ubuntu:14.04 bash      flag -e will add env variable SECRET

# docker run --rm -ti --link catserver --name dogserver  ubuntu:14.04 bash     flag --link  will link container with
# catserver container.   !!!!!!! link working only in one direction, dogserver will see env variable of catserver,
# catserver will not see env of dogserver

#  -------------            docker-compose.yml    ---------------------------
#  Environment variables do persist across lines if you use the ENV command to set them. Just remember that each line
#  in a Dockerfile is its own call to docker run, and then its own call to docker command.
#                       example lists in yml format
# fruits:
#   - apple
#   - banana
#   - orange

#                   example vocabulary in yml format
# pen:
#   color: yellow
#   model:
#       material: plastic
#   price: 2


# version: '3'

# services:
#   app:                      will create service of our app
#     build: ./app            instruction says to create image based on dockerfile located in ./app
#   mongo:
#     image: mongo            will create service mongo based on official image mongo

# docker-compose up     create containers and net between containers
# docker-compose down     close containers and remove containers and net
# docker-compose up -d --build   rebuild  containers and images
# docker logs <id containers>

# -------------------------------------------------------------------------------------------------------------

# Apart from having one of the coolest logos out there, you can think of Docker as a platform to develop, deploy and run
# applications with containers. This means that your application works in exactly the same environment whether that's on
# your computer or someone else's. This is especially important for machine learning and data science

#  An image is an executable package that includes everything needed to run an application, so that's the code, runtime,
#  libraries, environment variables, and the configuration files.

#  So, what we do is define these portable images in something called a Docker file. Now a Docker file is just a couple
#  of lines of text that has instructions that defines what goes on in the environment inside your container, so things
#  like how do you access network resources or what ports do you need to map to reach the outside world

#  The place we push that to is a Docker registry, so a collection of images is called a repository, a bit like what you
#  have in a GitHub repository and a collection of repositories is a registry. We'll use Docker Hub in this course.

# docker pull ubuntu:18.10  will pull ubuntu version 18.10
#  What's really helpful is that all of the Docker image commands start with the keyword docker image. So we can type
#  a docker image ls -a and this will display all of the images that we have in Docker, so docker image ls -a. Now the
# docker image ls -a will give you a list containing all of the intermediate images used in builds, and the docker image
# ls command will give you a list of all of the images in the local repository. So let's type docker image ls, and you
# can see that in this instance there's no difference between the two. You can also delete an image by typing docker
# image rm and providing the image name. Now you don't have to specify the entire image name, you can just use the first
# few characters. So if I want to delete hello world, I type docker image rm, and I'm going to use the first two
# characters of the image Id, which is fc. If I then do a docker image ls, you can see that that image doesn't exist in
# the local repository.

# A Container is a running Docker image. So in this section on containers, let's create our own Docker file that we'll
# run in a container.

# docker images      or docker image ls -a    show all images in local repository

# docker image rm <image name>   will remove image


# docker container ls    show all running container
# docker container ls -a  show all container

# docker container stop <container_id>    gracefully stop container
# docker container kill <hash>   force shutdown container

# *************************       example Dockerfile        ****************************
# from ubuntu:18.10      Where do we begin? That's FROM, and I'm gonna start from an image called ubuntu
# RUN apt update && apt install -y python3
# CMD           to run when this image is started.

# docker build -t <name_new_image> .    create image from a dockerfile in our project

# So I do a Docker Build. I'll give it a tag -t ts for troubleshooting and dot to specify the docker file's in this
# directory.

# docker container run first     run container with name first and shutdown
# docker container run -it first     run container in interactive mode

#  we can then run this image So, docker container run, and we give our image the name First. Now what this does is it
#  brings up the image, and then shuts it down again. What you probably want to do is to be able to interact with the
#  image. In this case, let's use the -it flag, so that's docker container run -it, and then the image name. And this
#  allows us to interact with the image
# now we can access to ubuntu
# cat /etc/*release   information about running ubuntu

# exit     command to exit from container
#
# docker container ls -aq   will show hash of containers
# docker  container rm <hash container>  remove container

# The WORKDIR command sets the working directory for any run, command, entry point, copy and add instructions that fall
# in the Dockerfile.

# COPY instruction copies new files or directories from the source and adds them to the file system of the container
# at the path destination. So in line 10 we're copying all of the files in the current directory and adding them to the
# data directory in the container.

# ADD notes.txt /notes.txt      add file notes.txt from directory to container in /notes.txt

# The RUN instruction will execute any commands in a new layer on top of the current image and commits the results.
#
# The EXPOSE instruction is really a message from the creator of the container to whoever uses it. You're telling them
# which ports will need to be used. However, you will only publish the port when you use the dash P flag when running
# a container.
# EXPOSE 8888

#  the CMD instruction. There can only be one CMD instruction in a Dockerfile and if you have more than one then only
#  the last CMD will take effect. The main purpose of a CMD is to provide defaults so you're telling the container what
#  it should do after launching.
# CMD ["--port=8888", "--ip=0.0.0.0", "--no-browser", "--allow-root", "notebook"]    example!!
#
# ************************        Uploading images to Docker Hub     *************************
# docker login       command to login to docker hub
# docker tag feb5d9fea6a5 shypilovd1986/myhello-world:latest    will create image based on hash image feb5d9fea6a5
# docker push shypilovd1986/myhello-world:latest    will push on docker hub
# go to docker.io check our rep and press button public view

# **Docker** — технология для создания и управления контейнерами.
#
# Мы оборачиваем какой то код или приложение в контейнеры для того, чтобы он нам гарантировал одинаковое поведение в
# разных окружениях. Мы можем просто брать докер контейнеры и запускать их где угодно, где есть докер. Нам не важно,
# что это будет за ОС, его версия. Все поведение будет зафиксировано в контейнере.
#
# # Базовая информация
#
# `docker` - какие вообще команды есть в докере
#
# `docker version` - узнаем версию докера
#
# # Быстрый пример с Python
#
# ```python
# print('Hello Python!')
# ```
#
# ```docker
# FROM python
#
# WORKDIR /app
#
# COPY . /app
#
# CMD ["python", "index.py"]
# ```
#
# 1. `docker build .`
# 2. `docker image ls`
# 3. `docker run IMAGE_ID`
#
# # Образы и контейнеры (Images & Containers)

# **Containers** - запускаются на основе образов
#
# **Images** - шаблоны, только для чтения для создания контейнеров
#
# Качаем ноду
#
# `docker pull node`
#
# Она качается отсюда: [https://hub.docker.com/_/node](https://hub.docker.com/_/node)
#
# Смотрим, что скачалось
#
# `docker images`
#
# Запускаем контейнер с нодой
#
# `docker run node`
#
# `docker ps`
#
# Смотрим на параметры
#
# `docker ps —help`
#
# `docker ps -a`
#
# Запускаем в интерактивном режиме и сравниваем версии
#
# `docker run -it node`
#
# > process.version
# >
#
# `node -v`
#
# Удаляем контейнер
#
# `docker ps -a`
#
# `docker rm CONTAINER_ID`
#
# # Практика Node приложения
#
# Качаем приложение с Git: [https://github.com/vladilenm/logs-app](https://github.com/vladilenm/logs-app)
#
# Создаем **Dockerfile**
#
# ```docker
# FROM node # с какого image хотим сделать свой
#
# WORKDIR /app # контекст проекта
#
# COPY . . # копируем из локального проекта
#
# EXPOSE 3000 # какой порт запускается
#
# RUN npm install # запускаем команду когда собирается образ
#
# CMD ["node", "app.js"] # запускаем команду, когда запускается образ
# ```
#
# Создаем свой образ:
#
# `docker build .`
#
# `docker image ls`
#
# `docker run IMAGE_ID`
#
# `docker ps -a`
#
# `docker stop CONTAINER_ID`
#
# `docker run -p -d 3000:3000 IMAGE_ID`
#
# Открываем localhost:3000
#
# Изменяем код в приложении и заного строим образ
#
# Оптимизация докера:
#
# ```docker
# FROM node
#
# WORKDIR /app
#
# COPY package.json /app
#
# RUN npm install
#
# COPY . .
#
# EXPOSE 3000
#
# CMD ["node", "app.js"]
# ```
#
# ## Основные команды
#
# `docker stop CONTAINER_ID` - останавливает контенер
#
# `docker run -p 3000:3000 IMAGE_ID`
#
# `docker attach CONTAINER_ID` - присоединяется к контейнеру
#
# `docker start`  - запускает существующий контейнер
#
# `docker images` - список образов
#
# `docker run -p 3000:3000 -d —rm —name nodeapp IMAGE_ID` - запускает и удаляет контейнер с именем
#
# `docker build -t nodeapp:latest .` - создает образ с именем
#
# `docker image inspect IMAGE` - информация по образу
#
# `docker logs CONTAINER` - смотрим, что происходит в контейнере
#
# `docker rmi IMAGE` - удаляем образвы
#
# `docker rm CONTAINER_IDS` - удаляем контейнеры
#
# `docker container prune` - удаляем все неиспользуемые контейнеры
#
# ## Деплой
#
# Заходим в [docker.com](http://docker.com)
#
# `docker tag OLD_NAME NEW_NAME` - переименовывает образ
#
# `docker push REPO_NAME` - Заливает образ
#
# `docker pull` - забирает образ
#
# # Добавляем .dockerignore
#
# ```docker
# node_modules
# Dockerfile
# .git
# .idea
# ```
#
# # ENV переменные
#
# ```docker
# ENV PORT 3000
#
# EXPOSE $PORT
# ```
#
# Задаем переменные из консоли
#
# `docker run -p 3000:80 -d --rm --name logsapp -e PORT=80 logsapp:env`
#
# Или через файл
#
# ```docker
# PORT=3000
# ```
#
# `docker run -p 3000:80 -d --rm --name logsapp --env-file ./.env logsapp:env`
#
# # Тома (Volumes)
#
# Это просто папка на локальной машине, которая может монтироваться в докер контейнер. Служит для того, чтобы данные существовали вне зависимости от контейнеров.
#
# Например данные для базы данных, или исходный код самого приложения.
#
# ```docker
# VOLUME ["/app/data"] # Добавляем в докер
# ```
#
# Собираем образ
#
# `docker build -t logsapp:volumes .`
#
# `docker run -p 3000:3000 -d —rm —name logsapp -v logs:/app/data logsapp:volumes`
#
# `docker volume ls` - смотрим список
#
# `docker volume inspect logs`
#
# `docker volume create VOLUME`
#
# `docker volume prune`
#
# `docker volume rm VOLUME`
#
# ## Монтирование каталога (Bind Mount)
#
# Это нужно для разработки
#
# Если собрать контейнер, то он не меняется, когда мы меняем исходники в редакторе
#
# Добавляем еще один volume
#
# `docker run -p 3000:3000 -d --rm --name logsapp -v logs:/app/data -v /app/node_modules -v "/Users/vladilen/WebstormProjects/express-sample-app:/app" logsapp:volumes`
#
# Или с сокращением
#
# `docker run -p 3000:3000 -d --rm --name logsapp -v logs:/app/data -v /app/node_modules -v $(pwd):/app logsapp:volumes`
#
# ## Команды
#
# `docker volume ls` - список
#
# `docker stop CONTAINER` - удаляем контейнер
#
# `docker volume ls` - удалились анонимные volumes
#
# # Deployment
#
# На локальной машине заливаем образ в Docker Hub:
#
# `docker tag LOCAL_IMG vladilenm/nodeapp`
#
# `docker push vladilenm/nodeapp`
#
# Я взял сервер на [vscale.io](http://vscale.io) . Можно использовать любой удобный VPS
#
# <aside>
# 💡 **Как создать SSH ключ**
#
# ssh-keygen -t rsa
# pbcopy < ~/.ssh/id_rsa.pub
#
# </aside>
#
# На VPS
#
# `docker pull vladilenm/nodeapp`
#
# `docker run -d -p 80:3000 --name nodeapp --rm vladilenm/nodeapp`
#
# Переходим по адресу:
#
# ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8badc49e-3be1-4573-861f-f08c77ff8633/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8badc49e-3be1-4573-861f-f08c77ff8633/Untitled.png)
#
# Открываем в браузере IP
#
# #