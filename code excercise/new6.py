def person(name, **data):

    print(name)

    for i,j in data.items():
        print(i,j)

person('sanket',age=20,city='surat',mo_no=432525)