from alerts.telegram_alert import TelegramAlert


def main():

    telegram = TelegramAlert()

    response = telegram.send_message(
        "✅ TelegramAlert class is working!"
    )

    print(response)


if __name__ == "__main__":
    main()