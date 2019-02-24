from sqlalchemy import Table, MetaData, Integer, Column

metadata = MetaData(schema='schema1_B')

test_table = Table('test1', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('two', Integer),
                   Column('three', Integer),
                   Column('four', Integer),
                   Column('six', Integer)
                   )
