# Cold Email Automation with n8n

A local Docker setup for automating cold emails using n8n, Gmail SMTP, and CSV data.

## Prerequisites

- Docker Desktop installed and running
- Gmail account with 2-Step Verification enabled
- Gmail App Password (see Gmail Setup section)

## Quick Start

### 1. Start n8n

```bash
docker-compose up -d
```

### 2. Access n8n

Open your browser and navigate to: `http://localhost:5678`

### 3. Stop n8n

```bash
docker-compose down
```

## Gmail Setup

### Step 1: Enable 2-Step Verification

1. Go to your Google Account settings
2. Navigate to Security → 2-Step Verification
3. Follow the prompts to enable it

### Step 2: Create App Password

1. Go to Google Account → Security
2. Under "2-Step Verification", click "App passwords"
3. Select "Mail" and "Other (Custom name)"
4. Enter "n8n" as the name
5. Click "Generate"
6. Copy the 16-character password (you'll use this in n8n)

## n8n Workflow Setup

### 1. Configure Gmail SMTP Credentials

1. In n8n, go to **Credentials** (top right)
2. Click **Add Credential** → Search for **SMTP**
3. Fill in the details:
   - **Host**: `smtp.gmail.com`
   - **Port**: `587`
   - **User**: Your Gmail address
   - **Password**: The 16-character App Password from Gmail
   - **Secure**: Enable TLS/SSL
4. Test the connection and save

### 2. Create the Workflow

**Option A: Import Pre-built Workflow (Recommended)**

Try these methods to import `workflow-cold-email.json`:

**Method 1: Drag and Drop (Easiest)**

1. Open n8n in your browser (`http://localhost:5678`)
2. Go to the **Workflows** page (click "Workflows" in the left sidebar)
3. Simply **drag and drop** the `workflow-cold-email.json` file onto the n8n interface
4. The workflow should appear automatically

**Method 2: Import Button**

1. In n8n, go to **Workflows** page
2. Click the **"+"** button or **"New Workflow"** button
3. Look for **"Import"** or **"Import from File"** option in the dropdown/menu
4. Select `workflow-cold-email.json` from your computer

**Method 3: Copy-Paste JSON**

1. Open `workflow-cold-email.json` in a text editor
2. Copy the entire JSON content
3. In n8n, create a new workflow
4. Click the **three dots menu (⋮)** in the top right of the workflow editor
5. Select **"Import from JSON"** or **"Import"**
6. Paste the JSON content

**Method 4: Direct URL Import (if available)**

1. If you've hosted the JSON file online, use **"Import from URL"** option
2. Enter the URL to the workflow JSON file

**After Importing:**

1. Update the workflow:
   - Configure your Gmail SMTP credentials (see step 1 above)
   - The "fromEmail" is already set to `sejalguptawork@gmail.com` (update if needed)
   - Customize the email template in the "Send Email" node if desired
2. Create your `local-files/contacts.csv` file (see Sample CSV Format below)

**Option B: Build Manually**

#### Node 1: Read CSV Data

- **Node**: "Read Binary Files" or "Read Files from Disk"
- **Path**: `/files/contacts.csv` (or use a manual data node)
- This reads your HR contact list

#### Node 2: Process Data (Optional)

- **Node**: "Set" or "Code" node
- Format the data for email sending
- Extract: `hrName`, `companyName`, `email`

#### Node 3: Send Email

- **Node**: "Email" node
- **Credential**: Select your Gmail SMTP credential
- **To**: `{{$json.email}}` (or `{{$json.body.email}}`)
- **Subject**: `Cold Outreach: {{$json.companyName}}`
- **Body**:

  ```
  Hi {{$json.hrName}},

  I noticed {{$json.companyName}} is hiring...

  Best regards,
  [Your Name]
  ```

#### Node 4: Add Delay

- **Node**: "Wait" node
- **Wait Time**: 60-120 seconds (to avoid Gmail throttling)
- Place this between email sends

#### Node 5: Schedule Trigger

- **Node**: "Cron" node
- **Cron Expression**: `0 9 * * *` (runs daily at 9 AM)
- Or use "Schedule Trigger" for more options

### 3. Workflow Structure

```
Cron Trigger → Read CSV → Loop Items → Send Email → Wait → Next Item
```

## Sample CSV Format

Create `local-files/contacts.csv` with the following structure:

```csv
hrName,companyName,email
John Doe,Acme Corp,john.doe@acme.com
Jane Smith,Tech Inc,jane.smith@techinc.com
```

## File Structure

```
cold-email-n8n/
├── docker-compose.yml
├── README.md
├── workflow-cold-email.json (import this into n8n)
├── .gitignore
└── local-files/
    ├── contacts.csv.example (template)
    └── contacts.csv (create this file with your data)
```

## Important Notes

- **Rate Limiting**: Gmail has sending limits (500 emails/day for regular accounts). Use delays between sends.
- **Data Persistence**: All n8n workflows and data are stored in the `n8n_data` Docker volume.
- **Local Files**: Files in `./local-files` are accessible to n8n at `/files/`
- **Security**: This setup disables basic auth for local development. For production, enable authentication.

## Troubleshooting

### n8n won't start

- Ensure Docker Desktop is running
- Check if port 5678 is already in use: `lsof -i :5678`

### Gmail authentication fails

- Verify you're using the App Password (16 characters), not your regular password
- Ensure 2-Step Verification is enabled
- Check that "Less secure app access" is not required (App Passwords replace this)

### Emails not sending

- Check Gmail sending limits
- Verify SMTP credentials in n8n
- Check n8n execution logs for error messages

## Resources

- [n8n Documentation](https://docs.n8n.io/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Gmail App Passwords](https://support.google.com/accounts/answer/185833)
