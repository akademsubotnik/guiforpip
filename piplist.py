import pkg_resources

# Get a list of installed packages
installed_packages = pkg_resources.working_set

# Sort and print the package names and versions
for package in sorted(installed_packages, key=lambda p: p.project_name):
    print(f"{package.project_name}=={package.version}")