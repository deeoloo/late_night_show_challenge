# Late Show Project

## Overview

A web application for managing and viewing episodes, guests, and appearances on a late-night talk show. This project provides an API backend with a potential frontend interface to browse show episodes, guest information, and ratings.

## Features

- **Episode Management**: Track show episodes with dates and episode numbers
- **Guest Database**: Maintain information about show guests and their occupations
- **Appearance Tracking**: Record guest appearances on specific episodes with ratings
- **API Endpoints**: RESTful API for accessing all data
- **Data Relationships**: Model complex relationships between episodes, guests, and appearances

## Technologies Used

- **Backend**: 
  - Python
  - Flask
  - SQLAlchemy (ORM)
  - PostgreSQL (database)
  - Flask-Migrate (database migrations)
  
- **Frontend** (if applicable):
  - HTML/CSS/JavaScript
  - React/Vue (if used)
  - Bootstrap/Tailwind (if used)

## Installation

### Prerequisites

- Python 3.8+
- PostgreSQL
- pip

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/late_night_show_challenge.git
   cd late_show
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the root directory with:
   ```
   DATABASE_URL=postgresql://username:password@localhost/late_show
   FLASK_APP=app.py
   FLASK_ENV=development
   SECRET_KEY=your-secret-key
   ```

5. Initialize the database:
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

6. Seed the database (optional):
   ```bash
   python seed.py
   ```

7. Run the application:
   ```bash
   flask run
   ```

## API Documentation

### Endpoints

#### Episodes
- `GET /episodes` - List all episodes
- `GET /episodes/<id>` - Get a specific episode
- `POST /episodes` - Create a new episode
- `PATCH /episodes/<id>` - Update an episode
- `DELETE /episodes/<id>` - Delete an episode

#### Guests
- `GET /guests` - List all guests
- `GET /guests/<id>` - Get a specific guest
- `POST /guests` - Create a new guest
- `PATCH /guests/<id>` - Update a guest
- `DELETE /guests/<id>` - Delete a guest

#### Appearances
- `GET /appearances` - List all appearances
- `GET /appearances/<id>` - Get a specific appearance
- `POST /appearances` - Create a new appearance
- `PATCH /appearances/<id>` - Update an appearance
- `DELETE /appearances/<id>` - Delete an appearance

## Database Schema

```
Episodes
- id: Integer (PK)
- date: Date
- number: Integer

Guests
- id: Integer (PK)
- name: String
- occupation: String

Appearances
- id: Integer (PK)
- rating: Integer
- guest_id: Integer (FK to Guests)
- episode_id: Integer (FK to Episodes)
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

