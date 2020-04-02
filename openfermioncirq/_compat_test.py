#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
import warnings

import pytest
import deprecation

import openfermioncirq as ofc
from openfermioncirq._compat import deprecated_test, wrap_module


@deprecation.deprecated()
def f():
    pass


@deprecated_test
def test_deprecated_test():
    warnings.simplefilter('error')
    f()


def test_wrap_module():
    ofc.deprecated_attribute = None
    wrapped_ofc = wrap_module(ofc, {'deprecated_attribute': ('', '')})
    with pytest.deprecated_call():
        _ = wrapped_ofc.deprecated_attribute
