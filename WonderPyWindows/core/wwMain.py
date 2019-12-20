import threading
import WonderPyWindows


def start(delegate_instance, arguments=None):
    WonderPyWindows.core.wwBTLEMgr.WWBTLEManager(delegate_instance, arguments).run()


thread_local_data = threading.local()
