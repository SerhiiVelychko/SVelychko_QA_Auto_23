import requests


class GitHub:
    def get_user(self, username):
        r = requests.get(f"https://api.github.com/users/{username}")
        body = r.json()

        return body

    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories", params={"q": name}
        )
        body = r.json()

        return body

    def get_emojis(self):
        r = requests.get("https://api.github.com/emojis")
        body = r.json()

        return body

    def get_emoji_image_url(self, emoji_name):
        emojis = self.get_emojis()
        if emoji_name in emojis:
            return emojis[emoji_name]
        return None

    def get_non_existing_emoji_info(self, emoji_name):
        r = requests.get("https://api.github.com/emojis/{emoji_name}")
        return r

    def get_commit(self, owner, repo):
        r = requests.get(
            "https://api.github.com/repos/{owner}/{repo}/commits",
            params={"owner": owner, "repo": repo},
        )
        body = r.json()

        return body

    def get_latest_commits(self, owner, repo):
        r = requests.get("https://api.github.com/repos/{owner}/{repo}/commits")
        body = r.json()

        return body
