from main import qushish

assert qushish(1,2) == 3
assert qushish(1,"1") == 2
assert qushish("1","1") == 2
assert qushish("a", "b") == "ab"
assert qushish("a", "2") == "a2"
