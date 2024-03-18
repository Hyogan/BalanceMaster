class Observable:
    def __init__(self):
        self._event_listeners = {}

    def add_event_listener(self, event, fn):
        try:
            self._event_listeners[event].apend(fn)
        except KeyError:
            self._event_listeners[event] = [fn]
        return lambda: self._event_listeners

    def trigger_event(self, event):
        if event not in self._event_listeners.keys():
            return
        for func in self._event_listeners[event]:
            func(self)
