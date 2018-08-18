import pytest

import pythotk as tk


# https://docs.pytest.org/en/latest/doctest.html#the-doctest-namespace-fixture
@pytest.fixture(autouse=True)
def add_tk(doctest_namespace):
    doctest_namespace['tk'] = tk


@pytest.fixture
def deinit_threads():
    """Make sure that init_threads() has not been called when test completes.

    If you have a test like this...

        def test_tootie():
            tk.init_threads()

    ...the test will cause problems for any other tests that also call
    init_threads(), because it can't be called twice. Using this fixture in
    test_tootie() would fix that problem.
    """
    yield
    tk.after_idle(tk.quit)
    tk.run()
