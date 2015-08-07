import testtools
import unittest

from tests.test_toscadef import ToscaDefTest
from tests.test_toscatpl import ToscaTemplateTest
from tests.test_exception import ExceptionTest
from tests.test_toscatplvalidation import ToscaTemplateValidationTest
from tests.test_functions import IntrinsicFunctionsTest
from tests.test_properties import PropertyTest
from tests.test_functions import GetAttributeTest
from tests.test_scalarunit import GetNumFromScalarUnitSizePositive
from tests.test_scalarunit import GetNumFromScalarUnitFrequencyNegative
from tests.test_scalarunit import ScalarUnitPositiveTest
from tests.test_scalarunit import GetNumFromScalarUnitFrequencyPositive
from tests.test_scalarunit import GetNumFromScalarUnitTimePositive
from tests.test_scalarunit import GetNumFromScalarUnitSizeNegative

if __name__ == '__main__':
    unittest.main()
