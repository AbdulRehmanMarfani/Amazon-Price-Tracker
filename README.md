---

# 🛍️ Amazon Price Tracker

A Python automation script that tracks the price of a product on Amazon and sends you an email alert when the price drops below a target value.

---

## 🚀 Features

- ✅ Scrapes Amazon product price using BeautifulSoup
- ✅ Sends **email notifications** if the price falls below your set limit
- ✅ Uses environment variables to secure sensitive credentials
- ✅ Mimics a real browser with headers to bypass bot detection
- ✅ Easily customizable target URL and price

---

## ⚙️ How It Works

1. Sends a request to the Amazon product page using realistic headers.
2. Parses the HTML with BeautifulSoup to extract the current price.
3. Compares it with your desired `target_price`.
4. If the current price is lower, it sends an email to notify you.

---

## 📦 Requirements

- Python 3.6+
- Libraries:
  - `requests`
  - `beautifulsoup4`
  - `smtplib` (built-in)
  - `email.message` (built-in)
  - `os` (built-in)
- A Gmail account with [“Less secure apps” access enabled](https://myaccount.google.com/lesssecureapps) **or** [App Passwords](https://support.google.com/accounts/answer/185833)

---

## 🛠️ Setup

1. Clone the repository or copy the script.
2. Install dependencies (if not already):

   ```bash
   pip install requests beautifulsoup4


3. Set up environment variables (see below).
4. Change the `url` and `target_price` to your desired product and price.
5. Run the script:

   ```bash
   python amazon_price_tracker.py
   ```

---

## 🧪 .env Configuration

Make sure you have the following environment variables set in your system or in a `.env` file if using something like `python-dotenv`:

```bash
EMAIL_ADDRESS=your_gmail_address@gmail.com
EMAIL_PASSWORD=your_gmail_app_password
```

> ⚠️ Use an **App Password** if you have 2FA enabled on your Google account.

---

## 📝 Notes

* Amazon frequently updates their page structure. If parsing fails, inspect the page and update the selectors accordingly.
* For regular price checks, set this script up using:

  * **Windows:** Task Scheduler
  * **Mac/Linux:** `cron`

---

## 📫 Output Example

```
Subject: 🚨🚨🚨 Price Alert!

Price of Echo Dot (3rd Gen, Charcoal) dropped to 98.99!
```

---

## 📌 TODO / Ideas

* [ ] Store price history in a CSV
* [ ] Track multiple products at once
* [ ] Add Telegram or Discord notification options
* [ ] Use `selenium` to bypass Amazon’s anti-bot detection if needed

---

## 👨‍💻 Made by Abdul Rehman Marfani


