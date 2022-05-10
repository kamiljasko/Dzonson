def plural(n):
   if n >= 2 or n == 0:
       return True
   else:
       return False


if __name__ == '__main__':
    assert (plural(0) == True)
    assert (plural(1) == False)
    assert (plural(100) == True)
