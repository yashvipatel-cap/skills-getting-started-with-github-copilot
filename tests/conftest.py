import pytest
from fastapi.testclient import TestClient
from src.app import app, activities
import copy


@pytest.fixture
def client():
    """Provide a test client for the FastAPI app"""
    return TestClient(app)


@pytest.fixture
def reset_activities():
    """Reset activities to initial state before each test"""
    # Store original state
    original_activities = copy.deepcopy(activities)
    
    # Run the test
    yield
    
    # Restore original state
    activities.clear()
    activities.update(original_activities)
