from setuptools import setup

setup(
  name='sqlalchemy_tools',
  version='0.0.1',
  author='Renou Benteau',
  author_email='rebe01@dfki.de',
  packages=['sqlalchemy_tools', 'domain_db'],
  description='Generate SQLAclhemy database url, connect to session. Domain DB with defined models',
  install_requires=[
    "alembic==1.7.5",
    "certifi==2021.10.8",
    "greenlet==1.1.2",
    "Mako==1.1.6",
    "MarkupSafe==2.0.1",
    "numpy==1.21.4",
    "pandas==1.3.5",
    "psycopg2==2.9.2",
    "python-dateutil==2.8.2",
    "python-dotenv==0.19.2",
    "pytz==2021.3",
    "six==1.16.0",
    "SQLAlchemy==1.4.28"
    ]
)