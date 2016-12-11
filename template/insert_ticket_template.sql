/*
-- create ticket
insert into ticket (
    title,
    body,
    category,
    progress,
    priority,
    start_day,
    end_day,
    deadline
) values (
    '',
    '',
    'bug',
    0.0,
    10,
    '2016-01-01',
    '2016-01-01',
    '2016-01-01'
);

-- add related ticket info
insert into related_ticket_id (
    parent_ticket_id,
    related_ticket_id
) values (
    0,
    0
);

-- add revision info
insert into related_revision (
    parent_id,
    revision_string
) values (
    0,
    ''
);

-- add ticket authors
insert into ticket_authors (
    parent_ticket_id,
    documenter,
    worker
) values (
    0,
    '',
    ''
);

-- add ticket tags
insert into ticket_tags (
    parent_ticket_id,
    text
) values (
    0,
    ''
);

-- add ticket timestamp
insert into ticket_last_update_stamp (
    parent_id,
    description
) values (
    0,
    ''
);
*/
