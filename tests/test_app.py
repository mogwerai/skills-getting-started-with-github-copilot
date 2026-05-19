import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    # Arrange: (nothing to set up)
    # Act
    response = client.get("/activities")
    # Assert
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_signup_and_unregister():
    # Arrange
    email = "testuser@mergington.edu"
    activity = "Chess Club"

    # Act: Signup
    resp_signup = client.post(f"/activities/{activity}/signup", params={"email": email})
    # Assert
    assert resp_signup.status_code == 200 or "already signed up" in resp_signup.text

    # Act: Duplicate signup
    resp_dup = client.post(f"/activities/{activity}/signup", params={"email": email})
    # Assert
    assert resp_dup.status_code == 400

    # Act: Unregister
    resp_unreg = client.delete(f"/activities/{activity}/unregister", params={"email": email})
    # Assert
    assert resp_unreg.status_code == 200

    # Act: Unregister again
    resp_unreg2 = client.delete(f"/activities/{activity}/unregister", params={"email": email})
    # Assert
    assert resp_unreg2.status_code == 400
