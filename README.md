# Smart Signals

![Build](https://github.com/grobbles/SmartSignals/actions/workflows/test.yml/badge.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![codecov](https://codecov.io/gh/grobbles/SmartSignals/branch/main/graph/badge.svg?token=GAHKYKS1SD)](https://codecov.io/gh/grobbles/SmartSignals)

# Install 

You can install this package with pip from PyPi.

````bash
pip install SmartSignals
````

# Usage

````python
from smart_signals import *

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