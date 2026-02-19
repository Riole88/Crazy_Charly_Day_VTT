DROP TABLE IF EXISTS user2box;
DROP TABLE IF EXISTS article2box;
DROP TABLE IF EXISTS article;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS box;

CREATE TYPE CATEGORY AS ENUM ('SOC','FIG','CON','EXT','EVL','LIV');
CREATE TYPE AGE AS ENUM ('BB','PE','EN','AD');
CREATE TYPE STATE AS ENUM ('N','TB','B');

CREATE TABLE article (
    id UUID PRIMARY KEY,
    designation VARCHAR(255),
    category CATEGORY,
    age AGE,
    state STATE,
    price DECIMAL(8,2),
    weight DECIMAL(8,2)
);

CREATE TABLE users (
    id UUID PRIMARY KEY,
    email VARCHAR(50),
    last_name VARCHAR(50),
    first_name VARCHAR(50),
    password VARCHAR(255),
    role VARCHAR(20) DEFAULT 'user',
    preferences VARCHAR(255)
);

CREATE TABLE box (
    id UUID PRIMARY KEY,
    name VARCHAR(50),
    total_price  DECIMAL(8,2),
    total_weight DECIMAL(8,2),
    score DECIMAL(8,0)
);

CREATE TABLE user2box (
    id UUID PRIMARY KEY,
    id_user UUID,
    id_box UUID,
    FOREIGN KEY (id_user) REFERENCES users(id) ON DELETE SET NULL,
    FOREIGN KEY (id_box) REFERENCES box(id) ON DELETE SET NULL
);

CREATE TABLE article2box (
    id UUID PRIMARY KEY,
    id_article UUID,
    id_box UUID,
    FOREIGN KEY (id_article) REFERENCES article(id) ON DELETE SET NULL,
    FOREIGN KEY (id_box) REFERENCES box(id) ON DELETE SET NULL
);