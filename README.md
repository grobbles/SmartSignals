# Smart Signals

![Build](https://github.com/grobbles/SmartSignals/actions/workflows/release.yml/badge.svg)
[![codecov](https://codecov.io/gh/grobbles/SmartSignals/branch/main/graph/badge.svg?token=GAHKYKS1SD)](https://codecov.io/gh/grobbles/SmartSignals)
[![PyPi version](https://badgen.net/pypi/v/SmartSignals/)](https://pypi.com/project/SmartSignals)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is a small lib for the signal-slot-pattern. This corresponds to a modification of the observer pattern. It originally comes from QT.

The input types are checked to ensure that they also correspond to the definition. The default python data types (str, int, float, list) and also the typing data types (List[str], Dict[str, int]) are supported. In addition, the log can be
used to track which signal called which slot for error diagnosis.

# Install

You can install this package with pip tool from https://pypi.org/.

````bash
pip install SmartSignals
````

# Usage

````python
import logging

from smart_signals import SmartSignal, SmartSignalSlot

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s | %(levelname)-10.10s | %(name)-30.30s | %(message)s")


class Test:
    @SmartSignalSlot(str)
    def slot(self, message: str):
        print(message)
        pass


test = Test()
signal = SmartSignal(str)
signal.connect(test.slot)
signal.emit("message")
````

Log output

````
2022-06-07 21:16:52 | DEBUG      | SmartSignal                    | emit signal from: .\PySignals\smart_signals_tests\test_smart_signals.py:test_py_signal_check_emit_type_string:145 to slot <function TestPySignal.test_py_signal_check_emit_type_string.<locals>.signal_slot_with_typ_list_of_string at 0x000001B9259A6F70>
````