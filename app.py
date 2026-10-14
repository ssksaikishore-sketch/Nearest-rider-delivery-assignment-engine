
from flask import Flask, request, render_template_string
import math

app = Flask(__name__)

html = """
<style>
body {
    font-family: Arial;
    background-color: #f2f5f9;
    margin: 40px;
}
h1 { color: #1769aa; }
input { margin: 4px; padding: 6px; }
button {
    padding: 8px 14px;
    background: #1769aa;
    color: white;
    cursor: pointer;
}
</style>
<h1>DashDispatch</h1>
<h3>Nearest-Rider Delivery Assignment Engine</h3>
<form method="POST">
Order Name: <input name="order" required><br><br>
Restaurant X: <input name="rx" type="number" step="any" required><br><br>
Restaurant Y: <input name="ry" type="number" step="any" required><br><br>
Rider 1 X: <input name="x1" type="number" step="any" required><br>
Rider 1 Y: <input name="y1" type="number" step="any" required><br><br>
Rider 2 X: <input name="x2" type="number" step="any" required><br>
Rider 2 Y: <input name="y2" type="number" step="any" required><br><br>
Rider 3 X: <input name="x3" type="number" step="any" required><br>
Rider 3 Y: <input name="y3" type="number" step="any" required><br><br>
<button type="submit">Assign Rider</button>
</form>
{% if result %}
<h2>Delivery Assignment Result</h2>
<p>Order: {{ order }}</p>
<p>Nearest Rider: {{ result[0] }}</p>
<p>Distance: {{ result[1] }} units</p>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    order = ""
    if request.method == "POST":
        order = request.form["order"]
        rx = float(request.form["rx"])
        ry = float(request.form["ry"])
        riders = []
        for i in range(1, 4):
            x = float(request.form[f"x{i}"])
            y = float(request.form[f"y{i}"])
            d = math.hypot(x-rx, y-ry)
            riders.append((f"Rider {i}", d))
        name, distance = min(riders, key=lambda r: r[1])
        result = (name, round(distance, 2))
    return render_template_string(html, result=result, order=order)

if __name__ == "__main__":
    app.run(debug=True)
