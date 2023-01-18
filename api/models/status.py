from enum import Enum

class Status(str, Enum):
    OPEN = 'Open'
    IN_PROGRESS = 'In Progress'
    CLOSED = 'Closed'