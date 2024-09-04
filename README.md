# Container Vulnerability Report Script

This script retrieves vulnerability data from Trend Micro Cloud One Container Security and generates a report in Excel format. 
1. **Clone the Repository**
   - Begin by cloning the repository that contains the migration script:
     ```sh
     git clone https://github.com/marbsangr/actions-test.git
     cd actions-test
     ```

2. **Set Up Python Environment**
   - Ensure you have Python installed. It's recommended to create a virtual environment to manage dependencies:
     ```sh
     python3 -m venv venv
     source venv/bin/activate  # On Windows use `venv\Scripts\activate`
     ```

3. **Install Dependencies**
   - Install the required Python packages using the `requirements.txt` file provided:
     ```sh
     pip install -r requirements.txt
     ```

4. **Execute Script**
    - Add your Cloud One Api Key in config.yaml file

5. **Execute Script**
     ```sh
     python Reporte_Vuln.py
     ```

## Additional Notes
- Ensure that all changes are documented and approved by your compliance team.