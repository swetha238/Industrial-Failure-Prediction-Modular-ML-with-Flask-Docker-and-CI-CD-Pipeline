import os


def test_artifacts_exist():
    base = os.path.join('artificats')
    assert os.path.isdir(base), "artificats directory should exist"
    assert os.path.isfile(os.path.join(base, 'model.pkl')), "model.pkl missing"
    assert os.path.isfile(os.path.join(base, 'processor.pkl')), "processor.pkl missing"
