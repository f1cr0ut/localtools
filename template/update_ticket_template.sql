/*
update ticket set 
title = 
'',
body =
'',
category = '',
progress = 0.0,
priority = 0,
start_day = '2016-01-01',
end_day = '2016-01-01',
deadline = '2016-01-01',
finished = 0,
deleted = 0

where id = 0;

insert into related_revision(
    parent_id,
    revsion_string,
    deleted
)values(
    0,
    '',
    0
);

insert into related_ticket_id(
    parent_ticket_id,
    related_ticket_id,
    deleted
)values(
    0,
    0,
    0
);

insert into ticket_authors(
    parent_ticket_id,
    documenter,
    worker,
    deleted
)values(
    0,
    '',
    '',
    0
);

insert into ticket_tags(
    parent_ticket_id,
    text,
    deleted
)values(
    0,
    '',
    0
);

insert into ticket_last_update_stamp(
    parent_id,
    description
)values(
    0,
    ''
);
*/
