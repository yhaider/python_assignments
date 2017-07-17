-- SELECT * FROM friendships;
-- INSERT INTO users (first_name, last_name, created_at, updated_at)
-- VALUES ('Yasmeen', 'Haider', NOW(), NOW());
-- INSERT INTO users (first_name, last_name, created_at, updated_at)
-- VALUES ('Isaac', 'Suntag', NOW(), NOW()); 
-- INSERT INTO users (first_name, last_name, created_at, updated_at)
-- VALUES ('Jane', 'Doe', NOW(), NOW()); 
-- INSERT INTO users (first_name, last_name, created_at, updated_at)
-- VALUES ('John', 'Doe', NOW(), NOW());

-- SELECT * FROM friendships;
-- INSERT INTO friendships (created_at, updated_at, user_id, friend_id)
-- VALUES (NOW(),NOW(), 1, 2);
-- INSERT INTO friendships (created_at, updated_at, user_id, friend_id)
-- VALUES (NOW(),NOW(), 2, 1);
-- INSERT INTO friendships (created_at, updated_at, user_id, friend_id)
-- VALUES (NOW(),NOW(), 3, 4);
-- INSERT INTO friendships (created_at, updated_at, user_id, friend_id)
-- VALUES (NOW(),NOW(), 4, 3);
-- INSERT INTO friendships (created_at, updated_at, user_id, friend_id)
-- VALUES (NOW(),NOW(), 2, 3);
-- INSERT INTO friendships (created_at, updated_at, user_id, friend_id)
-- VALUES (NOW(),NOW(), 3, 2);
-- INSERT INTO friendships (created_at, updated_at, user_id, friend_id)
-- VALUES (NOW(),NOW(), 1, 4);
-- INSERT INTO friendships (created_at, updated_at, user_id, friend_id)
-- VALUES (NOW(),NOW(), 4, 1);
-- 
-- SELECT * FROM users 
-- LEFT JOIN friendships ON users.id = friendships.user_id
-- LEFT JOIN users as user2 ON friendships.friend_id = user2.id;
-- 

SELECT users.first_name, users.last_name, user2.first_name AS friend_first_name, user2.last_name AS friend_last_name
FROM users
LEFT JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users as user2 ON friendships.friend_id = user2.id;
