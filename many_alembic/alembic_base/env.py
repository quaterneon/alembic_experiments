from __future__ import with_statement

from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context
import base.tables as base_t

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = base_t.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


exclude_tables = []
exclude_indices = []


def include_object(obj, name, typ, reflected, compare_to):
    """
    Objects to include/exclude for/from consideration when creating autogenerated revisions.
    http://alembic.zzzcomputing.com/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.include_object
    Args:
        obj:
        name:
        typ:
        reflected:
        compare_to:

    Returns:

    """
    if typ == "table" and name in exclude_tables:
        return False
    elif typ == "index" and name in exclude_indices:
        return False
    elif typ == 'table' and obj.schema != target_metadata.schema:  # New, might need to include sequences
        return False

    return True



def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True,
        include_schemas=True,  # New
        version_table_schema=target_metadata.schema,  # New
        include_object=include_object  # New
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata,
            include_schemas=True,  # New
            version_table_schema=target_metadata.schema,  # New
            include_object=include_object  # New
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
