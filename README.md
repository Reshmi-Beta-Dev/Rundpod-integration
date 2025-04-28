
# Ticket Booking API

This is a FastAPI backend application for managing ticket bookings. It provides routes to upload images, create, read, update, and delete ticket bookings. The backend is connected to a MongoDB database for storing ticket booking data and file uploads.

## Features

- **Image Upload**: Upload images along with optional prompt and parameters.
- **Ticket Booking CRUD**: Create, retrieve, update, and delete ticket bookings.
- **MongoDB Integration**: Data is stored in a MongoDB database.
- **File Storage**: Files are stored temporarily on the server.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn (for running the server)
- MongoDB
- Python MongoDB client (`pymongo`)
- Python dependencies: `python-multipart`, `aiofiles`

## Installation

### 1. Clone the repository:

```bash
git clone https://github.com/yourusername/ticket-booking-backend.git
cd ticket-booking-backend
```

### 2. Set up a Python virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
```

### 3. Install required dependencies:

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file, create one by running:

```bash
pip freeze > requirements.txt
```

You will need to install these specific packages:

```bash
pip install fastapi pymongo uvicorn python-multipart aiofiles
```

### 4. Set up MongoDB:

Ensure you have MongoDB running locally or use a cloud-based solution like [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).

Update the connection string in the `main.py` file:

```python
client = MongoClient("your_mongo_connection_string")
```

### 5. Run the application:

```bash
uvicorn main:app --reload
```

The backend will now be running at `http://localhost:8000`.

## API Endpoints

### 1. **GET `/`**
- **Description**: Health check endpoint to verify the server is running.
- **Response**: `{"message": "FastAPI Backend Running"}`

### 2. **POST `/upload/`**
- **Description**: Upload an image along with a prompt and parameters.
- **Request**:
  - `file` (required): The image file to upload.
  - `prompt` (optional): Text prompt associated with the image.
  - `params` (optional): Parameters for the image.
  
- **Response**:
  ```json
  {
    "filename": "example.jpg",
    "prompt": "Example prompt",
    "params": "example params"
  }
  ```

### 3. **POST `/ticket_bookings/`**
- **Description**: Create a new ticket booking.
- **Request**:
  - `user_name`: Name of the user.
  - `event`: Event name.
  - `date`: Date of the event.
  - `seats`: Number of seats booked.
  - `status`: Status of the booking (Pending, Confirmed, Cancelled).

- **Response**:
  ```json
  {
    "id": "ticket_id",
    "user_name": "John Doe",
    "event": "Concert",
    "date": "2025-05-01",
    "seats": 2,
    "status": "Pending"
  }
  ```

### 4. **GET `/ticket_bookings/`**
- **Description**: Get all ticket bookings.
- **Response**:
  ```json
  [
    {
      "id": "ticket_id_1",
      "user_name": "John Doe",
      "event": "Concert",
      "date": "2025-05-01",
      "seats": 2,
      "status": "Pending"
    },
    {
      "id": "ticket_id_2",
      "user_name": "Jane Smith",
      "event": "Theater",
      "date": "2025-06-15",
      "seats": 1,
      "status": "Confirmed"
    }
  ]
  ```

### 5. **GET `/ticket_bookings/{ticket_id}`**
- **Description**: Get ticket booking details by ID.
- **Response**:
  ```json
  {
    "id": "ticket_id",
    "user_name": "John Doe",
    "event": "Concert",
    "date": "2025-05-01",
    "seats": 2,
    "status": "Pending"
  }
  ```

### 6. **PUT `/ticket_bookings/{ticket_id}`**
- **Description**: Update a ticket booking by ID.
- **Request**:
  - Same as the **POST /ticket_bookings/** request.

- **Response**:
  ```json
  {
    "id": "ticket_id",
    "user_name": "John Doe",
    "event": "Concert",
    "date": "2025-05-01",
    "seats": 2,
    "status": "Confirmed"
  }
  ```

### 7. **DELETE `/ticket_bookings/{ticket_id}`**
- **Description**: Delete a ticket booking by ID.
- **Response**:
  ```json
  {
    "message": "Ticket booking deleted successfully"
  }
  ```

## Testing

You can use Postman or cURL to interact with the API. The API supports the following actions:

- **Upload a file** via the `/upload/` endpoint.
- **Create, read, update, and delete** ticket bookings via the `/ticket_bookings/` endpoints.

Example cURL for creating a ticket booking:

```bash
curl -X 'POST' \
  'http://localhost:8000/ticket_bookings/' \
  -H 'Content-Type: application/json' \
  -d '{
    "user_name": "John Doe",
    "event": "Concert",
    "date": "2025-05-01",
    "seats": 2,
    "status": "Pending"
  }'
```

## Docker Setup (Optional)

To run the backend in a Docker container, you can create a `Dockerfile` and use it to build the image. Here's a sample `Dockerfile`:

```Dockerfile
# Use official Python runtime as base image
FROM python:3.9-slim

# Set working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Build and run the Docker container:

```bash
docker build -t ticket-booking-backend .
docker run -p 8000:8000 ticket-booking-backend
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
