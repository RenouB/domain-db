from setuptools import setup

setup(
  name='sqlalchemy_tools',
  version='0.0.1',
  author='Renou Benteau',
  author_email='rebe01@dfki.de',
  packages=['sqlalchemy_tools'],
  description='Generate SQLAclhemy database url, connect to session',
  install_requires=[
      "python-dotenv==0.19.2",
      "psycopg2==2.9.2",
      "SQLAlchemy==1.4.28"

  ]
)