from instaloader import Instaloader, Profile
# print(dir(Instaloader))
L = Instaloader()
username = "laakou0"#input("ادخل اسم الحساب: ")
password ="ism123.."#input("ادخل كلمة السر: ")
L.context.login(username, password)
profile = Profile.from_username(L.context, username)

print("Profile ID:", profile.userid)
print("Followers:", profile.followers)
print("Followees:", profile.followees)

# post download ----------------------------------------
# # while True:
#     You_want = input("هل تريد تحميل اخر منشور? (Yes/No) ")
#     if You_want == "Y":
#         for post in profile.get_posts():
#
#             L.download_post(post, "PostDownload")
#             # Download only the latest post for this example
#             break
#     if You_want == "N":
#         print("Exiting..."

while True:
    You_want = input("هل تريد تحميل اخر منشور? (Yes/No) ")
    if You_want == "Y":
        for post in profile.get_posts():

            L.download_post(post, "PostDownload")
            # Download only the latest post for this example
            break
    if You_want == "N":
        print("Exiting...")

# -------------------------------------------------------






# ('_get_id_filename', 'anonymous_copy', 'check_profile_id',
#  'close', 'download_feed_posts', 'download_hashtag',
#  'download_hashtag_profilepic', 'download_highlight_cover',
#  'download_highlights', 'download_igtv', 'download_location',
#  'download_pic', 'download_post', 'download_profile', 'download_profilepic',
#  'download_profilepic_if_new', 'download_profiles', 'download_saved_posts',
#  'download_stories', 'download_storyitem', 'download_tagged',
#  'download_title_pic', 'format_filename', 'format_filename_within_target_path',
#  'get_explore_posts', 'get_feed_posts', 'get_hashtag_posts', 'get_highlights',
#  'get_location_posts', 'get_stories', 'interactive_login', 'load_profile_id', '
#                                                                               ''
#  load_session', 'load_session_from_file', 'login','
#  ' 'posts_download_loop', 'save_caption', 'save_location','
#  ' 'save_metadata_json', 'save_profile_id', 'save_session', '
#  ''save_session_to_file', 'test_login', 'two_factor_login', 'update_comments')
#     profile.download()
