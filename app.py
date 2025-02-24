from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    hourly_rate = ""

    if request.method == "POST":
        start_time = request.form.get("start_time")
        end_time = request.form.get("end_time")
        earnings = request.form.get("earnings")

        try:
            fmt = "%H:%M"
            start = datetime.strptime(start_time, fmt)
            end = datetime.strptime(end_time, fmt)

            diff = (end - start).total_seconds() / 3600  # Разница во времени в часах
            hours = int(diff)
            minutes = round((diff - hours) * 60)

            # Вычисляем почасовую оплату
            earnings = float(earnings) * 0.75
            hourly_rate = earnings / diff if diff > 0 else 0

            result = f"{diff:.5f} ({hours}ч {minutes}мин)"
            hourly_rate = f"{hourly_rate:.2f} в час"

        except ValueError:
            result = "Ошибка ввода!"
            hourly_rate = ""

    return render_template("index.html", result=result, hourly_rate=hourly_rate)

if __name__ == "__main__":
    app.run(debug=True)
