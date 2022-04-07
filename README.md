# DevOps_Practical_Project

## This repo contains the deliverable for QA's DevOps Practical Project. 




<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#Project-Brief">Project Brief</a>
    </li>  
        <li><a href="#Built-With">Built With</a></li>
    
  <li><a href="#Project-Planning"> Project Planning </a></li>
    <li>
      <a href="#App-Design">App Design</a>    
      </li>
        <li><a href="#CI/CD-Pipeline"> CI/CD Pipeline </a></li>
        <li><a href="#Known-Issues"> Known Issues </a></li>  
    <li><a href="#Future-Work"> Future Work </a></li>

  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## Project Brief
The brief for this project was to produce an application consisting of four microservices, which interact with one another to generate objects using some defined logic. This application was produced and maintained using a fully automated CI/CD pipeline. The full tech stack required was as follows:
<ul>
  <li>Kanban Board (or similar) for project tracking</li>
  <li>Git for version control</li>
  <li>Jenkins as a CI server</li>
  <li>Ansible for configuration management</li>
  <li>GCP cloud platform</li>
  <li>Docker as a containerisation tool</li>
  <li>Docker swarm for container orchestration</li>
  <li>NGINX as a reverse proxy</li>
 </ul>


<p align="right">(<a href="#top">back to top</a>)</p>


## Built With

* [Python](https://docs.python.org/)
* [Docker](https://docs.docker.com/)
* [Google Cloud Platform](https://cloud.google.com/docs)
* [Ansible](https://docs.ansible.com/)
* [NGINX](http://nginx.org/en/docs/)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Jenkins](https://www.jenkins.io/doc/)
* [Github](https://docs.github.com/en)
* [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
* [Bootstrap](https://getbootstrap.com/docs/4.1/getting-started/introduction/)

### Project Planning
While planning this project a full risk assessment was undertaken in order to identify hazards associated with this project, as shown below: 

![risk assessment](https://github.com/Jack-Middleton/DevOps_Practical_Project/blob/main/readme_images/Risk%20Assessment.png)

Since users are not submitting any information to this app, the main focus of this risk assessment was on operational risks ie; those associated with building and deployment. An SQL database was not used either so I didnt have to worry about environment keys being leaked as they were not used in the development of this application.

<p align="right">(<a href="#top">back to top</a>)</p>

### App Design

In response to this brief I have decided to develop a football player generator, akin to Football Managers youth player generation, utilising a microservice architecture as described below. 

<ul>
  <li> Front-end (service 1): The service with which the user interacts. This service sends requests to the other services to generate random events and displays the generated events to the user. </li>
  <li> Personal Stats (service 2): This service receives HTTP GET requests from service 1 and responds with randomly generated information such as player name, height, weight etc using random.choice() and random.randint() </li>
  <li> Non-Dependent Stats (service 3): This service receives HTTP GET requests from service 1 and responds with randomly generated stats that arent dependent on any other information such as first touch, anticipation etc. Making use of globals()[] to iterate through a list of strings and assign the value of random.randint(1,20) to each of them as variables. </li>
  <li> Dependent Stats (service 4): This service receives HTTP POST requests from service 1, providing the results of the randomly generated information from service 2 and using it to determine the dependent stats eg; a Goalkeeper would have a different stat array to a striker. It uses the information given to set caps for randint and then makes use of globals()[] again to iterate through a list or dictionary and assign the value of randint(base,cap) to each variable.  </li>
  </ul>

In addition to these main services, a reverse proxy NGINX was implemented. The NGINX service listens to port 80 on the host machine and performs a proxy pass, directing traffic from port 80 on the host to port 5000 on the front-end container where the app is accessible. 
The image below shows the front-end in action:

![Front-End](https://github.com/Jack-Middleton/DevOps_Practical_Project/blob/main/readme_images/App%20webpage.png)

The image shows the front-end, zoomed out to show all the statistics in one screenshot. The refresh button at the top will create a new character each time it is pressed. In future I would like to integrate an SQL database so that I can add save functionality to the home page so any particularly favourable generations can be saved by the user, this would also include some kind of login functionality so each user only see's what they personally have saved. The risk assessment will be updated accordingly when this work takes place. 

The overall microservice architecture is as follows: 

![Architecture](https://github.com/Jack-Middleton/DevOps_Practical_Project/blob/readme/readme_images/Service%20Architecture.png)

<p align="right">(<a href="#top">back to top</a>)</p>

### CI/CD Pipeline

The project utilises a full CI/CD pipeline to test, build, deploy and maintain the application. The major components of this pipeline are:
<ul>
  <li>Project Tracking</li>
  <li>Version Control</li>
  <li>Development environment</li>
  <li>CI server</li>
  <li>Deployment environment</li>
</ul>

Project tracking was done using Trello. Tasks were assigned story points, acceptance criteria and a MoSCoW prioritisation and moved through the stages from project backlog to complete as the project progressed. 

![Trello Board](https://github.com/Jack-Middleton/DevOps_Practical_Project/blob/main/readme_images/Trello%20Board.png)

For more details, the trello board can be accessed <a href='https://trello.com/b/QLkX32iv/devops-practical'>here</a>

Git was used for version control with the repository hosted on github. A feature-branch model was implemented in the project to insulate the stable version of the application from ongoing development. To show that this was achieved I've included the image below: 

![Feature Branch Image](https://github.com/Jack-Middleton/DevOps_Practical_Project/blob/main/readme_images/feature%20branch.png)

The development environment used was an Ubuntu 20.04 virtual machine, hosted on GCP and accessed via VSCode. 

Jenkins was used as a CI server. In response to a github webhook Jenkins cloned down the repo and executed the pipeline script defined in the Jenkinsfile. This pipeline consists of 4 main stages: test, build/push, deploy and post-build actions. The test stage executes a bash script which cycles through the directories for the four services and runs unit tests using pytest. The front-end and all API's had unit tests written to test all areas of functionality. To test the HTTP requests made by the front-end, requests_mock was used to simulate responses from the APIs. To test the functionality of the API's themselves the random.choice/random.randint function was patched with unittest.mock to ensure reproducible performance. The results of the tests were archived in HTML format, one for each service and is shown below:

Front-End:

![Front-end Tests](https://github.com/Jack-Middleton/DevOps_Practical_Project/blob/main/readme_images/Tests%20Front-End.png)

Personal Stats API:

![Personal API Tests](https://github.com/Jack-Middleton/DevOps_Practical_Project/blob/main/readme_images/Tests%20Personal.png)

Non-Dependent Stats API:

![NDStats API Tests](https://github.com/Jack-Middleton/DevOps_Practical_Project/blob/main/readme_images/Tests%20ND%20Stats.png)

Dependent Stats API:

![DStats API Tests](https://github.com/Jack-Middleton/DevOps_Practical_Project/blob/main/readme_images/Tests%20D%20Stats.png)

As can be seen here, 100% coverage was achieved for all tests; this ensured that all of the functions in the app worked exactly as intended. 

If the tests were successful, the build/push stage uses docker-compose to build the images for the different services, logs into docker using credentials configured on the Jenkins VM and then pushes the images to Dockerhub. The use of a Jenkins pipeline, with this stage-by-stage breakdown, makes optimisation of the project easier. The pip installs were separated into two different requirements files, one for testing and one for deployment, doing it this way eliminated unnecessary pip installs from the build stage and sped up the pipeline. 

Following the build/puish stage, the deploy stage deploys the application. First the docker-compose.yaml and nginx.conf files are copied to the manager node by secure copy (scp). Then an Ansible playbook is used to run three roles: The first installs docker on the swarm machines if it is not present already and adds Jenkins to the Docker group, the second initialises a swarm on the manager node and uses the Ansible docker stack module to deploy the application and the third adds the worker node to the swarm, creatring an overlay network that looks like so:

![Overlay Network](https://github.com/Jack-Middleton/DevOps_Practical_Project/blob/main/readme_images/Overlay%20network.png)

Finally, in the post-build stage the HTML coverage reports are published. The results of this pipeline is shown below: 

![Pipeline image](https://github.com/Jack-Middleton/DevOps_Practical_Project/blob/main/readme_images/Pipeline%20Image.png)

Successful stages appear green, unstable builds are indicated by yellow stages and failures are indicated via red stages. If a stage fails, later stages will be skipped preventing failed versions from being deployed, this can be seen in the console output here: 

![Failed Build](https://github.com/Jack-Middleton/DevOps_Practical_Project/blob/main/readme_images/failed%20build.png)

The overall structure of the CI/CD pipeline is as follows: 

![CI/CD Pipeline](https://github.com/Jack-Middleton/DevOps_Practical_Project/blob/main/readme_images/CICD%20Pipeline.png)

<p align="right">(<a href="#top">back to top</a>)</p>

### Known Issues

No known issues at present. 

### Future Work

As mentioned previously I'd like to add the ability to save favourable generations to a database, which would require SQL integration and potentially some sort of login system. 

### Version

1.0.0

### Updates

No Updates to show.

<p align="right">(<a href="#top">back to top</a>)</p>
