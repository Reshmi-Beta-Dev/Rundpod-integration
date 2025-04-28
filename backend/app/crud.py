from pymongo.collection import Collection
from bson import ObjectId
from .models import TicketBooking
from typing import List, Optional

# Function to create a new ticket booking
def create_ticket_booking(ticket_data: TicketBooking, collection: Collection) -> dict:
    ticket_dict = ticket_data.dict(exclude_unset=True)
    result = collection.insert_one(ticket_dict)
    return {"id": str(result.inserted_id), **ticket_dict}

# Function to get all ticket bookings
def get_all_ticket_bookings(collection: Collection) -> List[dict]:
    tickets = collection.find()
    return [ticket_serializer(ticket) for ticket in tickets]

# Function to get a ticket booking by ID
def get_ticket_booking_by_id(ticket_id: str, collection: Collection) -> Optional[dict]:
    ticket = collection.find_one({"_id": ObjectId(ticket_id)})
    if ticket:
        return ticket_serializer(ticket)
    return None

# Function to update a ticket booking
def update_ticket_booking(ticket_id: str, updated_data: TicketBooking, collection: Collection) -> dict:
    update_dict = updated_data.dict(exclude_unset=True)
    result = collection.update_one(
        {"_id": ObjectId(ticket_id)},
        {"$set": update_dict}
    )
    if result.matched_count == 0:
        return {"error": "Ticket not found"}
    return {"message": "Ticket updated successfully"}

# Function to delete a ticket booking
def delete_ticket_booking(ticket_id: str, collection: Collection) -> dict:
    result = collection.delete_one({"_id": ObjectId(ticket_id)})
    if result.deleted_count == 0:
        return {"error": "Ticket not found"}
    return {"message": "Ticket deleted successfully"}

# Helper function to serialize ticket data for response
def ticket_serializer(ticket) -> dict:
    return {
        "id": str(ticket["_id"]),
        "user_name": ticket.get("user_name"),
        "event": ticket.get("event"),
        "date": ticket.get("date"),
        "seats": ticket.get("seats"),
        "status": ticket.get("status"),
    }

