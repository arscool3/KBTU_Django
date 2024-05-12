# Hair Salon Booking Application

## Aim of the project:

The project aims to streamline the booking and management processes within a hair salon environment, providing an efficient way for managers, barbers, and clients to interact and manage their appointments.

## Models
The project includes several models representing different entities within the hair salon ecosystem:
- Manager: Represents a manager of the salon.
- Barber: Represents a barber working at the salon.
- Client: Represents a client of the salon.
- Barbershop: Represents a physical salon location.
- BookingRequest: Represents a request from a client to book a seat in the salon.
- ApplicationRequest: Represents a request from a barber to work at the salon.
## Functionality
- Managers: Can manage barbers, clients, barbershops, and requests. They can accept/reject applications from barbers and bookings from clients.
- Barbers: Can apply to work at a barbershop and change the status of their bookings to "done" after finishing work.
- Clients: Can book seats in barbershops.
## Permissions
Permissions are implemented to control access to different parts of the application:
- Managers have full control over all aspects of the application.
- Barbers and clients have restricted access to certain operations.
- Admin users have full permissions over the data through the Django admin interface.
## REST API
- The project provides a RESTful API using Django REST Framework to interact with the application's data.Viewsets are used to define the API endpoints for each model, and serializers are used to convert model instances to JSON representations.