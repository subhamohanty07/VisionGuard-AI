class EventLogger:

    def log(self, event):

        print("\n========== EVENT ==========")
        print(f"Type       : {event.event_type}")
        print(f"Time       : {event.timestamp}")
        print(f"Person     : {event.person_name}")
        print(f"Confidence : {event.confidence:.2f}")

        if event.image_path:
            print(f"Image      : {event.image_path}")

        print("===========================\n")