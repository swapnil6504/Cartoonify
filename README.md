# Cartoonify
A Flask-based web app that lets users instantly cartoonify uploaded images using OpenCV. Easily adjustable parameters for a personalized cartoon effect.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Customization](#customization)
- [License](#license)
- [Contributors](#contributors)

## Prerequisites

Before running the project, ensure you have the following installed:

- Python (version 3.x)
- Flask (`pip install Flask`)
- OpenCV (`pip install opencv-python`)
- NumPy (`pip install numpy`)

## Getting Started

1. Clone the repository:

   bash
   git clone https://github.com/swapnil6504/Cartoonify.git
   cd cartoonify
   

2. Install dependencies:

   bash
   pip install -r requirements.txt
   

3. Run the Flask app:

   bash
   python app.py
   

   The app will be accessible at [http://localhost:5000](http://localhost:5000).

## Usage

1. Open your web browser and go to [http://localhost:5000](http://localhost:5000).

2. Upload an image using the provided form.

3. Click the "Upload and Cartoonify" button.

4. View the cartoonified image on the page.

## Customization

- Adjust the styling of the web page by modifying the CSS in the `templates/index.html` file.
- Customize the image processing parameters in the `app.py` file to achieve different cartoon effects.

## License

This project is licensed under the [MIT License](LICENSE).

## Contributors

- Swapnil Chhibber
- Saanuj Joshi
