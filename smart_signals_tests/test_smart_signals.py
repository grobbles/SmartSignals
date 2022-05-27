import typing
from typing import List
from unittest import TestCase

from smart_signals.smart_signals import SmartSignal, SmartSignalWrongDataTypeException, SmartSignalSlot, SmartSlotWrongDataTypeException, SmartSignalWrongSlotTypeException


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

    def test_py_signal(self):
        def signal_slot():
            self.flag = True
            pass

        signal = SmartSignal()
        signal.connect(signal_slot)
        signal.emit()

        self.assertTrue(self.flag, "The signal is not transmitted or received!!")
        pass

    def test_py_signal_with_two_slots(self):
        def signal_slot_1():
            self.flag_1 = True
            pass

        def signal_slot_2():
            self.flag_2 = True
            pass

        signal = SmartSignal()
        signal.connect(signal_slot_1)
        signal.connect(signal_slot_2)
        signal.emit()

        self.assertTrue(self.flag_1 and self.flag_2, "The signal is not transmitted or received!!")
        pass

    def test_py_signal_emit_a_string(self):
        def signal_slot_with_typ_string(test_message: str):
            if "fuu" in test_message:
                self.flag = True
            pass

        signal = SmartSignal(str)
        signal.connect(signal_slot_with_typ_string)
        signal.emit("fuu")

        assert self.flag, "The signal is not transmitted or received!!"

    def test_py_signal_emit_a_list(self):
        def signal_slot_with_typ_list_of_string(test_message: list):
            if "fuu" in test_message:
                self.flag = True
            pass

        signal = SmartSignal(list)
        signal.connect(signal_slot_with_typ_list_of_string)
        signal.emit(["fuu"])

        assert self.flag, "The signal is not transmitted or received!!"

    def test_py_signal_check_emit_type_string(self):
        def signal_slot_with_typ_list_of_string(test_message: list):
            if "fuu" in test_message:
                self.flag = True
            pass

        signal = SmartSignal(str)
        signal.connect(signal_slot_with_typ_list_of_string)
        signal.emit("fuu")

        assert self.flag, "The signal is not transmitted or received!!"

    def test_py_signal_check_emit_type_string__wrong_type(self):
        def signal_slot_with_typ_list_of_string(test_message: list):
            if "fuu" in test_message:
                self.flag = True
            pass

        signal = SmartSignal(str)
        signal.connect(signal_slot_with_typ_list_of_string)

        with self.assertRaises(SmartSignalWrongDataTypeException):
            signal.emit(1)

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
            pass

        signal = SmartSignal(str, str)
        signal.connect(signal_slot_with_typ_list_of_string)

        with self.assertRaises(SmartSignalWrongDataTypeException):
            signal.emit("fuu", 1)

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
            pass

        signal = SmartSignal(List[str])
        signal.connect(signal_slot_with_typ_list_of_string)

        with self.assertRaises(SmartSignalWrongDataTypeException):
            signal.emit("fuu")

    def test_py_signal_check_emit_type_dict(self):
        def signal_slot_with_typ_list_of_string(test_message):
            if {"fuu": "faa"} == test_message:
                self.flag = True
            pass

        signal = SmartSignal(typing.Dict[str, str])
        signal.connect(signal_slot_with_typ_list_of_string)
        signal.emit({"fuu": "faa"})

        assert self.flag, "The signal is not transmitted or received!!"

    def test_py_signal_check_emit_type_dict__wrong_key_type(self):
        def signal_slot_with_typ_list_of_string(test_message):
            if {"fuu": "faa"} == test_message:
                self.flag = True
            pass

        signal = SmartSignal(typing.Dict[str, str])
        signal.connect(signal_slot_with_typ_list_of_string)
        with self.assertRaises(SmartSignalWrongDataTypeException):
            signal.emit({1: "faa"})

    def test_py_signal_check_emit_type_dict__wrong_value_type(self):
        def signal_slot_with_typ_list_of_string(test_message):
            if {"fuu": "faa"} == test_message:
                self.flag = True
            pass

        signal = SmartSignal(typing.Dict[str, str])
        signal.connect(signal_slot_with_typ_list_of_string)
        with self.assertRaises(SmartSignalWrongDataTypeException):
            signal.emit({"fuu": 1})

    def test_py_signal_check_emit_length__wrong_value_type(self):
        def signal_slot_with_typ_list_of_string(message_1, message_2):
            if "fuu" == message_1:
                self.flag = True
            pass

        signal = SmartSignal(str, str)
        signal.connect(signal_slot_with_typ_list_of_string)
        with self.assertRaises(SmartSignalWrongDataTypeException):
            signal.emit("fuu")

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
                pass

        test = Test()
        signal = SmartSignal(str, str, multithreading=False)
        signal.connect(test.slot)
        with self.assertRaises(SmartSlotWrongDataTypeException):
            signal.emit("message_1", "message_2")

    def test_py_slot_check_type_string__wrong_decorator_type(self):
        class Test:
            flag = False

            @SmartSignalSlot(int)
            def slot(self, message):
                if "message" in message:
                    self.flag = True
                pass

        test = Test()
        signal = SmartSignal(str, multithreading=False)
        signal.connect(test.slot)

        with self.assertRaises(SmartSlotWrongDataTypeException):
            signal.emit("message")

    # def test_wrong_typ_definition(self):
    #     def signal_slot_with_typ_list_of_string(test_message: list):
    #         if "test_py_signal_with_string" in test_message:
    #             self.flag = True
    #         pass
    #
    #     signal = PySignal(str)
    #     signal.connect(signal_slot_with_typ_list_of_string)
    #
    #     with self.assertRaises(ValueError):
    #         signal.emit(["test_py_signal_with_string"])
    #     pass
    #
    # def test_py_slot_decorator_with_typ_definition(self):
    #
    #     @PySlotFunction(list)
    #     def signal_slot_with_typ_list_of_string(test_message: list):
    #         if "test_py_signal_with_string" in test_message:
    #             self.flag = True
    #         pass
    #
    #     signal = PySignal(list)
    #     signal.connect(signal_slot_with_typ_list_of_string)
    #     signal.emit(["test_py_signal_with_string"])
    #
    #     self.assertTrue(self.flag, "The signal is not transmitted or received!!")
    #     pass
    #
    # def test_py_slot_decorator_with_class_typ_definition(self):
    #     class Test:
    #         flag = False
    #
    #         @PySlot(list)
    #         def signal_slot_with_typ_list_of_string(self, test_message: list):
    #             if "test_py_signal_with_string" in test_message:
    #                 self.flag = True
    #             pass
    #
    #     test = Test()
    #
    #     signal = PySignal(list)
    #     signal.connect(test.signal_slot_with_typ_list_of_string)
    #     signal.emit(["test_py_signal_with_string"])
    #
    #     self.assertTrue(test.flag, "The signal is not transmitted or received!!")
    #     pass
    #
    # def test_py_slot_decorator_with_class_typ_definition__(self):
    #     class Test:
    #         flag = False
    #
    #         @PySlot(list, str)
    #         def signal_slot_with_typ_list_of_string(self, test_message: list, message: str):
    #             if "testListMessage" in test_message and message == 'testMessage':
    #                 self.flag = True
    #             pass
    #
    #     test = Test()
    #
    #     signal = PySignal(list, str, multithreading=False)
    #     signal.connect(test.signal_slot_with_typ_list_of_string)
    #     signal.emit(["testListMessage"], 'testMessage')
    #
    #     self.assertTrue(test.flag, "The signal is not transmitted or received!!")
    #     pass
    #
    # def test_py_slot_decorator_with_class_wrong_typ_definition(self):
    #     class Test:
    #         flag = False
    #
    #         @PySlot(str)
    #         def signal_slot_with_typ_list_of_string(self, test_message: list):
    #             if "test_py_signal_with_string" in test_message:
    #                 self.flag = True
    #             pass
    #
    #     test = Test()
    #
    #     signal = PySignal(typ=list, multithreading=False)
    #     signal.connect(test.signal_slot_with_typ_list_of_string)
    #
    #     with self.assertRaises(ValueError):
    #         signal.emit(["test_py_signal_with_string"])
    #     pass
    #
    # def test_py_slot_decorator_with_wrong_typ_definition(self):
    #
    #     @PySlotFunction(str)
    #     def signal_slot_with_typ_list_of_string(test_message: list):
    #         if "test_py_signal_with_string" in test_message:
    #             self.flag = True
    #         pass
    #
    #     signal = PySignal(typ=list, multithreading=False)
    #     signal.connect(signal_slot_with_typ_list_of_string)
    #
    #     with self.assertRaises(ValueError):
    #         signal.emit(["test_py_signal_with_string"])
    #     pass
