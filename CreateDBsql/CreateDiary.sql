CREATE TABLE `diary` (
    `id`              INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    `title`           TEXT NOT NULL,
    `body`            TEXT,
    `created`         TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `deleted`         INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE `contents` (
    `id`              INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    `title`           TEXT NOT NULL,
    `parent_id`       INTEGER NOT NULL,
    `data`            BLOB NOT NULL
);
