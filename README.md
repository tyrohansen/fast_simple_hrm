# A Simple Employee Management with fast api
This is a simple Employee Management Application built with the FastAPI framework. The application allows you to perform basic CRUD operations (Create, Read, Update, Delete) on employee records.

## Features
- Create new employee records by providing their details such as name, email, and department.
- Retrieve a list of all employees.
- Retrieve details of a specific employee by their ID.
- Update the details of an existing employee.
- Delete an employee record from the database.

## Requirements
Make sure you have the following software installed on your system:

- Python 3.7 or higher
- Pip (Python package manager)

## Installation
Clone the repository to your local machine:

- git clone <repository-url>
Navigate to the project directory:

cd employee-management-app
Install the required dependencies using pip:

pip install -r requirements.txt
## Configuration
The application uses a SQLite database by default, which is included in the repository. However, you can change the database configuration if needed. Open the main.py file and modify the following line according to your database settings:

database_url = "sqlite:///./employee.db"
## Usage
Start the application server by running the following command:

uvicorn main:app --reload
This will start the FastAPI server locally, and you can access the application through your browser at http://localhost:8000.

The API documentation (Swagger UI) can be accessed at http://localhost:8000/docs. Here, you can see the available endpoints and test them directly from the browser.

## API Endpoints
The following API endpoints are available:

- GET /employees: Retrieve a list of all employees.
- POST /employees: Create a new employee record.
- GET /employees/{employee_id}: Retrieve details of a specific employee.
- PUT /employees/{employee_id}: Update details of a specific employee.
- DELETE /employees/{employee_id}: Delete a specific employee.

### Data Model
The application uses the following data model for employee records:


[code]
{
  "id": 1,
  "name": "John Doe",
  "email": "john.doe@example.com",
  "department": "Sales"
}
[/code]
## Contributing
Contributions to this project are welcome. If you find any issues or want to add new features, please create a pull request or submit an issue on the repository.

## License
This project is licensed under the MIT License. You can find the details in the LICENSE file.

## Contact
If you have any questions or suggestions regarding this application, please feel free to contact the project maintainer.

Thank you for using the Employee Management Application!