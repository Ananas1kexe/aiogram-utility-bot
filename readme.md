
# Telegram Bot in Python

Universal and lightweight template for your bot built with `aiogram`. Easily add commands, handlers, and modular features to fit any use case.

---

## Features

- Full support for Telegram Bot API using `aiogram`
- Modular and clean code architecture
- Command handlers for quick bot interaction
- Environment-based or `config.py` configuration
- Example commands:
  - `/start`
  - `/ping`
  - `/random`
  - `/qrcode`
  - `/dice`
  - `/time`
  - `/date`
  - `/say`
  - `/avatar`
  - `/user_info`
  - `/get_id`
  - `/color`

---

## Requirements

- Python 3.9 or newer
- `aiogram` library
- `python-dotenv` (if using a `.env` file)
- Other dependencies listed in `requirements.txt`

> Install all dependencies:
> ```bash
> pip install -r requirements.txt
> ```

---

## Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Ananas1kexe/aiogram-utility-bot.git
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your bot**:
   - Create a `.env` file in the project root:
     ```ini
     BOT_TOKEN=yourbottoken
     ```

---

## Running the Bot

Start your bot by running:
```bash
python main.py
```

---

## Commands

| Command | Description |
|:--------|:------------|
| `/start` | Welcome message |
| `/ping` | Check bot's response time |
| `/random <number>` | Get a random number (default 100) |
| `/qrcode <text>` | Generate a QR code from text |
| `/dice` | Roll a dice |
| `/time` | Show the current time |
| `/date` | Show the current date |
| `/say <text>` | Echo your text |
| `/avatar` | Get your Telegram profile picture |
| `/user_info` | Show your user information |
| `/get_id` | Get your Telegram user ID |
| `/color <hex>` | Show color preview by hex code |

---

## Contributing

1. Fork the repository
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes and commit:
   ```bash
   git commit -m "Add new command or feature"
   ```
4. Push to your branch and open a Pull Request

---

## Useful Links

- [Project Repository](https://github.com/Ananas1kexe/aiogram-utility-bot)
- [MIT License](https://github.com/Ananas1kexe/aiogram-utility-bot/blob/main/LICENSE)

---

## License

This project is licensed under the **MIT License**.  
See [LICENSE](https://github.com/Ananas1kexe/aiogram-utility-bot/blob/main/LICENSE) for details.
