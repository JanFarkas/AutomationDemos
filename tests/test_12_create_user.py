import json
import time
import pytest


with open("create_users.json") as f:
    test_data = json.load(f)


@pytest.mark.parametrize("user_data", test_data)
def test_post_create_user(api_context, user_data):
    start_time = time.time()

    response = api_context.post(
        "/api/users",
        data=user_data
    )

    elapsed_ms = (time.time() - start_time) * 1000

    # HTTP code
    assert response.status == 201

    # response time
    assert elapsed_ms < 1000

    body = response.json()

    # required assertions
    assert "id" in body
    assert "createdAt" in body

    # data integrity
    assert body["name"] == user_data["name"]
    assert body["job"] == user_data["job"]

    # bonus: schema/type validation
    assert isinstance(body["id"], str)
    assert isinstance(body["createdAt"], str)
