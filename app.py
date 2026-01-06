from flask import Flask, render_template, request, jsonify
import math, json, os, re

app = Flask(__name__)

HISTORY_FILE = "history.json"

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history[-20:], f)  # Keep last 20

@app.route("/", methods=["GET"])
def index():
    history = load_history()
    return render_template("index.html", history=history[-12:][::-1])

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json
    expr = data.get("expression", "").strip()
    mode = data.get("mode", "deg")
    
    if not expr:
        return jsonify({"result": "", "history": load_history()[-12:][::-1]})

    try:
        # Security check
        if not re.match(r'^[\d\+\-\*\/\(\)\.\s\%a-zA-Z_]+$', expr):
             raise ValueError("Invalid characters in expression")
        
        forbidden = ["import", "exec", "eval", "os", "sys", "subprocess", "open", "__"]
        if any(bad in expr for bad in forbidden):
             raise ValueError("Unsafe expression detected")

        allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
        
        if mode == 'deg':
            def sin_f(x): return math.sin(math.radians(x))
            def cos_f(x): return math.cos(math.radians(x))
            def tan_f(x): return math.tan(math.radians(x))
        else:
            def sin_f(x): return math.sin(x)
            def cos_f(x): return math.cos(x)
            def tan_f(x): return math.tan(x)
        
        allowed_names.update({
            'abs': abs, 'round': round, 'pi': math.pi, 'e': math.e, 'math': math,
            'sin': sin_f, 'cos': cos_f, 'tan': tan_f
        })
        
        # Calculate
        result = str(eval(expr, {"__builtins__": None}, allowed_names))
        
    except Exception as e:
        result = "Error: " + str(e)

    history = load_history()
    # Save successful or error results? usually just successful steps, but user might want to see errors.
    # We will save only valid results or meaningful errors usually, but let's save all for now as per previous logic.
    history.append({"expression": expr, "result": result})
    save_history(history)
    
    # Return history reversed (newest first)
    return jsonify({"result": result, "history": history[-12:][::-1]})

@app.route("/clear_history", methods=["POST"])
def clear_history():
    save_history([])
    return jsonify({"ok": True})

if __name__ == "__main__":
    app.run(debug=True)
