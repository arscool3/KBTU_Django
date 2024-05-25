# Project Title: Social Media App with FastAPI

## Introduction

Welcome to the documentation for Final Project within KBTU DJANGO 2024 Spring. This platform is designed to offer a comprehensive social media experience, enabling users to connect, share content, and interact with each other. Leveraging Docker Compose for easy setup and deployment, this project is built to support a wide array of features common in today's social media landscape, including user profiles, post creation, following/followers mechanisms, and activity tracking. 

## Features

- **User Profiles:** Users can create and manage personal profiles, including basic information, profile pictures, and bios.
- **Posting Content:** Users can share text updates, images, and videos with the community.
- **Following and Followers:** Users can build and grow their networks by following others and having followers.
- **Interactions:** Users can like posts, comment on updates, and engage with the community through various activities.
- **Hashtags:** Users can utilize hashtags to categorize and discover content.
![image](https://github.com/yantay0/KBTU_Django/assets/93054482/d7062d3f-645b-4937-841a-6fa5bccd2d93)

![image](https://github.com/yantay0/KBTU_Django/assets/93054482/a8a6074b-8ea8-4137-8587-19ae7f4ebd4d)

![image](https://github.com/yantay0/KBTU_Django/assets/93054482/0ab4c05e-62ed-4494-baf7-c5f368457a6e)

check others on http://0.0.0.0:8000/docs
![image](https://github.com/yantay0/KBTU_Django/assets/93054482/5169f854-5fc8-4410-bbed-b45d1b69245f)


## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Docker and Docker Compose installed on your machine.
- Basic knowledge of Docker and containerization concepts.


### Installation

1. Clone the repository to your local machine.
   ```
   git clone https://github.com/yantay0/KBTU_Django.git
   cd final_project/social-media-app/src
   ```

2. Navigate to the project directory where the `docker-compose.yml` file is located.

3. Build and start the containers defined in the `docker-compose.yml` file.
   ```
   docker-compose up --build
   ```

This command will pull the necessary base images, build the containers according to the configurations in the `docker-compose.yml` file, and start them. The application should now be accessible at the specified ports.

### Running the Application

- After the containers are up and running, you can access the application through the specified ports in the `docker-compose.yml` file. Typically, a web interface would be accessible via a web browser at `http://localhost:<port>`.

### Stopping the Containers

To stop and remove the containers, networks, and volumes defined in the `docker-compose.yml` file, run:

```
docker-compose down
```

## Contributing

Contributions are welcome Please feel free to submit a Pull Request.
