import sequences


def test_version():
    assert sequences.__version__ == '0.1.0'


def test_explicit():
    seq = sequences.ExplicitSequence('5*n+4*n**2')
    terms = seq.exec(10, True)
    print(terms)


def test_recursive():
    seq2 = sequences.RecursiveSequence('2*an')
    terms = seq2.exec(1, 10, True)
    print(terms)
