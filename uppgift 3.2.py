års_kort=int(input("hur mycket kostar ett årskort?"))
engångs_kort=int(input("hur mycket kostar ett engångskort?"))
antal_besök=int(input("hur många gånger planerar du att besöka under ett år?"))
total_kostnad=antal_besök*engångs_kort
if total_kostnad<års_kort:
    print("års kort är inte värt det")
else:
    print("det är värt att köpa årskort")