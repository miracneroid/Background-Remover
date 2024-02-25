# Background Removal with GrabCut

This Python script utilizes the GrabCut algorithm from OpenCV to remove the background from an input image, focusing on accurately isolating a person. This project is part of an internship assignment provided by Celebrare.

## Getting Started

### Prerequisites

- Python 3
- OpenCV

### Installation

Install the required libraries using:

```bash
pip install opencv-python numpy
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/your-username/background-removal.git
cd background-removal
```

2. Provide the path to the image you want to process in the script:

```python
# Provide the path to the image you downloaded
image_path = "path/to/your/downloaded/image.jpg"
```

3. Run the script:

```bash
python background_removal.py
```

The script will display the original image and the resulting foreground with the background removed.

## Code Explanation

- **mask, bgd_model, fgd_model**: Arrays used by GrabCut to store information about the image's regions.
- **rect**: Rectangle defining the region of interest in the image.
- **cv2.grabCut**: OpenCV function applying the GrabCut algorithm to segment the image.
- **np.where**: NumPy function creating a binary mask for the foreground based on GrabCut results.
- **result**: The final image with the background removed.

Feel free to experiment and enhance the script to suit your specific needs.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The script is based on the GrabCut algorithm from OpenCV.
- Celebrare for providing the internship assignment.

```

Make sure to customize it with your specific details, such as your GitHub username, repository name, and any additional acknowledgments or licensing information.