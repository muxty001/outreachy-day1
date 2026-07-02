from main import run_application

def test_application_execution():
    # If the function runs completely without crashing, this test passes
    assert run_application() is None 