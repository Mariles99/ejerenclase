from funcion import numero_menor

def test_numero_menor():
    assert numero_menor([5,8,3,9,4])==3
    assert numero_menor([7,3,1,5,0])==0
    assert numero_menor([3,2,5])==2