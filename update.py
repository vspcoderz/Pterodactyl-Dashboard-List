import os
import json

def generate_dashboard_table(dash_folder):
    table_rows = []
    table_header = "| Name | Owner | Link | Github | 🆓Free / 💵Paid | Docs |\n"
    table_header += "|------|-------|------|--------|-------------|-----------|\n"

  #  {chr(92)} Iterate through each folder in the Dash directory
    for dashboard in os.listdir(dash_folder):
        dashboard_path = os.path.join(dash_folder, dashboard)
        
       # {chr(92)} Check if it's a directory
        if os.path.isdir(dashboard_path):
            detail_file = os.path.join(dashboard_path, 'detail.json')
            
           # {chr(92)} Check if detail.json exists
            if os.path.isfile(detail_file):
                with open(detail_file, 'r') as f:
                    details = json.load(f)
                   # {chr(92)} Create a table row
                    row = f"| {dashboard} | {details['owner']} | {details['link']} | {details['github']} | {details['pricing']} | [Docs]({details['docs']}) |"
                    table_rows.append(row)

   # {chr(92)} Combine header and rows
    full_table = table_header + "\n".join(table_rows)
    return full_table

if __name__ == "__main__":
    dash_folder = 'Dash' # {chr(92)} Change this if your folder is named differently
    table = generate_dashboard_table(dash_folder)
    hash = '#'
    
   # {chr(92)} Prepare the full README content
    readme_content = f"""
     Hi There!
{hash} Pterodactyl-Dashboard-List
Want To Get Best Dashboard But Don't Know Where Are They? Here Is a List

{table}

{hash} How it works

In Folder Dash Make a New Folder Named Your Dash In There Make a 2 Things `detail.json` And `README.md`  In README.md Put Details Of Your Dash And In detail.json Do like Following

```json
{
  {hash} Name Will Be Shown Of Folder Name
  "owner": "Your Name",
  "link": "https://your-dashboard-link.com", {hash} If Not Have Then Put Your Discord Server Link
  "github": "https://github.com/yourusername/repo",
  "pricing": "Free",
  "docs": "dash/my-awesome-dash/README.md" {hash} Also Fill This Properly
}

```
<pre>


  
</pre>



{hash} Star This Project!
Star This Project And Share This To Any Hosting Startup How need help About It 

{hash} Send Pull Request to Add Yours

{hash}{hash} Upcoming ..
I'll Make a Website With Docs To Install All Dash Easily

- [ ] Proper List In Website
- [ ] Docs

{hash}{hash} Milestone 🙌

{hash}{hash}{hash} Free Dashboard
- [ ] 10 Dashboard Listed
- [ ] 20 Dashboard Listed
- [ ] 30 Dashboard Listed

{hash}{hash}{hash} Paid Dashboard
- [ ] 1 Paid Dashboard Listed
- [ ] 5 Paid Dashboard Listed
- [ ] 10 Paid Dashboard Listed

{hash}{hash}{hash} Custom Dashboard (Which Is Made For Customer And It Will Show It)
- [ ] 5 Custom Dashboard Listed

{hash}{hash}{hash} Stars
- [ ] 10 Stars
- [ ] 20 Stars
- [ ] 50 Stars
- [ ] 100 Stars
- [ ] 200 Stars
    
  ""
     Hi There!
{hash} Pterodactyl-Dashboard-List
Want To Get Best Dashboard But Don't Know Where Are They? Here Is a List

{table}

{hash} How it works

In Folder Dash Make a New Folder Named Your Dash In There Make a 2 Things `detail.json` And `README.md`  In README.md Put Details Of Your Dash And In detail.json Do like Following

```json
{
  # Name Will Be Shown Of Folder Name
  "owner": "Your Name",
  "link": "https://your-dashboard-link.com", {hash} If Not Have Then Put Your Discord Server Link
  "github": "https://github.com/yourusername/repo",
  "pricing": "Free",
  "docs": "dash/my-awesome-dash/README.md" {hash} Also Fill This Properly
}

```
<pre>


  
</pre>



{hash} Star This Project!
Star This Project And Share This To Any Hosting Startup How need help About It 

{hash} Send Pull Request to Add Yours

{hash}{hash} Upcoming ..
I'll Make a Website With Docs To Install All Dash Easily

- [ ] Proper List In Website
- [ ] Docs

{hash}{hash} Milestone 🙌

{hash}{hash}{hash} Free Dashboard
- [ ] 10 Dashboard Listed
- [ ] 20 Dashboard Listed
- [ ] 30 Dashboard Listed

{hash}{hash}{hash} Paid Dashboard
- [ ] 1 Paid Dashboard Listed
- [ ] 5 Paid Dashboard Listed
- [ ] 10 Paid Dashboard Listed

{hash}{hash}{hash} Custom Dashboard (Which Is Made For Customer And It Will Show It)
- [ ] 5 Custom Dashboard Listed

{hash}{hash}{hash} Stars
- [ ] 10 Stars
- [ ] 20 Stars
- [ ] 50 Stars
- [ ] 100 Stars
- [ ] 200 Stars
    
  """

    #{chr(92)} Save the complete README content to README.md
    with open('README.md', 'w') as f:
        f.write(readme_content)

    print("list.md has been updated successfully.")


