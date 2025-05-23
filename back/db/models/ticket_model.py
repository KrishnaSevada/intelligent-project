from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Ticket(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    active: Optional[bool] = Field(default=True, nullable=True, index=True)
    created_at: Optional[datetime] = Field(default=None, nullable=True, index=True)
    created_by: Optional[str] = Field(default=None, nullable=True, index=True)
    updated_by: Optional[str] = Field(default=None, nullable=True, index=True)
    updated_at: Optional[datetime] = Field(default=None, nullable=True, index=True)
    email: str
    subject: str
    description: str
    category: Optional[str] = None 
    priority: str
    status: Optional[str] = "pending"

class TicketCreate(SQLModel):
    email: str
    subject: str
    description: str
    priority: str
