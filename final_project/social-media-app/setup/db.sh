#!/bin/bash
set -eu

# ==================================================================================== #
# VARIABLES
# ==================================================================================== #

# ==================================================================================== #
# SCRIPT LOGIC
# ==================================================================================== #

# Set up the social_media DB and create a user account with the password entered earlier.
sudo -i -u postgres psql -c "CREATE DATABASE social_media"
sudo -i -u postgres psql -d social_media -c "CREATE ROLE social_media WITH LOGIN PASSWORD 'social_media'"
sudo -i -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE social_media TO social_media;"
sudo -i -u postgres psql -c "ALTER DATABASE social_media OWNER TO social_media;"

# 

echo "Script complete!"
