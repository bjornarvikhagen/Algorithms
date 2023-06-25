import cv2
import numpy as np


def analyze_fish_behavior(video_path):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Define parameters for fish behavior analysis
    # You can customize these parameters based on your specific requirements

    # Define ROI (Region of Interest) for tracking fish
    roi_x = 100
    roi_y = 100
    roi_width = 300
    roi_height = 200

    # Define threshold for detecting fish movement
    movement_threshold = 20

    # Initialize variables for behavior analysis
    total_frames = 0
    moving_frames = 0

    # Read frames from the video and analyze fish behavior
    while True:
        # Read the next frame
        ret, frame = cap.read()

        if not ret:
            break

        # Extract the ROI for fish tracking
        roi = frame[roi_y:roi_y + roi_height, roi_x:roi_x + roi_width]

        # Convert the ROI to grayscale for movement analysis
        gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian blur to reduce noise
        blurred_roi = cv2.GaussianBlur(gray_roi, (5, 5), 0)

        # Calculate the absolute difference between consecutive frames
        if total_frames > 0:
            frame_diff = cv2.absdiff(prev_frame, blurred_roi)

            # Apply thresholding to detect movement
            _, threshold = cv2.threshold(frame_diff, movement_threshold, 255, cv2.THRESH_BINARY)

            # Count the number of non-zero pixels (indicating movement)
            moving_pixels = cv2.countNonZero(threshold)

            # Increment the moving frames count if movement is detected
            if moving_pixels > 0:
                moving_frames += 1

        # Display the processed frame for visualization (optional)
        cv2.imshow('Fish Behavior Analysis', threshold)

        # Store the current frame as the previous frame for the next iteration
        prev_frame = blurred_roi.copy()

        # Increment the total frames count
        total_frames += 1

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture and close all windows
    cap.release()
    cv2.destroyAllWindows()

    # Calculate the percentage of frames with fish movement
    movement_percentage = (moving_frames / total_frames) * 100

    # Return the results of fish behavior analysis
    return total_frames, moving_frames, movement_percentage


# Example usage
video_path = 'fish_behavior_video.mp4'
total_frames, moving_frames, movement_percentage = analyze_fish_behavior(video_path)

# Output the results
print('Fish Behavior Analysis Results:')
print('Total Frames:', total_frames)
print('Moving Frames:', moving_frames)
print('Movement Percentage:', movement_percentage)
