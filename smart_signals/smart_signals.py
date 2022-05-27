import inspect
import threading
from typing import List, _GenericAlias


class SmartSignalWrongSlotTypeException(Exception):
    pass


class SmartSignalWrongDataTypeException(Exception):
    pass


class SmartSlotWrongDataTypeException(Exception):
    pass


class SmartSignalSlot:

    def __init__(self, *args):
        self._slot_types = args
        self._owner = self._get_owner()
        pass

    @classmethod
    def _get_owner(cls) -> str:
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)
        return calframe[2][1]

    def __call__(self, method):
        def wrapped_f(*args, **kwargs):
            if len(args[1:]) != len(self._slot_types):
                raise SmartSlotWrongDataTypeException(f"The number of input parameters: {len(args[1:])} does not match those in the slot definition: {len(self._slot_types)}.")

            if self._slot_types is not None:
                for index, slot_types in enumerate(self._slot_types):
                    arg = args[index + 1]
                    if not isinstance(arg, self._slot_types):
                        raise SmartSlotWrongDataTypeException(f"The object: {arg} is not an instance of '{self._slot_types}', the owner is '{self._owner}'!!")
            method(*args, **kwargs)

        return wrapped_f


class SmartSignal:
    signal_lock = threading.RLock()

    def __init__(self, *args, name: str = None, multithreading: bool = False):
        self._name = name
        self._multithreading = multithreading
        self._slot_types = args
        self._slots = []

        self._emit_thread: List[threading.Thread] = []

        pass

    def __str__(self) -> str:
        return f"PySignal({self.__repr__()}, slot: {self._slots})"

    @property
    def slots(self):
        return self._slots

    def reset(self):
        self._slots = []

    def delete_connection(self, slot):
        if slot in self._slots:
            self._slots.remove(slot)

    def emit(self, *args, **kwargs):
        if self._slot_types is not None:
            if len(args) != len(self._slot_types):
                raise SmartSignalWrongDataTypeException("Connection to non-callable '{}' object failed")

            for index, slot_type in enumerate(self._slot_types):
                if isinstance(slot_type, _GenericAlias):
                    container_types = slot_type.__origin__
                    inner_types = slot_type.__args__

                    container = args[index]
                    if not isinstance(container, container_types):
                        raise SmartSignalWrongDataTypeException("Connection to non-callable '{}' object failed")

                    if container_types == list:
                        for element in container:
                            if not isinstance(element, inner_types):
                                raise SmartSignalWrongDataTypeException("Connection to non-callable '{}' object failed")

                    elif container_types == dict:
                        for key, value in container.items():
                            if not isinstance(key, inner_types[0]):
                                raise SmartSignalWrongDataTypeException("Connection to non-callable '{}' object failed")
                            if not isinstance(value, inner_types[1]):
                                raise SmartSignalWrongDataTypeException("Connection to non-callable '{}' object failed")
                else:
                    if not isinstance(args[index], slot_type):
                        raise SmartSignalWrongDataTypeException("Connection to non-callable '{}' object failed")

        if self._multithreading:
            emit_thread = threading.Thread(target=self._emit_thread_runner, args=args, kwargs=kwargs)
            emit_thread.start()
            self._emit_thread.append(emit_thread)
        else:
            self._emit_thread_runner(*args, **kwargs)
        pass

    def _emit_thread_runner(self, *args, **kwargs):
        for slot in self._slots:
            if not callable(slot):
                raise SmartSignalWrongSlotTypeException(f"The solt: '{slot.__class__.__name__}' is not a callable object!!!")

            slot(*args, **kwargs)
        pass

    def connect(self, slot):
        if not callable(slot):
            raise SmartSignalWrongSlotTypeException(f"The solt: '{slot.__class__.__name__}' is not a callable object!!!")

        if slot not in self._slots:
            self._slots.append(slot)
        pass
