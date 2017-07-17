-- SELECT messages.id, messages.user_id, messages.message, messages.created_at, users.id, users.first_name, users.last_name FROM messages
-- JOIN users
-- ON messages.user_id = users.id;

-- SELECT comments.id, comments.comment, comments.created_at, messages.id, messages.message, users.id, users.first_name, users.last_name FROM comments
-- JOIN messages
-- ON comments.message_id = messages.id
-- JOIN users
-- ON messages.user_id = users.id;

SELECT comments.id AS comment_id, comments.message_id, comments.comment, comments.created_at, messages.id, messages.message, users.id as user_id, users.first_name, users.last_name 
FROM comments 
JOIN messages ON comments.message_id = messages.id 
JOIN users ON comments.user_id = users.id;