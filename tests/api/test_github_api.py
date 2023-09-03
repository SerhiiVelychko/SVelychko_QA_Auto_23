import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user("defunkt")
    assert user["login"] == "defunkt"


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user("butenkosergii")
    assert r["message"] == "Not Found"


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo("become-qa-auto")
    assert r["total_count"] == 43
    assert "become-qa-auto" in r["items"][0]["name"]


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo("sergiibutenko_repo_non_exist")
    assert r["total_count"] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo("s")
    assert r["total_count"] != 0


@pytest.mark.api
def test_get_emojis(github_api):
    r = github_api.get_emojis()
    print(r)


@pytest.mark.api
def test_get_emoji_image_url(github_api):
    emoji_name = "heart"
    image_url = github_api.get_emoji_image_url(emoji_name)

    assert image_url is not None
    assert (
        "https://github.githubassets.com/images/icons/emoji/unicode/2764.png"
        in image_url
    )


@pytest.mark.api
def test_get_non_existing_emoji_info(github_api):
    non_existing_emoji_name = "non_existing_emoji"
    r = github_api.get_non_existing_emoji_info(non_existing_emoji_name)

    assert r.status_code == 404
    assert "Not Found" in r.text


@pytest.mark.api
def test_get_latest_commits(github_api):
    owner = "SerhiiVelychko"
    repo = "SVelychko_QA_Auto_23"
    r = github_api.get_latest_commits(owner, repo)
    print(r)
