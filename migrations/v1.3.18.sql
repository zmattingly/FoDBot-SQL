INSERT INTO badge_info (badge_name, badge_filename, badge_url, quadrant, time_period, franchise, reference) VALUES ("Friends Of DeSoto", "Friends_Of_DeSoto.png", "https://maximumfun.org/podcasts/greatest-generation/", "Alpha", "2000s", "The Greatest Generation", "https://maximumfun.org/episodes/greatest-generation/greatest-generation-ep-162-friends-desoto-s7e11/");
INSERT INTO badges (user_discord_id, badge_name) SELECT discord_id, "Friends_Of_DeSoto.png" FROM users;