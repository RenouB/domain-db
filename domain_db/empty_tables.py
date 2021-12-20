from models import Gemuese
from sqlalchemy_tools.get_sqlalchemy_session import get_sqlalchemy_session
import pandas as pd

session = get_sqlalchemy_session()

if __name__ == "__main__":
    session.query(Gemuese).delete()
    session.commit()

