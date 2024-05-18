# from fastapi.testclient import TestClient
# from main import app
# import pytest
# import pytest_asyncio
# import httpx
# from typing import AsyncIterator

# import requests_mock
# # from sending_pdf.stat_gov import get_by_bin_stat_egov

# client = TestClient(app)
# @pytest_asyncio.fixture()
# async def test_client() -> AsyncIterator[httpx.AsyncClient]:
#     async with httpx.AsyncClient(app=app, base_url="http://test") as test_client:
#         yield test_client
    
  
def test_mock():
    assert 1 == 1

# def test_create_user() -> None:
#     response = client.post("/user/register", json={
#     "name": "aAAasd",
#     "surname": "ydsa",
#     "email": "clkasdasr@example.com",
#     "password": "raadsddasiasdasdng",
#     "iin": "stridsasasdaasdg",
#     "call": "strinag",
#     "tg_id": "striaadsds"
#     })
#     assert response.status_code == 200
    
# @pytest.mark.asyncio
# async def test_get_user_by_email(test_client) -> None:
#     email_data = {
#         "email": "user2@example.com"
#     }
#     email = email_data["email"]
#     response = await test_client.get(f"/user/user2@example.com")
    
#     assert response.status_code == 200

# def test_login_success():
#     # данные для тестирования успешного логина
#     login_data = {
#         "username": "user3@example.com",
#         "password": "string"
#     }
#     response = client.post("/login/token", data=login_data)
#     assert response.status_code == 200
#     assert "access_token" in response.json()
#     assert response.json()["token_type"] == "bearer"

# @pytest.mark.asyncio  
# async def test_get_manager(test_client) -> None:
#     response = await test_client.get("/manager/apps")
#     assert response.status_code == 200
    

# # def create_moderation_request(token: str, changes: dict):
# #     headers = {"Authorization": f"Bearer {token}"}
# #     response = client.post("/moderation/create/", json={"fields_to_change": changes}, headers=headers)
# #     assert response.status_code == 201
# #     return response.json()["id"]

# # def send_mock_request(bin: str, response_data: dict):
# #     with requests_mock.Mocker() as m:
# #         m.get(f"https://old.stat.gov.kz/api/juridical/counter/api/?bin={bin}&lang=en", json=response_data)
# #         return get_by_bin_stat_egov(bin)

# def assert_response(response, status_code: int, key: str = None, value = None):
#     assert response.status_code == status_code
#     if key:
#         assert response.json()[key] == value # Adjust according to your response structure
# def test_authorized_endpoint():
#     # Obtain the JWT token from the login response
#     token = login_and_get_token("admin@example.com", "None")

#     # Use the token in the Authorization header for subsequent requests
#     headers = {"Authorization": f"Bearer {token}"}
#     response = client.get("/moderation", headers=headers)

#     # Perform your assertions here
#     assert response.status_code == 200
#     # More assertions based on the expected response
# def test_signup_success():
#     # Assuming your SignUpSchema includes fields like email and phone_number
#     user_data = {
#         'email': "user@example.com",
#         'phone_number': "1234567890",
#         'first_name': "Name",
#         'last_name': "LastName",
#         'address': "Address",
#         'password': "Password",
#         'telegram_chat_id': "000"
#     }
#     response = client.post("/signup/", json=user_data)
#     assert_response(response, 201, 'message', user_data)

# def test_signup_existing_email():
#     response = client.post("/signup/", json={'email': "user@example.com", 'phone_number': "0987654321"})
#     assert_response(response, 400, 'detail', "User by that email already registered")

# def test_signup_existing_phone():
#     response = client.post("/signup/", json={'email': "someuser@example.com", 'phone_number': "1234567890"})
#     assert_response(response, 400, 'detail', "User by that phone number already exist")
# def test_login_functions():
#     test_cases = [
#         {'email': 'newuser@example.com', 'password': 'Password', 'status': 200, 'key': 'access_token'},
#         {'email': 'newuser@example.com', 'password': 'wrongpassword', 'status': 400},
#         {'email': 'nonexistent@example.com', 'password': 'anyPassword', 'status': 400}
#     ]
#     for case in test_cases:
#         response = client.post("/login/", json={'email': case['email'], 'password': case['password']})

# def test_moderation_create_success():
#     token = login_and_get_token('newuser@example.com', 'Password')
#     response = create_moderation_request(token, {"name": "NewName"})
#     assert response

# def test_get_by_bin_stat_egov():
#     test_cases = [
#         {"bin": "1234567890", "response": {"success": True, "obj": {"bin": "1234567890", "name": "Test Company"}}, "expected": {"bin": "1234567890", "name": "Test Company"}},
#         {"bin": "nonexistent", "response": {}, "expected": {}}
#     ]
#     for case in test_cases:
#         result = send_mock_request(case["bin"], case["response"])
#         assert result == case["expected"]

# def test_moderation_request_approve():
#     user_token = login_and_get_token('newuser@example.com', 'Password')
#     admin_token = login_and_get_token('admin@example.com', 'None')
#     request_id = create_moderation_request(user_token, {"first_name": "NewName"})
#     headers = {"Authorization": f"Bearer {admin_token}"}
#     response = client.post(f"/moderation/{request_id}/approve/", headers=headers)
#     assert_response(response, 201)
