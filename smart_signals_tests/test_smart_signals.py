import logging
import time
import typing
from typing import List
from unittest import TestCase

from smart_signals.smart_signals import SmartSignal, SmartSignalWrongDataTypeException, SmartSignalSlot, SmartSlotWrongDataTypeException, SmartSignalWrongSlotTypeException

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s | %(levelname)-10.10s | %(name)-30.30s | %(message)s")
log = logging.getLogger()


class TestPySignal(TestCase):
    flag = False
    flag_1 = False
    flag_2 = False

    def setUp(self):
        self.flag = False
        self.flag_1 = False
        self.flag_2 = False
        pass

    def test_py_signal_check_callable(self):
        signal = SmartSignal(str, str)
        with self.assertRaises(SmartSignalWrongSlotTypeException):
            signal.connect(1)

    def test_py_signal_add_slot(self):
        def signal_slot():
            self.flag = True
            pass

        signal = SmartSignal()
        signal.connect(signal_slot)
        assert signal_slot in signal.slots

    def test_py_signal_string(self):
        def signal_slot():
            self.flag = True
            pass

        signal = SmartSignal()
        signal.connect(signal_slot)
        assert str(signal) == "PySignal( multithreading: 'False' )"

        signal = SmartSignal(name="TestSignal")
        signal.connect(signal_slot)
        assert str(signal) == "PySignal( name: 'TestSignal', multithreading: 'False' )"

    def test_py_signal_disconnect(self):
        def signal_slot():
            self.flag = True
            pass

        signal = SmartSignal()
        signal.connect(signal_slot)
        assert signal_slot in signal.slots
        assert signal.disconnect(signal_slot)
        assert signal_slot not in signal.slots

    def test_py_signal_try_disconnect(self):
        def signal_slot():
            pass

        signal = SmartSignal()
        assert not signal.disconnect(signal_slot)

    def test_py_signal_reset_all_connection(self):
        def signal_slot():
            self.flag = True
            pass

        signal = SmartSignal()
        signal.connect(signal_slot)
        assert signal_slot in signal.slots
        signal.reset()
        assert signal_slot not in signal.slots

    def test_py_signal(self):
        def signal_slot():
            self.flag = True
            pass

        signal = SmartSignal()
        signal.connect(signal_slot)
        signal.emit()

        assert self.flag, "The signal is not transmitted or received!!"

    def test_py_signal_multithreading(self):
        def signal_slot():
            self.flag = True
            pass

        signal = SmartSignal(multithreading=True)
        signal.connect(signal_slot)
        signal.emit()
        time.sleep(1)
        assert self.flag, "The signal is not transmitted or received!!"

    def test_py_signal_with_two_slots(self):
        def signal_slot_1():
            self.flag_1 = True

        def signal_slot_2():
            self.flag_2 = True

        signal = SmartSignal()
        signal.connect(signal_slot_1)
        signal.connect(signal_slot_2)
        signal.emit()

        assert self.flag_1 and self.flag_2, "The signal is not transmitted or received!!"

    def test_py_signal_emit_a_string(self):
        def signal_slot_with_typ_string(test_message: str):
            if "fuu" in test_message:
                self.flag = True

        signal = SmartSignal(str)
        signal.connect(signal_slot_with_typ_string)
        signal.emit("fuu")

        assert self.flag, "The signal is not transmitted or received!!"

    def test_py_signal_emit_a_list(self):
        def signal_slot_with_typ_list_of_string(test_message: list):
            if "fuu" in test_message:
                self.flag = True

        signal = SmartSignal(list)
        signal.connect(signal_slot_with_typ_list_of_string)
        signal.emit(["fuu"])

        assert self.flag, "The signal is not transmitted or received!!"

    def test_py_signal_check_emit_type_string(self):
        def signal_slot_with_typ_list_of_string(test_message: list):
            if "fuu" in test_message:
                self.flag = True

        signal = SmartSignal(str)
        signal.connect(signal_slot_with_typ_list_of_string)
        signal.emit("fuu")

        assert self.flag, "The signal is not transmitted or received!!"

    def test_py_signal_check_emit_type_string__wrong_type(self):
        def signal_slot_with_typ_list_of_string(test_message: list):
            if "fuu" in test_message:
                self.flag = True

        signal = SmartSignal(str)
        signal.connect(signal_slot_with_typ_list_of_string)

        with self.assertRaises(SmartSignalWrongDataTypeException):
            signal.emit(1)
        assert not self.flag

    def test_py_signal_check_emit_type_strings(self):
        def signal_slot_with_typ_list_of_string(message_1, message_2):
            if "fuu" in message_1 and "faa" == message_2:
                self.flag = True
            pass

        signal = SmartSignal(str, str)
        signal.connect(signal_slot_with_typ_list_of_string)
        signal.emit("fuu", "faa")

        assert self.flag, "The signal is not transmitted or received!!"

    def test_py_signal_check_emit_type_strings__wrong_type(self):
        def signal_slot_with_typ_list_of_string(message_1, message_2):
            if "fuu" in message_1 and "faa" == message_2:
                self.flag = True

        signal = SmartSignal(str, str)
        signal.connect(signal_slot_with_typ_list_of_string)

        with self.assertRaises(SmartSignalWrongDataTypeException):
            signal.emit("fuu", 1)
        assert not self.flag

    def test_py_signal_check_emit_type_list(self):
        def signal_slot_with_typ_list_of_string(test_message: list):
            if "fuu" in test_message:
                self.flag = True
            pass

        signal = SmartSignal(List[str])
        signal.connect(signal_slot_with_typ_list_of_string)
        signal.emit(["fuu"])

        assert self.flag, "The signal is not transmitted or received!!"

    def test_py_signal_check_emit_type_list__wrong_type(self):
        def signal_slot_with_typ_list_of_string(test_message: list):
            if "fuu" in test_message:
                self.flag = True

        signal = SmartSignal(List[str])
        signal.connect(signal_slot_with_typ_list_of_string)

        with self.assertRaises(SmartSignalWrongDataTypeException):
            signal.emit("fuu")
        assert not self.flag

    def test_py_signal_check_emit_type_list__wrong_element_in_list(self):
        def signal_slot_with_typ_list_of_string(test_message: list):
            if "fuu" in test_message:
                self.flag = True

        signal = SmartSignal(List[str])
        signal.connect(signal_slot_with_typ_list_of_string)

        with self.assertRaises(SmartSignalWrongDataTypeException):
            signal.emit(["fuu", 1])
        assert not self.flag

    def test_py_signal_check_emit_type_dict(self):
        def signal_slot_with_typ_list_of_string(test_message):
            if {"fuu": "faa"} == test_message:
                self.flag = True

        signal = SmartSignal(typing.Dict[str, str])
        signal.connect(signal_slot_with_typ_list_of_string)
        signal.emit({"fuu": "faa"})

        assert self.flag, "The signal is not transmitted or received!!"

    def test_py_signal_check_emit_type_dict__wrong_key_type(self):
        def signal_slot_with_typ_list_of_string(test_message):
            if {"fuu": "faa"} == test_message:
                self.flag = True

        signal = SmartSignal(typing.Dict[str, str])
        signal.connect(signal_slot_with_typ_list_of_string)
        with self.assertRaises(SmartSignalWrongDataTypeException):
            signal.emit({1: "faa"})
        assert not self.flag

    def test_py_signal_check_emit_type_dict__wrong_value_type(self):
        def signal_slot_with_typ_list_of_string(test_message):
            if {"fuu": "faa"} == test_message:
                self.flag = True
            pass

        signal = SmartSignal(typing.Dict[str, str])
        signal.connect(signal_slot_with_typ_list_of_string)
        with self.assertRaises(SmartSignalWrongDataTypeException):
            signal.emit({"fuu": 1})
        assert not self.flag

    def test_py_signal_check_emit_length__wrong_value_type(self):
        def signal_slot_with_typ_list_of_string(message_1, message_2):
            if "fuu" == message_1:
                self.flag = True

        signal = SmartSignal(str, str)
        signal.connect(signal_slot_with_typ_list_of_string)
        with self.assertRaises(SmartSignalWrongDataTypeException):
            signal.emit("fuu")
        assert not self.flag

    def test_py_slot_check_number_of_types(self):
        class Test:
            flag = False

            @SmartSignalSlot(str)
            def slot(self, message: str):
                if "message" in message:
                    self.flag = True
                pass

        test = Test()
        signal = SmartSignal(str, multithreading=False)
        signal.connect(test.slot)
        signal.emit("message")

        assert test.flag, "The signal is not transmitted or received!!"

    def test_py_slot_check_number_of_types__wrong_number(self):
        class Test:
            flag = False

            @SmartSignalSlot(str, str, str)
            def slot(self, message_1: str, message_2: str, message_3: str):
                if "message_1" == message_1 and message_2 == "message_2":
                    self.flag = True

        test = Test()
        signal = SmartSignal(str, str, multithreading=False)
        signal.connect(test.slot)
        with self.assertRaises(SmartSlotWrongDataTypeException):
            signal.emit("message_1", "message_2")
        assert not self.flag

    def test_py_slot_check_type_string__wrong_decorator_type(self):
        class Test:
            flag = False

            @SmartSignalSlot(int)
            def slot(self, message):
                if "message" in message:
                    self.flag = True

        test = Test()
        signal = SmartSignal(str, multithreading=False)
        signal.connect(test.slot)

        with self.assertRaises(SmartSlotWrongDataTypeException):
            signal.emit("message")
        assert not self.flag
