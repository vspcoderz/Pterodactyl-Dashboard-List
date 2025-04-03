import os
import json

def generate_dashboard_table(dash_folder):
    table_rows = []
    table_header = "| Name | Owner | Link | Github | 🆓Free / 💵Paid | Docs |\n"
    table_header += "|------|-------|------|--------|-------------|-----------|\n"

    # Iterate through each folder in the Dash directory
    for dashboard in os.listdir(dash_folder):
        dashboard_path = os.path.join(dash_folder, dashboard)
        
        # Check if it's a directory
        if os.path.isdir(dashboard_path):
            detail_file = os.path.join(dashboard_path, 'detail.json')
            
            # Check if detail.json exists
            if os.path.isfile(detail_file):
                with open(detail_file, 'r') as f:
                    details = json.load(f)
                    # Create a table row
                    row = f"| {dashboard} | {details['owner']} | {details['link']} | {details['github']} | {details['pricing']} | [Docs]({details['docs']}) |"
                    table_rows.append(row)

    # Combine header and rows
    full_table = table_header + "\n".join(table_rows)
    return full_table

if __name__ == "__main__":
    dash_folder = 'Dash'  # Change this if your folder is named differently
    table = generate_dashboard_table(dash_folder)
    
    # Prepare the full README content
    readme_content = """
     Hi There!
# Pterodactyl-Dashboard-List
Want To Get Best Dashboard But Don't Know Where Are They? Here Is a List

{table}

# How it works

In Folder Dash Make a New Folder Named Your Dash In There Make a 2 Things `detail.json` And `README.md`  In README.md Put Details Of Your Dash And In detail.json Do like Following

```json
{
  # Name Will Be Shown Of Folder Name
  "owner": "Your Name",
  "link": "https://your-dashboard-link.com", # If Not Have Then Put Your Discord Server Link
  "github": "https://github.com/yourusername/repo",
  "pricing": "Free",
  "docs": "dash/my-awesome-dash/README.md" # Also Fill This Properly
}

```
<pre>


  
</pre>



# Star This Project!
Star This Project And Share This To Any Hosting Startup How need help About It 

# Send Pull Request to Add Yours

## Upcoming ..
I'll Make a Website With Docs To Install All Dash Easily

- [ ] Proper List In Website
- [ ] Docs

## Milestone 🙌

### Free Dashboard
- [ ] 10 Dashboard Listed
- [ ] 20 Dashboard Listed
- [ ] 30 Dashboard Listed

### Paid Dashboard
- [ ] 1 Paid Dashboard Listed
- [ ] 5 Paid Dashboard Listed
- [ ] 10 Paid Dashboard Listed

### Custom Dashboard (Which Is Made For Customer And It Will Show It)
- [ ] 5 Custom Dashboard Listed

### Stars
- [ ] 10 Stars
- [ ] 20 Stars
- [ ] 50 Stars
- [ ] 100 Stars
- [ ] 200 Stars
    
    """

    # Save the complete README content to README.md
    with open('README.md', 'w') as f:
        f.write(readme_content)

    print("list.md has been updated successfully.")


