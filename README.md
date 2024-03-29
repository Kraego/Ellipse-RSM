# Adapted Rubber Sheet Model (RSM)

## About

In the need for unwrapping a ellipse instead of a circle, during my master-thesis (https://opus.fhv.at/frontdoor/index/index/docId/4530)
this adapted version of the Rubber Sheet Model (RSM) was created. And served it's purpose. Since in my
usecase the thickness is allways fixed there is **no normalization** as in the original
method, regarding the radius (or axis increasement in this case).

The original RSM by Daugman see:

*Daugman, J. (Jan. 2004). “How iris recognition works”. In: IEEE Transactions
on Circuits and Systems for Video Technology 14.1. Conference Name: IEEE
Transactions on Circuits and Systems for Video Technology, pp. 21–30. issn:
1558-2205. doi: 10.1109/TCSVT.2003.818350.*

The implementation is a altered version of https://github.com/YifengChen94/IrisReco.

## Content

* *2_RSM_Try.ipynb* - Jupyter book with tryouts
* *adaptedRSM.py* - Concrete implementation of the idea
* *math_utils.py* - Helper functions for RSM
