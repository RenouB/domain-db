import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pathlib

env_path = os.path.join(pathlib.Path(__file__).parent.resolve(), ".env")

if not os.environ.get("DOMAIN_DB_PASSWORD"):
    dotenv = load_dotenv(env_path)

def get_sqlalchemy_url():
    DOMAIN_DB_TYPE = os.environ.get('DOMAIN_DB_TYPE')
    DOMAIN_DB_USERNAME = os.environ.get('DOMAIN_DB_USERNAME')
    DOMAIN_DB_PASS = os.environ.get('DOMAIN_DB_PASSWORD')
    DOMAIN_DB_NAME = os.environ.get('DOMAIN_DB_NAME')
    DOMAIN_DB_PORT = os.environ.get('DOMAIN_DB_PORT')
    sqlalchemy_url = DOMAIN_DB_TYPE+"://"+DOMAIN_DB_USERNAME+":"+DOMAIN_DB_PASS+"@localhost:"+DOMAIN_DB_PORT+"/"+DOMAIN_DB_NAME
    return sqlalchemy_url

def get_sqlalchemy_session():
    sqlalchemy_url = get_sqlalchemy_url()
    print(sqlalchemy_url)
    engine = create_engine(sqlalchemy_url)
    engine.connect()
    Session = sessionmaker(engine)
    return Session()

if __name__ == "__main__":
    session = get_sqlalchemy_session()