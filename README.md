# -Formal-and-Informal-Outfit-Detection-using-YOLOv8
Formal and Informal Outfit Detection using YOLOv8
📝 Project Description
This project uses YOLOv8 (a deep learning model) to detect whether a person in an image is dressed formally or informally. It is deployed using Flask and has a simple interface built with HTML and CSS.

Users can:

Upload a photo

The system analyzes the image using the trained YOLOv8 model

It then displays whether the clothing is formal or informal

The model is trained using two custom datasets:

Formal dataset (e.g., suits, uniforms)

Informal dataset (e.g., casual wear)

🧩 Module 1: Attendance Marker
In this module, the system is used to mark attendance automatically based on clothing type.

If the person is wearing formal dress, the system marks attendance.

If the clothing is informal, the system can reject or notify that the dress code is not followed.

This can be useful for schools, offices, or events where formal dress is required.

⚙️ Technologies Used:
YOLOv8 – for object detection and classification

Flask – for backend and model handling

HTML & CSS – for the user interface

Custom Datasets – for formal and informal classification

How the Project Works (Step-by-Step)
🔹 Step 1: User Uploads a Photo
On the web page (created using HTML and CSS), the user sees a simple form to upload an image.

The image can be a photo of a person wearing either formal or informal clothes.

🔹 Step 2: Flask Backend Receives the Image
The image is sent to the backend (built using Flask).

Flask processes the uploaded image and sends it to the YOLOv8 model for prediction.

🔹 Step 3: YOLOv8 Model Analyzes the Image
The YOLOv8 model, which is already trained on formal and informal clothing datasets, analyzes the image.

It detects the clothing style (formal/informal) in the image.

The model draws a bounding box and labels it (e.g., "Formal" or "Informal").

🔹 Step 4: Attendance Marker Logic (Module 1)
If the model detects the clothing as formal, the system:

✅ Marks attendance (e.g., stores it in a database or displays "Attendance Marked").

If the clothing is informal, it:

❌ Shows a message like “Informal dress detected – attendance not marked.”

This is useful for enforcing dress code policies in schools, offices, or official events.

🔹 Step 5: Output Displayed to User
The result (prediction + attendance status) is sent back to the web page.

The user sees:

The uploaded image with labels, and

A message like “Formal Detected – Attendance Marked ✅”
or “Informal Detected – Attendance Not Marked ❌”

