CREATE TABLE `related_revision` (
    `id`                INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    `parent_ticket_id`  INTEGER NOT NULL,
    `revision_string`   TEXT NOT NULL,
    `deleted`           INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE `related_ticket_id` (
    `id`                INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    `parent_ticket_id`  INTEGER NOT NULL ,
    `related_ticket_id` INTEGER NOT NULL ,
    `deleted`           INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE `ticket` (
    `id`                INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    `title`             TEXT NOT NULL,
    `body`              TEXT,
    `category`          TEXT NOT NULL DEFAULT 'todo',   /* bug,test,add,remove,proposal,create,delete,investigate,todo */
    `progress`          REAL NOT NULL DEFAULT 0.0,      /* [0.0, 1.0] 1.0 == 100% */
    `priority`          INTEGER,                        /* disallow negative value */
    `start_day`         TEXT,
    `end_day`           TEXT,
    `deadline`          TEXT,
    `created`           TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `finished`          INTEGER NOT NULL DEFAULT 0,
    `deleted`           INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE `ticket_authors` (
    `id`                INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    `parent_ticket_id`  INTEGER NOT NULL,
    `documenter`        TEXT NOT NULL,
    `worker`            TEXT NOT NULL,
    `deleted`           INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE `ticket_tags` (
    `id`                INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    `parent_ticket_id`  INTEGER NOT NULL DEFAULT 0,
    `text`              TEXT NOT NULL,
    `deleted`           INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE `postscript` (
    `id`                INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    `parent_ticket_id`  INTEGER NOT NULL,
    `description`       TEXT NOT NULL,
    `updated_time`      TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE `media` (
    `id`                INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    `parent_ticket_id`  INTEGER NOT NULL,
    `description`       TEXT,
    `data`              BLOB NOT NULL,
    `updated_time`      TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `deleted`           INTEGER NOT NULL DEFAULT 0
);
