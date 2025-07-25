Signature Verification using Structural Similarity Index (SSIM)
This is a simple Python project that compares two signature images and determines whether the second signature is genuine or forged. It uses the Structural Similarity Index (SSIM) from the skimage library to calculate similarity between two images.

📌 Features
Compares two signature images using structural similarity

Preprocesses images by converting to grayscale and resizing

Displays a similarity score

Detects forged vs verified signature based on a threshold

🖼️ Demo
For example:

yaml
Copy
Edit
Similarity score: 0.89  
Result: Original and Verified
📂 Project Structure
bash
Copy
Edit
signatureVerification/
├── signatureVerification.py    # Main script
├── sign1.jpeg                  # Reference/original signature
├── sign4.jpeg                  # Signature to verify
├── README.md                   # Project documentation
⚙️ Requirements
Install dependencies using pip:

bash
Copy
Edit
pip install opencv-python scikit-image numpy
🚀 How to Use
Place your images
Ensure you have two signature images:

sign1.jpeg → The original signature

sign4.jpeg → The signature to verify

Run the script
Use the following command in your terminal:

bash
Copy
Edit
python signatureVerification.py
Check the result
The console will display:

Similarity score

Verdict: Original and Verified or Forged

🧠 How It Works
Reading Images: Loads the two images using OpenCV.

Grayscale Conversion: Converts them to grayscale to simplify comparison.

Resize: Ensures both images have the same dimensions.

SSIM Comparison: Calculates how structurally similar the images are.

Thresholding: If the similarity is ≥ 0.75, it's accepted as Verified, otherwise flagged as Forged.

✏️ Customization
You can adjust the similarity threshold by changing the THRESHOLD value in the script:

python
Copy
Edit
THRESHOLD = 0.75  # Increase for stricter matching, decrease for more leniency
To test different images, simply replace sign1.jpeg and sign4.jpeg with your own.

🛠️ Future Improvements
Support for batch verification

UI for easy upload and result display

Integration with ML models for more accurate verification

📄 License
This project is open source and available under the MIT License.

🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss your ideas.

👨‍💻 Author
Srujan N Hiremath
