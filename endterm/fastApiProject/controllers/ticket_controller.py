from fastapi import Depends, HTTPException, Request
from sqlalchemy.orm import Session

import schemas
from main import app, ticket_log_filename, log_to_file, create_log, get_db, TokenVerifier
from crud import ticket_crud
