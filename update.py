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
    
    # Print the table or save it to a file
    print(table)
    
    # Optionally, save to a Markdown file
    with open('dashboard_list.md', 'w') as f:
        f.write(table)
