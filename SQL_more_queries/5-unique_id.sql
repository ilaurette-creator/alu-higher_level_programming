-- Creates the table unique_id on MySQL server with default id 1 and unique constraint
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
