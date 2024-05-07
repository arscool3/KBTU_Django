from alembic import context
from sqlalchemy import engine_from_config, MetaData
from app.models.models import User

# Initialize metadata
metadata = MetaData()

# Bind metadata to the engine
engine = engine_from_config(context.config.get_section('alembic'), prefix='sqlalchemy.')
metadata.bind = engine

# Reflect existing database tables
metadata.reflect(bind=engine)

# Include the metadata in the context
with engine.connect() as connection:
    context.configure(
        connection=connection,
        target_metadata=metadata,
        render_as_batch=True  # Enable render as batch mode
    )

    # Provide metadata to the context
    context.run_migrations()