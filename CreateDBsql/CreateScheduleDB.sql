CREATE TABLE `schedule` (
    `id`              INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    `title`           TEXT NOT NULL,
    `body`            TEXT,
    `all_day`         INTEGER NOT NULL DEFAULT 0,
    `deadline`        TEXT,
    `created`         TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `finished`        INTEGER NOT NULL DEFAULT 0,
    `deleted`         INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE `additional_info` (
    `id`              INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    `parent_id`       INTEGER NOT NULL,
    `description`     TEXT,
    `start_day`       TEXT,
    `end_day`         TEXT,
    `place`           TEXT,
    `price`           INTEGER,
    `price_unit`      TEXT
);
