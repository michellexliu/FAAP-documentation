# FAAP-documentation
## Importing Legacy Users
### Formatting the CSV
Since the “import and export users and customers” plugin requires a specific format for the CSV, you will need to run a script to format the existing users CSV into an importable CSV. 

1. Rename your existing users CSV to “master.csv”
2. Place this CSV file in the same folder as your map.exe executable (will be given to you).
3. Run map.exe
4. The resulting file will be called target.csv.

### Importing a CSV
1. Install the “[Import and export users and customers](https://wordpress.org/plugins/import-users-from-csv-with-meta/)” plugin
2. Once installed go to Tools > Import > Import users or customers (CSV) > Run Importer
3. Choose the target.csv file created from the script in the last step
4. Click “Start Importing”

### Customizing “forgot your password email”
1. Install the "[Customize WordPress Emails and Alerts](https://wordpress.org/plugins/bnfw/)" plugin
2. Once installed click “Notifications” in the sidebar of WordPress
   
   ![image](https://user-images.githubusercontent.com/50491000/235256639-0a3e07c4-2647-42f2-80a3-5338a7b08f94.png)

3. Click “Add New”
4. Set the “notification for” field to “Password Changed  - For User"

    ![image](https://user-images.githubusercontent.com/50491000/235256773-34d04ace-cf71-4b63-8dec-90fb422f38a6.png)

5. Customize the message body to your desired email

### Sending out Password Resets

1. Navigate to the “Users” tab of your Wordpress admin portal
2. To select all users (assuming all current users in the database are legacy users), click the box in the upper left corner of the users table
    ![image](https://user-images.githubusercontent.com/50491000/235256854-223e9beb-7ef2-49a9-bb50-65ca21ab0cc9.png)

3. Select “Send password reset” and click “Apply”
	
