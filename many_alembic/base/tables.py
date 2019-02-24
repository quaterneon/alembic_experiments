from sqlalchemy import Table, MetaData, Integer, Column

metadata = MetaData()

test_table = Table('test_base', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('A', Integer)
                   )
