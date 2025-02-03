import os
from dotenv import load_dotenv
from ultralytics import YOLO
import cv2

# Load environment variables from .env file
load_dotenv()

# Load the trained model
model_path = os.getenv('MODEL_PATH', './models/best.pt')  # Default to './models/best.pt'
model = YOLO(model_path)

# Function to process images
def process_images(image_folder, output_folder):
    image_files = [f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.png', '.jpeg'))]
    
    for image_file in image_files:
        # Construct the full image path
        image_path = os.path.join(image_folder, image_file)
        
        # Perform tracking (or detection) on the image
        results = model.track(source=image_path, imgsz=640, conf=0.3, save=True)  # Removed show=False
        
        # Save the results for each result object in the list
        for result in results:
            output_path = os.path.join(output_folder, f"{os.path.splitext(image_file)[0]}_result.jpg")  # Avoid overwriting
            result.save(output_path)

# Function to process videos
def process_videos(video_folder, output_folder):
    video_files = [f for f in os.listdir(video_folder) if f.endswith(('.mp4', '.avi', '.mov'))]
    
    for video_file in video_files:
        # Construct the full video path
        video_path = os.path.join(video_folder, video_file)
        
        # Perform tracking (or detection) on the video
        results = model.track(source=video_path, imgsz=640, conf=0.3, save=True)  # Removed show=False
        
        # Save the results for each result object in the list
        for result in results:
            output_path = os.path.join(output_folder, f"{os.path.splitext(video_file)[0]}_result.mp4")  # Avoid overwriting
            result.save(output_path)

# Function to process webcam
def process_webcam(output_folder):
    # Open webcam (the user can provide the device number if necessary)
    webcam_input = cv2.VideoCapture(0)  # You can change the '0' if you have multiple webcams

    if not webcam_input.isOpened():
        print("Error: Could not access the webcam.")
        return

    while True:
        ret, frame = webcam_input.read()
        
        if not ret:
            print("Error: Failed to grab frame.")
            break

        # Perform tracking (or detection) on the frame
        results = model.track(source=frame, imgsz=640, conf=0.3, save=True)  # Removed show=False
        
        # Save the frame to the output folder
        output_filename = os.path.join(output_folder, "webcam_frame.jpg")
        for result in results:
            result.save(output_filename)
        
        # Optionally show the frame
        cv2.imshow("Webcam Feed", frame)

        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    webcam_input.release()
    cv2.destroyAllWindows()

# Prompt user for input options
def choose_input_type():
    print("Select the input type:")
    print("1. Process images")
    print("2. Process videos")
    print("3. Process webcam feed")
    
    choice = input("Enter the number(s) corresponding to your choice (separate multiple choices with commas, e.g., '1, 2'): ").split(',')
    return [int(x.strip()) for x in choice]

# Main function
def main():
    # Folder paths (using environment variables for security)
    image_folder = os.getenv('IMAGE_FOLDER', './data/image_tests')  # Default to './data/image_tests' if not set
    video_folder = os.getenv('VIDEO_FOLDER', './data/video_tests')  # Default to './data/video_tests' if not set
    image_output_folder = os.getenv('IMAGE_OUTPUT_FOLDER', './data/image_tests_results')
    video_output_folder = os.getenv('VIDEO_OUTPUT_FOLDER', './data/video_test_results')
    webcam_output_folder = os.getenv('WEBCAM_OUTPUT_FOLDER', './data/webcam_frames')
    
    # Ask user for input options
    selected_options = choose_input_type()

    if 1 in selected_options:
        process_images(image_folder, image_output_folder)
    
    if 2 in selected_options:
        process_videos(video_folder, video_output_folder)
    
    if 3 in selected_options:
        process_webcam(webcam_output_folder)

if __name__ == "__main__":
    main()
