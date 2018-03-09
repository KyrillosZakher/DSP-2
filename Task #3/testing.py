import timeit

cy = timeit.timeit('exapmle_cy.test(5)', setup = 'import example_cy', number = 100)
py = timeit.timeit('exapmle_py.test(5)', setup = 'import example_py', number = 100)


print(cy,py)
print('Cython is {}x faster'.format(py/cy))