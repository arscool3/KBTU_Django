# Project name: maglnuse_egov

## Description 
This project is a FastAPI-based backend system integrated with Kafka for message streaming and PostgreSQL for data persistence. It includes features like user authentication, data moderation, and Telegram bot integration. 
 
This project developed for Advanced Python CSE1123 Course Fall 2023 tough by Roman Savoskin at School of Information Technologies and Engineering at Kazakh-British Technical University.  
 
## Schemas
1. Docker hub realisation
<details>
<summary>Click to expand</summary>
![example1](/images/docker_hub_scheme.jpg)
</details>
2. Schema of frontend
<details>
<summary>Click to expand</summary>
![example2](/images/front_schema.jpg)
</details>
3. Schema of server side
<details>
<summary>Click to expand</summary>
![example3](/images/server_schema.jpg)
</details>

 
### Features 
 
*   User Management: Sign up, login, and profile management. 
*   Data Moderation: Create and manage moderation requests. 
*   Kafka Integration: Consume and process messages from Kafka topics. 
*   Telegram Bot: Send PDFs and messages to Telegram users. 
*   PDF Generation: Generate and send PDF documents based on data. 
*   Database: PostgreSQL for storing user data and moderation requests. 
 
## Team 
- 21B030662 - Glazhdin Sabir  (Role): Teamlead, Contact Information: @sabirgl 
- 21B030699 - Maulen Nursultan (Role): Devops Engineer, Contact Information: @nmaulen 
- 21B030702 - Nussip Arsen(Role): Telegram, email, Makefile, pre-commit, Contact Information: @new_meanings 
- 21B030716 - Serikbay Amirkhan (Role): Backender 
 
## INSTALL 
Instructions on how to install and run your project. 
- Step 1: Clone the repository: you need access  
 
  git clone https://gitlab.com/di-halyk-academy-maglnuse/maglnuse-egov 
 
- Step 2: Navigate to the project directory: 
   
  cd maglnuse_egov 
 
- Step 3: Build and run the Docker containers: 
 
  docker-compose up --build 
 
- Step 4: Make option 
 
  make dcup 
 
CONTRIBUTING 
### Reporting Bugs/Issues 
 
If you encounter a problem or bug in a project, we want to know about it. Here's how you can report them: 
 
1. How to Report: If you find a bug or issue, please let us know via our Telegram channel [@new_meanings]. 
