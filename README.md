# SimuPhish: Phishing Simulation and Awareness Tool

SimuPhish is a phishing simulation tool designed to raise security awareness by sending mock phishing emails and tracking user responses to assess susceptibility to phishing attacks. This tool helps organizations educate their employees about phishing threats and improve their overall security posture.

## Features

- **Email Simulation**: Send mock phishing emails to users.
- **User Tracking**: Track email opens, link clicks, and credential submissions.
- **Report Generation**: Generate reports on user interactions to evaluate phishing awareness.
- **Customizable Templates**: Easily modify email templates for different phishing scenarios.

## Technologies Used

- **Backend**: Flask, SQLAlchemy
- **Frontend**: HTML, CSS (Tailwind CSS)
- **Database**: SQLite
- **Email**: Flask-Mail for sending emails
- **Version Control**: Git

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/SimuPhish.git
   cd SimuPhish
   ```

2. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the database**:
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

4. **Configure email settings** in `app/config.py`:
   ```python
   MAIL_USERNAME = 'your-email@gmail.com'
   MAIL_PASSWORD = 'your-email-password'
   ```

5. **Run the application**:
   ```bash
   python run.py
   ```

6. **Access the application** at `http://127.0.0.1:5000`.

## Usage

- To send a phishing email, navigate to the `/send_phishing_email/<recipient>` route, replacing `<recipient>` with the recipient's email address.
- The tool tracks interactions through a tracking pixel and handles user responses through the `/verify` and `/submit_credentials` routes.

## Running the Project

The programs have been tested on the Visual Studio Code IDE in Windows 11. You are free to choose any IDE that suits your needs.

## Contact

If you have any questions, suggestions, or feedback regarding the portfolio website, please feel free to contact me at `jaya2004kra@gmail.com`. I welcome any input that can help me improve the site.

## License

All the code in this repository is licensed under the GNU GENERAL PUBLIC License. You are free to use and modify it for educational purposes. However, I do not take any responsibility for the accuracy or reliability of the code.

## My Social Profiles:

- [**LINKEDIN**](https://www.linkedin.com/in/jayashrek/)
