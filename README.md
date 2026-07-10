# instai
[![Python](https://img.shields.io/badge/Python-3.12+-blue?logo=python)](https://docs.python.org/3/)
[![Instagram Graph API](https://img.shields.io/badge/Instagram%20Graph%20API-FF006E?logo=instagram)](https://developers.facebook.com/documentation/instagram-platform/instagram-api-with-instagram-login)

<p align="center">
  <b>Modern asynchronous framework for building Instagram bots with Python.</b>
</p>

<p align="center">
  Create Instagram automation bots with handlers, filters, FSM, dependency injection and async support.
</p>

---

## ✨ Features

- ⚡ Fully asynchronous architecture
- 🧩 Event-based handlers
- 🔍 Custom filters
- 💉 Dependency injection system
- 🧠 FSM (Finite State Machine) support
- 🗄 Redis storage support
- 📦 Message and callback event handling
- 🖼 Rich messages with cards and buttons
- 🔌 Webhook-based architecture
- 🐍 Python 3.12+ support

---

## 📦 Installation

Install from PyPI:

```bash
pip install -U instai
```

Or install from source:

```bash
git clone https://github.com/zerowkaPy/instai
cd instai

pip install .
```
### 🚀 Quick start

Example of a simple Instagram bot:

```python
from fastapi import FastAPI, Request

from instai import Instai, Dispatcher, Message, TextFilter, StateFilter
from instai.fsm import FSMContext

bot = Instai(
    access_token="YOUR_ACCESS_TOKEN",
    ig_id="YOUR_INSTAGRAM_ID")

dp = Dispatcher(bot)

@dp.message(TextFilter("hello"))
async def hello(msg: Message, fsm: FSMContext):
    await fsm.set_state("name")
    await msg.send_message("Type your name")

@dp.message(StateFilter("name"))
async def answer(msg: Message, fsm: FSMContext):
    await fsm.clear()
    await msg.send_message(f"Hello, {msg.text}!")


router = FastAPI()

@router.post("/webhook")
async def webhook(request: Request):
    webhook = await request.json()
    await dp.feed_update(webhook)
```

### 🎯 Handlers

Instai uses an event-based handler system.

Example:

```python
from instai import Message

@dp.message()
async def echo(msg: Message):
    await msg.send_message(msg.text)
```

You can use filters, for example filter that executes handler if the text of user message is "I like Python!":

```python
@dp.message(TextFilter("I like Python!"))
async def hello(msg: Message):
    await msg.send_message("I like it too!")
```
### 🔘 Buttons

Create interactive buttons:

```python
from instai import Callback, InlineButton, CallbackFilter

buttons = [
    InlineButton(
        text="Menu 📲",
        payload="menu"
        )
    ]

@dp.callback(CallbackFilter(payload="menu"))
async def go_to_menu(cb: Callback):
    await cb.send_buttons("Go to menu:", buttons)
```

### 🃏 Cards

Send rich card messages:
```python
from instai.types import Card


cards = [
    Card(
        title="Nike Air Force 1",
        subtitle="price: 100$",
        image_url="https://example.com/nike-af1.png"
    )
]

@dp.message()
async def shoes(msg: Message):
    await msg.send_cards(cards)
```

### 🧠 FSM

Store user states and create conversations

FSM storage can use the default in-memory storage or Redis:

```python
from instai.fsm import RedisStorage

RedisStorage(url="redis://localhost:6379/0")
```

## ⚙️ Requirements
Python >= 3.12

Instagram Professional Account

Instagram Graph API access token

Webhook server. For example: FastAPI(as above), aiohttp, Django etc.

## 📌 Project status

🚧 Currently under active development.

Planned features:

- More Instagram API methods
  
- Better documentation

- Middleware system

- Testing suite

## 🤝 Contributing
Contributions are welcome!

**Steps:**
1. Fork the repository

2. Create a new branch
```bash
git checkout -b feature/new-feature
```
3. Commit changes
```bash
git commit -m "Add new feature"
```
4. Push branch
```bash
git push origin feature/new-feature
```
5. Open Pull Request


## 📄 License
MIT License

## Author
Created by **zerowkaPy**