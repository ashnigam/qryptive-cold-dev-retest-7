import hashlib
def test_legacy_digest():
    assert len(hashlib.md5(b'fixture').digest()) == 16
