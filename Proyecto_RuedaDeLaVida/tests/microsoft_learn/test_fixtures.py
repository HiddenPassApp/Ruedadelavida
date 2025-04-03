import pytest
import tempfile
import os



@pytest.fixture(scope="module")
def tmp_file(request):
    # Create a temporary file that persists beyond the function scope
    temp = tempfile.NamedTemporaryFile(delete=False)

    def create():
        # Returns the path of the temporary file
        return temp.name

    def cleanup():
        # Remove the file after the tests are done
        os.remove(temp.name)

    # Register the cleanup function to be called after the last test in the module
    request.addfinalizer(cleanup)

    return create


def test_file(tmp_file):
    path = tmp_file()
    assert os.path.exists(path)