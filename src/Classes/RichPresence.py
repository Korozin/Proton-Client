import time, threading, pypresence



class ProtonClientRPC:
    def __init__(self, client_id, main_image_key, connected_image_key, disconnected_image_key):
        self.client_id = client_id
        self.main_image_key = main_image_key
        self.connected_image_key = connected_image_key
        self.disconnected_image_key = disconnected_image_key
        self.connected = False
        self.rpc = None
        self.presence_thread = None
        self.start_time = int(time.time())

    def update_connection_state(self, connection_state):
        self.connected = connection_state

    def start_presence(self):
        self.rpc = pypresence.Presence(client_id=self.client_id)
        self.rpc.connect()
        self.presence_thread = threading.Thread(target=self.update_presence)
        self.presence_thread.daemon = True # This is necessary to exit properly
        self.presence_thread.start()

    def stop_presence(self):
        if self.rpc:
            self.rpc.close()

    def update_presence(self):
        while True:
            state = "Another Wii U Cheat Client"
            small_image = self.connected_image_key if self.connected else self.disconnected_image_key
            small_text = "Connected" if self.connected else "Disconnected"

            self.rpc.update(
                state=state,
                large_image=self.main_image_key,
                large_text="Created By: KorOwOzin",
                small_image=small_image,
                small_text=small_text,
                buttons=[{"label": "Download Proton Client", "url": "https://example.com"}],
                start=self.start_time
            )

            time.sleep(15)
