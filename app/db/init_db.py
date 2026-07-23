from app.db.database import Base, engine
from app.models.complaint import Complaint


def init_db():
    Base.metadata.create_all(bind=engine)
    print("Database initialized")

if __name__ == "__main__":
    init_db()
