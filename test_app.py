import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_request(client):
    """Test the GET request to the root endpoint."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Having a bum day? Let's make it better! Hit this button:" in response.data

def test_post_request(client):
    """Test the POST request to the root endpoint."""
    response = client.post('/')
    assert response.status_code == 200
    assert any(phrase.encode() in response.data for phrase in [
        "Data never sleeps, but neither do breakthroughs—you're crushing it!",
        "You’re like a neural net—always learning and adapting!",
        "Remember, even NaN values are part of the dataset!",
        "Life’s a gradient descent—keep moving toward your optimum!",
        "Your hard work is the feature everyone notices!",
        "Keep calm and let the algorithm do the heavy lifting!",
        "Debugging life one line of code at a time—keep it up!",
        "Your data game is *outlier-level* impressive!",
        "You're a clustering champ—always finding your center!",
        "Master’s degree: Loading... 90% complete. You’ve got this!",
        "You’re the key to cracking the ultimate dataset: life!",
        "Machine learning? More like *mastered* learning!",
        "A few more semesters, and you’re the top variable in the model!",
        "Data wrangling = life wrangling. You’re doing both like a pro!",
        "Remember, correlation doesn’t imply exhaustion—rest up and conquer!"
    ])

if __name__ == '__main__':
    pytest.main()