import os

def gather_django_files(project_path, output_file):
    important_files = [
        'settings.py', 'urls.py', 'wsgi.py', 'asgi.py',
        'models.py', 'views.py', 'admin.py', 'forms.py', 'serializers.py',
        'permissions.py', 'pagination.py'
    ]
    
    def write_structure(out_file):
        for root, dirs, files in os.walk(project_path):
            level = root.replace(project_path, '').count(os.sep)
            indent = ' ' * 4 * level
            out_file.write(f"{indent}{os.path.basename(root)}/\n")
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                out_file.write(f"{subindent}{f}\n")
                
    def write_files(out_file):
        for root, dirs, files in os.walk(project_path):
            for file in files:
                if file in important_files or file.endswith(('.html', '.css', '.js')):
                    file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(file_path, start=project_path)
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        out_file.write(f"### File: {relative_path} ###\n")
                        out_file.write(infile.read())
                        out_file.write("\n\n")
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write("### Project Structure ###\n")
        write_structure(outfile)
        outfile.write("\n\n### Important Files ###\n")
        write_files(outfile)

if __name__ == "__main__":
    project_directory = "C:\\Users\\sushi\\OneDrive\\Desktop\\Django_Assignment_Project\\myproject"  # Specified project directory
    output_txt = "django_project_files.txt"
    gather_django_files(project_directory, output_txt)
    print(f"Django project files and structure gathered into {output_txt}")
