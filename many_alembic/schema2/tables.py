from sqlalchemy import Table, MetaData, Integer, Column

metadata = MetaData(schema='schema2')

test_table = Table('test2', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('other', Integer, nullable=True),
                   )
