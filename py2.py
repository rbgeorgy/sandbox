from instapy import InstaPy

session = InstaPy(username="greedy_algorithm", password="emanon", headless_browser=True)
session.login()
session.set_relationship_bounds(enabled=True, max_followers=700, min_followers=40)
session.set_quota_supervisor(enabled=True, sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"], sleepyhead=True, stochastic_flow=True, notify_me=True,
                              peak_likes_hourly=20,
                              peak_likes_daily=450,
                               peak_comments_hourly=20,
                               peak_comments_daily=100,
                                peak_follows_hourly=20,
                                peak_follows_daily=450,
                                 peak_unfollows_hourly=25,
                                 peak_unfollows_daily=402,
                                  peak_server_calls_hourly=None,
                                  peak_server_calls_daily=4700)

#session.unfollow_users(amount=60, instapy_followed_enabled=True, instapy_followed_param="nonfollowers", style="FIFO", unfollow_after=90*60*60, sleep_delay=501)
session.set_delimit_liking(enabled=True, max_likes=150, min_likes=20)
session.set_relationship_bounds(enabled=True,
				   max_followers=900,
				    max_following=1500,
				     min_followers=100,
				      min_following=90,
				       min_posts=10,
                max_posts=500)

session.like_by_tags(['art', 'photo', 'nature', 'people', 'architecture'], amount=10000)

session.end()
