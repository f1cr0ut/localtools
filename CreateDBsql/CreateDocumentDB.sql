CREATE TABLE `document` (
    `id`                INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    `title`             TEXT,
    `description`       TEXT,
    `created`           TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `deleted`           INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE `section` (
    `id`                INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    `document_id`       INTEGER NOT NULL,
    `title`             TEXT,
    `body`              TEXT NOT NULL,
    `section_list_id`   INTEGER,
    `tag_list_id`       INTEGER,
    `created`           TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `deleted`           INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE `section_list` (
    `id`                INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    `section_first`     INTEGER NOT NULL UNIQUE,
    `section_second`    INTEGER NOT NULL UNIQUE,
    `section_third`     INTEGER NOT NULL UNIQUE,
    `section_fourth`    INTEGER NOT NULL UNIQUE,
    `deleted`           INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE `tag_list` (
    `id`                INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    `name`              TEXT NOT NULL UNIQUE,
    `deleted`           INTEGER NOT NULL DEFAULT 0
);
