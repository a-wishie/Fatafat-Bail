# SwiftBail-Bail Reckoner

Bail Reckoner is a web application designed to streamline the bail process for undertrial prisoners, legal aid providers, and judicial authorities. It offers an easy-to-use interface to calculate bail amounts, access legal resources, and manage bail-related documentation.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Bail Application Form:** A comprehensive form to capture all necessary details for bail applications.
- **Bail Amount Calculator:** Automatically calculates the bail amount based on input criteria.
- **Dashboard:** Provides an overview of bail applications and related data.
- **Resources Section:** Offers legal resources including video tutorials and document templates.
- **Responsive Design:** Optimized for both desktop and mobile devices.
- **Bottom-to-Top Transition Effects:** Engaging animations for a better user experience.

## Installation

### Prerequisites
- [Node.js](https://nodejs.org/) (for running local server if needed)
- [Git](https://git-scm.com/)

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/bail-reckoner.git
    cd bail-reckoner
    ```

2. Open the project in your preferred code editor.

3. Start a local server to test the application. If you have Node.js installed, you can use the following command:
    ```bash
    npx live-server
    ```
    Alternatively, you can simply open the `index.html` file in a web browser.

## Usage
1. **Bail Form:** Navigate to the Bail Form page to fill out the application form and calculate bail.
2. **Dashboard:** Use the Dashboard to monitor and manage bail applications.
3. **Resources:** Access valuable legal resources via the Resources dropdown in the navigation bar.

### Page Navigation
- **Home:** Provides a brief introduction to the Bail Reckoner application.
- **Bail Form:** Directs to the form where users can submit bail applications.
- **Dashboard:** Access and manage ongoing and past bail cases.
- **Sign Up:** Users can sign up for an account to manage bail applications.
- **Resources:** Find additional materials such as videos and documents to assist with bail procedures.

## Project Structure
bail-reckoner/ 
├── frontend/ 
│ ├── landing-page/ 
│ ├── landing.html 
│ ├── styles.css 
│ └── bailer2.jpg 
│ ├── form-page/ 
│ ├── form.html 
│ └── form.css 
│ ├── Sign Up Page/ 
│ ├── signUp.html 
│ └── signUp.css 
│ ├── index.html 
└── README.md


- `landing-page/`: Contains the home page files.
- `form-page/`: Includes the bail application form and related styles.
- `Sign Up Page/`: Contains the sign-up page files.
- `index.html`: Entry point of the application.

## Contributing
Contributions are welcome! If you would like to contribute to this project, please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Create a new Pull Request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
