from flask import Flask, render_template, request
from ultralytics import YOLO
import os
import uuid

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load models
dress_model = YOLO("best.pt")
id_model = YOLO("best1.pt")

@app.route("/", methods=["GET", "POST"])
def index():
    status = None
    class_detected = None
    original = None

    if request.method == "POST":
        file = request.files["image"]
        if file:
            filename = f"{uuid.uuid4()}.jpg"
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)
            original = filepath

            # Run dress and ID detection
            dress_results = dress_model(filepath)[0]
            id_results = id_model(filepath)[0]

            dress_classes = [dress_results.names[int(cls.item())].lower() for cls in dress_results.boxes.cls] if dress_results.boxes else []
            id_classes = [id_results.names[int(cls.item())].lower() for cls in id_results.boxes.cls] if id_results.boxes else []

            # Check if no objects detected
            if not dress_classes and not id_classes:
                status = "❌ Image not clear – no objects detected."
                class_detected = "No objects detected by either model."
            else:
                has_formal = "formal" in dress_classes
                has_informal = "informal" in dress_classes
                has_id = "id-card" in id_classes  # fixed here

                if has_formal and has_id and not has_informal:
                    status = "✅ Present"
                else:
                    absent_reasons = []
                    if has_informal or not has_formal:
                        absent_reasons.append("Informal Dress")
                    if not has_id:
                        absent_reasons.append("ID Card Missing")
                        status = f"❌ Absent ({' & '.join(absent_reasons)})"

                class_detected = f"Dress: {', '.join(dress_classes).upper() or 'NONE'} | ID: {', '.join(id_classes).upper() or 'NONE'}"

    return render_template("index.html",
                           original=original,
                           class_detected=class_detected,
                           status=status)

if __name__ == "__main__":
    app.run(debug=True)
