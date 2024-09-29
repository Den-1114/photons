# Flask Image Upload & Login App

This is a simple Flask web application that allows users to upload images and view them in a gallery after logging in with a password. The application demonstrates basic login functionality using sessions and file uploads.

## Features

- **Login System**: Users must log in with a password to access the image gallery.
- **Session Management**: Once logged in, the session remembers the user until they close the browser or log out.
- **Image Upload**: Users can upload images, which will be displayed in the image gallery.
- **Error Handling**: Redirects to an error page if the user tries to access the gallery without logging in.

## Folder Structure

photons_app/
│
├── static/
│   └── images/           # Folder where uploaded images are stored
│
├── templates/
│   ├── index.html        # Gallery page to display uploaded images
│   ├── login.html        # Login page with a password form
│   └── add_a_file.html   # Form page to upload new images
│
├── app.py                # Main Flask application code
├── README.md             # This file
└── requirements.txt      # List of dependencies for the project


## Setup Instructions

### Prerequisites

- Python 3.7+
- Flask
- Flask-Session

### Installation

1. **Clone or Download the Repository**:

    ```
    git clone <repository-url>
    cd photons_app
    ```

2. **Install Dependencies**:

    Install the necessary Python packages using `pip`:

    ```
    pip install -r requrements.txt
    ```

3. **Set Up the Project Structure**:

    Ensure that the `static/images` folder exists, where all uploaded images will be stored.

4. **Run the Application**:

    Run the app using the Python command:

    ```
    flask run --debug --host 0.0.0.0
    ```

5. **Access the App**:

    Open your web browser and navigate to `http://127.0.0.1:5000` to access the login page.

### Default Password

To log in, use the following default password:
`photons_user`


Once logged in, you will be able to see and upload images.

## How It Works

1. **Login**:
   - Users are required to enter the correct password to access the main page.
   - Password: `photons_user` (hardcoded in the app for demonstration purposes).

2. **Image Gallery**:
   - Once logged in, users can view the list of uploaded images in the gallery.

3. **Uploading Images**:
   - Users can navigate to the "Add Image" page to upload images to the `static/images` folder.

4. **Session Handling**:
   - The app uses Flask Sessions to maintain login status across requests.
   - Sessions are stored on the server (using `filesystem` by default).

5. **Deleting images**

    - Currently, the application does not support deleting images through the web interface. To remove images from the gallery, you will need to manually delete them from the server. Please follow these steps:

    - 1. Navigate to the `./static/images` directory on the machine where the application is hosted.
    - 2. Locate the images you wish to delete.
    - 3. Select the desired images and remove them from the folder.

    - **Important**: Ensure that you only delete images that you no longer need, as this action cannot be undone.

6. **Changing the password**
    - To change the password for the application you need to:
  
    - 1. Navigate to the root folder.
    - 2. Open password.key using your perferred text editor (The content of this file is the passoword).
    - 3. Chage the password.

## Templates

- **login.html**: A simple login page that prompts the user to enter a password.
- **index.html**: Displays the gallery of uploaded images after a successful login.
- **add_a_file.html**: Allows users to upload new images to the server.

## Error Handling

- If a user attempts to access the image gallery without logging in, they are redirected to an error page.

## Future Improvements

- Add password hashing and user authentication.
- Implement user management with unique logins.
- Allow users to log out.
- Validate image uploads to ensure only valid image files are uploaded.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.


