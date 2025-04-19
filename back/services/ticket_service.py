# import joblib
# import os

# # Load AI model and encoder
# model_path = os.path.join(os.path.dirname(__file__), "../ai_model.pkl")
# encoder_path = os.path.join(os.path.dirname(__file__), "../label_encoder.pkl")
# model = joblib.load(model_path)
# encoder = joblib.load(encoder_path)

# def predict_category(subject: str, description: str, priority: str) -> str:
#     input_text = f"{subject} {description} {priority}"
#     prediction = model.predict([input_text])
#     category = encoder.inverse_transform(prediction)[0]
#     return category



import datetime

from sqlmodel import select

from back.db.models.ticket_model import Ticket


class TicketService:
    def __init__(self, db_session):
        self.db_session = db_session

    def create_ticket(self, ticket_data):
        try:
            category = self.predict_category(ticket_data.subject, ticket_data.description, ticket_data.priority)
            new_ticket = Ticket(
                email=ticket_data.email,
                subject=ticket_data.subject,
                description=ticket_data.description,
                priority=ticket_data.priority,
                category=category,
                status="pending",
                created_at=datetime.utcnow()
            )
            self.db_session.add(new_ticket)
            self.db_session.commit()
            self.db_session.refresh(new_ticket)
            return new_ticket
        except Exception as e:
            self.db_session.rollback()
            return None

    def get_all_tickets(self):
        return self.db_session.exec(select(Ticket)).all()

    def predict_category(self, subject: str, description: str, priority: str) -> str:
        input_text = f"{subject} {description} {priority}"
        prediction = model.predict([input_text])
        category = encoder.inverse_transform(prediction)[0]
        return category