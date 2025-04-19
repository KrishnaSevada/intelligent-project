



class ticket_controller:
    def __init__(self, ticket_service):
        self.ticket_service = ticket_service

    def create_ticket(self, ticket_data):
        return self.ticket_service.create_ticket(ticket_data)

    def get_ticket(self, ticket_id):
        return self.ticket_service.get_ticket(ticket_id)

    def update_ticket(self, ticket_id, ticket_data):
        return self.ticket_service.update_ticket(ticket_id, ticket_data)

    def delete_ticket(self, ticket_id):
        return self.ticket_service.delete_ticket(ticket_id)