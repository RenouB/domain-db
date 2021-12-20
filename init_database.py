from models import Gemuese
from sqlalchemy_tools.get_sqlalchemy_session import get_sqlalchemy_session
import pandas as pd

session = get_sqlalchemy_session()

if __name__ == "__main__":
    if not len(session.query(Gemuese).all()):
        print("adding some stuff to database")
        gemuese_df = pd.read_csv("./data/gemuese.csv")
        gemuese_list = gemuese_df.to_dict(orient="records")

        gemuese_to_add = []
        for gemuese in gemuese_list:
            gemuese_to_add.append(Gemuese(**gemuese))
            
        session.add_all(gemuese_to_add)
        session.commit()
        session.close()
        
    print(session.query(Gemuese).all())


