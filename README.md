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

![image](https://github.com/yantay0/KBTU_Django/assets/93054482/5169f854-5fc8-4410-bbed-b45d1b69245f)

check others on http://0.0.0.0:8000/docs

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

## MIn requirements
1) 6 models
2) 4 Relationships
3) Authorization
4) Background Tasks (Dramatiq / Celery)
5) Postgres DB
6) 3 DI (2 func, 1 class)

### 1&2 Database Report: Models and Relationships

This report outlines the structure of the database, detailing the models and their relationships within the application. The database is structured around several core entities: `User`, `Activity`, `Post`, `Follow`, `Hashtag`, and additional join tables for handling many-to-many relationships.

## Models Overview

#### 1. User Model

- **Table Name:** users
- **Columns:**
  - id (Integer, Primary Key)
  - email (String, Unique)
  - username (String, Unique)
  - name (String)
  - hashed_password (String, Not Null)
  - created_dt (DateTime, Default Current UTC Timestamp)
  - dob (Date)
  - gender (Enum)
  - profile_pic (String)
  - bio (String)
  - location (String)
  - followers_count (Integer, Default 0)
  - following_count (Integer, Default 0)
- **Relationships:**
  - Posts (One-to-Many)
  - Liked Posts (Many-to-Many)
  - Followers (Many-to-Many)
  - Following (Many-to-Many)
  - Post Hashtags (Many-to-Many)

#### 2. Activity Model

- **Table Name:** activities
- **Columns:**
  - id (Integer, Primary Key)
  - username (String, Not Null)
  - timestamp (DateTime, Not Null, Default Current UTC Timestamp)
  - liked_post_id (Integer)
  - username_like (String)
  - liked_post_image (String)
  - followed_username (String)
  - followed_user_pic (String)
- **Relationships:** None specified in the provided schema.

#### 3. Post Model

- **Table Name:** posts
- **Columns:**
  - id (Integer, Primary Key)
  - content (String)
  - image (String)
  - location (String)
  - created_dt (DateTime, Default Current UTC Timestamp)
  - likes_count (Integer, Default 0)
- **Relationships:**
  - Author (Foreign Key to User)
  - Hashtags (Many-to-Many)
  - Liked By Users (Many-to-Many)

#### 4. Follow Model

- **Table Name:** follows
- **Columns:**
  - follower_id (Integer, Foreign Key to User, Primary Key)
  - following_id (Integer, Foreign Key to User, Primary Key)
- **Relationships:**
  - Follower (Back Populates Followers in User)
  - Following (Back Populates Following in User)

#### 5. Hashtag Model

- **Table Name:** hashtags
- **Columns:**
  - id (Integer, Primary Key)
  - name (String, Index)
- **Relationships:**
  - Posts (Many-to-Many)

#### 6. Models for join tables

- **post_hashtags:** A join table used to implement the Many-to-Many relationship between `Post` and `Hashtag`.
- **post_likes:** A join table used to implement the Many-to-Many relationship between `User` and `Post` for liking posts.
- **Relationships:**
  Both represent Many-to-Many relationships.

### Relationships Summary

- **User to Post:** One-to-Many (A user can create multiple posts, but each post belongs to one user.)
- **User to Activity:** Many-to-One (Multiple users can perform activities, but each activity is associated with one user.)
- **User to Follow:** Many-to-Many (Users can follow and be followed by other users.)
- **Post to Hashtag:** Many-to-Many (Posts can contain multiple hashtags, and each hashtag can be associated with multiple posts.)
- **Post to Activity:** Many-to-One (Activities can reference posts, but each post can be involved in multiple activities.)

### 3. Authorization implemented with OAuth2 with Password (and hashing), Bearer with JWT tokens (check auth module)
### 4. Background Tasks with Celery, Redis and Flower
- ![image](https://github.com/yantay0/KBTU_Django/assets/93054482/079c69e7-310c-4a37-bbe6-2659294f9588)
- ![image](https://github.com/yantay0/KBTU_Django/assets/93054482/dac31e45-ac13-41c5-be9e-652071054b30)
- ![image](https://github.com/yantay0/KBTU_Django/assets/93054482/149bfcd5-d68a-43e0-b4d0-88a7a68b78ad)
- ![image](https://github.com/yantay0/KBTU_Django/assets/93054482/c4d59b68-b2f9-4fc0-99ea-92f60d058b33)
- ![image](https://github.com/yantay0/KBTU_Django/assets/93054482/1d9cf5cc-b474-4c3a-8f3c-9111b55d97d0)

### 5. Postgres DB
- ![image](https://github.com/yantay0/KBTU_Django/assets/93054482/8aa2f7b6-8489-47db-9623-31f6649a5645)

### 6. DI usage
- 1. func ![image](https://github.com/yantay0/KBTU_Django/assets/93054482/8eda6282-3d44-4359-ab5e-a70c45e68cd1)
- 2. func ![image](https://github.com/yantay0/KBTU_Django/assets/93054482/b324ebfa-7280-42dc-9cc4-a73e423e1f28)
- 3. class ![image](https://github.com/yantay0/KBTU_Django/assets/93054482/7b1698d0-d9da-4cb2-b565-c59d504dbb89)





## Contributing

Contributions are welcome Please feel free to submit a Pull Request.
