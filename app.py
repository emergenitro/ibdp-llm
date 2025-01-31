from flask import Flask, request, render_template_string
from model.inference import IBDPSubjectLLM

app = Flask(__name__)
model = IBDPSubjectLLM("./checkpoints/ibdp_llm")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form.get("user_input", "")
        answer = model.generate_answer(user_input, 512)
        return render_template_string(
            """
            <html>
            <head>
                <link rel="stylesheet"
                      href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css"
                      integrity="sha384"
                      crossorigin="anonymous">
            </head>
            <body class="p-3">
            <div class="container mt-3">
                <form method="POST" class="mb-3">
                    <div class="mb-3">
                        <label for="user_input" class="form-label">Enter your prompt</label>
                        <input id="user_input" name="user_input" class="form-control" />
                    </div>
                    <button type="submit" class="btn btn-primary">Submit</button>
                </form>
                <p class="mt-2 text-danger">Note: Please do not spam the submit button</p>
                <p class="mt-2">Answer: {{ answer }}</p>
            </div>
            </body>
            </html>
            """,
            answer=answer,
        )
    return render_template_string("""
        <html>
        <head>
            <link rel="stylesheet"
                  href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css"
                  integrity="sha384"
                  crossorigin="anonymous">
        </head>
        <body class="p-3">
        <div class="container mt-3">
            <form method="POST" class="mb-3">
                <div class="mb-3">
                    <label for="user_input" class="form-label">Enter your prompt</label>
                    <input id="user_input" name="user_input" class="form-control" />
                </div>
                <button type="submit" class="btn btn-primary">Submit</button>
            </form>
            <p class="mt-2 text-danger">Note: Please do not spam the submit button</p>
        </div>
        </body>
        </html>
    """)


if __name__ == "__main__":
    app.run(debug=True)
