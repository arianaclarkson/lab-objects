
from lab_classes import User, Tweet


def build_feed():
    # Create users
    user1 = User('volleyballcaptain')
    user2 = User('teamlibero')
    users = [user1, user2]

    # Create posts
    post1 = Tweet('volleyballcaptain',
                  'Game day today! #Volleyball')
    post2 = Tweet('teamlibero',
                  'Ready for the big game! #GoTeam')
    post3 = Tweet('volleyballcaptain',
                  'We won! #Victory')

    posts = [post1, post2, post3]

    # User interactions
    user1.follow()
    user2.follow()
    user1.unfollow()

    # Post interactions
    post1.like()
    post2.like()
    post1.unlike()

    return users, posts


def main():
    users, posts = build_feed()

    print('USERS:')
    for user in users:
        print(user)

    print('POSTS:')
    for post in posts:
        print(post)
        print(post.hashtags())


if __name__ == '__main__':
    main()
