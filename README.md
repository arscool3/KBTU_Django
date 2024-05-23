### Terminology
<ul>
  <li>Encoder – packages the video stream and sends it via transport protocol (in our case RTMP)</li>
  <li>RTMP (Real Time Messaging Protocol) – is a TCP-based protocol used for streaming audio, videos, and data over Internet.</li>
  <li>Transcoding – when video’s properties are changed (quality, size, etc.) based on user’s bandwidth</li>
  <li>Segmentation – separating data chunks, which can be as small as couple seconds long.</li>
  <li>Packaging – protocol for organizing video chunks and transporting it</li>
  <li>HTTP Live Streaming (HLS) - is an HTTP-based adaptive bitrate streaming communications protocol.</li>
</ul>

### Functional Requirements
<ul>
  <li>User should be able to create accounts, log in, and log out.</li>
  <li>User should be able to stream, watch streams, watch stream clips and videos of streams.</li>
  <li>Personalized content recommendations based on user’s preferences and view history.</li>
</ul>

### Non-Functional Requirements
<ul>
  <li>Low latency and fast responsiveness during watching streams and streaming.</li>
  <li>Ability of handling a lot of viewers on one stream</li>
  <li>Ability of handling a lot of viewers on one stream</li>
  <li>Easy navigation and seamless user experience</li>
  <li>Secure authorizations and authentication</li>
</ul>

### High-Level Design
<img width="468" alt="image" src="https://github.com/Walparis/KBTU_Django/assets/123378945/7d754037-7741-4649-8eb3-bce3becf3d23">

### Tech Stack
<ul>
  <li>Uvicorn: server application, which binds browser or API service and FastAPI to serve it the requests.</li>
  <li>httpx: For making HTTP requests to external services.</li>
  <li>python-decouple: For managing configuration settings and environment variables.</li>
  <li>Dramatiq and Redis: For handling background tasks and task queues.</li>
  <li>SQLAlchemy, Databases, and asyncpg: For ORM capabilities and asynchronous database interactions.</li>
  <li>Alembic: For database migrations.</li>
  <li>Pydantic: For data validation and settings management.</li>
  <li>passlib[bcrypt]: For secure password hashing.</li>
  <li>Python-jose: For handling JWT-based authentication and authorization.</li>
  <li>Locust: Collects metrics from the application.</li>
</ul>

### Performance
<img width="468" alt="image" src="https://github.com/Walparis/KBTU_Django/assets/123378945/e3b1e0b3-e944-4f6d-8187-8cb6f12c0e9a">
####Response time:
<ul>
  <li>The median response time for GET requests is 3ms, and for POST requests, it's 4ms, which are quite low and indicate good performance.</li>
  <li>The 95th percentile response time for GET requests is 8ms and for POST requests is 18ms. These times are still reasonable.</li>
  <li>The 99th percentile response time for both GET and POST requests is 61ms, indicating that 99% of requests are handled within 61ms.</li>
</ul>

####Request volume:
<ul>
  <li>The total number of requests is 2440, with GET requests being 1239 and POST requests being 1201. This distribution seems balanced.</li>
</ul>

####Failures:
<ul>
  <li>There are a few failed requests (3 for GET and 4 for POST). This is a very low failure rate.</li>
</ul>

####Throughput:
<ul>
  <li>The current RPS (Requests Per Second) is 66.1, which is a solid throughput rate. This indicates that the system can handle a significant number of requests per second.</li>
</ul>

