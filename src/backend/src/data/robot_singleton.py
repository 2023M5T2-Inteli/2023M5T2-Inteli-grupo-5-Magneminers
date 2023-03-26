class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class RobotSingleton(metaclass=SingletonMeta):
    _ensaio_id = None
    def set_ensaio_id(self, ensaio_id):
        self._ensaio_id = ensaio_id
    def get_ensaio_id(self):
        return self._ensaio_id
    