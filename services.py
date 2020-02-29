from time import sleep
    
from nameko.events import EventDispatcher, event_handler
from nameko.rpc import rpc


class ServiceA:
    """ Event dispatching service. """
    name = "service_a"

    dispatch = EventDispatcher()

    @rpc
    def dispatching_method(self, payload):
        self.dispatch("event_type", payload)
        return {"result": payload}


class ServiceB:
    """ Event listening service. """
    name = "service_b"

    @event_handler("service_a", "event_type")
    def handle_event(self, payload):
        print(f"working... {payload}")
        sleep(1)
        print("service b received:", payload)