
# YOLOv9 Emergency Service Vehicle Detection

This project uses YOLOv9 to detect emergency service vehicles in live traffic feed. It processes images, videos, and webcam input, performs detection, and saves the results.

## Requirements

To run this project, make sure you have the following dependencies installed:

- Python 3.8+
- `ultralytics` library for YOLOv9
- OpenCV for video and webcam processing
- Other required libraries in `requirements.txt`

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the `.env` file:

   After cloning the repository, create a `.env` file in the root directory with the following content:

   ```bash
   IMAGE_FOLDER=./data/image_tests
   VIDEO_FOLDER=./data/video_tests
   IMAGE_OUTPUT_FOLDER=./data/image_tests_results
   VIDEO_OUTPUT_FOLDER=./data/video_test_results
   WEBCAM_OUTPUT_FOLDER=./data/webcam_frames
   MODEL_PATH=./models/best.pt
   ```

4. Run the detection script:
   ```bash
   python custom_model.py
   ```

## Folder Structure

The project folder structure should look like this:

```
ROOT PROJECT FOLDER
│
├── data/
│   ├── image_tests/
│   ├── image_tests_results/
│   ├── video_tests/
│   └── video_test_results/
│
├── models/
│   └── best.pt
│
├── runs/
│   └── detect/
│
├── utils/
├── .env
├── .gitignore
├── custom_model.py
├── LICENSE.md
├── README.md
├── requirements.txt
└── tempCodeRunnerFile.py
```
