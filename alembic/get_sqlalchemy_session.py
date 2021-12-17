import os
from dotenv import DotEnv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

dotenv = DotEnv()

def get_sqlalchemy_url():
    DOMAIN_DB_TYPE = dotenv.get('DOMAIN_DB_TYPE')
    DOMAIN_DB_USERNAME = dotenv.get('DOMAIN_DB_USERNAME')
    DOMAIN_DB_PASS = dotenv.get('DOMAIN_DB_PASSWORD')
    DOMAIN_DB_NAME = dotenv.get('DOMAIN_DB_NAME')
    DOMAIN_DB_PORT = dotenv.get('DOMAIN_DB_PORT')
    sqlalchemy_url = DOMAIN_DB_TYPE+"://"+DOMAIN_DB_NAME+":"+DOMAIN_DB_PASS+"@localhost:"+DOMAIN_DB_PORT+"/"+DOMAIN_DB_NAME
    return sqlalchemy_url

def get_sqlalchemy_session():
    sqlalchemy_url = get_sqlalchemy_url()
    engine = create_engine(sqlalchemy_url)
    Session = sessionmaker(engine)
    return Session()
    


if __name__ == "__main__":
    session = get_sqlalchemy_session)