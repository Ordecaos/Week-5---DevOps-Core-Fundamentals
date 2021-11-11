# Week-5---DevOps-Core-Fundamentals

This repository contains all deliverables for the Week 5 QA DevOps fundementals project. This document will look into the project itself, with such facets as the risk assessment, technical design as well as a post mortem on the project.


## Contents:

* [Project Brief](#Project-Brief)
* [Continuous Intergreation Pipeline](#Continuous-Intergreation-Pipeline)
* [App Design](#App-Design)
* [Techncal Design](#Technical-Design)
* [Risk Assessment](#Risk-Assessment)
* [Testing](#Testing)
* [The Application](#The-Application)
* [Known Issues](#Known-Issues)
* [Future Developments](#Future-Developments)
* [What would be done differently](#What-would-be-done-differently)

## Project Brief

This project, provided by QA, was to design a CRUD(Create, Read, Update and Delete) application that can be accessed on many different machines. Additionally, it required the use of Flask, a 'micro-framework' that allows the design of HTML webpages using Python and HTML. It also required the use of a database, with at least two tables and at least one 'One to Many' relationship within them

## Continuous Intergreation Pipeline

This Project also requires the implementation of Continuous Intergreation (CI) including tacking the project, version control and so on. 

Jira is the software that will be used in order to track the project. This particular project can be found [here](https://ordecaos.atlassian.net/jira/software/projects/DCF/boards/2) and was chosen not only due to its status as the industry standard but also due to my familiarity with it through the course of my university education. Jira has automation features that allow tasks and user stories to be automatically updated when certain commands are issued, however I will not be using this feature sadly due to an issue involving e-mails.

Git and Github are the choices of repository that I have decided to go with. Git is an extremely intuative and useful due to it's versitility in what it can connect to, primarily the virutal machine that this project will be run on.

Speaking of Virtual Machine, this project will be using the Google Cloud Platform (GCP) and running on a virtual machine that runs Ubuntu 20.04. GCP allows all necessary portions of the project including the SQL database to be implemented and used online as well as adding a firewall for security purposes.

Finally, Jenkins will be used as a build server in order to provide automation in building and testing this project. Jenkins is an extremely useful CI tool and allows quick and easy understanding as if the project works and how or why it may not.

## App Design

On the subject of the application itself, I have decided to implement a database that contains three tables and two 'one to many' relationships.

The database will be one based on the popular Tabletop Roleplaying Game, Dungeons and Dragons. It will allow the storage of player infromation, campaign information as well as information on the various books used in D&D. Campaigns will have a one to many relationship with Players, as many players can be in a single campaign, and Books will have a one to many relationship with campaigns, as one book can be used in multiple campaigns.

![EDR](https://github.com/Ordecaos/Week-5---DevOps-Core-Fundamentals/blob/main/Images/D&D%20database%20Design.png?raw=true)

## Technical Design

When undertaking a project, it's always important to consider the various technologies that will be used in it's development as well as the rationale as to why it was chosen, as such this section will give an overview of these technologies.

#### Google Cloud Platform

Google Cloud Platform is an essential piece of technology for this project. Housing the compute engine, the SQL database and the firewall this project literally could not be completed without it.

#### Jenkins

Allowing for constant intergreation, Jenkins is an essential piece of technology for this project as it allows for continual builds and testing of the project.

#### Visual Studio Code

Visual studio code is what will be used to develop the project. Thanks to its user friendly interface and a variety of additional features that allow a direct connection to the virtual machine, github and so on.

#### Github

An online repository, Github is not only fantastic for its ability to backup the data of the virtual machine, but also as a way to share this application reliably anywhere in the world.

#### Google Chrome

Googles main search engine. Google Chrome will be used throughout this project to not only access a variety of resources already mentioned, but also to search for solutions should I find myself unable to resolve a logical issue within the code.

#### Microsoft Teams

Microsoft teams will be used in order to communicate with my cohorts and tutor over the course of this project. This is useful when I'm in need of asking somebody for a second opinion on code or to simply talk through it.

#### PC and Peripherals

In order to run everything, there must be a local machine that is capable of doing everything that is needed. As such my PC and all it's peripheral hardware, software and the operating system is one of the most essential portions of the project.

## Risk Assessment

When considering any project, a risk assessment is an essential portion of it. As such, this segment will go over the various hazards, risks, the who's responsibility it is, who's likely to be affected, control measures and so on. As well as this discussion, this will include a risk assessment matrix.

#### Man-in-the-middle attack (MITM attack)

An MITM attack occurs when a user embeds themselbes between the connection of two or more parties and observes or manipulates the data being sent, either by interfacing with networks or establishing fake networks that this malicious user controls. This can result in the stealing or changing of data on the network. This can be devastating to both users and developers and can lead to a vast amount of other issues.

In order to combat this, I will simply not include seneisitve information for the users, only requiring their first real name and no other personal information. If this project were to expand then this would likely need to be reviewed.

#### SQL injector etc.

An SQL injector is a vullnerability that allows the malicious user to interfere with queries that an application such as this one may make to its database. This would allow the malicious user to view information within the database that belongs to users or developers, affecting them both.

In order to combat this, again I will have no sensitive information within the database, however additonally SQLAlchemy will allow Flask to be used while proventing SQL commands from going straight to the database from the application, instead using secret keys in order to maintain security.

#### Distrubuted denial-of-serice attack (Ddos attack)

A Ddos attack is a malicious attempt to disrupt traffic on a targeted server or network by overwhelming it with a flood of internet traffic. This can result of sending junk data to the server through online services.

Apart from greatly increased network capacity, which is far more of a cost than this project is capable of undertaking. As such, if this was to occure then the best thing for myself as the developer to do would be to amend the firewall rules in order to block out the user who caused the attack.

#### Out of Date or inaccurate Information

For information to be defined as information, it must be up to date and accurate. If one of both of these is untrue, then the information instead becomes useless data. If this were to occur then users of the application may view it as untrustworthy or unreliable.

To combat this, the databases would be updated regularly by an administrator or a developer to ensure up-to-date and accurate information.

#### Jenkins VM goes doen

If the Jenkins VM was to go down then the automation of tests and builds of the application would hault. This could place a bottleneck on the development of the application or even grind it to a hault entirely.

To control this risk, I will keep a version of the script on hand so that tests can be run until Jenkins is back up and running.

#### Development VM goes down

If the virtual enviroment used to develop this project were to fo down, this would result in a catastropic loss of data, and the project as a whole would need to be started again. 

In order to counteract this, I will not only be regularly pushing the project to the main branch of my Github repository but also ensuring that a personal copy is on hand on an external drive that I wold be able to access.

#### SQL instance goes down

Were the instance of the SQL database on GCP to go down, this would result in a massive loss of data and continuity within the project. If the SQL database were to come back online, then it may be wiped clean, otherwise it may be unrecoverable and a new instance would need to be created.

To combat this, the data will be backed up at regular intervals on a local machine to at least maintain the information to be inputted manually later.

#### Physical hazards

While rarely considered, there are several physical issues that can crop up during the development of a project. This can include such issues as mental fatigue or burnout for the developer and Repetative Strain Injury (RSI) or eyestrain for the developer or the user. 

These Physical Hazards are bound to occur eventually. However the effects can be mitigated or controlled on the developers side by taking regular 15 minute breaks throughout developments, ensuring that the mind and body are allowed enough rest before continuing with the project. 

![Matrix](https://github.com/Ordecaos/Week-5---DevOps-Core-Fundamentals/blob/dev/Images/Matrix.png?raw=true)

## Testing

Testing is an essential part of any and all development processes, especially with the Test Driven Development nature of projects such as these. 

These tests will primarily be used to test the functionality of the application, having tests for creating, reading, editing and deleting records within the three databases and ensuring correct and thorough working.

As you can see from the following image, my program fully passes all 21 tests with 99% coverage.

![Tests](https://github.com/Ordecaos/Week-5---DevOps-Core-Fundamentals/blob/main/Images/Sucessful%20Tests.png?raw=true)

## The Application

Working fully and completely the following images display the functionality of the webpage. Allowing naviagation to the three main portions of the web page as well as the information section and inputs and edits.

![Homepage](https://github.com/Ordecaos/Week-5---DevOps-Core-Fundamentals/blob/main/Images/Homepage.png?raw=true)

![PlayersPage](https://github.com/Ordecaos/Week-5---DevOps-Core-Fundamentals/blob/main/Images/PlayerPage.png?raw=true)

![PlayerInput](https://github.com/Ordecaos/Week-5---DevOps-Core-Fundamentals/blob/main/Images/PlayerInsert.png?raw=true)

![PlayerInformation](https://github.com/Ordecaos/Week-5---DevOps-Core-Fundamentals/blob/main/Images/PlayerInfo.png?raw=true)

![PlayerEdit](https://github.com/Ordecaos/Week-5---DevOps-Core-Fundamentals/blob/main/Images/PlayerEdit.png?raw=true)

![CampaignsPage](https://github.com/Ordecaos/Week-5---DevOps-Core-Fundamentals/blob/main/Images/CampaignPage.png?raw=true)

![CampaignInput](https://github.com/Ordecaos/Week-5---DevOps-Core-Fundamentals/blob/main/Images/CampaignInsert.png?raw=true)

![CampaignInformation](https://github.com/Ordecaos/Week-5---DevOps-Core-Fundamentals/blob/main/Images/CampaignInfo.png?raw=true)

![CampaignEdit](https://github.com/Ordecaos/Week-5---DevOps-Core-Fundamentals/blob/main/Images/CampaignEdit.png?raw=true)

![BooksPage](https://github.com/Ordecaos/Week-5---DevOps-Core-Fundamentals/blob/main/Images/BookPage.png?raw=true)

![BookInput](https://github.com/Ordecaos/Week-5---DevOps-Core-Fundamentals/blob/main/Images/BookInsert.png?raw=true)

![BookInformation](https://github.com/Ordecaos/Week-5---DevOps-Core-Fundamentals/blob/main/Images/BookInfo.png?raw=true)

![BookEdit](https://github.com/Ordecaos/Week-5---DevOps-Core-Fundamentals/blob/main/Images/BookEdit.png?raw=true)

## Known Issues

The following is a brief list of known issues involving the application.

1. When creating a file, the application does not count the ID's correctly. When a file is deleted, it still goes to the next number in the sequence.
2. Jenkins implementation is not as thorough as I wish. Jenkins is only able to test the application, not deploy it.

## Future Developments

If I were to continue developing this project I would add additional functionality. The ability to filter records, adding subclasses to Players, Notes to Campaigns and more detils to book contents and so on. Additionally, I would add a log in page so that only authorized individuals could use the webpage and work on ironing out any issuesn that are present within the application.

## What would be done differently

Given my current skill and ability and the education I have been given thus far I believe that this is the best project that I would be able to produce. 
