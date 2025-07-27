# Insta-No-Crop 📸

**Insta-No-Crop** is a simple Python script that resizes and pads images to fit Instagram's 4:5 portrait aspect ratio without cropping. It adds white borders where necessary to maintain the original image content while making it upload-ready for Instagram.

-----

## ✨ Features

  * Preserves original image content without cropping
  * Resizes and centers images to fit Instagram’s 1080×1350 (4:5) dimensions
  * Automatically adds white space and a consistent border
  * Supports multiple image formats: `.jpg`, `.jpeg`, `.png`, `.webp`, `.bmp`, `.tiff`

-----

## 🖼 Example Use Case

Have a landscape or square image you want to upload to Instagram without losing any content? This tool resizes it and adds padding to make it fit the 4:5 frame perfectly — no cropping required.

-----

## 🚀 Getting Started

### 1\. Clone the Repository

```bash
git clone git@github.com:BhaswarDutta/Insta-No-Crop.git
cd Insta-No-Crop
```

### 2\. Install Dependencies

Make sure you have Python 3 and [Pillow](https://python-pillow.org/) installed:

```bash
pip install pillow
```

### 3\. Prepare Your Images

  * Place your images inside the `image/` folder.
  * Supported formats: `.jpg`, `.jpeg`, `.png`, `.webp`, `.bmp`, `.tiff`

### 4\. Run the Script

```bash
python insta_no_crop.py
```

Processed images will be saved in the `exports/` folder.

-----

## 🛠 Folder Structure

```
Insta-No-Crop/
├── image/            # Input folder for your images
├── exports/          # Output folder with padded images
├── insta_no_crop.py # Main processing script
└── README.md
```

-----

## 🧠 How It Works

  * Detects whether the image is portrait or landscape
  * Scales the image proportionally to fit within 1080×1350 (minus border)
  * Adds white padding to fill any gaps
  * Adds a consistent white border of 20px around the image

-----

## ✅ Output Specs

  * Final image size: **1080 x 1350 px** (suitable for Instagram posts)
  * Padding color: **white**
  * Filename format: `nocrop_originalfilename.jpg`

-----

## 📃 License

This project is open-source and available under the [MIT License](https://www.google.com/search?q=LICENSE).

-----

## 🙋‍♂️ Author

**Bhaswar Dutta**
[GitHub Profile →](https://github.com/BhaswarDutta)

-----

## 🌟 Show Your Support

If this tool saved you time, feel free to give the repo a ⭐ on GitHub\!
