SELECT
	user.first_name AS first_name,
	user.last_name AS last_name,
	user2.first_name AS friend_first_name,
	user2.last_name AS friend_last_name
FROM
	users AS user
		JOIN
	friendships ON user.id = friendships.user_id
		JOIN
	users AS user2 ON friendships.friend_id = user2.id
ORDER BY user2.last_name;
