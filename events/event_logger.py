class EventLogger:
    """
    Logs VisionGuard AI events.
    """

    def log(self, event):

        print("\n" + "=" * 50)
        print("           VISIONGUARD AI EVENT")
        print("=" * 50)

        print(f"Event Type : {event.event_type}")
        print(f"Session ID : {event.session_id}")
        print(f"Time       : {event.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Person     : {event.person_name}")
        print(f"Confidence : {event.confidence:.2%}")

        if event.image_path:
            print(f"Image      : {event.image_path}")

        print("=" * 50 + "\n")

    def log_session_end(self, session):

        duration = session.last_seen - session.start_time

        print("\n" + "=" * 50)
        print("          VISIONGUARD AI SESSION")
        print("=" * 50)

        print("Status     : SESSION ENDED")
        print(f"Session ID : {session.session_id}")
        print(
            f"Start Time : {session.start_time.strftime('%Y-%m-%d %H:%M:%S')}"
        )
        print(
            f"End Time   : {session.last_seen.strftime('%Y-%m-%d %H:%M:%S')}"
        )
        print(f"Duration   : {duration}")

        print("=" * 50 + "\n")