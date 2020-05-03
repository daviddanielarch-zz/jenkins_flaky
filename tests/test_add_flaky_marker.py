from utils.add_flaky_marker import add_flaky_marker


def test_marker_gets_added_with_class():
    original_file = """
class TestClass:

    def other_func1(self):
        pass

    def function_to_mark(self, arg1, arg2):
        pass

    def other_func2(self):
        pass
"""

    new_file = add_flaky_marker(original_file, 'function_to_mark', 'TestClass')
    assert new_file.splitlines() == """
class TestClass:

    def other_func1(self):
        pass

    @pytest.mark.flaky
    def function_to_mark(self, arg1, arg2):
        pass

    def other_func2(self):
        pass
""".splitlines()


def test_marker_gets_added_without_class():
    original_file = """
def other_func1(self):
    pass

def function_to_mark(self, arg1, arg2):
    pass

def other_func2(self):
    pass
"""

    new_file = add_flaky_marker(original_file, 'function_to_mark')
    assert new_file.splitlines() == """
def other_func1(self):
    pass

@pytest.mark.flaky
def function_to_mark(self, arg1, arg2):
    pass

def other_func2(self):
    pass
""".splitlines()


def test_marker_gets_added_without_class_and_other_decorator():
    original_file = """
def other_func1(self):
    pass

@pytest.ads
@papapa
def function_to_mark(self, arg1, arg2):
    pass

def other_func2(self):
    pass
"""

    new_file = add_flaky_marker(original_file, 'function_to_mark')
    assert new_file.splitlines() == """
def other_func1(self):
    pass

@pytest.mark.flaky
@pytest.ads
@papapa
def function_to_mark(self, arg1, arg2):
    pass

def other_func2(self):
    pass
""".splitlines()
