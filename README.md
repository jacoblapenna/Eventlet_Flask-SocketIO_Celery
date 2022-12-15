If the data stream's external process is ran from within the `if __name__ == "__main__":` block, the application works perfectly.

If the data stream's external process is ran from an event handler, websockets only randomly work and hundreds are attempted with only a few successful.

Gevent does work with the event handler code.