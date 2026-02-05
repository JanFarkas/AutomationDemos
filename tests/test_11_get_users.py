def test_get_users_page_2(api_context):
    response = api_context.get("/api/users?page=2")

    # required status code check
    assert response.status == 200

    body = response.json()

    # required assertions
    assert "total" in body
    assert "data" in body

    users = body["data"]

    # last_name check
    assert users[0]["last_name"] == "Lawson"
    assert users[1]["last_name"] == "Ferguson"

    # count vs total
    assert len(users) <= body["total"]

    # data types
    for user in users:
        assert isinstance(user["id"], int)
        assert isinstance(user["email"], str)
        assert isinstance(user["first_name"], str)
        assert isinstance(user["last_name"], str)
        assert isinstance(user["avatar"], str)
        print(user["email"])  # debug
