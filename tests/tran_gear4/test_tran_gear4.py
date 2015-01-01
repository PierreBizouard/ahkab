from __future__ import unicode_literals, print_function
from ahkab.testing import NetlistTest
from ahkab import options
options.plotting_show_plots = False

def test():
    nt = NetlistTest('tran_gear4')
    nt.setUp()
    nt.test()
    nt.tearDown()

test.__doc__ = "GEAR4 DF TRAN test"

if __name__ == '__main__':
    nt = NetlistTest('tran_gear4')
    nt.setUp()
    nt.test()
